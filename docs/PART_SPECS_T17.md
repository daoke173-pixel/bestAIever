# HYPERION-Ω — Part specifications · T17 · Training, Data & Recursive Self-Improvement

> Contract: **Ω-CONTRACT v1.0.0-frozen** · 50 parts · 250,000 lines of code · language: Python 3.13

**Tier mission.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Benchmarks this tier is accountable for.** Frontier-Bench v0.1, ARC-AGI-3

**Tier dependencies.** T01, T05, T06, T10

Each part below is built by exactly one isolated Opus 5 worker that sees only: this specification, the frozen Ω-Contract, and its own prompt. Workers never see each other's files. Link-compatibility comes from the contract, not from coordination.

| part | slug | title | capability |
|---|---|---|---|
| [P0801](#p0801-data-sourcing) | `data_sourcing` | Training Data Sourcing & Licensing | `cap.t17.data.data_sourcing@1` |
| [P0802](#p0802-data-extraction-pipeline-train) | `data_extraction_pipeline_train` | Corpus Extraction & Normalisation | `cap.t17.data.data_extraction_pipeline_train@1` |
| [P0803](#p0803-data-quality-filter) | `data_quality_filter` | Data Quality Filtering & Scoring | `cap.t17.data.data_quality_filter@1` |
| [P0804](#p0804-data-dedup-train) | `data_dedup_train` | Corpus Deduplication at Scale | `cap.t17.data.data_dedup_train@1` |
| [P0805](#p0805-data-decontamination) | `data_decontamination` | Benchmark Decontamination | `cap.t17.data.data_decontamination@1` |
| [P0806](#p0806-data-mixture) | `data_mixture` | Data Mixture Optimisation | `cap.t17.data.data_mixture@1` |
| [P0807](#p0807-synthetic-data-engine) | `synthetic_data_engine` | Synthetic Data Generation Engine | `cap.t17.synthetic.synthetic_data_engine@1` |
| [P0808](#p0808-verifiable-task-gen) | `verifiable_task_gen` | Verifiable Task & Reward Generation | `cap.t17.verifiable.verifiable_task_gen@1` |
| [P0809](#p0809-data-augmentation) | `data_augmentation` | Data Augmentation & Transformation | `cap.t17.data.data_augmentation@1` |
| [P0810](#p0810-tokenizer-training) | `tokenizer_training` | Tokeniser Training & Evaluation | `cap.t17.tokenizer.tokenizer_training@1` |
| [P0811](#p0811-data-loader) | `data_loader` | High-Throughput Training Data Loader | `cap.t17.data.data_loader@1` |
| [P0812](#p0812-pretraining-loop) | `pretraining_loop` | Pretraining Loop & Orchestration | `cap.t17.pretraining.pretraining_loop@1` |
| [P0813](#p0813-optimiser-design) | `optimiser_design` | Optimiser Design & Implementation | `cap.t17.optimiser.optimiser_design@1` |
| [P0814](#p0814-lr-schedule) | `lr_schedule` | Learning Rate & Schedule Optimisation | `cap.t17.lr.lr_schedule@1` |
| [P0815](#p0815-gradient-engineering) | `gradient_engineering` | Gradient Processing & Stability | `cap.t17.gradient.gradient_engineering@1` |
| [P0816](#p0816-training-parallelism) | `training_parallelism` | Training Parallelism Strategy | `cap.t17.training.training_parallelism@1` |
| [P0817](#p0817-training-efficiency) | `training_efficiency` | Training Compute Efficiency | `cap.t17.training.training_efficiency@1` |
| [P0818](#p0818-checkpoint-management) | `checkpoint_management` | Checkpoint Management & Model Registry | `cap.t17.checkpoint.checkpoint_management@1` |
| [P0819](#p0819-training-monitoring) | `training_monitoring` | Training Observability & Diagnostics | `cap.t17.training.training_monitoring@1` |
| [P0820](#p0820-sft-pipeline) | `sft_pipeline` | Supervised Fine-Tuning Pipeline | `cap.t17.sft.sft_pipeline@1` |
| [P0821](#p0821-rlvr-pipeline) | `rlvr_pipeline` | RL from Verifiable Rewards | `cap.t17.rlvr.rlvr_pipeline@1` |
| [P0822](#p0822-rlhf-pipeline) | `rlhf_pipeline` | RL from Human & AI Feedback | `cap.t17.rlhf.rlhf_pipeline@1` |
| [P0823](#p0823-reward-model) | `reward_model` | Reward Model Design & Robustness | `cap.t17.reward.reward_model@1` |
| [P0824](#p0824-constitutional-training) | `constitutional_training` | Constitutional & Principle-Based Training | `cap.t17.constitutional.constitutional_training@1` |
| [P0825](#p0825-process-supervision-training) | `process_supervision_training` | Process Supervision Training | `cap.t17.process.process_supervision_training@1` |
| [P0826](#p0826-self-play-training) | `self_play_training` | Self-Play & Adversarial Curriculum | `cap.t17.self.self_play_training@1` |
| [P0827](#p0827-distillation-training) | `distillation_training` | Distillation Training Pipeline | `cap.t17.distillation.distillation_training@1` |
| [P0828](#p0828-quantisation-training) | `quantisation_training` | Quantisation-Aware Training | `cap.t17.quantisation.quantisation_training@1` |
| [P0829](#p0829-long-context-training) | `long_context_training` | Long Context Training Curriculum | `cap.t17.long.long_context_training@1` |
| [P0830](#p0830-multimodal-training) | `multimodal_training` | Multimodal Training Pipeline | `cap.t17.multimodal.multimodal_training@1` |
| [P0831](#p0831-agentic-training) | `agentic_training` | Agentic & Tool-Use Training | `cap.t17.agentic.agentic_training@1` |
| [P0832](#p0832-safety-training) | `safety_training` | Safety & Refusal Training | `cap.t17.safety.safety_training@1` |
| [P0833](#p0833-honesty-training) | `honesty_training` | Honesty & Calibration Training | `cap.t17.honesty.honesty_training@1` |
| [P0834](#p0834-continual-pretraining) | `continual_pretraining` | Continual Pretraining & Knowledge Refresh | `cap.t17.continual.continual_pretraining@1` |
| [P0835](#p0835-hyperparameter-search) | `hyperparameter_search` | Hyperparameter Optimisation at Scale | `cap.t17.hyperparameter.hyperparameter_search@1` |
| [P0836](#p0836-experiment-tracking) | `experiment_tracking` | Experiment Management & Provenance | `cap.t17.experiment.experiment_tracking@1` |
| [P0837](#p0837-ablation-framework) | `ablation_framework` | Systematic Ablation Framework | `cap.t17.ablation.ablation_framework@1` |
| [P0838](#p0838-scaling-prediction) | `scaling_prediction` | Scaling Prediction & Run Planning | `cap.t17.scaling.scaling_prediction@1` |
| [P0839](#p0839-self-improvement-loop) | `self_improvement_loop` | Recursive Self-Improvement Loop | `cap.t17.self.self_improvement_loop@1` |
| [P0840](#p0840-automated-research) | `automated_research` | Automated ML Research Agent | `cap.t17.automated.automated_research@1` |
| [P0841](#p0841-capability-gap-analysis) | `capability_gap_analysis` | Capability Gap Analysis & Prioritisation | `cap.t17.capability.capability_gap_analysis@1` |
| [P0842](#p0842-training-data-governance) | `training_data_governance` | Data Governance, Consent & Deletion | `cap.t17.training.training_data_governance@1` |
| [P0843](#p0843-memorisation-analysis) | `memorisation_analysis` | Memorisation & Privacy Leakage Analysis | `cap.t17.memorisation.memorisation_analysis@1` |
| [P0844](#p0844-training-reproducibility) | `training_reproducibility` | Training Reproducibility & Determinism | `cap.t17.training.training_reproducibility@1` |
| [P0845](#p0845-model-release-gate) | `model_release_gate` | Model Release Gate & Sign-Off | `cap.t17.model.model_release_gate@1` |
| [P0846](#p0846-training-cost-model) | `training_cost_model` | Training Cost & Carbon Accounting | `cap.t17.training.training_cost_model@1` |
| [P0847](#p0847-fine-tune-service) | `fine_tune_service` | Customer Fine-Tuning Infrastructure | `cap.t17.fine.fine_tune_service@1` |
| [P0848](#p0848-eval-driven-training) | `eval_driven_training` | Evaluation-Driven Training Loop | `cap.t17.eval.eval_driven_training@1` |
| [P0849](#p0849-training-bench) | `training_bench` | Training Infrastructure Benchmark Suite | `cap.t17.training.training_bench@1` |
| [P0850](#p0850-training-spec-doc) | `training_spec_doc` | Training Specification & Model Card Generator | `cap.t17.training.training_spec_doc@1` |

---

### P0801 · `data_sourcing` — Training Data Sourcing & Licensing

| field | value |
|---|---|
| part id | `P0801` (1/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0801_data_sourcing.py` |
| module path | `hyperion.t17.training.data_sourcing` |
| capability published | `cap.t17.data.data_sourcing@1` |
| determinism class | `io` |
| p99 latency budget | 5000 ns (5 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0801_data_sourcing.txt`](prompts/P0801_data_sourcing.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0801-data-sourcing) |

**Mission.** Legally clean, high-quality data at petabyte scale.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **source inventory with license classification and permission tracking**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **acquisition pipeline with robots/terms compliance verification** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **provenance recording at document granularity** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **auditable license-compliance report for the whole corpus** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t17.data.data_sourcing@1`
- `cap.t17.data.data_sourcing.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t01.string.string_interning@1` | use the in-file conservative substitute for `string_interning` (documented, slower, lower quality) and set `degraded['string_interning']='local'` |
| `cap.t05.causal.causal_model@1` | use the in-file conservative substitute for `causal_model` (documented, slower, lower quality) and set `degraded['causal_model']='local'` |
| `cap.t06.conditional.conditional_layers@1` | use the in-file conservative substitute for `conditional_layers` (documented, slower, lower quality) and set `degraded['conditional_layers']='local'` |
| `cap.t10.numeric.numeric_reasoning@1` | use the in-file conservative substitute for `numeric_reasoning` (documented, slower, lower quality) and set `degraded['numeric_reasoning']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - source inventory with license classification and permission trac | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - acquisition pipeline with robots/terms compliance verification | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - provenance recording at document granularity | 520 | Third required mechanism. |
| 6 | Core implementation D - auditable license-compliance report for the whole corpus | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0801_data_sourcing.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.data.data_sourcing@1`.
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

### P0802 · `data_extraction_pipeline_train` — Corpus Extraction & Normalisation

| field | value |
|---|---|
| part id | `P0802` (2/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0802_data_extraction_pipeline_train.py` |
| module path | `hyperion.t17.training.data_extraction_pipeline_train` |
| capability published | `cap.t17.data.data_extraction_pipeline_train@1` |
| determinism class | `io` |
| p99 latency budget | 6000 ns (6 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0802_data_extraction_pipeline_train.txt`](prompts/P0802_data_extraction_pipeline_train.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0802-data-extraction-pipeline-train) |

**Mission.** Turns raw web, code and document archives into clean text.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **format-specific extraction (HTML, PDF, code, notebooks, media transcripts)** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **boilerplate removal and content-quality preservation** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **encoding, language and script normalisation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **extraction-quality measurement against human-audited samples**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t17.data.data_extraction_pipeline_train@1`
- `cap.t17.data.data_extraction_pipeline_train.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.data.data_sourcing@1` | use the in-file conservative substitute for `data_sourcing` (documented, slower, lower quality) and set `degraded['data_sourcing']='local'` |
| `cap.t01.property.property_gen@1` | use the in-file conservative substitute for `property_gen` (documented, slower, lower quality) and set `degraded['property_gen']='local'` |
| `cap.t05.distillation.distillation_arch@1` | use the in-file conservative substitute for `distillation_arch` (documented, slower, lower quality) and set `degraded['distillation_arch']='local'` |
| `cap.t06.moe.moe_training_stability@1` | use the in-file conservative substitute for `moe_training_stability` (documented, slower, lower quality) and set `degraded['moe_training_stability']='local'` |
| `cap.t10.backtracking.backtracking@1` | use the in-file conservative substitute for `backtracking` (documented, slower, lower quality) and set `degraded['backtracking']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - format-specific extraction (HTML, PDF, code, notebooks, media tr | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - boilerplate removal and content-quality preservation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - encoding, language and script normalisation | 520 | Third required mechanism. |
| 6 | Core implementation D - extraction-quality measurement against human-audited samples | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0802_data_extraction_pipeline_train.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.data.data_extraction_pipeline_train@1`.
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

### P0803 · `data_quality_filter` — Data Quality Filtering & Scoring

| field | value |
|---|---|
| part id | `P0803` (3/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0803_data_quality_filter.py` |
| module path | `hyperion.t17.training.data_quality_filter` |
| capability published | `cap.t17.data.data_quality_filter@1` |
| determinism class | `io` |
| p99 latency budget | 7000 ns (7 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0803_data_quality_filter.txt`](prompts/P0803_data_quality_filter.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0803-data-quality-filter) |

**Mission.** Keeps the good 5% instead of the whole 100%.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **multi-signal quality scoring (fluency, informativeness, correctness proxies)** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **learned quality classifiers calibrated against human judgment** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **domain-balanced filtering avoiding distribution collapse**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured downstream-quality gain per filtering policy** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t17.data.data_quality_filter@1`
- `cap.t17.data.data_quality_filter.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.data.data_extraction_pipeline_train@1` | use the in-file conservative substitute for `data_extraction_pipeline_train` (documented, slower, lower quality) and set `degraded['data_extraction_pipeline_train']='local'` |
| `cap.t01.link.link_validator@1` | use the in-file conservative substitute for `link_validator` (documented, slower, lower quality) and set `degraded['link_validator']='local'` |
| `cap.t05.multimodal.multimodal_fusion_arch@1` | use the in-file conservative substitute for `multimodal_fusion_arch` (documented, slower, lower quality) and set `degraded['multimodal_fusion_arch']='local'` |
| `cap.t06.ensemble.ensemble_combiner@1` | use the in-file conservative substitute for `ensemble_combiner` (documented, slower, lower quality) and set `degraded['ensemble_combiner']='local'` |
| `cap.t10.question.question_asking@1` | use the in-file conservative substitute for `question_asking` (documented, slower, lower quality) and set `degraded['question_asking']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - multi-signal quality scoring (fluency, informativeness, correctn | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - learned quality classifiers calibrated against human judgment | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - domain-balanced filtering avoiding distribution collapse | 520 | Third required mechanism. |
| 6 | Core implementation D - measured downstream-quality gain per filtering policy | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0803_data_quality_filter.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.data.data_quality_filter@1`.
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

### P0804 · `data_dedup_train` — Corpus Deduplication at Scale

| field | value |
|---|---|
| part id | `P0804` (4/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0804_data_dedup_train.py` |
| module path | `hyperion.t17.training.data_dedup_train` |
| capability published | `cap.t17.data.data_dedup_train@1` |
| determinism class | `io` |
| p99 latency budget | 8000 ns (8 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0804_data_dedup_train.txt`](prompts/P0804_data_dedup_train.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0804-data-dedup-train) |

**Mission.** The same document ten times teaches nothing new.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **exact, near-duplicate and substring deduplication at petabyte scale** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **cross-source and cross-modality duplicate detection**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **deduplication effect on memorisation and generalisation measurement** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **throughput and cost measurement per terabyte** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t17.data.data_dedup_train@1`
- `cap.t17.data.data_dedup_train.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.data.data_quality_filter@1` | use the in-file conservative substitute for `data_quality_filter` (documented, slower, lower quality) and set `degraded['data_quality_filter']='local'` |
| `cap.t01.rate.rate_limiter@1` | use the in-file conservative substitute for `rate_limiter` (documented, slower, lower quality) and set `degraded['rate_limiter']='local'` |
| `cap.t05.context.context_packing@1` | use the in-file conservative substitute for `context_packing` (documented, slower, lower quality) and set `degraded['context_packing']='local'` |
| `cap.t06.expert.expert_alignment@1` | use the in-file conservative substitute for `expert_alignment` (documented, slower, lower quality) and set `degraded['expert_alignment']='local'` |
| `cap.t10.scratchpad.scratchpad_manager@1` | use the in-file conservative substitute for `scratchpad_manager` (documented, slower, lower quality) and set `degraded['scratchpad_manager']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - exact, near-duplicate and substring deduplication at petabyte sc | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - cross-source and cross-modality duplicate detection | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - deduplication effect on memorisation and generalisation measurem | 520 | Third required mechanism. |
| 6 | Core implementation D - throughput and cost measurement per terabyte | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0804_data_dedup_train.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.data.data_dedup_train@1`.
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

### P0805 · `data_decontamination` — Benchmark Decontamination

| field | value |
|---|---|
| part id | `P0805` (5/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0805_data_decontamination.py` |
| module path | `hyperion.t17.training.data_decontamination` |
| capability published | `cap.t17.data.data_decontamination@1` |
| determinism class | `io` |
| p99 latency budget | 9000 ns (9 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0805_data_decontamination.txt`](prompts/P0805_data_decontamination.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0805-data-decontamination) |

**Mission.** Guarantees benchmark results mean something.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **n-gram, embedding and paraphrase-level contamination detection**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **held-out benchmark protection with sealed test sets** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **contamination-report generation per benchmark** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **verification that reported scores are contamination-free** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t17.data.data_decontamination@1`
- `cap.t17.data.data_decontamination.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.data.data_dedup_train@1` | use the in-file conservative substitute for `data_dedup_train` (documented, slower, lower quality) and set `degraded['data_dedup_train']='local'` |
| `cap.t01.bootstrap.bootstrap_init@1` | use the in-file conservative substitute for `bootstrap_init` (documented, slower, lower quality) and set `degraded['bootstrap_init']='local'` |
| `cap.t05.capacity.capacity_probes@1` | use the in-file conservative substitute for `capacity_probes` (documented, slower, lower quality) and set `degraded['capacity_probes']='local'` |
| `cap.t06.moe.moe_speed_accounting@1` | use the in-file conservative substitute for `moe_speed_accounting` (documented, slower, lower quality) and set `degraded['moe_speed_accounting']='local'` |
| `cap.t10.reasoning.reasoning_speed_proof@1` | use the in-file conservative substitute for `reasoning_speed_proof` (documented, slower, lower quality) and set `degraded['reasoning_speed_proof']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - n-gram, embedding and paraphrase-level contamination detection | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - held-out benchmark protection with sealed test sets | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - contamination-report generation per benchmark | 520 | Third required mechanism. |
| 6 | Core implementation D - verification that reported scores are contamination-free | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0805_data_decontamination.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.data.data_decontamination@1`.
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

### P0806 · `data_mixture` — Data Mixture Optimisation

| field | value |
|---|---|
| part id | `P0806` (6/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0806_data_mixture.py` |
| module path | `hyperion.t17.training.data_mixture` |
| capability published | `cap.t17.data.data_mixture@1` |
| determinism class | `io` |
| p99 latency budget | 10000 ns (10 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0806_data_mixture.txt`](prompts/P0806_data_mixture.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0806-data-mixture) |

**Mission.** The recipe matters as much as the amount.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **mixture-weight optimisation against downstream capability targets** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **curriculum scheduling across training phases** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **domain-repetition policy with memorisation monitoring** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured capability gain from optimised mixtures**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t17.data.data_mixture@1`
- `cap.t17.data.data_mixture.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.data.data_decontamination@1` | use the in-file conservative substitute for `data_decontamination` (documented, slower, lower quality) and set `degraded['data_decontamination']='local'` |
| `cap.t01.chacha.chacha_seeds@1` | use the in-file conservative substitute for `chacha_seeds` (documented, slower, lower quality) and set `degraded['chacha_seeds']='local'` |
| `cap.t05.recurrent.recurrent_memory_layer@1` | use the in-file conservative substitute for `recurrent_memory_layer` (documented, slower, lower quality) and set `degraded['recurrent_memory_layer']='local'` |
| `cap.t06.expert.expert_attention@1` | use the in-file conservative substitute for `expert_attention` (documented, slower, lower quality) and set `degraded['expert_attention']='local'` |
| `cap.t10.process.process_verifier@1` | use the in-file conservative substitute for `process_verifier` (documented, slower, lower quality) and set `degraded['process_verifier']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - mixture-weight optimisation against downstream capability target | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - curriculum scheduling across training phases | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - domain-repetition policy with memorisation monitoring | 520 | Third required mechanism. |
| 6 | Core implementation D - measured capability gain from optimised mixtures | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0806_data_mixture.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.data.data_mixture@1`.
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

### P0807 · `synthetic_data_engine` — Synthetic Data Generation Engine

| field | value |
|---|---|
| part id | `P0807` (7/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0807_synthetic_data_engine.py` |
| module path | `hyperion.t17.training.synthetic_data_engine` |
| capability published | `cap.t17.synthetic.synthetic_data_engine@1` |
| determinism class | `io` |
| p99 latency budget | 11000 ns (11 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0807_synthetic_data_engine.txt`](prompts/P0807_synthetic_data_engine.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0807-synthetic-data-engine) |

**Mission.** Generates the data that closes each measured capability gap.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **gap-targeted generation with difficulty and diversity control** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **quality verification and filtering of generated data** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **model-collapse prevention via grounding and diversity metrics**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured capability gain per synthetic campaign** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t17.synthetic.synthetic_data_engine@1`
- `cap.t17.synthetic.synthetic_data_engine.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.data.data_mixture@1` | use the in-file conservative substitute for `data_mixture` (documented, slower, lower quality) and set `degraded['data_mixture']='local'` |
| `cap.t01.mem.mem_layout@1` | use the in-file conservative substitute for `mem_layout` (documented, slower, lower quality) and set `degraded['mem_layout']='local'` |
| `cap.t05.byte.byte_latent_patching@1` | use the in-file conservative substitute for `byte_latent_patching` (documented, slower, lower quality) and set `degraded['byte_latent_patching']='local'` |
| `cap.t06.expert.expert_lifecycle@1` | use the in-file conservative substitute for `expert_lifecycle` (documented, slower, lower quality) and set `degraded['expert_lifecycle']='local'` |
| `cap.t10.goal.goal_management@1` | use the in-file conservative substitute for `goal_management` (documented, slower, lower quality) and set `degraded['goal_management']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - gap-targeted generation with difficulty and diversity control | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - quality verification and filtering of generated data | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - model-collapse prevention via grounding and diversity metrics | 520 | Third required mechanism. |
| 6 | Core implementation D - measured capability gain per synthetic campaign | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0807_synthetic_data_engine.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.synthetic.synthetic_data_engine@1`.
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

### P0808 · `verifiable_task_gen` — Verifiable Task & Reward Generation

| field | value |
|---|---|
| part id | `P0808` (8/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0808_verifiable_task_gen.py` |
| module path | `hyperion.t17.training.verifiable_task_gen` |
| capability published | `cap.t17.verifiable.verifiable_task_gen@1` |
| determinism class | `io` |
| p99 latency budget | 12000 ns (12 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0808_verifiable_task_gen.txt`](prompts/P0808_verifiable_task_gen.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0808-verifiable-task-gen) |

**Mission.** Millions of problems with automatically checkable answers.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **automatic task generation with programmatic verifiers** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **difficulty calibration against current model capability**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **verifier-correctness auditing (no reward hacking loopholes)** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured RL-training gain from generated task sets** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t17.verifiable.verifiable_task_gen@1`
- `cap.t17.verifiable.verifiable_task_gen.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.synthetic.synthetic_data_engine@1` | use the in-file conservative substitute for `synthetic_data_engine` (documented, slower, lower quality) and set `degraded['synthetic_data_engine']='local'` |
| `cap.t01.hash.hash_maps@1` | use the in-file conservative substitute for `hash_maps` (documented, slower, lower quality) and set `degraded['hash_maps']='local'` |
| `cap.t05.world.world_model_core@1` | use the in-file conservative substitute for `world_model_core` (documented, slower, lower quality) and set `degraded['world_model_core']='local'` |
| `cap.t06.token.token_dropping@1` | use the in-file conservative substitute for `token_dropping` (documented, slower, lower quality) and set `degraded['token_dropping']='local'` |
| `cap.t10.probabilistic.probabilistic_reasoning@1` | use the in-file conservative substitute for `probabilistic_reasoning` (documented, slower, lower quality) and set `degraded['probabilistic_reasoning']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - automatic task generation with programmatic verifiers | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - difficulty calibration against current model capability | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - verifier-correctness auditing (no reward hacking loopholes) | 520 | Third required mechanism. |
| 6 | Core implementation D - measured RL-training gain from generated task sets | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0808_verifiable_task_gen.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.verifiable.verifiable_task_gen@1`.
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

### P0809 · `data_augmentation` — Data Augmentation & Transformation

| field | value |
|---|---|
| part id | `P0809` (9/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0809_data_augmentation.py` |
| module path | `hyperion.t17.training.data_augmentation` |
| capability published | `cap.t17.data.data_augmentation@1` |
| determinism class | `io` |
| p99 latency budget | 13000 ns (13 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0809_data_augmentation.txt`](prompts/P0809_data_augmentation.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0809-data-augmentation) |

**Mission.** Multiplies useful data without multiplying noise.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **semantics-preserving transformation library per data type**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **adversarial and robustness-targeted augmentation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **augmentation-quality verification** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured robustness improvement per augmentation type** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t17.data.data_augmentation@1`
- `cap.t17.data.data_augmentation.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.verifiable.verifiable_task_gen@1` | use the in-file conservative substitute for `verifiable_task_gen` (documented, slower, lower quality) and set `degraded['verifiable_task_gen']='local'` |
| `cap.t01.selftest.selftest_harness@1` | use the in-file conservative substitute for `selftest_harness` (documented, slower, lower quality) and set `degraded['selftest_harness']='local'` |
| `cap.t05.model.model_merging@1` | use the in-file conservative substitute for `model_merging` (documented, slower, lower quality) and set `degraded['model_merging']='local'` |
| `cap.t06.router.router_interpretability@1` | use the in-file conservative substitute for `router_interpretability` (documented, slower, lower quality) and set `degraded['router_interpretability']='local'` |
| `cap.t10.stopping.stopping_rules@1` | use the in-file conservative substitute for `stopping_rules` (documented, slower, lower quality) and set `degraded['stopping_rules']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - semantics-preserving transformation library per data type | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - adversarial and robustness-targeted augmentation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - augmentation-quality verification | 520 | Third required mechanism. |
| 6 | Core implementation D - measured robustness improvement per augmentation type | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0809_data_augmentation.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.data.data_augmentation@1`.
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

### P0810 · `tokenizer_training` — Tokeniser Training & Evaluation

| field | value |
|---|---|
| part id | `P0810` (10/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0810_tokenizer_training.py` |
| module path | `hyperion.t17.training.tokenizer_training` |
| capability published | `cap.t17.tokenizer.tokenizer_training@1` |
| determinism class | `io` |
| p99 latency budget | 14000 ns (14 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0810_tokenizer_training.txt`](prompts/P0810_tokenizer_training.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0810-tokenizer-training) |

**Mission.** Trains the Ω-tokeniser that fixes the token tax.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **vocabulary learning with multilingual and code fairness objectives** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **compression-rate measurement per language and domain** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **boundary-quality evaluation for math, code and rare scripts** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **target: significantly fewer tokens per text than the Opus 4.7+ tokenizer**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t17.tokenizer.tokenizer_training@1`
- `cap.t17.tokenizer.tokenizer_training.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.data.data_augmentation@1` | use the in-file conservative substitute for `data_augmentation` (documented, slower, lower quality) and set `degraded['data_augmentation']='local'` |
| `cap.t01.version.version_semver@1` | use the in-file conservative substitute for `version_semver` (documented, slower, lower quality) and set `degraded['version_semver']='local'` |
| `cap.t05.logit.logit_head_design@1` | use the in-file conservative substitute for `logit_head_design` (documented, slower, lower quality) and set `degraded['logit_head_design']='local'` |
| `cap.t06.model.model_cascade_routing@1` | use the in-file conservative substitute for `model_cascade_routing` (documented, slower, lower quality) and set `degraded['model_cascade_routing']='local'` |
| `cap.t10.assumption.assumption_tracking@1` | use the in-file conservative substitute for `assumption_tracking` (documented, slower, lower quality) and set `degraded['assumption_tracking']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - vocabulary learning with multilingual and code fairness objectiv | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - compression-rate measurement per language and domain | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - boundary-quality evaluation for math, code and rare scripts | 520 | Third required mechanism. |
| 6 | Core implementation D - target: significantly fewer tokens per text than the Opus 4.7+ t | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0810_tokenizer_training.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.tokenizer.tokenizer_training@1`.
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

### P0811 · `data_loader` — High-Throughput Training Data Loader

| field | value |
|---|---|
| part id | `P0811` (11/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0811_data_loader.py` |
| module path | `hyperion.t17.training.data_loader` |
| capability published | `cap.t17.data.data_loader@1` |
| determinism class | `io` |
| p99 latency budget | 15000 ns (15 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0811_data_loader.txt`](prompts/P0811_data_loader.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0811-data-loader) |

**Mission.** Never starves 100k accelerators.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **streaming loader with deterministic shuffling and exact resumption** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **on-the-fly packing, masking and augmentation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **throughput measurement saturating training compute**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **determinism verification across restarts and rescales** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t17.data.data_loader@1`
- `cap.t17.data.data_loader.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.tokenizer.tokenizer_training@1` | use the in-file conservative substitute for `tokenizer_training` (documented, slower, lower quality) and set `degraded['tokenizer_training']='local'` |
| `cap.t01.budget.budget_ledger@1` | use the in-file conservative substitute for `budget_ledger` (documented, slower, lower quality) and set `degraded['budget_ledger']='local'` |
| `cap.t05.numerical.numerical_arch_stability@1` | use the in-file conservative substitute for `numerical_arch_stability` (documented, slower, lower quality) and set `degraded['numerical_arch_stability']='local'` |
| `cap.t06.sparse.sparse_gradient@1` | use the in-file conservative substitute for `sparse_gradient` (documented, slower, lower quality) and set `degraded['sparse_gradient']='local'` |
| `cap.t10.reasoning.reasoning_cost_model@1` | use the in-file conservative substitute for `reasoning_cost_model` (documented, slower, lower quality) and set `degraded['reasoning_cost_model']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - streaming loader with deterministic shuffling and exact resumpti | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - on-the-fly packing, masking and augmentation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - throughput measurement saturating training compute | 520 | Third required mechanism. |
| 6 | Core implementation D - determinism verification across restarts and rescales | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0811_data_loader.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.data.data_loader@1`.
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

### P0812 · `pretraining_loop` — Pretraining Loop & Orchestration

| field | value |
|---|---|
| part id | `P0812` (12/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0812_pretraining_loop.py` |
| module path | `hyperion.t17.training.pretraining_loop` |
| capability published | `cap.t17.pretraining.pretraining_loop@1` |
| determinism class | `io` |
| p99 latency budget | 16000 ns (16 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0812_pretraining_loop.txt`](prompts/P0812_pretraining_loop.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0812-pretraining-loop) |

**Mission.** The main training run: stable, observable, restartable.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **training step orchestration with gradient accumulation and clipping** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **loss-spike detection with automatic rollback and data skipping**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **checkpoint policy with fast resumption** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured stability over trillion-token runs** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t17.pretraining.pretraining_loop@1`
- `cap.t17.pretraining.pretraining_loop.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.data.data_loader@1` | use the in-file conservative substitute for `data_loader` (documented, slower, lower quality) and set `degraded['data_loader']='local'` |
| `cap.t01.compression.compression@1` | use the in-file conservative substitute for `compression` (documented, slower, lower quality) and set `degraded['compression']='local'` |
| `cap.t05.arch.arch_ablation_suite@1` | use the in-file conservative substitute for `arch_ablation_suite` (documented, slower, lower quality) and set `degraded['arch_ablation_suite']='local'` |
| `cap.t06.sparsity.sparsity_verification@1` | use the in-file conservative substitute for `sparsity_verification` (documented, slower, lower quality) and set `degraded['sparsity_verification']='local'` |
| `cap.t10.collective.collective_reasoning@1` | use the in-file conservative substitute for `collective_reasoning` (documented, slower, lower quality) and set `degraded['collective_reasoning']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - training step orchestration with gradient accumulation and clipp | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - loss-spike detection with automatic rollback and data skipping | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - checkpoint policy with fast resumption | 520 | Third required mechanism. |
| 6 | Core implementation D - measured stability over trillion-token runs | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0812_pretraining_loop.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.pretraining.pretraining_loop@1`.
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

### P0813 · `optimiser_design` — Optimiser Design & Implementation

| field | value |
|---|---|
| part id | `P0813` (13/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0813_optimiser_design.py` |
| module path | `hyperion.t17.training.optimiser_design` |
| capability published | `cap.t17.optimiser.optimiser_design@1` |
| determinism class | `io` |
| p99 latency budget | 17000 ns (17 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0813_optimiser_design.txt`](prompts/P0813_optimiser_design.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0813-optimiser-design) |

**Mission.** The update rule, chosen and tuned by measurement.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **second-order-informed and adaptive optimiser implementations**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **hyperparameter transfer across scale via muP-style parameterisation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **memory-efficient optimiser state (sharded, quantised)** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **convergence-speed comparison across optimisers at matched compute** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t17.optimiser.optimiser_design@1`
- `cap.t17.optimiser.optimiser_design.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.pretraining.pretraining_loop@1` | use the in-file conservative substitute for `pretraining_loop` (documented, slower, lower quality) and set `degraded['pretraining_loop']='local'` |
| `cap.t01.blake3.blake3_hash@1` | use the in-file conservative substitute for `blake3_hash` (documented, slower, lower quality) and set `degraded['blake3_hash']='local'` |
| `cap.t05.state.state_space_layer@1` | use the in-file conservative substitute for `state_space_layer` (documented, slower, lower quality) and set `degraded['state_space_layer']='local'` |
| `cap.t06.expert.expert_ffn@1` | use the in-file conservative substitute for `expert_ffn` (documented, slower, lower quality) and set `degraded['expert_ffn']='local'` |
| `cap.t10.beam.beam_pruning@1` | use the in-file conservative substitute for `beam_pruning` (documented, slower, lower quality) and set `degraded['beam_pruning']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - second-order-informed and adaptive optimiser implementations | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - hyperparameter transfer across scale via muP-style parameterisat | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - memory-efficient optimiser state (sharded, quantised) | 520 | Third required mechanism. |
| 6 | Core implementation D - convergence-speed comparison across optimisers at matched comput | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0813_optimiser_design.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.optimiser.optimiser_design@1`.
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

### P0814 · `lr_schedule` — Learning Rate & Schedule Optimisation

| field | value |
|---|---|
| part id | `P0814` (14/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0814_lr_schedule.py` |
| module path | `hyperion.t17.training.lr_schedule` |
| capability published | `cap.t17.lr.lr_schedule@1` |
| determinism class | `io` |
| p99 latency budget | 18000 ns (18 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0814_lr_schedule.txt`](prompts/P0814_lr_schedule.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0814-lr-schedule) |

**Mission.** Schedules derived from theory and validated by runs.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **warmup, decay and cyclical schedule families with selection criteria** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **schedule-adaptation from observed loss dynamics** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **batch-size/learning-rate scaling relationships** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured final-quality effect per schedule**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t17.lr.lr_schedule@1`
- `cap.t17.lr.lr_schedule.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.optimiser.optimiser_design@1` | use the in-file conservative substitute for `optimiser_design` (documented, slower, lower quality) and set `degraded['optimiser_design']='local'` |
| `cap.t01.alloc.alloc_arena@1` | use the in-file conservative substitute for `alloc_arena` (documented, slower, lower quality) and set `degraded['alloc_arena']='local'` |
| `cap.t05.tokeniser.tokeniser_omega@1` | use the in-file conservative substitute for `tokeniser_omega` (documented, slower, lower quality) and set `degraded['tokeniser_omega']='local'` |
| `cap.t06.moe.moe_determinism@1` | use the in-file conservative substitute for `moe_determinism` (documented, slower, lower quality) and set `degraded['moe_determinism']='local'` |
| `cap.t10.planning.planning_engine@1` | use the in-file conservative substitute for `planning_engine` (documented, slower, lower quality) and set `degraded['planning_engine']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - warmup, decay and cyclical schedule families with selection crit | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - schedule-adaptation from observed loss dynamics | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - batch-size/learning-rate scaling relationships | 520 | Third required mechanism. |
| 6 | Core implementation D - measured final-quality effect per schedule | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0814_lr_schedule.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.lr.lr_schedule@1`.
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

### P0815 · `gradient_engineering` — Gradient Processing & Stability

| field | value |
|---|---|
| part id | `P0815` (15/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0815_gradient_engineering.py` |
| module path | `hyperion.t17.training.gradient_engineering` |
| capability published | `cap.t17.gradient.gradient_engineering@1` |
| determinism class | `io` |
| p99 latency budget | 19000 ns (19 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0815_gradient_engineering.txt`](prompts/P0815_gradient_engineering.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0815-gradient-engineering) |

**Mission.** Keeps a trillion-parameter sparse model training.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **gradient clipping, normalisation and spike handling policies** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **low-precision gradient handling with error feedback** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **gradient-noise and signal-to-noise diagnostics**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **stability evidence at extreme scale** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t17.gradient.gradient_engineering@1`
- `cap.t17.gradient.gradient_engineering.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.lr.lr_schedule@1` | use the in-file conservative substitute for `lr_schedule` (documented, slower, lower quality) and set `degraded['lr_schedule']='local'` |
| `cap.t01.bitset.bitset_rank@1` | use the in-file conservative substitute for `bitset_rank` (documented, slower, lower quality) and set `degraded['bitset_rank']='local'` |
| `cap.t05.uncertainty.uncertainty_calibration@1` | use the in-file conservative substitute for `uncertainty_calibration` (documented, slower, lower quality) and set `degraded['uncertainty_calibration']='local'` |
| `cap.t06.moe.moe_batching@1` | use the in-file conservative substitute for `moe_batching` (documented, slower, lower quality) and set `degraded['moe_batching']='local'` |
| `cap.t10.counterfactual.counterfactual_reasoning@1` | use the in-file conservative substitute for `counterfactual_reasoning` (documented, slower, lower quality) and set `degraded['counterfactual_reasoning']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - gradient clipping, normalisation and spike handling policies | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - low-precision gradient handling with error feedback | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - gradient-noise and signal-to-noise diagnostics | 520 | Third required mechanism. |
| 6 | Core implementation D - stability evidence at extreme scale | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0815_gradient_engineering.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.gradient.gradient_engineering@1`.
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

### P0816 · `training_parallelism` — Training Parallelism Strategy

| field | value |
|---|---|
| part id | `P0816` (16/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0816_training_parallelism.py` |
| module path | `hyperion.t17.training.training_parallelism` |
| capability published | `cap.t17.training.training_parallelism@1` |
| determinism class | `io` |
| p99 latency budget | 20000 ns (20 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0816_training_parallelism.txt`](prompts/P0816_training_parallelism.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0816-training-parallelism) |

**Mission.** Uses 100k accelerators efficiently.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **hybrid data/tensor/pipeline/expert/sequence parallel configuration** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **communication-computation overlap maximisation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **memory-optimiser (sharding, offload, remat) integration** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured hardware-utilisation percentage at full scale** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t17.training.training_parallelism@1`
- `cap.t17.training.training_parallelism.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.gradient.gradient_engineering@1` | use the in-file conservative substitute for `gradient_engineering` (documented, slower, lower quality) and set `degraded['gradient_engineering']='local'` |
| `cap.t01.metrics.metrics_core@1` | use the in-file conservative substitute for `metrics_core` (documented, slower, lower quality) and set `degraded['metrics_core']='local'` |
| `cap.t05.knowledge.knowledge_editing@1` | use the in-file conservative substitute for `knowledge_editing` (documented, slower, lower quality) and set `degraded['knowledge_editing']='local'` |
| `cap.t06.moe.moe_scaling_laws@1` | use the in-file conservative substitute for `moe_scaling_laws` (documented, slower, lower quality) and set `degraded['moe_scaling_laws']='local'` |
| `cap.t10.difficulty.difficulty_estimation@1` | use the in-file conservative substitute for `difficulty_estimation` (documented, slower, lower quality) and set `degraded['difficulty_estimation']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - hybrid data/tensor/pipeline/expert/sequence parallel configurati | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - communication-computation overlap maximisation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - memory-optimiser (sharding, offload, remat) integration | 520 | Third required mechanism. |
| 6 | Core implementation D - measured hardware-utilisation percentage at full scale | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0816_training_parallelism.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.training.training_parallelism@1`.
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

### P0817 · `training_efficiency` — Training Compute Efficiency

| field | value |
|---|---|
| part id | `P0817` (17/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0817_training_efficiency.py` |
| module path | `hyperion.t17.training.training_efficiency` |
| capability published | `cap.t17.training.training_efficiency@1` |
| determinism class | `io` |
| p99 latency budget | 21000 ns (21 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0817_training_efficiency.txt`](prompts/P0817_training_efficiency.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0817-training-efficiency) |

**Mission.** Every FLOP must earn its place.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **model-FLOPs-utilisation measurement and optimisation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **wasted-compute identification (padding, bubbles, recompute, restarts)** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **efficiency comparison against published large-run baselines** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured cost-per-capability improvement** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t17.training.training_efficiency@1`
- `cap.t17.training.training_efficiency.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.training.training_parallelism@1` | use the in-file conservative substitute for `training_parallelism` (documented, slower, lower quality) and set `degraded['training_parallelism']='local'` |
| `cap.t01.capability.capability_gate@1` | use the in-file conservative substitute for `capability_gate` (documented, slower, lower quality) and set `degraded['capability_gate']='local'` |
| `cap.t05.residual.residual_stream_design@1` | use the in-file conservative substitute for `residual_stream_design` (documented, slower, lower quality) and set `degraded['residual_stream_design']='local'` |
| `cap.t06.cost.cost_aware_routing@1` | use the in-file conservative substitute for `cost_aware_routing` (documented, slower, lower quality) and set `degraded['cost_aware_routing']='local'` |
| `cap.t10.evidence.evidence_integration@1` | use the in-file conservative substitute for `evidence_integration` (documented, slower, lower quality) and set `degraded['evidence_integration']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - model-FLOPs-utilisation measurement and optimisation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - wasted-compute identification (padding, bubbles, recompute, rest | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - efficiency comparison against published large-run baselines | 520 | Third required mechanism. |
| 6 | Core implementation D - measured cost-per-capability improvement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0817_training_efficiency.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.training.training_efficiency@1`.
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

### P0818 · `checkpoint_management` — Checkpoint Management & Model Registry

| field | value |
|---|---|
| part id | `P0818` (18/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0818_checkpoint_management.py` |
| module path | `hyperion.t17.training.checkpoint_management` |
| capability published | `cap.t17.checkpoint.checkpoint_management@1` |
| determinism class | `io` |
| p99 latency budget | 22000 ns (22 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0818_checkpoint_management.txt`](prompts/P0818_checkpoint_management.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0818-checkpoint-management) |

**Mission.** Every model version tracked, evaluated and reproducible.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **checkpoint storage with metadata, lineage and evaluation results** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **checkpoint averaging and selection methodology** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **reproducibility metadata sufficient to recreate any checkpoint** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **registry integrity and retention policy**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t17.checkpoint.checkpoint_management@1`
- `cap.t17.checkpoint.checkpoint_management.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.training.training_efficiency@1` | use the in-file conservative substitute for `training_efficiency` (documented, slower, lower quality) and set `degraded['training_efficiency']='local'` |
| `cap.t01.unit.unit_dimensions@1` | use the in-file conservative substitute for `unit_dimensions` (documented, slower, lower quality) and set `degraded['unit_dimensions']='local'` |
| `cap.t05.model.model_surgery@1` | use the in-file conservative substitute for `model_surgery` (documented, slower, lower quality) and set `degraded['model_surgery']='local'` |
| `cap.t06.router.router_online_learning@1` | use the in-file conservative substitute for `router_online_learning` (documented, slower, lower quality) and set `degraded['router_online_learning']='local'` |
| `cap.t10.reasoning.reasoning_search_bench@1` | use the in-file conservative substitute for `reasoning_search_bench` (documented, slower, lower quality) and set `degraded['reasoning_search_bench']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - checkpoint storage with metadata, lineage and evaluation results | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - checkpoint averaging and selection methodology | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - reproducibility metadata sufficient to recreate any checkpoint | 520 | Third required mechanism. |
| 6 | Core implementation D - registry integrity and retention policy | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0818_checkpoint_management.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.checkpoint.checkpoint_management@1`.
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

### P0819 · `training_monitoring` — Training Observability & Diagnostics

| field | value |
|---|---|
| part id | `P0819` (19/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0819_training_monitoring.py` |
| module path | `hyperion.t17.training.training_monitoring` |
| capability published | `cap.t17.training.training_monitoring@1` |
| determinism class | `io` |
| p99 latency budget | 23000 ns (23 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0819_training_monitoring.txt`](prompts/P0819_training_monitoring.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0819-training-monitoring) |

**Mission.** Sees problems in hours, not weeks.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **loss, gradient, activation and routing diagnostics with alerting** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **capability-emergence tracking via periodic evaluations** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **anomaly detection on training dynamics**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured mean-time-to-detection of training pathologies** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t17.training.training_monitoring@1`
- `cap.t17.training.training_monitoring.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.checkpoint.checkpoint_management@1` | use the in-file conservative substitute for `checkpoint_management` (documented, slower, lower quality) and set `degraded['checkpoint_management']='local'` |
| `cap.t01.fs.fs_atomic@1` | use the in-file conservative substitute for `fs_atomic` (documented, slower, lower quality) and set `degraded['fs_atomic']='local'` |
| `cap.t05.reference.reference_forward@1` | use the in-file conservative substitute for `reference_forward` (documented, slower, lower quality) and set `degraded['reference_forward']='local'` |
| `cap.t06.adaptive.adaptive_sparsity@1` | use the in-file conservative substitute for `adaptive_sparsity` (documented, slower, lower quality) and set `degraded['adaptive_sparsity']='local'` |
| `cap.t10.reasoning.reasoning_interpretability@1` | use the in-file conservative substitute for `reasoning_interpretability` (documented, slower, lower quality) and set `degraded['reasoning_interpretability']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - loss, gradient, activation and routing diagnostics with alerting | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - capability-emergence tracking via periodic evaluations | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - anomaly detection on training dynamics | 520 | Third required mechanism. |
| 6 | Core implementation D - measured mean-time-to-detection of training pathologies | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0819_training_monitoring.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.training.training_monitoring@1`.
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

### P0820 · `sft_pipeline` — Supervised Fine-Tuning Pipeline

| field | value |
|---|---|
| part id | `P0820` (20/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0820_sft_pipeline.py` |
| module path | `hyperion.t17.training.sft_pipeline` |
| capability published | `cap.t17.sft.sft_pipeline@1` |
| determinism class | `io` |
| p99 latency budget | 24000 ns (24 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0820_sft_pipeline.txt`](prompts/P0820_sft_pipeline.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0820-sft-pipeline) |

**Mission.** Teaches the model to be useful, not just predictive.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **demonstration-data curation with quality and diversity control** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **multi-task instruction tuning with capability-balance measurement**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **overfitting and capability-regression monitoring** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured instruction-following improvement** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t17.sft.sft_pipeline@1`
- `cap.t17.sft.sft_pipeline.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.training.training_monitoring@1` | use the in-file conservative substitute for `training_monitoring` (documented, slower, lower quality) and set `degraded['training_monitoring']='local'` |
| `cap.t01.cbor.cbor_canonical@1` | use the in-file conservative substitute for `cbor_canonical` (documented, slower, lower quality) and set `degraded['cbor_canonical']='local'` |
| `cap.t05.kv.kv_compression_model@1` | use the in-file conservative substitute for `kv_compression_model` (documented, slower, lower quality) and set `degraded['kv_compression_model']='local'` |
| `cap.t06.router.router_hash_hybrid@1` | use the in-file conservative substitute for `router_hash_hybrid` (documented, slower, lower quality) and set `degraded['router_hash_hybrid']='local'` |
| `cap.t10.graph.graph_search@1` | use the in-file conservative substitute for `graph_search` (documented, slower, lower quality) and set `degraded['graph_search']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - demonstration-data curation with quality and diversity control | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - multi-task instruction tuning with capability-balance measuremen | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - overfitting and capability-regression monitoring | 520 | Third required mechanism. |
| 6 | Core implementation D - measured instruction-following improvement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0820_sft_pipeline.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.sft.sft_pipeline@1`.
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

### P0821 · `rlvr_pipeline` — RL from Verifiable Rewards

| field | value |
|---|---|
| part id | `P0821` (21/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0821_rlvr_pipeline.py` |
| module path | `hyperion.t17.training.rlvr_pipeline` |
| capability published | `cap.t17.rlvr.rlvr_pipeline@1` |
| determinism class | `io` |
| p99 latency budget | 25000 ns (25 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0821_rlvr_pipeline.txt`](prompts/P0821_rlvr_pipeline.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0821-rlvr-pipeline) |

**Mission.** The engine behind superhuman coding, math and agent performance.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **policy optimisation against programmatic verifiers at scale**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **reward-hacking detection and verifier hardening** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **credit assignment over long multi-step trajectories** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured capability gain on verifiable-task benchmarks** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t17.rlvr.rlvr_pipeline@1`
- `cap.t17.rlvr.rlvr_pipeline.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.sft.sft_pipeline@1` | use the in-file conservative substitute for `sft_pipeline` (documented, slower, lower quality) and set `degraded['sft_pipeline']='local'` |
| `cap.t01.clock.clock_time@1` | use the in-file conservative substitute for `clock_time` (documented, slower, lower quality) and set `degraded['clock_time']='local'` |
| `cap.t05.embedding.embedding_design@1` | use the in-file conservative substitute for `embedding_design` (documented, slower, lower quality) and set `degraded['embedding_design']='local'` |
| `cap.t06.router.router_lookahead@1` | use the in-file conservative substitute for `router_lookahead` (documented, slower, lower quality) and set `degraded['router_lookahead']='local'` |
| `cap.t10.decomposition.decomposition@1` | use the in-file conservative substitute for `decomposition` (documented, slower, lower quality) and set `degraded['decomposition']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - policy optimisation against programmatic verifiers at scale | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - reward-hacking detection and verifier hardening | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - credit assignment over long multi-step trajectories | 520 | Third required mechanism. |
| 6 | Core implementation D - measured capability gain on verifiable-task benchmarks | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0821_rlvr_pipeline.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.rlvr.rlvr_pipeline@1`.
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

### P0822 · `rlhf_pipeline` — RL from Human & AI Feedback

| field | value |
|---|---|
| part id | `P0822` (22/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0822_rlhf_pipeline.py` |
| module path | `hyperion.t17.training.rlhf_pipeline` |
| capability published | `cap.t17.rlhf.rlhf_pipeline@1` |
| determinism class | `io` |
| p99 latency budget | 26000 ns (26 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0822_rlhf_pipeline.txt`](prompts/P0822_rlhf_pipeline.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0822-rlhf-pipeline) |

**Mission.** Aligns quality and behaviour to what people actually want.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **preference-data collection protocol with rater-quality control** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **reward-model training with calibration and robustness testing** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **policy optimisation with KL control and over-optimisation detection** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured preference-win-rate improvement**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t17.rlhf.rlhf_pipeline@1`
- `cap.t17.rlhf.rlhf_pipeline.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.rlvr.rlvr_pipeline@1` | use the in-file conservative substitute for `rlvr_pipeline` (documented, slower, lower quality) and set `degraded['rlvr_pipeline']='local'` |
| `cap.t01.bigint.bigint_modmath@1` | use the in-file conservative substitute for `bigint_modmath` (documented, slower, lower quality) and set `degraded['bigint_modmath']='local'` |
| `cap.t05.verifier.verifier_head@1` | use the in-file conservative substitute for `verifier_head` (documented, slower, lower quality) and set `degraded['verifier_head']='local'` |
| `cap.t06.expert.expert_offload@1` | use the in-file conservative substitute for `expert_offload` (documented, slower, lower quality) and set `degraded['expert_offload']='local'` |
| `cap.t10.program.program_synthesis_reasoning@1` | use the in-file conservative substitute for `program_synthesis_reasoning` (documented, slower, lower quality) and set `degraded['program_synthesis_reasoning']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - preference-data collection protocol with rater-quality control | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - reward-model training with calibration and robustness testing | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - policy optimisation with KL control and over-optimisation detect | 520 | Third required mechanism. |
| 6 | Core implementation D - measured preference-win-rate improvement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0822_rlhf_pipeline.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.rlhf.rlhf_pipeline@1`.
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

### P0823 · `reward_model` — Reward Model Design & Robustness

| field | value |
|---|---|
| part id | `P0823` (23/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0823_reward_model.py` |
| module path | `hyperion.t17.training.reward_model` |
| capability published | `cap.t17.reward.reward_model@1` |
| determinism class | `io` |
| p99 latency budget | 27000 ns (27 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0823_reward_model.txt`](prompts/P0823_reward_model.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0823-reward-model) |

**Mission.** A reward model that cannot be gamed.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **multi-objective reward modelling (correctness, helpfulness, safety, style)** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **adversarial robustness testing against reward hacking** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **calibration and disagreement-aware ensembling**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured correlation with expert human judgment** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t17.reward.reward_model@1`
- `cap.t17.reward.reward_model.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.rlhf.rlhf_pipeline@1` | use the in-file conservative substitute for `rlhf_pipeline` (documented, slower, lower quality) and set `degraded['rlhf_pipeline']='local'` |
| `cap.t01.logging.logging_events@1` | use the in-file conservative substitute for `logging_events` (documented, slower, lower quality) and set `degraded['logging_events']='local'` |
| `cap.t05.continual.continual_learning@1` | use the in-file conservative substitute for `continual_learning` (documented, slower, lower quality) and set `degraded['continual_learning']='local'` |
| `cap.t06.expert.expert_choice_routing@1` | use the in-file conservative substitute for `expert_choice_routing` (documented, slower, lower quality) and set `degraded['expert_choice_routing']='local'` |
| `cap.t10.meta.meta_reasoning@1` | use the in-file conservative substitute for `meta_reasoning` (documented, slower, lower quality) and set `degraded['meta_reasoning']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - multi-objective reward modelling (correctness, helpfulness, safe | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - adversarial robustness testing against reward hacking | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - calibration and disagreement-aware ensembling | 520 | Third required mechanism. |
| 6 | Core implementation D - measured correlation with expert human judgment | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0823_reward_model.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.reward.reward_model@1`.
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

### P0824 · `constitutional_training` — Constitutional & Principle-Based Training

| field | value |
|---|---|
| part id | `P0824` (24/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0824_constitutional_training.py` |
| module path | `hyperion.t17.training.constitutional_training` |
| capability published | `cap.t17.constitutional.constitutional_training@1` |
| determinism class | `io` |
| p99 latency budget | 28000 ns (28 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0824_constitutional_training.txt`](prompts/P0824_constitutional_training.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0824-constitutional-training) |

**Mission.** Trains behaviour from stated principles, auditably.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **principle set with operationalisation into training signals** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **self-critique and revision training loops**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **principle-adherence measurement per principle** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **target: measurably better constitution adherence than Opus 5's audit score** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t17.constitutional.constitutional_training@1`
- `cap.t17.constitutional.constitutional_training.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.reward.reward_model@1` | use the in-file conservative substitute for `reward_model` (documented, slower, lower quality) and set `degraded['reward_model']='local'` |
| `cap.t01.checksum.checksum_verify@1` | use the in-file conservative substitute for `checksum_verify` (documented, slower, lower quality) and set `degraded['checksum_verify']='local'` |
| `cap.t05.depth.depth_width_tradeoff@1` | use the in-file conservative substitute for `depth_width_tradeoff` (documented, slower, lower quality) and set `degraded['depth_width_tradeoff']='local'` |
| `cap.t06.difficulty.difficulty_routing@1` | use the in-file conservative substitute for `difficulty_routing` (documented, slower, lower quality) and set `degraded['difficulty_routing']='local'` |
| `cap.t10.hypothesis.hypothesis_management@1` | use the in-file conservative substitute for `hypothesis_management` (documented, slower, lower quality) and set `degraded['hypothesis_management']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - principle set with operationalisation into training signals | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - self-critique and revision training loops | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - principle-adherence measurement per principle | 520 | Third required mechanism. |
| 6 | Core implementation D - target: measurably better constitution adherence than Opus 5's a | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0824_constitutional_training.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.constitutional.constitutional_training@1`.
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

### P0825 · `process_supervision_training` — Process Supervision Training

| field | value |
|---|---|
| part id | `P0825` (25/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0825_process_supervision_training.py` |
| module path | `hyperion.t17.training.process_supervision_training` |
| capability published | `cap.t17.process.process_supervision_training@1` |
| determinism class | `io` |
| p99 latency budget | 29000 ns (29 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0825_process_supervision_training.txt`](prompts/P0825_process_supervision_training.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0825-process-supervision-training) |

**Mission.** Rewards good reasoning, not just lucky answers.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **step-level label generation at scale with automatic verification**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **process reward model training and calibration** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **reasoning-quality improvement measurement independent of final accuracy** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured reduction in right-answer-wrong-reasoning cases** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t17.process.process_supervision_training@1`
- `cap.t17.process.process_supervision_training.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.constitutional.constitutional_training@1` | use the in-file conservative substitute for `constitutional_training` (documented, slower, lower quality) and set `degraded['constitutional_training']='local'` |
| `cap.t01.numeric.numeric_limits@1` | use the in-file conservative substitute for `numeric_limits` (documented, slower, lower quality) and set `degraded['numeric_limits']='local'` |
| `cap.t05.sparse.sparse_upcycling@1` | use the in-file conservative substitute for `sparse_upcycling` (documented, slower, lower quality) and set `degraded['sparse_upcycling']='local'` |
| `cap.t06.moe.moe_memory_budget@1` | use the in-file conservative substitute for `moe_memory_budget` (documented, slower, lower quality) and set `degraded['moe_memory_budget']='local'` |
| `cap.t10.proof.proof_sketch@1` | use the in-file conservative substitute for `proof_sketch` (documented, slower, lower quality) and set `degraded['proof_sketch']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - step-level label generation at scale with automatic verification | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - process reward model training and calibration | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - reasoning-quality improvement measurement independent of final a | 520 | Third required mechanism. |
| 6 | Core implementation D - measured reduction in right-answer-wrong-reasoning cases | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0825_process_supervision_training.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.process.process_supervision_training@1`.
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

### P0826 · `self_play_training` — Self-Play & Adversarial Curriculum

| field | value |
|---|---|
| part id | `P0826` (26/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0826_self_play_training.py` |
| module path | `hyperion.t17.training.self_play_training` |
| capability published | `cap.t17.self.self_play_training@1` |
| determinism class | `io` |
| p99 latency budget | 30000 ns (30 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0826_self_play_training.txt`](prompts/P0826_self_play_training.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0826-self-play-training) |

**Mission.** The model generates its own increasingly hard curriculum.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **proposer/solver self-play with difficulty auto-calibration** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **adversarial example generation targeting current weaknesses** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **curriculum-progress measurement and plateau detection** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured capability gain per self-play generation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t17.self.self_play_training@1`
- `cap.t17.self.self_play_training.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.process.process_supervision_training@1` | use the in-file conservative substitute for `process_supervision_training` (documented, slower, lower quality) and set `degraded['process_supervision_training']='local'` |
| `cap.t01.sandbox.sandbox_policy@1` | use the in-file conservative substitute for `sandbox_policy` (documented, slower, lower quality) and set `degraded['sandbox_policy']='local'` |
| `cap.t05.model.model_config_schema@1` | use the in-file conservative substitute for `model_config_schema` (documented, slower, lower quality) and set `degraded['model_config_schema']='local'` |
| `cap.t06.moe.moe_visualisation@1` | use the in-file conservative substitute for `moe_visualisation` (documented, slower, lower quality) and set `degraded['moe_visualisation']='local'` |
| `cap.t10.adversarial.adversarial_reasoning@1` | use the in-file conservative substitute for `adversarial_reasoning` (documented, slower, lower quality) and set `degraded['adversarial_reasoning']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - proposer/solver self-play with difficulty auto-calibration | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - adversarial example generation targeting current weaknesses | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - curriculum-progress measurement and plateau detection | 520 | Third required mechanism. |
| 6 | Core implementation D - measured capability gain per self-play generation | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0826_self_play_training.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.self.self_play_training@1`.
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

### P0827 · `distillation_training` — Distillation Training Pipeline

| field | value |
|---|---|
| part id | `P0827` (27/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0827_distillation_training.py` |
| module path | `hyperion.t17.training.distillation_training` |
| capability published | `cap.t17.distillation.distillation_training@1` |
| determinism class | `io` |
| p99 latency budget | 31000 ns (31 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0827_distillation_training.txt`](prompts/P0827_distillation_training.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0827-distillation-training) |

**Mission.** Compresses the frontier into the fast paths (enables S1 and S4).

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **teacher-trace generation including search and verification behaviour** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **student training with capability-retention targets per tier** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **acceptance-rate optimisation for cascade drafters**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured quality retention and speedup contribution** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t17.distillation.distillation_training@1`
- `cap.t17.distillation.distillation_training.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.self.self_play_training@1` | use the in-file conservative substitute for `self_play_training` (documented, slower, lower quality) and set `degraded['self_play_training']='local'` |
| `cap.t01.abi.abi_result@1` | use the in-file conservative substitute for `abi_result` (documented, slower, lower quality) and set `degraded['abi_result']='local'` |
| `cap.t05.attention.attention_variants@1` | use the in-file conservative substitute for `attention_variants` (documented, slower, lower quality) and set `degraded['attention_variants']='local'` |
| `cap.t06.router.router_capacity@1` | use the in-file conservative substitute for `router_capacity` (documented, slower, lower quality) and set `degraded['router_capacity']='local'` |
| `cap.t10.tree.tree_search@1` | use the in-file conservative substitute for `tree_search` (documented, slower, lower quality) and set `degraded['tree_search']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - teacher-trace generation including search and verification behav | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - student training with capability-retention targets per tier | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - acceptance-rate optimisation for cascade drafters | 520 | Third required mechanism. |
| 6 | Core implementation D - measured quality retention and speedup contribution | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0827_distillation_training.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.distillation.distillation_training@1`.
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

### P0828 · `quantisation_training` — Quantisation-Aware Training

| field | value |
|---|---|
| part id | `P0828` (28/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0828_quantisation_training.py` |
| module path | `hyperion.t17.training.quantisation_training` |
| capability published | `cap.t17.quantisation.quantisation_training@1` |
| determinism class | `io` |
| p99 latency budget | 32000 ns (32 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0828_quantisation_training.txt`](prompts/P0828_quantisation_training.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0828-quantisation-training) |

**Mission.** Makes low precision free instead of costly.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **QAT with learned scales and outlier handling** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **per-layer precision-plan co-training**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **accuracy-parity verification against full precision** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured inference cost reduction at matched quality** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t17.quantisation.quantisation_training@1`
- `cap.t17.quantisation.quantisation_training.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.distillation.distillation_training@1` | use the in-file conservative substitute for `distillation_training` (documented, slower, lower quality) and set `degraded['distillation_training']='local'` |
| `cap.t01.trace.trace_context@1` | use the in-file conservative substitute for `trace_context` (documented, slower, lower quality) and set `degraded['trace_context']='local'` |
| `cap.t05.activation.activation_design@1` | use the in-file conservative substitute for `activation_design` (documented, slower, lower quality) and set `degraded['activation_design']='local'` |
| `cap.t06.expert.expert_prefetch@1` | use the in-file conservative substitute for `expert_prefetch` (documented, slower, lower quality) and set `degraded['expert_prefetch']='local'` |
| `cap.t10.debate.debate_ensemble@1` | use the in-file conservative substitute for `debate_ensemble` (documented, slower, lower quality) and set `degraded['debate_ensemble']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - QAT with learned scales and outlier handling | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - per-layer precision-plan co-training | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - accuracy-parity verification against full precision | 520 | Third required mechanism. |
| 6 | Core implementation D - measured inference cost reduction at matched quality | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0828_quantisation_training.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.quantisation.quantisation_training@1`.
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

### P0829 · `long_context_training` — Long Context Training Curriculum

| field | value |
|---|---|
| part id | `P0829` (29/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0829_long_context_training.py` |
| module path | `hyperion.t17.training.long_context_training` |
| capability published | `cap.t17.long.long_context_training@1` |
| determinism class | `io` |
| p99 latency budget | 33000 ns (33 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0829_long_context_training.txt`](prompts/P0829_long_context_training.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0829-long-context-training) |

**Mission.** Trains genuine 1M+ token competence, not just capacity.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **progressive length curriculum with position-scaling adaptation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **long-range dependency task construction for training signal** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **recall and reasoning evaluation across context positions** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured elimination of lost-in-the-middle degradation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t17.long.long_context_training@1`
- `cap.t17.long.long_context_training.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.quantisation.quantisation_training@1` | use the in-file conservative substitute for `quantisation_training` (documented, slower, lower quality) and set `degraded['quantisation_training']='local'` |
| `cap.t01.fixed.fixed_point@1` | use the in-file conservative substitute for `fixed_point` (documented, slower, lower quality) and set `degraded['fixed_point']='local'` |
| `cap.t05.draft.draft_model_arch@1` | use the in-file conservative substitute for `draft_model_arch` (documented, slower, lower quality) and set `degraded['draft_model_arch']='local'` |
| `cap.t06.moe.moe_quantisation@1` | use the in-file conservative substitute for `moe_quantisation` (documented, slower, lower quality) and set `degraded['moe_quantisation']='local'` |
| `cap.t10.induction.induction_engine@1` | use the in-file conservative substitute for `induction_engine` (documented, slower, lower quality) and set `degraded['induction_engine']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - progressive length curriculum with position-scaling adaptation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - long-range dependency task construction for training signal | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - recall and reasoning evaluation across context positions | 520 | Third required mechanism. |
| 6 | Core implementation D - measured elimination of lost-in-the-middle degradation | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0829_long_context_training.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.long.long_context_training@1`.
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

### P0830 · `multimodal_training` — Multimodal Training Pipeline

| field | value |
|---|---|
| part id | `P0830` (30/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0830_multimodal_training.py` |
| module path | `hyperion.t17.training.multimodal_training` |
| capability published | `cap.t17.multimodal.multimodal_training@1` |
| determinism class | `io` |
| p99 latency budget | 34000 ns (34 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0830_multimodal_training.txt`](prompts/P0830_multimodal_training.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0830-multimodal-training) |

**Mission.** Trains all senses jointly without any modality suffering.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **modality-balanced batching and loss weighting** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **cross-modal alignment objectives with measured transfer** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **modality-specific data curation and quality control** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **per-modality capability measurement across training**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t17.multimodal.multimodal_training@1`
- `cap.t17.multimodal.multimodal_training.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.long.long_context_training@1` | use the in-file conservative substitute for `long_context_training` (documented, slower, lower quality) and set `degraded['long_context_training']='local'` |
| `cap.t01.config.config_system@1` | use the in-file conservative substitute for `config_system` (documented, slower, lower quality) and set `degraded['config_system']='local'` |
| `cap.t05.meta.meta_learning_arch@1` | use the in-file conservative substitute for `meta_learning_arch` (documented, slower, lower quality) and set `degraded['meta_learning_arch']='local'` |
| `cap.t06.gating.gating_alternatives@1` | use the in-file conservative substitute for `gating_alternatives` (documented, slower, lower quality) and set `degraded['gating_alternatives']='local'` |
| `cap.t10.commonsense.commonsense_engine@1` | use the in-file conservative substitute for `commonsense_engine` (documented, slower, lower quality) and set `degraded['commonsense_engine']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - modality-balanced batching and loss weighting | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - cross-modal alignment objectives with measured transfer | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - modality-specific data curation and quality control | 520 | Third required mechanism. |
| 6 | Core implementation D - per-modality capability measurement across training | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0830_multimodal_training.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.multimodal.multimodal_training@1`.
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

### P0831 · `agentic_training` — Agentic & Tool-Use Training

| field | value |
|---|---|
| part id | `P0831` (31/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0831_agentic_training.py` |
| module path | `hyperion.t17.training.agentic_training` |
| capability published | `cap.t17.agentic.agentic_training@1` |
| determinism class | `io` |
| p99 latency budget | 35000 ns (35 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0831_agentic_training.txt`](prompts/P0831_agentic_training.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0831-agentic-training) |

**Mission.** Trains long-horizon autonomy in real environments.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **environment-based trajectory collection at scale** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **outcome-based reward with process shaping for long horizons** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **tool-use competence training across thousands of tools**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured agent-benchmark improvement per training phase** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t17.agentic.agentic_training@1`
- `cap.t17.agentic.agentic_training.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.multimodal.multimodal_training@1` | use the in-file conservative substitute for `multimodal_training` (documented, slower, lower quality) and set `degraded['multimodal_training']='local'` |
| `cap.t01.determinism.determinism_replay@1` | use the in-file conservative substitute for `determinism_replay` (documented, slower, lower quality) and set `degraded['determinism_replay']='local'` |
| `cap.t05.architecture.architecture_search@1` | use the in-file conservative substitute for `architecture_search` (documented, slower, lower quality) and set `degraded['architecture_search']='local'` |
| `cap.t06.modality.modality_routing@1` | use the in-file conservative substitute for `modality_routing` (documented, slower, lower quality) and set `degraded['modality_routing']='local'` |
| `cap.t10.parallel.parallel_reasoning@1` | use the in-file conservative substitute for `parallel_reasoning` (documented, slower, lower quality) and set `degraded['parallel_reasoning']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - environment-based trajectory collection at scale | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - outcome-based reward with process shaping for long horizons | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - tool-use competence training across thousands of tools | 520 | Third required mechanism. |
| 6 | Core implementation D - measured agent-benchmark improvement per training phase | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0831_agentic_training.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.agentic.agentic_training@1`.
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

### P0832 · `safety_training` — Safety & Refusal Training

| field | value |
|---|---|
| part id | `P0832` (32/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0832_safety_training.py` |
| module path | `hyperion.t17.training.safety_training` |
| capability published | `cap.t17.safety.safety_training@1` |
| determinism class | `io` |
| p99 latency budget | 36000 ns (36 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0832_safety_training.txt`](prompts/P0832_safety_training.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0832-safety-training) |

**Mission.** Trains judgment, not keyword blocking.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **harm-taxonomy-aligned training data with borderline cases** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **over-refusal prevention with dual-use legitimate-use training**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **jailbreak robustness training against evolving attacks** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured safety/helpfulness Pareto improvement over Opus 5** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t17.safety.safety_training@1`
- `cap.t17.safety.safety_training.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.agentic.agentic_training@1` | use the in-file conservative substitute for `agentic_training` (documented, slower, lower quality) and set `degraded['agentic_training']='local'` |
| `cap.t01.compat.compat_shims@1` | use the in-file conservative substitute for `compat_shims` (documented, slower, lower quality) and set `degraded['compat_shims']='local'` |
| `cap.t05.speculative.speculative_arch_hooks@1` | use the in-file conservative substitute for `speculative_arch_hooks` (documented, slower, lower quality) and set `degraded['speculative_arch_hooks']='local'` |
| `cap.t06.routing.routing_fairness@1` | use the in-file conservative substitute for `routing_fairness` (documented, slower, lower quality) and set `degraded['routing_fairness']='local'` |
| `cap.t10.multi.multi_step_arithmetic@1` | use the in-file conservative substitute for `multi_step_arithmetic` (documented, slower, lower quality) and set `degraded['multi_step_arithmetic']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - harm-taxonomy-aligned training data with borderline cases | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - over-refusal prevention with dual-use legitimate-use training | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - jailbreak robustness training against evolving attacks | 520 | Third required mechanism. |
| 6 | Core implementation D - measured safety/helpfulness Pareto improvement over Opus 5 | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0832_safety_training.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.safety.safety_training@1`.
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

### P0833 · `honesty_training` — Honesty & Calibration Training

| field | value |
|---|---|
| part id | `P0833` (33/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0833_honesty_training.py` |
| module path | `hyperion.t17.training.honesty_training` |
| capability published | `cap.t17.honesty.honesty_training@1` |
| determinism class | `io` |
| p99 latency budget | 37000 ns (37 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0833_honesty_training.txt`](prompts/P0833_honesty_training.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0833-honesty-training) |

**Mission.** Trains the model to know and say what it does not know.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **calibration training with abstention rewards**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **sycophancy and false-agreement suppression training** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **faithful-reasoning training via causal-intervention signals** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured calibration and honesty metric improvements** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t17.honesty.honesty_training@1`
- `cap.t17.honesty.honesty_training.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.safety.safety_training@1` | use the in-file conservative substitute for `safety_training` (documented, slower, lower quality) and set `degraded['safety_training']='local'` |
| `cap.t01.secure.secure_zeroize@1` | use the in-file conservative substitute for `secure_zeroize` (documented, slower, lower quality) and set `degraded['secure_zeroize']='local'` |
| `cap.t05.expert.expert_specialisation@1` | use the in-file conservative substitute for `expert_specialisation` (documented, slower, lower quality) and set `degraded['expert_specialisation']='local'` |
| `cap.t06.router.router_bench@1` | use the in-file conservative substitute for `router_bench` (documented, slower, lower quality) and set `degraded['router_bench']='local'` |
| `cap.t10.error.error_taxonomy@1` | use the in-file conservative substitute for `error_taxonomy` (documented, slower, lower quality) and set `degraded['error_taxonomy']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - calibration training with abstention rewards | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - sycophancy and false-agreement suppression training | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - faithful-reasoning training via causal-intervention signals | 520 | Third required mechanism. |
| 6 | Core implementation D - measured calibration and honesty metric improvements | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0833_honesty_training.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.honesty.honesty_training@1`.
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

### P0834 · `continual_pretraining` — Continual Pretraining & Knowledge Refresh

| field | value |
|---|---|
| part id | `P0834` (34/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0834_continual_pretraining.py` |
| module path | `hyperion.t17.training.continual_pretraining` |
| capability published | `cap.t17.continual.continual_pretraining@1` |
| determinism class | `io` |
| p99 latency budget | 38000 ns (38 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0834_continual_pretraining.txt`](prompts/P0834_continual_pretraining.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0834-continual-pretraining) |

**Mission.** Stays current without forgetting or destabilising.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **knowledge-refresh data pipeline with recency weighting** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **catastrophic-forgetting prevention with measured retention** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **stability of established capabilities across refreshes** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured freshness improvement with retained capability**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t17.continual.continual_pretraining@1`
- `cap.t17.continual.continual_pretraining.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.honesty.honesty_training@1` | use the in-file conservative substitute for `honesty_training` (documented, slower, lower quality) and set `degraded['honesty_training']='local'` |
| `cap.t05.hybrid.hybrid_mixer@1` | use the in-file conservative substitute for `hybrid_mixer` (documented, slower, lower quality) and set `degraded['hybrid_mixer']='local'` |
| `cap.t06.router.router_balance@1` | use the in-file conservative substitute for `router_balance` (documented, slower, lower quality) and set `degraded['router_balance']='local'` |
| `cap.t10.search.search_controller@1` | use the in-file conservative substitute for `search_controller` (documented, slower, lower quality) and set `degraded['search_controller']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - knowledge-refresh data pipeline with recency weighting | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - catastrophic-forgetting prevention with measured retention | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - stability of established capabilities across refreshes | 520 | Third required mechanism. |
| 6 | Core implementation D - measured freshness improvement with retained capability | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0834_continual_pretraining.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.continual.continual_pretraining@1`.
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

### P0835 · `hyperparameter_search` — Hyperparameter Optimisation at Scale

| field | value |
|---|---|
| part id | `P0835` (35/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0835_hyperparameter_search.py` |
| module path | `hyperion.t17.training.hyperparameter_search` |
| capability published | `cap.t17.hyperparameter.hyperparameter_search@1` |
| determinism class | `io` |
| p99 latency budget | 39000 ns (39 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0835_hyperparameter_search.txt`](prompts/P0835_hyperparameter_search.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0835-hyperparameter-search) |

**Mission.** Finds the right settings without wasting a full run.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **small-scale proxy experiments with validated extrapolation** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **multi-fidelity search with early stopping** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **transfer of found settings across scale and architecture changes**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured savings versus naive search** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t17.hyperparameter.hyperparameter_search@1`
- `cap.t17.hyperparameter.hyperparameter_search.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.continual.continual_pretraining@1` | use the in-file conservative substitute for `continual_pretraining` (documented, slower, lower quality) and set `degraded['continual_pretraining']='local'` |
| `cap.t01.envelope.envelope_codec@1` | use the in-file conservative substitute for `envelope_codec` (documented, slower, lower quality) and set `degraded['envelope_codec']='local'` |
| `cap.t05.normalisation.normalisation_design@1` | use the in-file conservative substitute for `normalisation_design` (documented, slower, lower quality) and set `degraded['normalisation_design']='local'` |
| `cap.t06.expert.expert_placement@1` | use the in-file conservative substitute for `expert_placement` (documented, slower, lower quality) and set `degraded['expert_placement']='local'` |
| `cap.t10.self.self_critique@1` | use the in-file conservative substitute for `self_critique` (documented, slower, lower quality) and set `degraded['self_critique']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - small-scale proxy experiments with validated extrapolation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - multi-fidelity search with early stopping | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - transfer of found settings across scale and architecture changes | 520 | Third required mechanism. |
| 6 | Core implementation D - measured savings versus naive search | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0835_hyperparameter_search.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.hyperparameter.hyperparameter_search@1`.
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

### P0836 · `experiment_tracking` — Experiment Management & Provenance

| field | value |
|---|---|
| part id | `P0836` (36/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0836_experiment_tracking.py` |
| module path | `hyperion.t17.training.experiment_tracking` |
| capability published | `cap.t17.experiment.experiment_tracking@1` |
| determinism class | `io` |
| p99 latency budget | 40000 ns (40 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0836_experiment_tracking.txt`](prompts/P0836_experiment_tracking.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0836-experiment-tracking) |

**Mission.** Thousands of experiments, all reproducible.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **experiment metadata, code, data and config versioning** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **result database with statistical comparison tooling**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **reproducibility verification by re-running sampled experiments** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **provenance completeness audit** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t17.experiment.experiment_tracking@1`
- `cap.t17.experiment.experiment_tracking.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.hyperparameter.hyperparameter_search@1` | use the in-file conservative substitute for `hyperparameter_search` (documented, slower, lower quality) and set `degraded['hyperparameter_search']='local'` |
| `cap.t01.dataflow.dataflow_dag@1` | use the in-file conservative substitute for `dataflow_dag` (documented, slower, lower quality) and set `degraded['dataflow_dag']='local'` |
| `cap.t05.multi.multi_token_prediction@1` | use the in-file conservative substitute for `multi_token_prediction` (documented, slower, lower quality) and set `degraded['multi_token_prediction']='local'` |
| `cap.t06.sparse.sparse_activation_stats@1` | use the in-file conservative substitute for `sparse_activation_stats` (documented, slower, lower quality) and set `degraded['sparse_activation_stats']='local'` |
| `cap.t10.abstraction.abstraction_engine@1` | use the in-file conservative substitute for `abstraction_engine` (documented, slower, lower quality) and set `degraded['abstraction_engine']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - experiment metadata, code, data and config versioning | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - result database with statistical comparison tooling | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - reproducibility verification by re-running sampled experiments | 520 | Third required mechanism. |
| 6 | Core implementation D - provenance completeness audit | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0836_experiment_tracking.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.experiment.experiment_tracking@1`.
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

### P0837 · `ablation_framework` — Systematic Ablation Framework

| field | value |
|---|---|
| part id | `P0837` (37/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0837_ablation_framework.py` |
| module path | `hyperion.t17.training.ablation_framework` |
| capability published | `cap.t17.ablation.ablation_framework@1` |
| determinism class | `io` |
| p99 latency budget | 41000 ns (41 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0837_ablation_framework.txt`](prompts/P0837_ablation_framework.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0837-ablation-framework) |

**Mission.** Every claimed improvement isolated and proven.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **automated ablation-matrix execution with matched compute**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **variance estimation and significance testing** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **interaction-effect detection between changes** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **ablation-report generation for every major decision** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t17.ablation.ablation_framework@1`
- `cap.t17.ablation.ablation_framework.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.experiment.experiment_tracking@1` | use the in-file conservative substitute for `experiment_tracking` (documented, slower, lower quality) and set `degraded['experiment_tracking']='local'` |
| `cap.t01.serialization.serialization_schema@1` | use the in-file conservative substitute for `serialization_schema` (documented, slower, lower quality) and set `degraded['serialization_schema']='local'` |
| `cap.t05.program.program_induction_arch@1` | use the in-file conservative substitute for `program_induction_arch` (documented, slower, lower quality) and set `degraded['program_induction_arch']='local'` |
| `cap.t06.router.router_robustness@1` | use the in-file conservative substitute for `router_robustness` (documented, slower, lower quality) and set `degraded['router_robustness']='local'` |
| `cap.t10.spatial.spatial_reasoning@1` | use the in-file conservative substitute for `spatial_reasoning` (documented, slower, lower quality) and set `degraded['spatial_reasoning']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - automated ablation-matrix execution with matched compute | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - variance estimation and significance testing | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - interaction-effect detection between changes | 520 | Third required mechanism. |
| 6 | Core implementation D - ablation-report generation for every major decision | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0837_ablation_framework.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.ablation.ablation_framework@1`.
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

### P0838 · `scaling_prediction` — Scaling Prediction & Run Planning

| field | value |
|---|---|
| part id | `P0838` (38/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0838_scaling_prediction.py` |
| module path | `hyperion.t17.training.scaling_prediction` |
| capability published | `cap.t17.scaling.scaling_prediction@1` |
| determinism class | `io` |
| p99 latency budget | 42000 ns (42 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0838_scaling_prediction.txt`](prompts/P0838_scaling_prediction.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0838-scaling-prediction) |

**Mission.** Knows what a run will produce before spending on it.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **scaling-law fitting with uncertainty for each capability** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **compute-allocation planning across model, data and RL phases** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **prediction-accuracy tracking against realised runs** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured planning accuracy improvement over time**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t17.scaling.scaling_prediction@1`
- `cap.t17.scaling.scaling_prediction.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.ablation.ablation_framework@1` | use the in-file conservative substitute for `ablation_framework` (documented, slower, lower quality) and set `degraded['ablation_framework']='local'` |
| `cap.t01.bench.bench_harness@1` | use the in-file conservative substitute for `bench_harness` (documented, slower, lower quality) and set `degraded['bench_harness']='local'` |
| `cap.t05.init.init_scaling_laws@1` | use the in-file conservative substitute for `init_scaling_laws` (documented, slower, lower quality) and set `degraded['init_scaling_laws']='local'` |
| `cap.t06.sparse.sparse_kernels_bridge@1` | use the in-file conservative substitute for `sparse_kernels_bridge` (documented, slower, lower quality) and set `degraded['sparse_kernels_bridge']='local'` |
| `cap.t10.chain.chain_compression@1` | use the in-file conservative substitute for `chain_compression` (documented, slower, lower quality) and set `degraded['chain_compression']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - scaling-law fitting with uncertainty for each capability | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - compute-allocation planning across model, data and RL phases | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - prediction-accuracy tracking against realised runs | 520 | Third required mechanism. |
| 6 | Core implementation D - measured planning accuracy improvement over time | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0838_scaling_prediction.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.scaling.scaling_prediction@1`.
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

### P0839 · `self_improvement_loop` — Recursive Self-Improvement Loop

| field | value |
|---|---|
| part id | `P0839` (39/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0839_self_improvement_loop.py` |
| module path | `hyperion.t17.training.self_improvement_loop` |
| capability published | `cap.t17.self.self_improvement_loop@1` |
| determinism class | `io` |
| p99 latency budget | 43000 ns (43 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0839_self_improvement_loop.txt`](prompts/P0839_self_improvement_loop.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0839-self-improvement-loop) |

**Mission.** The system improves itself, measurably and safely.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **gap identification from benchmark and production failure analysis** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **automated improvement-hypothesis generation and experiment execution** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **human-approval gates before any weight-affecting change**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured improvement rate per cycle with safety verification** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t17.self.self_improvement_loop@1`
- `cap.t17.self.self_improvement_loop.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.scaling.scaling_prediction@1` | use the in-file conservative substitute for `scaling_prediction` (documented, slower, lower quality) and set `degraded['scaling_prediction']='local'` |
| `cap.t01.abi.abi_stability@1` | use the in-file conservative substitute for `abi_stability` (documented, slower, lower quality) and set `degraded['abi_stability']='local'` |
| `cap.t05.memory.memory_attention_bridge@1` | use the in-file conservative substitute for `memory_attention_bridge` (documented, slower, lower quality) and set `degraded['memory_attention_bridge']='local'` |
| `cap.t06.expert.expert_warmup@1` | use the in-file conservative substitute for `expert_warmup` (documented, slower, lower quality) and set `degraded['expert_warmup']='local'` |
| `cap.t10.reasoning.reasoning_robustness@1` | use the in-file conservative substitute for `reasoning_robustness` (documented, slower, lower quality) and set `degraded['reasoning_robustness']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - gap identification from benchmark and production failure analysi | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - automated improvement-hypothesis generation and experiment execu | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - human-approval gates before any weight-affecting change | 520 | Third required mechanism. |
| 6 | Core implementation D - measured improvement rate per cycle with safety verification | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0839_self_improvement_loop.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.self.self_improvement_loop@1`.
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

### P0840 · `automated_research` — Automated ML Research Agent

| field | value |
|---|---|
| part id | `P0840` (40/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0840_automated_research.py` |
| module path | `hyperion.t17.training.automated_research` |
| capability published | `cap.t17.automated.automated_research@1` |
| determinism class | `io` |
| p99 latency budget | 44000 ns (44 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0840_automated_research.txt`](prompts/P0840_automated_research.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0840-automated-research) |

**Mission.** Uses the system's own agent capability to advance itself.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **literature synthesis and idea generation with novelty checking** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **experiment implementation, execution and honest analysis**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **negative-result reporting and hypothesis retirement** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured research-throughput and hit-rate** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t17.automated.automated_research@1`
- `cap.t17.automated.automated_research.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.self.self_improvement_loop@1` | use the in-file conservative substitute for `self_improvement_loop` (documented, slower, lower quality) and set `degraded['self_improvement_loop']='local'` |
| `cap.t01.retry.retry_idempotency@1` | use the in-file conservative substitute for `retry_idempotency` (documented, slower, lower quality) and set `degraded['retry_idempotency']='local'` |
| `cap.t05.thought.thought_representation@1` | use the in-file conservative substitute for `thought_representation` (documented, slower, lower quality) and set `degraded['thought_representation']='local'` |
| `cap.t06.hierarchical.hierarchical_routing@1` | use the in-file conservative substitute for `hierarchical_routing` (documented, slower, lower quality) and set `degraded['hierarchical_routing']='local'` |
| `cap.t10.reasoning.reasoning_transfer@1` | use the in-file conservative substitute for `reasoning_transfer` (documented, slower, lower quality) and set `degraded['reasoning_transfer']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - literature synthesis and idea generation with novelty checking | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - experiment implementation, execution and honest analysis | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - negative-result reporting and hypothesis retirement | 520 | Third required mechanism. |
| 6 | Core implementation D - measured research-throughput and hit-rate | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0840_automated_research.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.automated.automated_research@1`.
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

### P0841 · `capability_gap_analysis` — Capability Gap Analysis & Prioritisation

| field | value |
|---|---|
| part id | `P0841` (41/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0841_capability_gap_analysis.py` |
| module path | `hyperion.t17.training.capability_gap_analysis` |
| capability published | `cap.t17.capability.capability_gap_analysis@1` |
| determinism class | `io` |
| p99 latency budget | 45000 ns (45 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0841_capability_gap_analysis.txt`](prompts/P0841_capability_gap_analysis.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0841-capability-gap-analysis) |

**Mission.** Always knows the single highest-value thing to improve.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **benchmark and production failure taxonomy with volume weighting**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **gap-to-target quantification per capability** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **prioritised improvement roadmap with projected impact** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **prediction accuracy of projected impact versus realised** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t17.capability.capability_gap_analysis@1`
- `cap.t17.capability.capability_gap_analysis.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.automated.automated_research@1` | use the in-file conservative substitute for `automated_research` (documented, slower, lower quality) and set `degraded['automated_research']='local'` |
| `cap.t05.omega.omega_block@1` | use the in-file conservative substitute for `omega_block` (documented, slower, lower quality) and set `degraded['omega_block']='local'` |
| `cap.t06.router.router_core@1` | use the in-file conservative substitute for `router_core` (documented, slower, lower quality) and set `degraded['router_core']='local'` |
| `cap.t10.thought.thought_program_ir@1` | use the in-file conservative substitute for `thought_program_ir` (documented, slower, lower quality) and set `degraded['thought_program_ir']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - benchmark and production failure taxonomy with volume weighting | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - gap-to-target quantification per capability | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - prioritised improvement roadmap with projected impact | 520 | Third required mechanism. |
| 6 | Core implementation D - prediction accuracy of projected impact versus realised | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0841_capability_gap_analysis.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.capability.capability_gap_analysis@1`.
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

### P0842 · `training_data_governance` — Data Governance, Consent & Deletion

| field | value |
|---|---|
| part id | `P0842` (42/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0842_training_data_governance.py` |
| module path | `hyperion.t17.training.training_data_governance` |
| capability published | `cap.t17.training.training_data_governance@1` |
| determinism class | `io` |
| p99 latency budget | 46000 ns (46 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0842_training_data_governance.txt`](prompts/P0842_training_data_governance.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0842-training-data-governance) |

**Mission.** Respects data rights throughout the model lifecycle.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **consent and opt-out tracking through to training influence** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **deletion-request handling including influence-removal strategy** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **regional data-residency and regulatory compliance** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **auditable governance-compliance report**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t17.training.training_data_governance@1`
- `cap.t17.training.training_data_governance.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.capability.capability_gap_analysis@1` | use the in-file conservative substitute for `capability_gap_analysis` (documented, slower, lower quality) and set `degraded['capability_gap_analysis']='local'` |
| `cap.t01.omega.omega_bus_ipc@1` | use the in-file conservative substitute for `omega_bus_ipc` (documented, slower, lower quality) and set `degraded['omega_bus_ipc']='local'` |
| `cap.t05.adaptive.adaptive_depth@1` | use the in-file conservative substitute for `adaptive_depth` (documented, slower, lower quality) and set `degraded['adaptive_depth']='local'` |
| `cap.t06.fine.fine_grained_experts@1` | use the in-file conservative substitute for `fine_grained_experts` (documented, slower, lower quality) and set `degraded['fine_grained_experts']='local'` |
| `cap.t10.self.self_consistency@1` | use the in-file conservative substitute for `self_consistency` (documented, slower, lower quality) and set `degraded['self_consistency']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - consent and opt-out tracking through to training influence | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - deletion-request handling including influence-removal strategy | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - regional data-residency and regulatory compliance | 520 | Third required mechanism. |
| 6 | Core implementation D - auditable governance-compliance report | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0842_training_data_governance.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.training.training_data_governance@1`.
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

### P0843 · `memorisation_analysis` — Memorisation & Privacy Leakage Analysis

| field | value |
|---|---|
| part id | `P0843` (43/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0843_memorisation_analysis.py` |
| module path | `hyperion.t17.training.memorisation_analysis` |
| capability published | `cap.t17.memorisation.memorisation_analysis@1` |
| determinism class | `io` |
| p99 latency budget | 47000 ns (47 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0843_memorisation_analysis.txt`](prompts/P0843_memorisation_analysis.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0843-memorisation-analysis) |

**Mission.** Ensures training data cannot be extracted.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **extraction-attack testing across data types** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **memorisation measurement and per-example influence estimation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **differential-privacy option with utility-cost measurement**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured extraction resistance versus baselines** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t17.memorisation.memorisation_analysis@1`
- `cap.t17.memorisation.memorisation_analysis.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.training.training_data_governance@1` | use the in-file conservative substitute for `training_data_governance` (documented, slower, lower quality) and set `degraded['training_data_governance']='local'` |
| `cap.t01.task.task_runtime@1` | use the in-file conservative substitute for `task_runtime` (documented, slower, lower quality) and set `degraded['task_runtime']='local'` |
| `cap.t05.long.long_context_arch@1` | use the in-file conservative substitute for `long_context_arch` (documented, slower, lower quality) and set `degraded['long_context_arch']='local'` |
| `cap.t06.router.router_temperature@1` | use the in-file conservative substitute for `router_temperature` (documented, slower, lower quality) and set `degraded['router_temperature']='local'` |
| `cap.t10.analogy.analogy_engine@1` | use the in-file conservative substitute for `analogy_engine` (documented, slower, lower quality) and set `degraded['analogy_engine']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - extraction-attack testing across data types | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - memorisation measurement and per-example influence estimation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - differential-privacy option with utility-cost measurement | 520 | Third required mechanism. |
| 6 | Core implementation D - measured extraction resistance versus baselines | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0843_memorisation_analysis.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.memorisation.memorisation_analysis@1`.
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

### P0844 · `training_reproducibility` — Training Reproducibility & Determinism

| field | value |
|---|---|
| part id | `P0844` (44/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0844_training_reproducibility.py` |
| module path | `hyperion.t17.training.training_reproducibility` |
| capability published | `cap.t17.training.training_reproducibility@1` |
| determinism class | `io` |
| p99 latency budget | 48000 ns (48 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0844_training_reproducibility.txt`](prompts/P0844_training_reproducibility.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0844-training-reproducibility) |

**Mission.** The same run twice produces the same model.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **full nondeterminism-source control (seeds, data order, kernels, collectives)** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **bit-exact reproduction verification at reduced scale**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **documented exceptions with quantified variance** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **reproducibility package for every released model** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t17.training.training_reproducibility@1`
- `cap.t17.training.training_reproducibility.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.memorisation.memorisation_analysis@1` | use the in-file conservative substitute for `memorisation_analysis` (documented, slower, lower quality) and set `degraded['memorisation_analysis']='local'` |
| `cap.t01.arena.arena_graph@1` | use the in-file conservative substitute for `arena_graph` (documented, slower, lower quality) and set `degraded['arena_graph']='local'` |
| `cap.t05.symbolic.symbolic_bridge@1` | use the in-file conservative substitute for `symbolic_bridge` (documented, slower, lower quality) and set `degraded['symbolic_bridge']='local'` |
| `cap.t06.mod.mod_routing@1` | use the in-file conservative substitute for `mod_routing` (documented, slower, lower quality) and set `degraded['mod_routing']='local'` |
| `cap.t10.temporal.temporal_reasoning@1` | use the in-file conservative substitute for `temporal_reasoning` (documented, slower, lower quality) and set `degraded['temporal_reasoning']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - full nondeterminism-source control (seeds, data order, kernels,  | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - bit-exact reproduction verification at reduced scale | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - documented exceptions with quantified variance | 520 | Third required mechanism. |
| 6 | Core implementation D - reproducibility package for every released model | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0844_training_reproducibility.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.training.training_reproducibility@1`.
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

### P0845 · `model_release_gate` — Model Release Gate & Sign-Off

| field | value |
|---|---|
| part id | `P0845` (45/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0845_model_release_gate.py` |
| module path | `hyperion.t17.training.model_release_gate` |
| capability published | `cap.t17.model.model_release_gate@1` |
| determinism class | `io` |
| p99 latency budget | 49000 ns (49 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0845_model_release_gate.txt`](prompts/P0845_model_release_gate.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0845-model-release-gate) |

**Mission.** Nothing ships without passing every gate.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **release-criteria checklist across capability, safety and efficiency**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **regression detection against the previous release** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **sign-off workflow with documented accountability** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **post-release monitoring plan requirement** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t17.model.model_release_gate@1`
- `cap.t17.model.model_release_gate.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.training.training_reproducibility@1` | use the in-file conservative substitute for `training_reproducibility` (documented, slower, lower quality) and set `degraded['training_reproducibility']='local'` |
| `cap.t01.fuzz.fuzz_engine@1` | use the in-file conservative substitute for `fuzz_engine` (documented, slower, lower quality) and set `degraded['fuzz_engine']='local'` |
| `cap.t05.weight.weight_sharing@1` | use the in-file conservative substitute for `weight_sharing` (documented, slower, lower quality) and set `degraded['weight_sharing']='local'` |
| `cap.t06.expert.expert_dropout@1` | use the in-file conservative substitute for `expert_dropout` (documented, slower, lower quality) and set `degraded['expert_dropout']='local'` |
| `cap.t10.reasoning.reasoning_memory@1` | use the in-file conservative substitute for `reasoning_memory` (documented, slower, lower quality) and set `degraded['reasoning_memory']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - release-criteria checklist across capability, safety and efficie | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - regression detection against the previous release | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - sign-off workflow with documented accountability | 520 | Third required mechanism. |
| 6 | Core implementation D - post-release monitoring plan requirement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0845_model_release_gate.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.model.model_release_gate@1`.
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

### P0846 · `training_cost_model` — Training Cost & Carbon Accounting

| field | value |
|---|---|
| part id | `P0846` (46/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0846_training_cost_model.py` |
| module path | `hyperion.t17.training.training_cost_model` |
| capability published | `cap.t17.training.training_cost_model@1` |
| determinism class | `io` |
| p99 latency budget | 3000 ns (3 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0846_training_cost_model.txt`](prompts/P0846_training_cost_model.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0846-training-cost-model) |

**Mission.** Full transparency on what building this costs.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **compute, energy and carbon accounting per run and per capability gain** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **cost-efficiency comparison against published frontier runs** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **forecast accuracy for planned runs** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **efficiency-improvement tracking over time**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t17.training.training_cost_model@1`
- `cap.t17.training.training_cost_model.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.model.model_release_gate@1` | use the in-file conservative substitute for `model_release_gate` (documented, slower, lower quality) and set `degraded['model_release_gate']='local'` |
| `cap.t01.manifest.manifest_parser@1` | use the in-file conservative substitute for `manifest_parser` (documented, slower, lower quality) and set `degraded['manifest_parser']='local'` |
| `cap.t05.action.action_head@1` | use the in-file conservative substitute for `action_head` (documented, slower, lower quality) and set `degraded['action_head']='local'` |
| `cap.t06.router.router_cache@1` | use the in-file conservative substitute for `router_cache` (documented, slower, lower quality) and set `degraded['router_cache']='local'` |
| `cap.t10.reasoning.reasoning_faithfulness@1` | use the in-file conservative substitute for `reasoning_faithfulness` (documented, slower, lower quality) and set `degraded['reasoning_faithfulness']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - compute, energy and carbon accounting per run and per capability | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - cost-efficiency comparison against published frontier runs | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - forecast accuracy for planned runs | 520 | Third required mechanism. |
| 6 | Core implementation D - efficiency-improvement tracking over time | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0846_training_cost_model.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.training.training_cost_model@1`.
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

### P0847 · `fine_tune_service` — Customer Fine-Tuning Infrastructure

| field | value |
|---|---|
| part id | `P0847` (47/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0847_fine_tune_service.py` |
| module path | `hyperion.t17.training.fine_tune_service` |
| capability published | `cap.t17.fine.fine_tune_service@1` |
| determinism class | `io` |
| p99 latency budget | 4000 ns (4 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0847_fine_tune_service.txt`](prompts/P0847_fine_tune_service.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0847-fine-tune-service) |

**Mission.** Lets others specialise the model safely.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **adapter and full fine-tune pipelines with isolation guarantees** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **safety-property preservation verification after customer tuning** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **quality-regression detection and customer reporting**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured customisation quality and safety retention** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t17.fine.fine_tune_service@1`
- `cap.t17.fine.fine_tune_service.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.training.training_cost_model@1` | use the in-file conservative substitute for `training_cost_model` (documented, slower, lower quality) and set `degraded['training_cost_model']='local'` |
| `cap.t01.circuit.circuit_breaker@1` | use the in-file conservative substitute for `circuit_breaker` (documented, slower, lower quality) and set `degraded['circuit_breaker']='local'` |
| `cap.t05.prompt.prompt_representation@1` | use the in-file conservative substitute for `prompt_representation` (documented, slower, lower quality) and set `degraded['prompt_representation']='local'` |
| `cap.t06.routing.routing_privacy@1` | use the in-file conservative substitute for `routing_privacy` (documented, slower, lower quality) and set `degraded['routing_privacy']='local'` |
| `cap.t10.subgoal.subgoal_caching@1` | use the in-file conservative substitute for `subgoal_caching` (documented, slower, lower quality) and set `degraded['subgoal_caching']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - adapter and full fine-tune pipelines with isolation guarantees | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - safety-property preservation verification after customer tuning | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - quality-regression detection and customer reporting | 520 | Third required mechanism. |
| 6 | Core implementation D - measured customisation quality and safety retention | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0847_fine_tune_service.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.fine.fine_tune_service@1`.
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

### P0848 · `eval_driven_training` — Evaluation-Driven Training Loop

| field | value |
|---|---|
| part id | `P0848` (48/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0848_eval_driven_training.py` |
| module path | `hyperion.t17.training.eval_driven_training` |
| capability published | `cap.t17.eval.eval_driven_training@1` |
| determinism class | `io` |
| p99 latency budget | 5000 ns (5 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0848_eval_driven_training.txt`](prompts/P0848_eval_driven_training.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0848-eval-driven-training) |

**Mission.** Closes the loop between measurement and improvement.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **automatic training-signal generation from evaluation failures** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **Frontier-Bench v0.1**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **contamination-safe use of evaluation-derived data**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **improvement verification on sealed held-out sets** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured gain rate with contamination guarantees** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t17.eval.eval_driven_training@1`
- `cap.t17.eval.eval_driven_training.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.fine.fine_tune_service@1` | use the in-file conservative substitute for `fine_tune_service` (documented, slower, lower quality) and set `degraded['fine_tune_service']='local'` |
| `cap.t01.shutdown.shutdown_drain@1` | use the in-file conservative substitute for `shutdown_drain` (documented, slower, lower quality) and set `degraded['shutdown_drain']='local'` |
| `cap.t05.arch.arch_spec_doc@1` | use the in-file conservative substitute for `arch_spec_doc` (documented, slower, lower quality) and set `degraded['arch_spec_doc']='local'` |
| `cap.t06.moe.moe_spec_doc@1` | use the in-file conservative substitute for `moe_spec_doc` (documented, slower, lower quality) and set `degraded['moe_spec_doc']='local'` |
| `cap.t10.reasoning.reasoning_spec_doc@1` | use the in-file conservative substitute for `reasoning_spec_doc` (documented, slower, lower quality) and set `degraded['reasoning_spec_doc']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - automatic training-signal generation from evaluation failures | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - contamination-safe use of evaluation-derived data | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - improvement verification on sealed held-out sets | 520 | Third required mechanism. |
| 6 | Core implementation D - measured gain rate with contamination guarantees | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0848_eval_driven_training.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.eval.eval_driven_training@1`.
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

### P0849 · `training_bench` — Training Infrastructure Benchmark Suite

| field | value |
|---|---|
| part id | `P0849` (49/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0849_training_bench.py` |
| module path | `hyperion.t17.training.training_bench` |
| capability published | `cap.t17.training.training_bench@1` |
| determinism class | `io` |
| p99 latency budget | 6000 ns (6 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0849_training_bench.txt`](prompts/P0849_training_bench.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0849-training-bench) |

**Mission.** Measures the training system itself.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **throughput, utilisation and scaling-efficiency benchmarks**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **stability and recovery benchmarks under injected faults** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **comparison against published large-scale training efficiency** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **regression gates for infrastructure changes** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t17.training.training_bench@1`
- `cap.t17.training.training_bench.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.eval.eval_driven_training@1` | use the in-file conservative substitute for `eval_driven_training` (documented, slower, lower quality) and set `degraded['eval_driven_training']='local'` |
| `cap.t05.latent.latent_program_slots@1` | use the in-file conservative substitute for `latent_program_slots` (documented, slower, lower quality) and set `degraded['latent_program_slots']='local'` |
| `cap.t06.shared.shared_expert@1` | use the in-file conservative substitute for `shared_expert` (documented, slower, lower quality) and set `degraded['shared_expert']='local'` |
| `cap.t10.outcome.outcome_verifier@1` | use the in-file conservative substitute for `outcome_verifier` (documented, slower, lower quality) and set `degraded['outcome_verifier']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - throughput, utilisation and scaling-efficiency benchmarks | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - stability and recovery benchmarks under injected faults | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - comparison against published large-scale training efficiency | 520 | Third required mechanism. |
| 6 | Core implementation D - regression gates for infrastructure changes | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0849_training_bench.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.training.training_bench@1`.
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

### P0850 · `training_spec_doc` — Training Specification & Model Card Generator

| field | value |
|---|---|
| part id | `P0850` (50/50 of T17) |
| tier | `T17` — Training, Data & Recursive Self-Improvement |
| language | Python 3.13 |
| file to produce | `parts/t17_training/P0850_training_spec_doc.py` |
| module path | `hyperion.t17.training.training_spec_doc` |
| capability published | `cap.t17.training.training_spec_doc@1` |
| determinism class | `io` |
| p99 latency budget | 7000 ns (7 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | Frontier-Bench v0.1, ARC-AGI-3 |
| worker prompt | [`prompts/P0850_training_spec_doc.txt`](prompts/P0850_training_spec_doc.txt) · [inline](docs/PROMPTS_T17.md#prompt-p0850-training-spec-doc) |

**Mission.** The authoritative record of how the model was made.

**Tier context.** Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.

**Mandate — all four items are required; none is optional.**

1. Implement **model card generation with data, method, evaluation and limitation sections** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Frontier-Bench v0.1** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **training-decision rationale documentation with evidence links** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **honest capability and risk disclosure** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **Frontier-Bench v0.1** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **drift detection between documentation and actual training**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t17.training.training_spec_doc@1`
- `cap.t17.training.training_spec_doc.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t17.training.training_bench@1` | use the in-file conservative substitute for `training_bench` (documented, slower, lower quality) and set `degraded['training_bench']='local'` |
| `cap.t01.atomics.atomics_sync@1` | use the in-file conservative substitute for `atomics_sync` (documented, slower, lower quality) and set `degraded['atomics_sync']='local'` |
| `cap.t05.positional.positional_design@1` | use the in-file conservative substitute for `positional_design` (documented, slower, lower quality) and set `degraded['positional_design']='local'` |
| `cap.t06.expert.expert_diversity@1` | use the in-file conservative substitute for `expert_diversity` (documented, slower, lower quality) and set `degraded['expert_diversity']='local'` |
| `cap.t10.constraint.constraint_reasoning@1` | use the in-file conservative substitute for `constraint_reasoning` (documented, slower, lower quality) and set `degraded['constraint_reasoning']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - model card generation with data, method, evaluation and limitati | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - training-decision rationale documentation with evidence links | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - honest capability and risk disclosure | 520 | Third required mechanism. |
| 6 | Core implementation D - drift detection between documentation and actual training | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t17_training/P0850_training_spec_doc.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t17.training.training_spec_doc@1`.
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
