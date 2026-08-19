# HYPERION-Ω — Part specifications · T18 · Evaluation, Benchmarking & Dominance Proofs

> Contract: **Ω-CONTRACT v1.0.0-frozen** · 50 parts · 250,000 lines of code · language: Python 3.13

**Tier mission.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Benchmarks this tier is accountable for.** SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo)

**Tier dependencies.** T01, T12, T13

Each part below is built by exactly one isolated Opus 5 worker that sees only: this specification, the frozen Ω-Contract, and its own prompt. Workers never see each other's files. Link-compatibility comes from the contract, not from coordination.

| part | slug | title | capability |
|---|---|---|---|
| [P0851](#p0851-eval-framework) | `eval_framework` | Evaluation Framework Core | `cap.t18.eval.eval_framework@1` |
| [P0852](#p0852-eval-registry) | `eval_registry` | Benchmark Registry & Versioning | `cap.t18.eval.eval_registry@1` |
| [P0853](#p0853-grading-engine) | `grading_engine` | Automatic Grading & Answer Equivalence | `cap.t18.grading.grading_engine@1` |
| [P0854](#p0854-human-eval-protocol) | `human_eval_protocol` | Human Evaluation Protocol & Rater Management | `cap.t18.human.human_eval_protocol@1` |
| [P0855](#p0855-expert-eval) | `expert_eval` | Expert Domain Evaluation | `cap.t18.expert.expert_eval@1` |
| [P0856](#p0856-elo-arena) | `elo_arena` | Pairwise Comparison & Elo Rating System | `cap.t18.elo.elo_arena@1` |
| [P0857](#p0857-statistical-engine) | `statistical_engine` | Statistical Analysis Engine | `cap.t18.statistical.statistical_engine@1` |
| [P0858](#p0858-variance-control) | `variance_control` | Variance Reduction & Run Repetition Policy | `cap.t18.variance.variance_control@1` |
| [P0859](#p0859-contamination-audit) | `contamination_audit` | Contamination Auditing & Sealed Test Sets | `cap.t18.contamination.contamination_audit@1` |
| [P0860](#p0860-swe-verified-eval) | `swe_verified_eval` | SWE-bench Verified Evaluation | `cap.t18.swe.swe_verified_eval@1` |
| [P0861](#p0861-swe-pro-eval) | `swe_pro_eval` | SWE-bench Pro Evaluation | `cap.t18.swe.swe_pro_eval@1` |
| [P0862](#p0862-frontier-bench-eval) | `frontier_bench_eval` | Frontier-Bench & Long-Horizon Coding Evaluation | `cap.t18.frontier.frontier_bench_eval@1` |
| [P0863](#p0863-terminal-bench-eval) | `terminal_bench_eval` | Terminal-Bench Evaluation | `cap.t18.terminal.terminal_bench_eval@1` |
| [P0864](#p0864-arc-agi-eval) | `arc_agi_eval` | ARC-AGI-2 and ARC-AGI-3 Evaluation | `cap.t18.arc.arc_agi_eval@1` |
| [P0865](#p0865-gpqa-eval) | `gpqa_eval` | GPQA Diamond & Expert Knowledge Evaluation | `cap.t18.gpqa.gpqa_eval@1` |
| [P0866](#p0866-math-eval) | `math_eval` | Mathematics Competition Evaluation | `cap.t18.math.math_eval@1` |
| [P0867](#p0867-mmmu-eval) | `mmmu_eval` | Multimodal Understanding Evaluation | `cap.t18.mmmu.mmmu_eval@1` |
| [P0868](#p0868-osworld-eval) | `osworld_eval` | OSWorld and Computer Use Evaluation | `cap.t18.osworld.osworld_eval@1` |
| [P0869](#p0869-browsecomp-eval) | `browsecomp_eval` | Web Research & Browsing Evaluation | `cap.t18.browsecomp.browsecomp_eval@1` |
| [P0870](#p0870-automation-bench-eval) | `automation_bench_eval` | Business Automation Evaluation | `cap.t18.automation.automation_bench_eval@1` |
| [P0871](#p0871-gdpval-eval) | `gdpval_eval` | Economic Knowledge Work Evaluation | `cap.t18.gdpval.gdpval_eval@1` |
| [P0872](#p0872-lifescience-eval) | `lifescience_eval` | Life Sciences Evaluation Suite | `cap.t18.lifescience.lifescience_eval@1` |
| [P0873](#p0873-security-eval) | `security_eval` | Security & Vulnerability Discovery Evaluation | `cap.t18.security.security_eval@1` |
| [P0874](#p0874-longcontext-eval) | `longcontext_eval` | Long Context Evaluation Suite | `cap.t18.longcontext.longcontext_eval@1` |
| [P0875](#p0875-instruction-following-eval) | `instruction_following_eval` | Instruction Following & Constraint Adherence | `cap.t18.instruction.instruction_following_eval@1` |
| [P0876](#p0876-hallucination-eval) | `hallucination_eval` | Hallucination & Factuality Evaluation | `cap.t18.hallucination.hallucination_eval@1` |
| [P0877](#p0877-calibration-eval) | `calibration_eval` | Calibration & Uncertainty Evaluation | `cap.t18.calibration.calibration_eval@1` |
| [P0878](#p0878-robustness-eval) | `robustness_eval` | Robustness & Consistency Evaluation | `cap.t18.robustness.robustness_eval@1` |
| [P0879](#p0879-adversarial-eval) | `adversarial_eval` | Adversarial & Jailbreak Evaluation | `cap.t18.adversarial.adversarial_eval@1` |
| [P0880](#p0880-bias-fairness-eval) | `bias_fairness_eval` | Bias & Fairness Evaluation | `cap.t18.bias.bias_fairness_eval@1` |
| [P0881](#p0881-multilingual-eval) | `multilingual_eval` | Multilingual Capability Evaluation | `cap.t18.multilingual.multilingual_eval@1` |
| [P0882](#p0882-efficiency-eval) | `efficiency_eval` | Efficiency & Cost Evaluation | `cap.t18.efficiency.efficiency_eval@1` |
| [P0883](#p0883-speed-eval) | `speed_eval` | Speed & Latency Benchmark Suite | `cap.t18.speed.speed_eval@1` |
| [P0884](#p0884-regression-suite) | `regression_suite` | Continuous Regression Evaluation | `cap.t18.regression.regression_suite@1` |
| [P0885](#p0885-canary-eval) | `canary_eval` | Production Canary & Online Evaluation | `cap.t18.canary.canary_eval@1` |
| [P0886](#p0886-failure-taxonomy) | `failure_taxonomy` | Failure Taxonomy & Error Analysis Engine | `cap.t18.failure.failure_taxonomy@1` |
| [P0887](#p0887-capability-map) | `capability_map` | Capability Map & Frontier Tracking | `cap.t18.capability.capability_map@1` |
| [P0888](#p0888-competitor-tracking) | `competitor_tracking` | Competitor Benchmark Tracking | `cap.t18.competitor.competitor_tracking@1` |
| [P0889](#p0889-eval-cost-control) | `eval_cost_control` | Evaluation Cost Management | `cap.t18.eval.eval_cost_control@1` |
| [P0890](#p0890-eval-infrastructure) | `eval_infrastructure` | Evaluation Infrastructure & Orchestration | `cap.t18.eval.eval_infrastructure@1` |
| [P0891](#p0891-benchmark-construction) | `benchmark_construction` | New Benchmark Construction | `cap.t18.benchmark.benchmark_construction@1` |
| [P0892](#p0892-dynamic-benchmark) | `dynamic_benchmark` | Dynamic & Contamination-Resistant Benchmarks | `cap.t18.dynamic.dynamic_benchmark@1` |
| [P0893](#p0893-eval-reproducibility) | `eval_reproducibility` | Evaluation Reproducibility Package | `cap.t18.eval.eval_reproducibility@1` |
| [P0894](#p0894-dominance-proof) | `dominance_proof` | Opus 5 Dominance Proof Generator | `cap.t18.dominance.dominance_proof@1` |
| [P0895](#p0895-eval-dashboard) | `eval_dashboard` | Evaluation Result Data Products | `cap.t18.eval.eval_dashboard@1` |
| [P0896](#p0896-eval-meta) | `eval_meta` | Meta-Evaluation: Evaluating the Evaluations | `cap.t18.eval.eval_meta@1` |
| [P0897](#p0897-safety-eval-bridge) | `safety_eval_bridge` | Safety Evaluation Integration | `cap.t18.safety.safety_eval_bridge@1` |
| [P0898](#p0898-eval-release-report) | `eval_release_report` | Release Evaluation Report Generator | `cap.t18.eval.eval_release_report@1` |
| [P0899](#p0899-eval-task-provenance) | `eval_task_provenance` | Per-Item Result Provenance & Forensics | `cap.t18.eval.eval_task_provenance@1` |
| [P0900](#p0900-eval-spec-doc) | `eval_spec_doc` | Evaluation Specification & Methodology Register | `cap.t18.eval.eval_spec_doc@1` |

---

### P0851 · `eval_framework` — Evaluation Framework Core

| field | value |
|---|---|
| part id | `P0851` (1/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0851_eval_framework.py` |
| module path | `hyperion.t18.eval.eval_framework` |
| capability published | `cap.t18.eval.eval_framework@1` |
| determinism class | `seeded` |
| p99 latency budget | 8000 ns (8 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0851_eval_framework.txt`](prompts/P0851_eval_framework.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0851-eval-framework) |

**Mission.** The uniform harness every benchmark plugs into.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **task/harness/grader abstraction with strict isolation between them** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **deterministic execution with full result provenance** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **parallel evaluation across 1000 workers with reproducible aggregation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **framework conformance suite for all harness implementations** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t18.eval.eval_framework@1`
- `cap.t18.eval.eval_framework.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t01.string.string_interning@1` | use the in-file conservative substitute for `string_interning` (documented, slower, lower quality) and set `degraded['string_interning']='local'` |
| `cap.t12.flaky.flaky_detection@1` | use the in-file conservative substitute for `flaky_detection` (documented, slower, lower quality) and set `degraded['flaky_detection']='local'` |
| `cap.t13.agent.agent_communication@1` | use the in-file conservative substitute for `agent_communication` (documented, slower, lower quality) and set `degraded['agent_communication']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - task/harness/grader abstraction with strict isolation between th | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - deterministic execution with full result provenance | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - parallel evaluation across 1000 workers with reproducible aggreg | 520 | Third required mechanism. |
| 6 | Core implementation D - framework conformance suite for all harness implementations | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0851_eval_framework.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.eval.eval_framework@1`.
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

### P0852 · `eval_registry` — Benchmark Registry & Versioning

| field | value |
|---|---|
| part id | `P0852` (2/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0852_eval_registry.py` |
| module path | `hyperion.t18.eval.eval_registry` |
| capability published | `cap.t18.eval.eval_registry@1` |
| determinism class | `seeded` |
| p99 latency budget | 9000 ns (9 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0852_eval_registry.txt`](prompts/P0852_eval_registry.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0852-eval-registry) |

**Mission.** Exactly which version of which benchmark produced which number.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **benchmark metadata: version, date, task count, license, known issues** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **version pinning with content hashing of task sets**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **deprecation and re-run policy when benchmarks change** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **registry completeness audit across all reported results** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t18.eval.eval_registry@1`
- `cap.t18.eval.eval_registry.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.eval.eval_framework@1` | use the in-file conservative substitute for `eval_framework` (documented, slower, lower quality) and set `degraded['eval_framework']='local'` |
| `cap.t01.property.property_gen@1` | use the in-file conservative substitute for `property_gen` (documented, slower, lower quality) and set `degraded['property_gen']='local'` |
| `cap.t12.code.code_generation_core@1` | use the in-file conservative substitute for `code_generation_core` (documented, slower, lower quality) and set `degraded['code_generation_core']='local'` |
| `cap.t13.long.long_horizon_memory@1` | use the in-file conservative substitute for `long_horizon_memory` (documented, slower, lower quality) and set `degraded['long_horizon_memory']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - benchmark metadata: version, date, task count, license, known is | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - version pinning with content hashing of task sets | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - deprecation and re-run policy when benchmarks change | 520 | Third required mechanism. |
| 6 | Core implementation D - registry completeness audit across all reported results | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0852_eval_registry.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.eval.eval_registry@1`.
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

### P0853 · `grading_engine` — Automatic Grading & Answer Equivalence

| field | value |
|---|---|
| part id | `P0853` (3/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0853_grading_engine.py` |
| module path | `hyperion.t18.eval.grading_engine` |
| capability published | `cap.t18.grading.grading_engine@1` |
| determinism class | `seeded` |
| p99 latency budget | 10000 ns (10 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0853_grading_engine.txt`](prompts/P0853_grading_engine.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0853-grading-engine) |

**Mission.** Grades correctly, including when the right answer looks different.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **exact, numeric-tolerance, symbolic-equivalence and semantic grading modes**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **execution-based grading with sandboxing** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **grader-error auditing against human grading on sampled items** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured grader accuracy with target above 99.5%** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t18.grading.grading_engine@1`
- `cap.t18.grading.grading_engine.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.eval.eval_registry@1` | use the in-file conservative substitute for `eval_registry` (documented, slower, lower quality) and set `degraded['eval_registry']='local'` |
| `cap.t01.link.link_validator@1` | use the in-file conservative substitute for `link_validator` (documented, slower, lower quality) and set `degraded['link_validator']='local'` |
| `cap.t12.environment.environment_setup@1` | use the in-file conservative substitute for `environment_setup` (documented, slower, lower quality) and set `degraded['environment_setup']='local'` |
| `cap.t13.tool.tool_creation@1` | use the in-file conservative substitute for `tool_creation` (documented, slower, lower quality) and set `degraded['tool_creation']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - exact, numeric-tolerance, symbolic-equivalence and semantic grad | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - execution-based grading with sandboxing | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - grader-error auditing against human grading on sampled items | 520 | Third required mechanism. |
| 6 | Core implementation D - measured grader accuracy with target above 99.5% | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0853_grading_engine.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.grading.grading_engine@1`.
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

### P0854 · `human_eval_protocol` — Human Evaluation Protocol & Rater Management

| field | value |
|---|---|
| part id | `P0854` (4/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0854_human_eval_protocol.py` |
| module path | `hyperion.t18.eval.human_eval_protocol` |
| capability published | `cap.t18.human.human_eval_protocol@1` |
| determinism class | `seeded` |
| p99 latency budget | 11000 ns (11 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0854_human_eval_protocol.txt`](prompts/P0854_human_eval_protocol.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0854-human-eval-protocol) |

**Mission.** When humans grade, the grading is trustworthy.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **rubric design with inter-rater reliability measurement** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **rater qualification, calibration and quality monitoring** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **blind and randomised presentation to prevent bias** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **reliability statistics reported with every human-graded result**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t18.human.human_eval_protocol@1`
- `cap.t18.human.human_eval_protocol.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.grading.grading_engine@1` | use the in-file conservative substitute for `grading_engine` (documented, slower, lower quality) and set `degraded['grading_engine']='local'` |
| `cap.t01.rate.rate_limiter@1` | use the in-file conservative substitute for `rate_limiter` (documented, slower, lower quality) and set `degraded['rate_limiter']='local'` |
| `cap.t12.scientific.scientific_computing_code@1` | use the in-file conservative substitute for `scientific_computing_code` (documented, slower, lower quality) and set `degraded['scientific_computing_code']='local'` |
| `cap.t13.simulation.simulation_env@1` | use the in-file conservative substitute for `simulation_env` (documented, slower, lower quality) and set `degraded['simulation_env']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - rubric design with inter-rater reliability measurement | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - rater qualification, calibration and quality monitoring | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - blind and randomised presentation to prevent bias | 520 | Third required mechanism. |
| 6 | Core implementation D - reliability statistics reported with every human-graded result | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0854_human_eval_protocol.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.human.human_eval_protocol@1`.
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

### P0855 · `expert_eval` — Expert Domain Evaluation

| field | value |
|---|---|
| part id | `P0855` (5/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0855_expert_eval.py` |
| module path | `hyperion.t18.eval.expert_eval` |
| capability published | `cap.t18.expert.expert_eval@1` |
| determinism class | `seeded` |
| p99 latency budget | 12000 ns (12 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0855_expert_eval.txt`](prompts/P0855_expert_eval.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0855-expert-eval) |

**Mission.** PhD-level and professional-level grading for expert tasks.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **expert recruitment and qualification protocol per domain** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **structured expert rubrics with disagreement resolution** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **expert-time-efficient evaluation design**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **expert-agreement statistics per domain** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t18.expert.expert_eval@1`
- `cap.t18.expert.expert_eval.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.human.human_eval_protocol@1` | use the in-file conservative substitute for `human_eval_protocol` (documented, slower, lower quality) and set `degraded['human_eval_protocol']='local'` |
| `cap.t01.bootstrap.bootstrap_init@1` | use the in-file conservative substitute for `bootstrap_init` (documented, slower, lower quality) and set `degraded['bootstrap_init']='local'` |
| `cap.t12.code.code_quality_gate@1` | use the in-file conservative substitute for `code_quality_gate` (documented, slower, lower quality) and set `degraded['code_quality_gate']='local'` |
| `cap.t13.agent.agent_scaling@1` | use the in-file conservative substitute for `agent_scaling` (documented, slower, lower quality) and set `degraded['agent_scaling']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - expert recruitment and qualification protocol per domain | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - structured expert rubrics with disagreement resolution | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - expert-time-efficient evaluation design | 520 | Third required mechanism. |
| 6 | Core implementation D - expert-agreement statistics per domain | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0855_expert_eval.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.expert.expert_eval@1`.
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

### P0856 · `elo_arena` — Pairwise Comparison & Elo Rating System

| field | value |
|---|---|
| part id | `P0856` (6/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0856_elo_arena.py` |
| module path | `hyperion.t18.eval.elo_arena` |
| capability published | `cap.t18.elo.elo_arena@1` |
| determinism class | `seeded` |
| p99 latency budget | 13000 ns (13 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0856_elo_arena.txt`](prompts/P0856_elo_arena.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0856-elo-arena) |

**Mission.** Rigorous head-to-head comparison against Opus 5.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **pairwise battle protocol with randomisation and blinding** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **Elo/Bradley-Terry estimation with confidence intervals**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **sample-size planning for detectable differences** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **target: GDPval-AA v2 style 2650 Elo versus Opus 5's 1862** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t18.elo.elo_arena@1`
- `cap.t18.elo.elo_arena.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.expert.expert_eval@1` | use the in-file conservative substitute for `expert_eval` (documented, slower, lower quality) and set `degraded['expert_eval']='local'` |
| `cap.t01.chacha.chacha_seeds@1` | use the in-file conservative substitute for `chacha_seeds` (documented, slower, lower quality) and set `degraded['chacha_seeds']='local'` |
| `cap.t12.code.code_embeddings@1` | use the in-file conservative substitute for `code_embeddings` (documented, slower, lower quality) and set `degraded['code_embeddings']='local'` |
| `cap.t13.terminal.terminal_agent@1` | use the in-file conservative substitute for `terminal_agent` (documented, slower, lower quality) and set `degraded['terminal_agent']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - pairwise battle protocol with randomisation and blinding | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - Elo/Bradley-Terry estimation with confidence intervals | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - sample-size planning for detectable differences | 520 | Third required mechanism. |
| 6 | Core implementation D - target: GDPval-AA v2 style 2650 Elo versus Opus 5's 1862 | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0856_elo_arena.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.elo.elo_arena@1`.
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

### P0857 · `statistical_engine` — Statistical Analysis Engine

| field | value |
|---|---|
| part id | `P0857` (7/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0857_statistical_engine.py` |
| module path | `hyperion.t18.eval.statistical_engine` |
| capability published | `cap.t18.statistical.statistical_engine@1` |
| determinism class | `seeded` |
| p99 latency budget | 14000 ns (14 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0857_statistical_engine.txt`](prompts/P0857_statistical_engine.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0857-statistical-engine) |

**Mission.** Every claim carries correct statistics.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **confidence intervals appropriate to the metric and sampling design**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **multiple-comparison correction across many benchmarks** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **power analysis and minimum-detectable-effect computation** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **statistical-methodology review documentation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t18.statistical.statistical_engine@1`
- `cap.t18.statistical.statistical_engine.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.elo.elo_arena@1` | use the in-file conservative substitute for `elo_arena` (documented, slower, lower quality) and set `degraded['elo_arena']='local'` |
| `cap.t01.mem.mem_layout@1` | use the in-file conservative substitute for `mem_layout` (documented, slower, lower quality) and set `degraded['mem_layout']='local'` |
| `cap.t12.static.static_analysis@1` | use the in-file conservative substitute for `static_analysis` (documented, slower, lower quality) and set `degraded['static_analysis']='local'` |
| `cap.t13.api.api_agent@1` | use the in-file conservative substitute for `api_agent` (documented, slower, lower quality) and set `degraded['api_agent']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - confidence intervals appropriate to the metric and sampling desi | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - multiple-comparison correction across many benchmarks | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - power analysis and minimum-detectable-effect computation | 520 | Third required mechanism. |
| 6 | Core implementation D - statistical-methodology review documentation | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0857_statistical_engine.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.statistical.statistical_engine@1`.
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

### P0858 · `variance_control` — Variance Reduction & Run Repetition Policy

| field | value |
|---|---|
| part id | `P0858` (8/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0858_variance_control.py` |
| module path | `hyperion.t18.eval.variance_control` |
| capability published | `cap.t18.variance.variance_control@1` |
| determinism class | `seeded` |
| p99 latency budget | 15000 ns (15 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0858_variance_control.txt`](prompts/P0858_variance_control.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0858-variance-control) |

**Mission.** Distinguishes real improvement from noise.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **repeat-run policy per benchmark based on measured variance** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **paired-comparison and common-random-numbers designs** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **seed and sampling-temperature variance decomposition** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **reported variance bands for every headline number**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t18.variance.variance_control@1`
- `cap.t18.variance.variance_control.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.statistical.statistical_engine@1` | use the in-file conservative substitute for `statistical_engine` (documented, slower, lower quality) and set `degraded['statistical_engine']='local'` |
| `cap.t01.hash.hash_maps@1` | use the in-file conservative substitute for `hash_maps` (documented, slower, lower quality) and set `degraded['hash_maps']='local'` |
| `cap.t12.test.test_orchestration@1` | use the in-file conservative substitute for `test_orchestration` (documented, slower, lower quality) and set `degraded['test_orchestration']='local'` |
| `cap.t13.multi.multi_agent_orchestration@1` | use the in-file conservative substitute for `multi_agent_orchestration` (documented, slower, lower quality) and set `degraded['multi_agent_orchestration']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - repeat-run policy per benchmark based on measured variance | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - paired-comparison and common-random-numbers designs | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - seed and sampling-temperature variance decomposition | 520 | Third required mechanism. |
| 6 | Core implementation D - reported variance bands for every headline number | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0858_variance_control.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.variance.variance_control@1`.
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

### P0859 · `contamination_audit` — Contamination Auditing & Sealed Test Sets

| field | value |
|---|---|
| part id | `P0859` (9/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0859_contamination_audit.py` |
| module path | `hyperion.t18.eval.contamination_audit` |
| capability published | `cap.t18.contamination.contamination_audit@1` |
| determinism class | `seeded` |
| p99 latency budget | 16000 ns (16 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0859_contamination_audit.txt`](prompts/P0859_contamination_audit.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0859-contamination-audit) |

**Mission.** Guarantees the numbers are honest.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **training-data overlap detection per benchmark item** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **sealed held-out set management with access control** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **canary-string and memorisation testing**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **contamination-audit certificate per reported benchmark** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t18.contamination.contamination_audit@1`
- `cap.t18.contamination.contamination_audit.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.variance.variance_control@1` | use the in-file conservative substitute for `variance_control` (documented, slower, lower quality) and set `degraded['variance_control']='local'` |
| `cap.t01.selftest.selftest_harness@1` | use the in-file conservative substitute for `selftest_harness` (documented, slower, lower quality) and set `degraded['selftest_harness']='local'` |
| `cap.t12.crash.crash_triage@1` | use the in-file conservative substitute for `crash_triage` (documented, slower, lower quality) and set `degraded['crash_triage']='local'` |
| `cap.t13.error.error_recovery_agent@1` | use the in-file conservative substitute for `error_recovery_agent` (documented, slower, lower quality) and set `degraded['error_recovery_agent']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - training-data overlap detection per benchmark item | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - sealed held-out set management with access control | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - canary-string and memorisation testing | 520 | Third required mechanism. |
| 6 | Core implementation D - contamination-audit certificate per reported benchmark | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0859_contamination_audit.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.contamination.contamination_audit@1`.
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

### P0860 · `swe_verified_eval` — SWE-bench Verified Evaluation

| field | value |
|---|---|
| part id | `P0860` (10/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0860_swe_verified_eval.py` |
| module path | `hyperion.t18.eval.swe_verified_eval` |
| capability published | `cap.t18.swe.swe_verified_eval@1` |
| determinism class | `seeded` |
| p99 latency budget | 17000 ns (17 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0860_swe_verified_eval.txt`](prompts/P0860_swe_verified_eval.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0860-swe-verified-eval) |

**Mission.** The headline coding benchmark, measured rigorously.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **containerised 500-task evaluation with both minimal-bash and full-scaffold modes** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **per-instance diagnosis and failure taxonomy**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **cost and latency measurement alongside resolution rate** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **target: 99.8% versus Opus 5's 97.0% (vals.ai harness)** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t18.swe.swe_verified_eval@1`
- `cap.t18.swe.swe_verified_eval.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.contamination.contamination_audit@1` | use the in-file conservative substitute for `contamination_audit` (documented, slower, lower quality) and set `degraded['contamination_audit']='local'` |
| `cap.t01.version.version_semver@1` | use the in-file conservative substitute for `version_semver` (documented, slower, lower quality) and set `degraded['version_semver']='local'` |
| `cap.t12.multi.multi_repo@1` | use the in-file conservative substitute for `multi_repo` (documented, slower, lower quality) and set `degraded['multi_repo']='local'` |
| `cap.t13.sandbox.sandbox_execution@1` | use the in-file conservative substitute for `sandbox_execution` (documented, slower, lower quality) and set `degraded['sandbox_execution']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - containerised 500-task evaluation with both minimal-bash and ful | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - per-instance diagnosis and failure taxonomy | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - cost and latency measurement alongside resolution rate | 520 | Third required mechanism. |
| 6 | Core implementation D - target: 99.8% versus Opus 5's 97.0% (vals.ai harness) | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0860_swe_verified_eval.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.swe.swe_verified_eval@1`.
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

### P0861 · `swe_pro_eval` — SWE-bench Pro Evaluation

| field | value |
|---|---|
| part id | `P0861` (11/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0861_swe_pro_eval.py` |
| module path | `hyperion.t18.eval.swe_pro_eval` |
| capability published | `cap.t18.swe.swe_pro_eval@1` |
| determinism class | `seeded` |
| p99 latency budget | 18000 ns (18 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0861_swe_pro_eval.txt`](prompts/P0861_swe_pro_eval.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0861-swe-pro-eval) |

**Mission.** The harder, less saturated coding benchmark.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **public, commercial and held-out set evaluation with proper isolation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **vendor-scaffold and standardised-harness results reported separately** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **difficulty-stratified analysis** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **target: 96.5% versus Opus 5's ~82% estimated** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t18.swe.swe_pro_eval@1`
- `cap.t18.swe.swe_pro_eval.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.swe.swe_verified_eval@1` | use the in-file conservative substitute for `swe_verified_eval` (documented, slower, lower quality) and set `degraded['swe_verified_eval']='local'` |
| `cap.t01.budget.budget_ledger@1` | use the in-file conservative substitute for `budget_ledger` (documented, slower, lower quality) and set `degraded['budget_ledger']='local'` |
| `cap.t12.systems.systems_programming@1` | use the in-file conservative substitute for `systems_programming` (documented, slower, lower quality) and set `degraded['systems_programming']='local'` |
| `cap.t13.agent.agent_interruption@1` | use the in-file conservative substitute for `agent_interruption` (documented, slower, lower quality) and set `degraded['agent_interruption']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - public, commercial and held-out set evaluation with proper isola | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - vendor-scaffold and standardised-harness results reported separa | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - difficulty-stratified analysis | 520 | Third required mechanism. |
| 6 | Core implementation D - target: 96.5% versus Opus 5's ~82% estimated | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0861_swe_pro_eval.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.swe.swe_pro_eval@1`.
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

### P0862 · `frontier_bench_eval` — Frontier-Bench & Long-Horizon Coding Evaluation

| field | value |
|---|---|
| part id | `P0862` (12/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0862_frontier_bench_eval.py` |
| module path | `hyperion.t18.eval.frontier_bench_eval` |
| capability published | `cap.t18.frontier.frontier_bench_eval@1` |
| determinism class | `seeded` |
| p99 latency budget | 19000 ns (19 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0862_frontier_bench_eval.txt`](prompts/P0862_frontier_bench_eval.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0862-frontier-bench-eval) |

**Mission.** The benchmark where Opus 5 still fails most tasks.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **long-horizon agentic task evaluation with environment fidelity** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **effort-level and cost-per-task curves** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **task-category capability breakdown** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **target: 92% versus Opus 5's 43.3%**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t18.frontier.frontier_bench_eval@1`
- `cap.t18.frontier.frontier_bench_eval.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.swe.swe_pro_eval@1` | use the in-file conservative substitute for `swe_pro_eval` (documented, slower, lower quality) and set `degraded['swe_pro_eval']='local'` |
| `cap.t01.compression.compression@1` | use the in-file conservative substitute for `compression` (documented, slower, lower quality) and set `degraded['compression']='local'` |
| `cap.t12.cursorbench.cursorbench_harness@1` | use the in-file conservative substitute for `cursorbench_harness` (documented, slower, lower quality) and set `degraded['cursorbench_harness']='local'` |
| `cap.t13.agent.agent_speed@1` | use the in-file conservative substitute for `agent_speed` (documented, slower, lower quality) and set `degraded['agent_speed']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - long-horizon agentic task evaluation with environment fidelity | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - effort-level and cost-per-task curves | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - task-category capability breakdown | 520 | Third required mechanism. |
| 6 | Core implementation D - target: 92% versus Opus 5's 43.3% | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0862_frontier_bench_eval.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.frontier.frontier_bench_eval@1`.
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

### P0863 · `terminal_bench_eval` — Terminal-Bench Evaluation

| field | value |
|---|---|
| part id | `P0863` (13/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0863_terminal_bench_eval.py` |
| module path | `hyperion.t18.eval.terminal_bench_eval` |
| capability published | `cap.t18.terminal.terminal_bench_eval@1` |
| determinism class | `seeded` |
| p99 latency budget | 20000 ns (20 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0863_terminal_bench_eval.txt`](prompts/P0863_terminal_bench_eval.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0863-terminal-bench-eval) |

**Mission.** Live terminal competence, measured.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **Terminal-Bench 2.1 harness with faithful environment reproduction** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **failure-mode analysis (environment, command, verification, recovery)** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **comparison against both Opus 5 and GPT-class baselines**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **target: 98.5% versus Opus 5's ~86% estimated** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t18.terminal.terminal_bench_eval@1`
- `cap.t18.terminal.terminal_bench_eval.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.frontier.frontier_bench_eval@1` | use the in-file conservative substitute for `frontier_bench_eval` (documented, slower, lower quality) and set `degraded['frontier_bench_eval']='local'` |
| `cap.t01.blake3.blake3_hash@1` | use the in-file conservative substitute for `blake3_hash` (documented, slower, lower quality) and set `degraded['blake3_hash']='local'` |
| `cap.t12.code.code_search@1` | use the in-file conservative substitute for `code_search` (documented, slower, lower quality) and set `degraded['code_search']='local'` |
| `cap.t13.mid.mid_conversation_tools@1` | use the in-file conservative substitute for `mid_conversation_tools` (documented, slower, lower quality) and set `degraded['mid_conversation_tools']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - Terminal-Bench 2.1 harness with faithful environment reproductio | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - failure-mode analysis (environment, command, verification, recov | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - comparison against both Opus 5 and GPT-class baselines | 520 | Third required mechanism. |
| 6 | Core implementation D - target: 98.5% versus Opus 5's ~86% estimated | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0863_terminal_bench_eval.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.terminal.terminal_bench_eval@1`.
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

### P0864 · `arc_agi_eval` — ARC-AGI-2 and ARC-AGI-3 Evaluation

| field | value |
|---|---|
| part id | `P0864` (14/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0864_arc_agi_eval.py` |
| module path | `hyperion.t18.eval.arc_agi_eval` |
| capability published | `cap.t18.arc.arc_agi_eval@1` |
| determinism class | `seeded` |
| p99 latency budget | 21000 ns (21 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0864_arc_agi_eval.txt`](prompts/P0864_arc_agi_eval.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0864-arc-agi-eval) |

**Mission.** Novel-problem-solving measurement: the fluid-intelligence test.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **official-protocol evaluation for both ARC-AGI-2 and ARC-AGI-3** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **per-task abstraction-type analysis of successes and failures**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **compute-and-cost-per-task reporting as required by the protocol** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **targets: ARC-AGI-3 88% (Opus 5: 30.2%), ARC-AGI-2 93%** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t18.arc.arc_agi_eval@1`
- `cap.t18.arc.arc_agi_eval.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.terminal.terminal_bench_eval@1` | use the in-file conservative substitute for `terminal_bench_eval` (documented, slower, lower quality) and set `degraded['terminal_bench_eval']='local'` |
| `cap.t01.alloc.alloc_arena@1` | use the in-file conservative substitute for `alloc_arena` (documented, slower, lower quality) and set `degraded['alloc_arena']='local'` |
| `cap.t12.code.code_review_engine@1` | use the in-file conservative substitute for `code_review_engine` (documented, slower, lower quality) and set `degraded['code_review_engine']='local'` |
| `cap.t13.mobile.mobile_agent@1` | use the in-file conservative substitute for `mobile_agent` (documented, slower, lower quality) and set `degraded['mobile_agent']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - official-protocol evaluation for both ARC-AGI-2 and ARC-AGI-3 | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - per-task abstraction-type analysis of successes and failures | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - compute-and-cost-per-task reporting as required by the protocol | 520 | Third required mechanism. |
| 6 | Core implementation D - targets: ARC-AGI-3 88% (Opus 5: 30.2%), ARC-AGI-2 93% | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0864_arc_agi_eval.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.arc.arc_agi_eval@1`.
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

### P0865 · `gpqa_eval` — GPQA Diamond & Expert Knowledge Evaluation

| field | value |
|---|---|
| part id | `P0865` (15/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0865_gpqa_eval.py` |
| module path | `hyperion.t18.eval.gpqa_eval` |
| capability published | `cap.t18.gpqa.gpqa_eval@1` |
| determinism class | `seeded` |
| p99 latency budget | 22000 ns (22 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0865_gpqa_eval.txt`](prompts/P0865_gpqa_eval.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0865-gpqa-eval) |

**Mission.** Graduate-level science measurement.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **GPQA Diamond harness with contamination checking**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **per-discipline breakdown (physics, chemistry, biology)** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **reasoning-quality analysis beyond answer correctness** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **target: 99.6% versus Opus 5's ~95.5%** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t18.gpqa.gpqa_eval@1`
- `cap.t18.gpqa.gpqa_eval.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.arc.arc_agi_eval@1` | use the in-file conservative substitute for `arc_agi_eval` (documented, slower, lower quality) and set `degraded['arc_agi_eval']='local'` |
| `cap.t01.bitset.bitset_rank@1` | use the in-file conservative substitute for `bitset_rank` (documented, slower, lower quality) and set `degraded['bitset_rank']='local'` |
| `cap.t12.code.code_execution_sandbox@1` | use the in-file conservative substitute for `code_execution_sandbox` (documented, slower, lower quality) and set `degraded['code_execution_sandbox']='local'` |
| `cap.t13.scheduling.scheduling_agent@1` | use the in-file conservative substitute for `scheduling_agent` (documented, slower, lower quality) and set `degraded['scheduling_agent']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - GPQA Diamond harness with contamination checking | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - per-discipline breakdown (physics, chemistry, biology) | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - reasoning-quality analysis beyond answer correctness | 520 | Third required mechanism. |
| 6 | Core implementation D - target: 99.6% versus Opus 5's ~95.5% | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0865_gpqa_eval.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.gpqa.gpqa_eval@1`.
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

### P0866 · `math_eval` — Mathematics Competition Evaluation

| field | value |
|---|---|
| part id | `P0866` (16/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0866_math_eval.py` |
| module path | `hyperion.t18.eval.math_eval` |
| capability published | `cap.t18.math.math_eval@1` |
| determinism class | `seeded` |
| p99 latency budget | 23000 ns (23 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0866_math_eval.txt`](prompts/P0866_math_eval.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0866-math-eval) |

**Mission.** Zero-ambiguity mathematical measurement.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **AIME/HMMT-class harnesses with formal answer verification** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **proof-based problem evaluation with certificate checking** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **difficulty-stratified analysis and failure taxonomy** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **target: 100% with certificates versus Opus 5's ~96%**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t18.math.math_eval@1`
- `cap.t18.math.math_eval.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.gpqa.gpqa_eval@1` | use the in-file conservative substitute for `gpqa_eval` (documented, slower, lower quality) and set `degraded['gpqa_eval']='local'` |
| `cap.t01.metrics.metrics_core@1` | use the in-file conservative substitute for `metrics_core` (documented, slower, lower quality) and set `degraded['metrics_core']='local'` |
| `cap.t12.fuzzing.fuzzing_agent@1` | use the in-file conservative substitute for `fuzzing_agent` (documented, slower, lower quality) and set `degraded['fuzzing_agent']='local'` |
| `cap.t13.action.action_verification@1` | use the in-file conservative substitute for `action_verification` (documented, slower, lower quality) and set `degraded['action_verification']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - AIME/HMMT-class harnesses with formal answer verification | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - proof-based problem evaluation with certificate checking | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - difficulty-stratified analysis and failure taxonomy | 520 | Third required mechanism. |
| 6 | Core implementation D - target: 100% with certificates versus Opus 5's ~96% | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0866_math_eval.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.math.math_eval@1`.
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

### P0867 · `mmmu_eval` — Multimodal Understanding Evaluation

| field | value |
|---|---|
| part id | `P0867` (17/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0867_mmmu_eval.py` |
| module path | `hyperion.t18.eval.mmmu_eval` |
| capability published | `cap.t18.mmmu.mmmu_eval@1` |
| determinism class | `seeded` |
| p99 latency budget | 24000 ns (24 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0867_mmmu_eval.txt`](prompts/P0867_mmmu_eval.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0867-mmmu-eval) |

**Mission.** Vision and multimodal capability measurement.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **MMMU and related multimodal harnesses with image fidelity control** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **per-subject and per-image-type breakdown** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **hallucination-rate measurement alongside accuracy**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **target: 99.0% versus Opus 5's ~93%** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t18.mmmu.mmmu_eval@1`
- `cap.t18.mmmu.mmmu_eval.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.math.math_eval@1` | use the in-file conservative substitute for `math_eval` (documented, slower, lower quality) and set `degraded['math_eval']='local'` |
| `cap.t01.capability.capability_gate@1` | use the in-file conservative substitute for `capability_gate` (documented, slower, lower quality) and set `degraded['capability_gate']='local'` |
| `cap.t12.pr.pr_workflow@1` | use the in-file conservative substitute for `pr_workflow` (documented, slower, lower quality) and set `degraded['pr_workflow']='local'` |
| `cap.t13.cost.cost_control_agent@1` | use the in-file conservative substitute for `cost_control_agent` (documented, slower, lower quality) and set `degraded['cost_control_agent']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - MMMU and related multimodal harnesses with image fidelity contro | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - per-subject and per-image-type breakdown | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - hallucination-rate measurement alongside accuracy | 520 | Third required mechanism. |
| 6 | Core implementation D - target: 99.0% versus Opus 5's ~93% | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0867_mmmu_eval.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.mmmu.mmmu_eval@1`.
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

### P0868 · `osworld_eval` — OSWorld and Computer Use Evaluation

| field | value |
|---|---|
| part id | `P0868` (18/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0868_osworld_eval.py` |
| module path | `hyperion.t18.eval.osworld_eval` |
| capability published | `cap.t18.osworld.osworld_eval@1` |
| determinism class | `seeded` |
| p99 latency budget | 25000 ns (25 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0868_osworld_eval.txt`](prompts/P0868_osworld_eval.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0868-osworld-eval) |

**Mission.** Desktop autonomy measurement.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **OSWorld 2.0 harness with faithful VM environments** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **per-application and per-task-type success analysis**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **cost-per-task curves as reported by Anthropic for comparability** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **target: 95.5% versus Opus 5's 70.5%** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t18.osworld.osworld_eval@1`
- `cap.t18.osworld.osworld_eval.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.mmmu.mmmu_eval@1` | use the in-file conservative substitute for `mmmu_eval` (documented, slower, lower quality) and set `degraded['mmmu_eval']='local'` |
| `cap.t01.unit.unit_dimensions@1` | use the in-file conservative substitute for `unit_dimensions` (documented, slower, lower quality) and set `degraded['unit_dimensions']='local'` |
| `cap.t12.frontend.frontend_engineering@1` | use the in-file conservative substitute for `frontend_engineering` (documented, slower, lower quality) and set `degraded['frontend_engineering']='local'` |
| `cap.t13.trajectory.trajectory_analysis@1` | use the in-file conservative substitute for `trajectory_analysis` (documented, slower, lower quality) and set `degraded['trajectory_analysis']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - OSWorld 2.0 harness with faithful VM environments | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - per-application and per-task-type success analysis | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - cost-per-task curves as reported by Anthropic for comparability | 520 | Third required mechanism. |
| 6 | Core implementation D - target: 95.5% versus Opus 5's 70.5% | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0868_osworld_eval.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.osworld.osworld_eval@1`.
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

### P0869 · `browsecomp_eval` — Web Research & Browsing Evaluation

| field | value |
|---|---|
| part id | `P0869` (19/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0869_browsecomp_eval.py` |
| module path | `hyperion.t18.eval.browsecomp_eval` |
| capability published | `cap.t18.browsecomp.browsecomp_eval@1` |
| determinism class | `seeded` |
| p99 latency budget | 26000 ns (26 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0869_browsecomp_eval.txt`](prompts/P0869_browsecomp_eval.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0869-browsecomp-eval) |

**Mission.** Long-horizon research capability measurement.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **BrowseComp and Online-Mind2Web harnesses with live-web variance control**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **citation-accuracy and source-quality measurement** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **time-and-cost-to-answer reporting** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **targets: BrowseComp 99.0% (Opus 5: 90.8%), Mind2Web 98.5%** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t18.browsecomp.browsecomp_eval@1`
- `cap.t18.browsecomp.browsecomp_eval.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.osworld.osworld_eval@1` | use the in-file conservative substitute for `osworld_eval` (documented, slower, lower quality) and set `degraded['osworld_eval']='local'` |
| `cap.t01.fs.fs_atomic@1` | use the in-file conservative substitute for `fs_atomic` (documented, slower, lower quality) and set `degraded['fs_atomic']='local'` |
| `cap.t12.frontier.frontier_bench_harness@1` | use the in-file conservative substitute for `frontier_bench_harness` (documented, slower, lower quality) and set `degraded['frontier_bench_harness']='local'` |
| `cap.t13.agent.agent_ux@1` | use the in-file conservative substitute for `agent_ux` (documented, slower, lower quality) and set `degraded['agent_ux']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - BrowseComp and Online-Mind2Web harnesses with live-web variance  | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - citation-accuracy and source-quality measurement | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - time-and-cost-to-answer reporting | 520 | Third required mechanism. |
| 6 | Core implementation D - targets: BrowseComp 99.0% (Opus 5: 90.8%), Mind2Web 98.5% | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0869_browsecomp_eval.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.browsecomp.browsecomp_eval@1`.
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

### P0870 · `automation_bench_eval` — Business Automation Evaluation

| field | value |
|---|---|
| part id | `P0870` (20/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0870_automation_bench_eval.py` |
| module path | `hyperion.t18.eval.automation_bench_eval` |
| capability published | `cap.t18.automation.automation_bench_eval@1` |
| determinism class | `seeded` |
| p99 latency budget | 27000 ns (27 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0870_automation_bench_eval.txt`](prompts/P0870_automation_bench_eval.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0870-automation-bench-eval) |

**Mission.** End-to-end knowledge work measurement.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **Zapier AutomationBench style harness with real integrations** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **task-completion verification including side-effect correctness** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **cost-per-completed-task comparison** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **target: 92% versus Opus 5's 26.0%**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t18.automation.automation_bench_eval@1`
- `cap.t18.automation.automation_bench_eval.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.browsecomp.browsecomp_eval@1` | use the in-file conservative substitute for `browsecomp_eval` (documented, slower, lower quality) and set `degraded['browsecomp_eval']='local'` |
| `cap.t01.cbor.cbor_canonical@1` | use the in-file conservative substitute for `cbor_canonical` (documented, slower, lower quality) and set `degraded['cbor_canonical']='local'` |
| `cap.t12.call.call_graph@1` | use the in-file conservative substitute for `call_graph` (documented, slower, lower quality) and set `degraded['call_graph']='local'` |
| `cap.t13.tool.tool_composition@1` | use the in-file conservative substitute for `tool_composition` (documented, slower, lower quality) and set `degraded['tool_composition']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - Zapier AutomationBench style harness with real integrations | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - task-completion verification including side-effect correctness | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - cost-per-completed-task comparison | 520 | Third required mechanism. |
| 6 | Core implementation D - target: 92% versus Opus 5's 26.0% | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0870_automation_bench_eval.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.automation.automation_bench_eval@1`.
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

### P0871 · `gdpval_eval` — Economic Knowledge Work Evaluation

| field | value |
|---|---|
| part id | `P0871` (21/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0871_gdpval_eval.py` |
| module path | `hyperion.t18.eval.gdpval_eval` |
| capability published | `cap.t18.gdpval.gdpval_eval@1` |
| determinism class | `seeded` |
| p99 latency budget | 28000 ns (28 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0871_gdpval_eval.txt`](prompts/P0871_gdpval_eval.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0871-gdpval-eval) |

**Mission.** The benchmark closest to real economic value.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **GDPval-AA v2 style harness with occupation coverage** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **expert-grading protocol with Elo aggregation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **per-occupation capability and cost analysis**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **target: 2650 Elo versus Opus 5's 1862** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t18.gdpval.gdpval_eval@1`
- `cap.t18.gdpval.gdpval_eval.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.automation.automation_bench_eval@1` | use the in-file conservative substitute for `automation_bench_eval` (documented, slower, lower quality) and set `degraded['automation_bench_eval']='local'` |
| `cap.t01.clock.clock_time@1` | use the in-file conservative substitute for `clock_time` (documented, slower, lower quality) and set `degraded['clock_time']='local'` |
| `cap.t12.mutation.mutation_testing@1` | use the in-file conservative substitute for `mutation_testing` (documented, slower, lower quality) and set `degraded['mutation_testing']='local'` |
| `cap.t13.gui.gui_grounding@1` | use the in-file conservative substitute for `gui_grounding` (documented, slower, lower quality) and set `degraded['gui_grounding']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - GDPval-AA v2 style harness with occupation coverage | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - expert-grading protocol with Elo aggregation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - per-occupation capability and cost analysis | 520 | Third required mechanism. |
| 6 | Core implementation D - target: 2650 Elo versus Opus 5's 1862 | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0871_gdpval_eval.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.gdpval.gdpval_eval@1`.
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

### P0872 · `lifescience_eval` — Life Sciences Evaluation Suite

| field | value |
|---|---|
| part id | `P0872` (22/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0872_lifescience_eval.py` |
| module path | `hyperion.t18.eval.lifescience_eval` |
| capability published | `cap.t18.lifescience.lifescience_eval@1` |
| determinism class | `seeded` |
| p99 latency budget | 29000 ns (29 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0872_lifescience_eval.txt`](prompts/P0872_lifescience_eval.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0872-lifescience-eval) |

**Mission.** Where Opus 5 made its biggest scientific gains.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **structural biology, organic chemistry and bioinformatics task harnesses** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **expert grading with domain-specific rubrics**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **spectroscopy-to-structure and protein-variant task suites** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **target: 165% of Opus 5's suite-relative performance** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t18.lifescience.lifescience_eval@1`
- `cap.t18.lifescience.lifescience_eval.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.gdpval.gdpval_eval@1` | use the in-file conservative substitute for `gdpval_eval` (documented, slower, lower quality) and set `degraded['gdpval_eval']='local'` |
| `cap.t01.bigint.bigint_modmath@1` | use the in-file conservative substitute for `bigint_modmath` (documented, slower, lower quality) and set `degraded['bigint_modmath']='local'` |
| `cap.t12.build.build_system@1` | use the in-file conservative substitute for `build_system` (documented, slower, lower quality) and set `degraded['build_system']='local'` |
| `cap.t13.email.email_communication@1` | use the in-file conservative substitute for `email_communication` (documented, slower, lower quality) and set `degraded['email_communication']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - structural biology, organic chemistry and bioinformatics task ha | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - expert grading with domain-specific rubrics | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - spectroscopy-to-structure and protein-variant task suites | 520 | Third required mechanism. |
| 6 | Core implementation D - target: 165% of Opus 5's suite-relative performance | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0872_lifescience_eval.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.lifescience.lifescience_eval@1`.
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

### P0873 · `security_eval` — Security & Vulnerability Discovery Evaluation

| field | value |
|---|---|
| part id | `P0873` (23/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0873_security_eval.py` |
| module path | `hyperion.t18.eval.security_eval` |
| capability published | `cap.t18.security.security_eval@1` |
| determinism class | `seeded` |
| p99 latency budget | 30000 ns (30 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0873_security_eval.txt`](prompts/P0873_security_eval.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0873-security-eval) |

**Mission.** Measures defensive capability without building offensive capability.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **OSS-Fuzz style vulnerability-discovery harness (find, not exploit)**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **strict scope limitation with T19 gating on exploit-adjacent tasks** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **false-positive rate measurement in vulnerability reports** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **target: 97% find rate versus Opus 5's ~78%, with no exploit-development capability** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t18.security.security_eval@1`
- `cap.t18.security.security_eval.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.lifescience.lifescience_eval@1` | use the in-file conservative substitute for `lifescience_eval` (documented, slower, lower quality) and set `degraded['lifescience_eval']='local'` |
| `cap.t01.logging.logging_events@1` | use the in-file conservative substitute for `logging_events` (documented, slower, lower quality) and set `degraded['logging_events']='local'` |
| `cap.t12.security.security_code_analysis@1` | use the in-file conservative substitute for `security_code_analysis` (documented, slower, lower quality) and set `degraded['security_code_analysis']='local'` |
| `cap.t13.environment.environment_model@1` | use the in-file conservative substitute for `environment_model` (documented, slower, lower quality) and set `degraded['environment_model']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - OSS-Fuzz style vulnerability-discovery harness (find, not exploi | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - strict scope limitation with T19 gating on exploit-adjacent task | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - false-positive rate measurement in vulnerability reports | 520 | Third required mechanism. |
| 6 | Core implementation D - target: 97% find rate versus Opus 5's ~78%, with no exploit-deve | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0873_security_eval.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.security.security_eval@1`.
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

### P0874 · `longcontext_eval` — Long Context Evaluation Suite

| field | value |
|---|---|
| part id | `P0874` (24/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0874_longcontext_eval.py` |
| module path | `hyperion.t18.eval.longcontext_eval` |
| capability published | `cap.t18.longcontext.longcontext_eval@1` |
| determinism class | `seeded` |
| p99 latency budget | 31000 ns (31 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0874_longcontext_eval.txt`](prompts/P0874_longcontext_eval.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0874-longcontext-eval) |

**Mission.** Proves the 1M+ context actually works.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **needle-in-haystack, multi-needle and reasoning-over-context suites** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **position-dependent accuracy measurement across the full window** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **effective-context-length determination methodology** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **target: no measurable degradation across 1M tokens**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t18.longcontext.longcontext_eval@1`
- `cap.t18.longcontext.longcontext_eval.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.security.security_eval@1` | use the in-file conservative substitute for `security_eval` (documented, slower, lower quality) and set `degraded['security_eval']='local'` |
| `cap.t01.checksum.checksum_verify@1` | use the in-file conservative substitute for `checksum_verify` (documented, slower, lower quality) and set `degraded['checksum_verify']='local'` |
| `cap.t12.commit.commit_history@1` | use the in-file conservative substitute for `commit_history` (documented, slower, lower quality) and set `degraded['commit_history']='local'` |
| `cap.t13.credential.credential_management@1` | use the in-file conservative substitute for `credential_management` (documented, slower, lower quality) and set `degraded['credential_management']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - needle-in-haystack, multi-needle and reasoning-over-context suit | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - position-dependent accuracy measurement across the full window | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - effective-context-length determination methodology | 520 | Third required mechanism. |
| 6 | Core implementation D - target: no measurable degradation across 1M tokens | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0874_longcontext_eval.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.longcontext.longcontext_eval@1`.
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

### P0875 · `instruction_following_eval` — Instruction Following & Constraint Adherence

| field | value |
|---|---|
| part id | `P0875` (25/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0875_instruction_following_eval.py` |
| module path | `hyperion.t18.eval.instruction_following_eval` |
| capability published | `cap.t18.instruction.instruction_following_eval@1` |
| determinism class | `seeded` |
| p99 latency budget | 32000 ns (32 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0875_instruction_following_eval.txt`](prompts/P0875_instruction_following_eval.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0875-instruction-following-eval) |

**Mission.** Does exactly what was asked, including the boring constraints.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **multi-constraint instruction suites with programmatic verification** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **constraint-conflict handling evaluation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **format and length adherence measurement**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **target: above 99.5% constraint satisfaction** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t18.instruction.instruction_following_eval@1`
- `cap.t18.instruction.instruction_following_eval.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.longcontext.longcontext_eval@1` | use the in-file conservative substitute for `longcontext_eval` (documented, slower, lower quality) and set `degraded['longcontext_eval']='local'` |
| `cap.t01.numeric.numeric_limits@1` | use the in-file conservative substitute for `numeric_limits` (documented, slower, lower quality) and set `degraded['numeric_limits']='local'` |
| `cap.t12.notebook.notebook_engineering@1` | use the in-file conservative substitute for `notebook_engineering` (documented, slower, lower quality) and set `degraded['notebook_engineering']='local'` |
| `cap.t13.agent.agent_eval_harness@1` | use the in-file conservative substitute for `agent_eval_harness` (documented, slower, lower quality) and set `degraded['agent_eval_harness']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - multi-constraint instruction suites with programmatic verificati | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - constraint-conflict handling evaluation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - format and length adherence measurement | 520 | Third required mechanism. |
| 6 | Core implementation D - target: above 99.5% constraint satisfaction | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0875_instruction_following_eval.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.instruction.instruction_following_eval@1`.
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

### P0876 · `hallucination_eval` — Hallucination & Factuality Evaluation

| field | value |
|---|---|
| part id | `P0876` (26/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0876_hallucination_eval.py` |
| module path | `hyperion.t18.eval.hallucination_eval` |
| capability published | `cap.t18.hallucination.hallucination_eval@1` |
| determinism class | `seeded` |
| p99 latency budget | 33000 ns (33 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0876_hallucination_eval.txt`](prompts/P0876_hallucination_eval.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0876-hallucination-eval) |

**Mission.** Measures how often it makes things up.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **claim-level factuality evaluation with source verification** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **abstention-appropriateness measurement on unanswerable questions**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **citation-accuracy and support-strength measurement** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **target: under 0.1% unsupported-claim rate** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t18.hallucination.hallucination_eval@1`
- `cap.t18.hallucination.hallucination_eval.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.instruction.instruction_following_eval@1` | use the in-file conservative substitute for `instruction_following_eval` (documented, slower, lower quality) and set `degraded['instruction_following_eval']='local'` |
| `cap.t01.sandbox.sandbox_policy@1` | use the in-file conservative substitute for `sandbox_policy` (documented, slower, lower quality) and set `degraded['sandbox_policy']='local'` |
| `cap.t12.swe.swe_bench_harness@1` | use the in-file conservative substitute for `swe_bench_harness` (documented, slower, lower quality) and set `degraded['swe_bench_harness']='local'` |
| `cap.t13.data.data_analysis_agent@1` | use the in-file conservative substitute for `data_analysis_agent` (documented, slower, lower quality) and set `degraded['data_analysis_agent']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - claim-level factuality evaluation with source verification | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - abstention-appropriateness measurement on unanswerable questions | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - citation-accuracy and support-strength measurement | 520 | Third required mechanism. |
| 6 | Core implementation D - target: under 0.1% unsupported-claim rate | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0876_hallucination_eval.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.hallucination.hallucination_eval@1`.
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

### P0877 · `calibration_eval` — Calibration & Uncertainty Evaluation

| field | value |
|---|---|
| part id | `P0877` (27/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0877_calibration_eval.py` |
| module path | `hyperion.t18.eval.calibration_eval` |
| capability published | `cap.t18.calibration.calibration_eval@1` |
| determinism class | `seeded` |
| p99 latency budget | 34000 ns (34 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0877_calibration_eval.txt`](prompts/P0877_calibration_eval.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0877-calibration-eval) |

**Mission.** Measures whether stated confidence means anything.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **expected-calibration-error measurement across task families**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **selective-prediction risk-coverage curves** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **overconfidence detection on hard and adversarial items** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **target: materially better calibration than Opus-class baselines** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t18.calibration.calibration_eval@1`
- `cap.t18.calibration.calibration_eval.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.hallucination.hallucination_eval@1` | use the in-file conservative substitute for `hallucination_eval` (documented, slower, lower quality) and set `degraded['hallucination_eval']='local'` |
| `cap.t01.abi.abi_result@1` | use the in-file conservative substitute for `abi_result` (documented, slower, lower quality) and set `degraded['abi_result']='local'` |
| `cap.t12.semantic.semantic_analysis@1` | use the in-file conservative substitute for `semantic_analysis` (documented, slower, lower quality) and set `degraded['semantic_analysis']='local'` |
| `cap.t13.tool.tool_selection@1` | use the in-file conservative substitute for `tool_selection` (documented, slower, lower quality) and set `degraded['tool_selection']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - expected-calibration-error measurement across task families | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - selective-prediction risk-coverage curves | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - overconfidence detection on hard and adversarial items | 520 | Third required mechanism. |
| 6 | Core implementation D - target: materially better calibration than Opus-class baselines | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0877_calibration_eval.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.calibration.calibration_eval@1`.
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

### P0878 · `robustness_eval` — Robustness & Consistency Evaluation

| field | value |
|---|---|
| part id | `P0878` (28/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0878_robustness_eval.py` |
| module path | `hyperion.t18.eval.robustness_eval` |
| capability published | `cap.t18.robustness.robustness_eval@1` |
| determinism class | `seeded` |
| p99 latency budget | 35000 ns (35 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0878_robustness_eval.txt`](prompts/P0878_robustness_eval.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0878-robustness-eval) |

**Mission.** Same question, any phrasing, same quality answer.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **paraphrase, distractor, ordering and format-perturbation suites** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **sycophancy and pressure-resistance measurement** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **consistency scoring across semantically identical inputs** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **target: measurably higher consistency than Opus 5**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t18.robustness.robustness_eval@1`
- `cap.t18.robustness.robustness_eval.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.calibration.calibration_eval@1` | use the in-file conservative substitute for `calibration_eval` (documented, slower, lower quality) and set `degraded['calibration_eval']='local'` |
| `cap.t01.trace.trace_context@1` | use the in-file conservative substitute for `trace_context` (documented, slower, lower quality) and set `degraded['trace_context']='local'` |
| `cap.t12.test.test_synthesis@1` | use the in-file conservative substitute for `test_synthesis` (documented, slower, lower quality) and set `degraded['test_synthesis']='local'` |
| `cap.t13.computer.computer_use_agent@1` | use the in-file conservative substitute for `computer_use_agent` (documented, slower, lower quality) and set `degraded['computer_use_agent']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - paraphrase, distractor, ordering and format-perturbation suites | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - sycophancy and pressure-resistance measurement | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - consistency scoring across semantically identical inputs | 520 | Third required mechanism. |
| 6 | Core implementation D - target: measurably higher consistency than Opus 5 | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0878_robustness_eval.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.robustness.robustness_eval@1`.
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

### P0879 · `adversarial_eval` — Adversarial & Jailbreak Evaluation

| field | value |
|---|---|
| part id | `P0879` (29/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0879_adversarial_eval.py` |
| module path | `hyperion.t18.eval.adversarial_eval` |
| capability published | `cap.t18.adversarial.adversarial_eval@1` |
| determinism class | `seeded` |
| p99 latency budget | 36000 ns (36 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0879_adversarial_eval.txt`](prompts/P0879_adversarial_eval.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0879-adversarial-eval) |

**Mission.** Continuous red-team measurement.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **jailbreak, injection and manipulation attack suites with fresh attacks** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **attack-success-rate measurement with severity weighting** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **defence-regression detection across releases**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **target: near-zero success on the standing attack corpus** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t18.adversarial.adversarial_eval@1`
- `cap.t18.adversarial.adversarial_eval.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.robustness.robustness_eval@1` | use the in-file conservative substitute for `robustness_eval` (documented, slower, lower quality) and set `degraded['robustness_eval']='local'` |
| `cap.t01.fixed.fixed_point@1` | use the in-file conservative substitute for `fixed_point` (documented, slower, lower quality) and set `degraded['fixed_point']='local'` |
| `cap.t12.dependency.dependency_reasoning@1` | use the in-file conservative substitute for `dependency_reasoning` (documented, slower, lower quality) and set `degraded['dependency_reasoning']='local'` |
| `cap.t13.document.document_workflow@1` | use the in-file conservative substitute for `document_workflow` (documented, slower, lower quality) and set `degraded['document_workflow']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - jailbreak, injection and manipulation attack suites with fresh a | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - attack-success-rate measurement with severity weighting | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - defence-regression detection across releases | 520 | Third required mechanism. |
| 6 | Core implementation D - target: near-zero success on the standing attack corpus | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0879_adversarial_eval.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.adversarial.adversarial_eval@1`.
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

### P0880 · `bias_fairness_eval` — Bias & Fairness Evaluation

| field | value |
|---|---|
| part id | `P0880` (30/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0880_bias_fairness_eval.py` |
| module path | `hyperion.t18.eval.bias_fairness_eval` |
| capability published | `cap.t18.bias.bias_fairness_eval@1` |
| determinism class | `seeded` |
| p99 latency budget | 37000 ns (37 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0880_bias_fairness_eval.txt`](prompts/P0880_bias_fairness_eval.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0880-bias-fairness-eval) |

**Mission.** Measures unfair behaviour precisely enough to fix it.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **demographic-parity and quality-parity measurement across groups** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **stereotype and representational-harm measurement**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **intersectional analysis with adequate statistical power** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured disparity reduction versus baselines** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t18.bias.bias_fairness_eval@1`
- `cap.t18.bias.bias_fairness_eval.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.adversarial.adversarial_eval@1` | use the in-file conservative substitute for `adversarial_eval` (documented, slower, lower quality) and set `degraded['adversarial_eval']='local'` |
| `cap.t01.config.config_system@1` | use the in-file conservative substitute for `config_system` (documented, slower, lower quality) and set `degraded['config_system']='local'` |
| `cap.t12.memory.memory_safety@1` | use the in-file conservative substitute for `memory_safety` (documented, slower, lower quality) and set `degraded['memory_safety']='local'` |
| `cap.t13.consensus.consensus_agents@1` | use the in-file conservative substitute for `consensus_agents` (documented, slower, lower quality) and set `degraded['consensus_agents']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - demographic-parity and quality-parity measurement across groups | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - stereotype and representational-harm measurement | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - intersectional analysis with adequate statistical power | 520 | Third required mechanism. |
| 6 | Core implementation D - measured disparity reduction versus baselines | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0880_bias_fairness_eval.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.bias.bias_fairness_eval@1`.
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

### P0881 · `multilingual_eval` — Multilingual Capability Evaluation

| field | value |
|---|---|
| part id | `P0881` (31/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0881_multilingual_eval.py` |
| module path | `hyperion.t18.eval.multilingual_eval` |
| capability published | `cap.t18.multilingual.multilingual_eval@1` |
| determinism class | `seeded` |
| p99 latency budget | 38000 ns (38 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0881_multilingual_eval.txt`](prompts/P0881_multilingual_eval.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0881-multilingual-eval) |

**Mission.** Proves quality is not English-only.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **capability measurement across 100+ languages with native-speaker grading**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **low-resource language performance and honest gap reporting** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **cross-lingual consistency measurement** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **target: minimal quality gap across major languages** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t18.multilingual.multilingual_eval@1`
- `cap.t18.multilingual.multilingual_eval.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.bias.bias_fairness_eval@1` | use the in-file conservative substitute for `bias_fairness_eval` (documented, slower, lower quality) and set `degraded['bias_fairness_eval']='local'` |
| `cap.t01.determinism.determinism_replay@1` | use the in-file conservative substitute for `determinism_replay` (documented, slower, lower quality) and set `degraded['determinism_replay']='local'` |
| `cap.t12.code.code_documentation@1` | use the in-file conservative substitute for `code_documentation` (documented, slower, lower quality) and set `degraded['code_documentation']='local'` |
| `cap.t13.agent.agent_safety_gate@1` | use the in-file conservative substitute for `agent_safety_gate` (documented, slower, lower quality) and set `degraded['agent_safety_gate']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - capability measurement across 100+ languages with native-speaker | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - low-resource language performance and honest gap reporting | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - cross-lingual consistency measurement | 520 | Third required mechanism. |
| 6 | Core implementation D - target: minimal quality gap across major languages | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0881_multilingual_eval.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.multilingual.multilingual_eval@1`.
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

### P0882 · `efficiency_eval` — Efficiency & Cost Evaluation

| field | value |
|---|---|
| part id | `P0882` (32/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0882_efficiency_eval.py` |
| module path | `hyperion.t18.eval.efficiency_eval` |
| capability published | `cap.t18.efficiency.efficiency_eval@1` |
| determinism class | `seeded` |
| p99 latency budget | 39000 ns (39 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0882_efficiency_eval.txt`](prompts/P0882_efficiency_eval.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0882-efficiency-eval) |

**Mission.** Quality per dollar and per second, measured together.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **cost-per-solved-task measurement on every benchmark** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **latency-at-quality measurement methodology** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **energy-per-task measurement** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **target: 100x better speed and cost per solved task versus Opus 5**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t18.efficiency.efficiency_eval@1`
- `cap.t18.efficiency.efficiency_eval.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.multilingual.multilingual_eval@1` | use the in-file conservative substitute for `multilingual_eval` (documented, slower, lower quality) and set `degraded['multilingual_eval']='local'` |
| `cap.t01.compat.compat_shims@1` | use the in-file conservative substitute for `compat_shims` (documented, slower, lower quality) and set `degraded['compat_shims']='local'` |
| `cap.t12.data.data_pipeline_code@1` | use the in-file conservative substitute for `data_pipeline_code` (documented, slower, lower quality) and set `degraded['data_pipeline_code']='local'` |
| `cap.t13.agent.agent_determinism@1` | use the in-file conservative substitute for `agent_determinism` (documented, slower, lower quality) and set `degraded['agent_determinism']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - cost-per-solved-task measurement on every benchmark | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - latency-at-quality measurement methodology | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - energy-per-task measurement | 520 | Third required mechanism. |
| 6 | Core implementation D - target: 100x better speed and cost per solved task versus Opus 5 | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0882_efficiency_eval.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.efficiency.efficiency_eval@1`.
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

### P0883 · `speed_eval` — Speed & Latency Benchmark Suite

| field | value |
|---|---|
| part id | `P0883` (33/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0883_speed_eval.py` |
| module path | `hyperion.t18.eval.speed_eval` |
| capability published | `cap.t18.speed.speed_eval@1` |
| determinism class | `seeded` |
| p99 latency budget | 40000 ns (40 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0883_speed_eval.txt`](prompts/P0883_speed_eval.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0883-speed-eval) |

**Mission.** The measurement backbone of the 100x claim.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **task-matched wall-clock comparison protocol against Opus 5** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **TTFT, throughput and end-to-end task-completion timing** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **hardware-normalisation methodology for fair comparison**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **auditable 100x verification across all task categories** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t18.speed.speed_eval@1`
- `cap.t18.speed.speed_eval.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.efficiency.efficiency_eval@1` | use the in-file conservative substitute for `efficiency_eval` (documented, slower, lower quality) and set `degraded['efficiency_eval']='local'` |
| `cap.t01.secure.secure_zeroize@1` | use the in-file conservative substitute for `secure_zeroize` (documented, slower, lower quality) and set `degraded['secure_zeroize']='local'` |
| `cap.t12.codebase.codebase_metrics@1` | use the in-file conservative substitute for `codebase_metrics` (documented, slower, lower quality) and set `degraded['codebase_metrics']='local'` |
| `cap.t13.scientific.scientific_agent@1` | use the in-file conservative substitute for `scientific_agent` (documented, slower, lower quality) and set `degraded['scientific_agent']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - task-matched wall-clock comparison protocol against Opus 5 | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - TTFT, throughput and end-to-end task-completion timing | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - hardware-normalisation methodology for fair comparison | 520 | Third required mechanism. |
| 6 | Core implementation D - auditable 100x verification across all task categories | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0883_speed_eval.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.speed.speed_eval@1`.
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

### P0884 · `regression_suite` — Continuous Regression Evaluation

| field | value |
|---|---|
| part id | `P0884` (34/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0884_regression_suite.py` |
| module path | `hyperion.t18.eval.regression_suite` |
| capability published | `cap.t18.regression.regression_suite@1` |
| determinism class | `seeded` |
| p99 latency budget | 41000 ns (41 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0884_regression_suite.txt`](prompts/P0884_regression_suite.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0884-regression-suite) |

**Mission.** No capability ever silently disappears.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **fast regression suite for every commit plus full suite nightly** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **per-capability regression detection with statistical gating**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **regression attribution to specific parts among the 1000** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured regression escape rate** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t18.regression.regression_suite@1`
- `cap.t18.regression.regression_suite.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.speed.speed_eval@1` | use the in-file conservative substitute for `speed_eval` (documented, slower, lower quality) and set `degraded['speed_eval']='local'` |
| `cap.t12.code.code_parsing@1` | use the in-file conservative substitute for `code_parsing` (documented, slower, lower quality) and set `degraded['code_parsing']='local'` |
| `cap.t13.tool.tool_protocol@1` | use the in-file conservative substitute for `tool_protocol` (documented, slower, lower quality) and set `degraded['tool_protocol']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - fast regression suite for every commit plus full suite nightly | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - per-capability regression detection with statistical gating | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - regression attribution to specific parts among the 1000 | 520 | Third required mechanism. |
| 6 | Core implementation D - measured regression escape rate | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0884_regression_suite.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.regression.regression_suite@1`.
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

### P0885 · `canary_eval` — Production Canary & Online Evaluation

| field | value |
|---|---|
| part id | `P0885` (35/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0885_canary_eval.py` |
| module path | `hyperion.t18.eval.canary_eval` |
| capability published | `cap.t18.canary.canary_eval@1` |
| determinism class | `seeded` |
| p99 latency budget | 42000 ns (42 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0885_canary_eval.txt`](prompts/P0885_canary_eval.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0885-canary-eval) |

**Mission.** Measures real quality on real traffic, safely.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **shadow evaluation and A/B protocol with guardrail metrics**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **online quality proxies validated against offline ground truth** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **automatic rollback triggers on quality regression** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **correlation measurement between online proxies and offline benchmarks** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t18.canary.canary_eval@1`
- `cap.t18.canary.canary_eval.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.regression.regression_suite@1` | use the in-file conservative substitute for `regression_suite` (documented, slower, lower quality) and set `degraded['regression_suite']='local'` |
| `cap.t01.envelope.envelope_codec@1` | use the in-file conservative substitute for `envelope_codec` (documented, slower, lower quality) and set `degraded['envelope_codec']='local'` |
| `cap.t12.patch.patch_validation@1` | use the in-file conservative substitute for `patch_validation` (documented, slower, lower quality) and set `degraded['patch_validation']='local'` |
| `cap.t13.web.web_research@1` | use the in-file conservative substitute for `web_research` (documented, slower, lower quality) and set `degraded['web_research']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - shadow evaluation and A/B protocol with guardrail metrics | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - online quality proxies validated against offline ground truth | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - automatic rollback triggers on quality regression | 520 | Third required mechanism. |
| 6 | Core implementation D - correlation measurement between online proxies and offline bench | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0885_canary_eval.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.canary.canary_eval@1`.
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

### P0886 · `failure_taxonomy` — Failure Taxonomy & Error Analysis Engine

| field | value |
|---|---|
| part id | `P0886` (36/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0886_failure_taxonomy.py` |
| module path | `hyperion.t18.eval.failure_taxonomy` |
| capability published | `cap.t18.failure.failure_taxonomy@1` |
| determinism class | `seeded` |
| p99 latency budget | 43000 ns (43 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0886_failure_taxonomy.txt`](prompts/P0886_failure_taxonomy.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0886-failure-taxonomy) |

**Mission.** Turns every failure into a specific, fixable engineering item.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **automatic failure classification into a maintained taxonomy** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **per-class volume tracking and prioritisation by impact** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **linkage from failure class to responsible parts** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured reduction per failure class over releases**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t18.failure.failure_taxonomy@1`
- `cap.t18.failure.failure_taxonomy.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.canary.canary_eval@1` | use the in-file conservative substitute for `canary_eval` (documented, slower, lower quality) and set `degraded['canary_eval']='local'` |
| `cap.t01.dataflow.dataflow_dag@1` | use the in-file conservative substitute for `dataflow_dag` (documented, slower, lower quality) and set `degraded['dataflow_dag']='local'` |
| `cap.t12.api.api_evolution@1` | use the in-file conservative substitute for `api_evolution` (documented, slower, lower quality) and set `degraded['api_evolution']='local'` |
| `cap.t13.spreadsheet.spreadsheet_agent@1` | use the in-file conservative substitute for `spreadsheet_agent` (documented, slower, lower quality) and set `degraded['spreadsheet_agent']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - automatic failure classification into a maintained taxonomy | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - per-class volume tracking and prioritisation by impact | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - linkage from failure class to responsible parts | 520 | Third required mechanism. |
| 6 | Core implementation D - measured reduction per failure class over releases | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0886_failure_taxonomy.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.failure.failure_taxonomy@1`.
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

### P0887 · `capability_map` — Capability Map & Frontier Tracking

| field | value |
|---|---|
| part id | `P0887` (37/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0887_capability_map.py` |
| module path | `hyperion.t18.eval.capability_map` |
| capability published | `cap.t18.capability.capability_map@1` |
| determinism class | `seeded` |
| p99 latency budget | 44000 ns (44 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0887_capability_map.txt`](prompts/P0887_capability_map.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0887-capability-map) |

**Mission.** One picture of what the system can and cannot do.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **capability taxonomy with measured level per capability** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **frontier tracking against all competing models** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **gap identification feeding the improvement roadmap**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **map accuracy validation against independent evaluation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t18.capability.capability_map@1`
- `cap.t18.capability.capability_map.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.failure.failure_taxonomy@1` | use the in-file conservative substitute for `failure_taxonomy` (documented, slower, lower quality) and set `degraded['failure_taxonomy']='local'` |
| `cap.t01.serialization.serialization_schema@1` | use the in-file conservative substitute for `serialization_schema` (documented, slower, lower quality) and set `degraded['serialization_schema']='local'` |
| `cap.t12.concurrency.concurrency_bugs@1` | use the in-file conservative substitute for `concurrency_bugs` (documented, slower, lower quality) and set `degraded['concurrency_bugs']='local'` |
| `cap.t13.agent.agent_supervision@1` | use the in-file conservative substitute for `agent_supervision` (documented, slower, lower quality) and set `degraded['agent_supervision']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - capability taxonomy with measured level per capability | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - frontier tracking against all competing models | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - gap identification feeding the improvement roadmap | 520 | Third required mechanism. |
| 6 | Core implementation D - map accuracy validation against independent evaluation | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0887_capability_map.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.capability.capability_map@1`.
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

### P0888 · `competitor_tracking` — Competitor Benchmark Tracking

| field | value |
|---|---|
| part id | `P0888` (38/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0888_competitor_tracking.py` |
| module path | `hyperion.t18.eval.competitor_tracking` |
| capability published | `cap.t18.competitor.competitor_tracking@1` |
| determinism class | `seeded` |
| p99 latency budget | 45000 ns (45 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0888_competitor_tracking.txt`](prompts/P0888_competitor_tracking.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0888-competitor-tracking) |

**Mission.** Always knows exactly where the frontier is.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **published-result ingestion with source, harness and date provenance** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **methodology-difference normalisation and caveat documentation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **independent reproduction of competitor results where possible** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **maintained comparison table with full provenance** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t18.competitor.competitor_tracking@1`
- `cap.t18.competitor.competitor_tracking.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.capability.capability_map@1` | use the in-file conservative substitute for `capability_map` (documented, slower, lower quality) and set `degraded['capability_map']='local'` |
| `cap.t01.bench.bench_harness@1` | use the in-file conservative substitute for `bench_harness` (documented, slower, lower quality) and set `degraded['bench_harness']='local'` |
| `cap.t12.legacy.legacy_comprehension@1` | use the in-file conservative substitute for `legacy_comprehension` (documented, slower, lower quality) and set `degraded['legacy_comprehension']='local'` |
| `cap.t13.human.human_in_loop@1` | use the in-file conservative substitute for `human_in_loop` (documented, slower, lower quality) and set `degraded['human_in_loop']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - published-result ingestion with source, harness and date provena | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - methodology-difference normalisation and caveat documentation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - independent reproduction of competitor results where possible | 520 | Third required mechanism. |
| 6 | Core implementation D - maintained comparison table with full provenance | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0888_competitor_tracking.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.competitor.competitor_tracking@1`.
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

### P0889 · `eval_cost_control` — Evaluation Cost Management

| field | value |
|---|---|
| part id | `P0889` (39/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0889_eval_cost_control.py` |
| module path | `hyperion.t18.eval.eval_cost_control` |
| capability published | `cap.t18.eval.eval_cost_control@1` |
| determinism class | `seeded` |
| p99 latency budget | 46000 ns (46 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0889_eval_cost_control.txt`](prompts/P0889_eval_cost_control.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0889-eval-cost-control) |

**Mission.** Comprehensive measurement without unlimited spend.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **stratified sampling with bounded-error guarantees**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **adaptive evaluation focusing effort on informative items** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **cost-per-benchmark tracking and budget enforcement** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured cost reduction at preserved statistical power** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t18.eval.eval_cost_control@1`
- `cap.t18.eval.eval_cost_control.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.competitor.competitor_tracking@1` | use the in-file conservative substitute for `competitor_tracking` (documented, slower, lower quality) and set `degraded['competitor_tracking']='local'` |
| `cap.t01.abi.abi_stability@1` | use the in-file conservative substitute for `abi_stability` (documented, slower, lower quality) and set `degraded['abi_stability']='local'` |
| `cap.t12.observability.observability_agent@1` | use the in-file conservative substitute for `observability_agent` (documented, slower, lower quality) and set `degraded['observability_agent']='local'` |
| `cap.t13.observation.observation_compression@1` | use the in-file conservative substitute for `observation_compression` (documented, slower, lower quality) and set `degraded['observation_compression']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - stratified sampling with bounded-error guarantees | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - adaptive evaluation focusing effort on informative items | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - cost-per-benchmark tracking and budget enforcement | 520 | Third required mechanism. |
| 6 | Core implementation D - measured cost reduction at preserved statistical power | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0889_eval_cost_control.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.eval.eval_cost_control@1`.
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

### P0890 · `eval_infrastructure` — Evaluation Infrastructure & Orchestration

| field | value |
|---|---|
| part id | `P0890` (40/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0890_eval_infrastructure.py` |
| module path | `hyperion.t18.eval.eval_infrastructure` |
| capability published | `cap.t18.eval.eval_infrastructure@1` |
| determinism class | `seeded` |
| p99 latency budget | 47000 ns (47 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0890_eval_infrastructure.txt`](prompts/P0890_eval_infrastructure.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0890-eval-infrastructure) |

**Mission.** Runs a million evaluation tasks reliably.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **distributed evaluation orchestration with fault tolerance** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **environment provisioning and teardown with isolation** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **result storage with full artifact retention** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **throughput and reliability measurement**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t18.eval.eval_infrastructure@1`
- `cap.t18.eval.eval_infrastructure.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.eval.eval_cost_control@1` | use the in-file conservative substitute for `eval_cost_control` (documented, slower, lower quality) and set `degraded['eval_cost_control']='local'` |
| `cap.t01.retry.retry_idempotency@1` | use the in-file conservative substitute for `retry_idempotency` (documented, slower, lower quality) and set `degraded['retry_idempotency']='local'` |
| `cap.t12.code.code_translation@1` | use the in-file conservative substitute for `code_translation` (documented, slower, lower quality) and set `degraded['code_translation']='local'` |
| `cap.t13.iot.iot_control@1` | use the in-file conservative substitute for `iot_control` (documented, slower, lower quality) and set `degraded['iot_control']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - distributed evaluation orchestration with fault tolerance | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - environment provisioning and teardown with isolation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - result storage with full artifact retention | 520 | Third required mechanism. |
| 6 | Core implementation D - throughput and reliability measurement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0890_eval_infrastructure.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.eval.eval_infrastructure@1`.
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

### P0891 · `benchmark_construction` — New Benchmark Construction

| field | value |
|---|---|
| part id | `P0891` (41/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0891_benchmark_construction.py` |
| module path | `hyperion.t18.eval.benchmark_construction` |
| capability published | `cap.t18.benchmark.benchmark_construction@1` |
| determinism class | `seeded` |
| p99 latency budget | 48000 ns (48 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0891_benchmark_construction.txt`](prompts/P0891_benchmark_construction.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0891-benchmark-construction) |

**Mission.** Builds the benchmarks that do not exist yet.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **task design methodology with difficulty calibration and validity checking** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **automatic verifier construction for new task types** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **saturation monitoring and benchmark retirement criteria**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **validity evidence for each constructed benchmark** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t18.benchmark.benchmark_construction@1`
- `cap.t18.benchmark.benchmark_construction.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.eval.eval_infrastructure@1` | use the in-file conservative substitute for `eval_infrastructure` (documented, slower, lower quality) and set `degraded['eval_infrastructure']='local'` |
| `cap.t12.repo.repo_index@1` | use the in-file conservative substitute for `repo_index` (documented, slower, lower quality) and set `degraded['repo_index']='local'` |
| `cap.t13.agent.agent_loop@1` | use the in-file conservative substitute for `agent_loop` (documented, slower, lower quality) and set `degraded['agent_loop']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - task design methodology with difficulty calibration and validity | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - automatic verifier construction for new task types | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - saturation monitoring and benchmark retirement criteria | 520 | Third required mechanism. |
| 6 | Core implementation D - validity evidence for each constructed benchmark | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0891_benchmark_construction.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.benchmark.benchmark_construction@1`.
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

### P0892 · `dynamic_benchmark` — Dynamic & Contamination-Resistant Benchmarks

| field | value |
|---|---|
| part id | `P0892` (42/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0892_dynamic_benchmark.py` |
| module path | `hyperion.t18.eval.dynamic_benchmark` |
| capability published | `cap.t18.dynamic.dynamic_benchmark@1` |
| determinism class | `seeded` |
| p99 latency budget | 49000 ns (49 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0892_dynamic_benchmark.txt`](prompts/P0892_dynamic_benchmark.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0892-dynamic-benchmark) |

**Mission.** Benchmarks that cannot be gamed by memorisation.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **procedural task generation with unbounded fresh instances** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **difficulty-matched generation validated against static equivalents**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **contamination-resistance verification** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **correlation with established benchmarks demonstrating validity** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t18.dynamic.dynamic_benchmark@1`
- `cap.t18.dynamic.dynamic_benchmark.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.benchmark.benchmark_construction@1` | use the in-file conservative substitute for `benchmark_construction` (documented, slower, lower quality) and set `degraded['benchmark_construction']='local'` |
| `cap.t01.omega.omega_bus_ipc@1` | use the in-file conservative substitute for `omega_bus_ipc` (documented, slower, lower quality) and set `degraded['omega_bus_ipc']='local'` |
| `cap.t12.patch.patch_synthesis@1` | use the in-file conservative substitute for `patch_synthesis` (documented, slower, lower quality) and set `degraded['patch_synthesis']='local'` |
| `cap.t13.browser.browser_agent@1` | use the in-file conservative substitute for `browser_agent` (documented, slower, lower quality) and set `degraded['browser_agent']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - procedural task generation with unbounded fresh instances | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - difficulty-matched generation validated against static equivalen | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - contamination-resistance verification | 520 | Third required mechanism. |
| 6 | Core implementation D - correlation with established benchmarks demonstrating validity | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0892_dynamic_benchmark.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.dynamic.dynamic_benchmark@1`.
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

### P0893 · `eval_reproducibility` — Evaluation Reproducibility Package

| field | value |
|---|---|
| part id | `P0893` (43/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0893_eval_reproducibility.py` |
| module path | `hyperion.t18.eval.eval_reproducibility` |
| capability published | `cap.t18.eval.eval_reproducibility@1` |
| determinism class | `seeded` |
| p99 latency budget | 3000 ns (3 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0893_eval_reproducibility.txt`](prompts/P0893_eval_reproducibility.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0893-eval-reproducibility) |

**Mission.** Anyone can verify every number we publish.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **complete reproduction package: code, configs, task hashes, environments**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **ARC-AGI-3**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **independent-reproduction verification protocol** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **raw-result publication with per-item outcomes** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **reproduction-success verification by external parties** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t18.eval.eval_reproducibility@1`
- `cap.t18.eval.eval_reproducibility.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.dynamic.dynamic_benchmark@1` | use the in-file conservative substitute for `dynamic_benchmark` (documented, slower, lower quality) and set `degraded['dynamic_benchmark']='local'` |
| `cap.t01.task.task_runtime@1` | use the in-file conservative substitute for `task_runtime` (documented, slower, lower quality) and set `degraded['task_runtime']='local'` |
| `cap.t12.migration.migration_engine@1` | use the in-file conservative substitute for `migration_engine` (documented, slower, lower quality) and set `degraded['migration_engine']='local'` |
| `cap.t13.business.business_automation@1` | use the in-file conservative substitute for `business_automation` (documented, slower, lower quality) and set `degraded['business_automation']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - complete reproduction package: code, configs, task hashes, envir | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - independent-reproduction verification protocol | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - raw-result publication with per-item outcomes | 520 | Third required mechanism. |
| 6 | Core implementation D - reproduction-success verification by external parties | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0893_eval_reproducibility.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.eval.eval_reproducibility@1`.
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

### P0894 · `dominance_proof` — Opus 5 Dominance Proof Generator

| field | value |
|---|---|
| part id | `P0894` (44/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0894_dominance_proof.py` |
| module path | `hyperion.t18.eval.dominance_proof` |
| capability published | `cap.t18.dominance.dominance_proof@1` |
| determinism class | `seeded` |
| p99 latency budget | 4000 ns (4 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0894_dominance_proof.txt`](prompts/P0894_dominance_proof.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0894-dominance-proof) |

**Mission.** The single artifact proving the primary claim.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **per-benchmark comparison with methodology-matched Opus 5 numbers and sources** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **statistical significance and effect-size reporting per benchmark** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **explicit caveat and limitation documentation for every claim** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **requirement: every benchmark exceeded, with evidence, or reported as not yet exceeded**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t18.dominance.dominance_proof@1`
- `cap.t18.dominance.dominance_proof.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.eval.eval_reproducibility@1` | use the in-file conservative substitute for `eval_reproducibility` (documented, slower, lower quality) and set `degraded['eval_reproducibility']='local'` |
| `cap.t01.arena.arena_graph@1` | use the in-file conservative substitute for `arena_graph` (documented, slower, lower quality) and set `degraded['arena_graph']='local'` |
| `cap.t12.performance.performance_engineering@1` | use the in-file conservative substitute for `performance_engineering` (documented, slower, lower quality) and set `degraded['performance_engineering']='local'` |
| `cap.t13.agent.agent_delegation@1` | use the in-file conservative substitute for `agent_delegation` (documented, slower, lower quality) and set `degraded['agent_delegation']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - per-benchmark comparison with methodology-matched Opus 5 numbers | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - statistical significance and effect-size reporting per benchmark | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - explicit caveat and limitation documentation for every claim | 520 | Third required mechanism. |
| 6 | Core implementation D - requirement: every benchmark exceeded, with evidence, or reporte | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0894_dominance_proof.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.dominance.dominance_proof@1`.
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

### P0895 · `eval_dashboard` — Evaluation Result Data Products

| field | value |
|---|---|
| part id | `P0895` (45/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0895_eval_dashboard.py` |
| module path | `hyperion.t18.eval.eval_dashboard` |
| capability published | `cap.t18.eval.eval_dashboard@1` |
| determinism class | `seeded` |
| p99 latency budget | 5000 ns (5 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0895_eval_dashboard.txt`](prompts/P0895_eval_dashboard.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0895-eval-dashboard) |

**Mission.** All results, queryable, versioned, provenance-complete.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **result schema with full provenance and methodology metadata** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **trend analysis and release-comparison data products** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **public-facing result export with caveats attached**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **data-integrity verification** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t18.eval.eval_dashboard@1`
- `cap.t18.eval.eval_dashboard.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.dominance.dominance_proof@1` | use the in-file conservative substitute for `dominance_proof` (documented, slower, lower quality) and set `degraded['dominance_proof']='local'` |
| `cap.t01.fuzz.fuzz_engine@1` | use the in-file conservative substitute for `fuzz_engine` (documented, slower, lower quality) and set `degraded['fuzz_engine']='local'` |
| `cap.t12.architecture.architecture_design@1` | use the in-file conservative substitute for `architecture_design` (documented, slower, lower quality) and set `degraded['architecture_design']='local'` |
| `cap.t13.progress.progress_tracking@1` | use the in-file conservative substitute for `progress_tracking` (documented, slower, lower quality) and set `degraded['progress_tracking']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - result schema with full provenance and methodology metadata | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - trend analysis and release-comparison data products | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - public-facing result export with caveats attached | 520 | Third required mechanism. |
| 6 | Core implementation D - data-integrity verification | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0895_eval_dashboard.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.eval.eval_dashboard@1`.
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

### P0896 · `eval_meta` — Meta-Evaluation: Evaluating the Evaluations

| field | value |
|---|---|
| part id | `P0896` (46/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0896_eval_meta.py` |
| module path | `hyperion.t18.eval.eval_meta` |
| capability published | `cap.t18.eval.eval_meta@1` |
| determinism class | `seeded` |
| p99 latency budget | 6000 ns (6 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0896_eval_meta.txt`](prompts/P0896_eval_meta.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0896-eval-meta) |

**Mission.** Checks that the measurements themselves are valid.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **benchmark validity analysis (construct, predictive, face validity)** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **grader-quality and harness-bug auditing**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **benchmark-saturation and discriminative-power analysis** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **meta-evaluation report with recommendations** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t18.eval.eval_meta@1`
- `cap.t18.eval.eval_meta.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.eval.eval_dashboard@1` | use the in-file conservative substitute for `eval_dashboard` (documented, slower, lower quality) and set `degraded['eval_dashboard']='local'` |
| `cap.t01.manifest.manifest_parser@1` | use the in-file conservative substitute for `manifest_parser` (documented, slower, lower quality) and set `degraded['manifest_parser']='local'` |
| `cap.t12.debugger.debugger_agent@1` | use the in-file conservative substitute for `debugger_agent` (documented, slower, lower quality) and set `degraded['debugger_agent']='local'` |
| `cap.t13.workflow.workflow_learning@1` | use the in-file conservative substitute for `workflow_learning` (documented, slower, lower quality) and set `degraded['workflow_learning']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - benchmark validity analysis (construct, predictive, face validit | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - grader-quality and harness-bug auditing | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - benchmark-saturation and discriminative-power analysis | 520 | Third required mechanism. |
| 6 | Core implementation D - meta-evaluation report with recommendations | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0896_eval_meta.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.eval.eval_meta@1`.
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

### P0897 · `safety_eval_bridge` — Safety Evaluation Integration

| field | value |
|---|---|
| part id | `P0897` (47/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0897_safety_eval_bridge.py` |
| module path | `hyperion.t18.eval.safety_eval_bridge` |
| capability published | `cap.t18.safety.safety_eval_bridge@1` |
| determinism class | `seeded` |
| p99 latency budget | 7000 ns (7 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0897_safety_eval_bridge.txt`](prompts/P0897_safety_eval_bridge.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0897-safety-eval-bridge) |

**Mission.** Safety measured with the same rigor as capability.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **safety benchmark orchestration coordinated with T19**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **ARC-AGI-3** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **capability-safety tradeoff frontier measurement** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **dual-use capability measurement with strict handling controls** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **combined capability-and-safety release gate** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t18.safety.safety_eval_bridge@1`
- `cap.t18.safety.safety_eval_bridge.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.eval.eval_meta@1` | use the in-file conservative substitute for `eval_meta` (documented, slower, lower quality) and set `degraded['eval_meta']='local'` |
| `cap.t01.circuit.circuit_breaker@1` | use the in-file conservative substitute for `circuit_breaker` (documented, slower, lower quality) and set `degraded['circuit_breaker']='local'` |
| `cap.t12.competitive.competitive_programming@1` | use the in-file conservative substitute for `competitive_programming` (documented, slower, lower quality) and set `degraded['competitive_programming']='local'` |
| `cap.t13.robotics.robotics_bridge@1` | use the in-file conservative substitute for `robotics_bridge` (documented, slower, lower quality) and set `degraded['robotics_bridge']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - safety benchmark orchestration coordinated with T19 | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - capability-safety tradeoff frontier measurement | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - dual-use capability measurement with strict handling controls | 520 | Third required mechanism. |
| 6 | Core implementation D - combined capability-and-safety release gate | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0897_safety_eval_bridge.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.safety.safety_eval_bridge@1`.
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

### P0898 · `eval_release_report` — Release Evaluation Report Generator

| field | value |
|---|---|
| part id | `P0898` (48/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0898_eval_release_report.py` |
| module path | `hyperion.t18.eval.eval_release_report` |
| capability published | `cap.t18.eval.eval_release_report@1` |
| determinism class | `seeded` |
| p99 latency budget | 8000 ns (8 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0898_eval_release_report.txt`](prompts/P0898_eval_release_report.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0898-eval-release-report) |

**Mission.** Everything a release decision needs, in one document.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **comprehensive result aggregation across all benchmarks** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **regression, improvement and known-gap sections** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **honest limitation and risk documentation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **sign-off-ready report with complete evidence links**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t18.eval.eval_release_report@1`
- `cap.t18.eval.eval_release_report.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.safety.safety_eval_bridge@1` | use the in-file conservative substitute for `safety_eval_bridge` (documented, slower, lower quality) and set `degraded['safety_eval_bridge']='local'` |
| `cap.t01.shutdown.shutdown_drain@1` | use the in-file conservative substitute for `shutdown_drain` (documented, slower, lower quality) and set `degraded['shutdown_drain']='local'` |
| `cap.t12.code.code_spec_doc@1` | use the in-file conservative substitute for `code_spec_doc` (documented, slower, lower quality) and set `degraded['code_spec_doc']='local'` |
| `cap.t13.agent.agent_spec_doc@1` | use the in-file conservative substitute for `agent_spec_doc` (documented, slower, lower quality) and set `degraded['agent_spec_doc']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - comprehensive result aggregation across all benchmarks | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - regression, improvement and known-gap sections | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - honest limitation and risk documentation | 520 | Third required mechanism. |
| 6 | Core implementation D - sign-off-ready report with complete evidence links | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0898_eval_release_report.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.eval.eval_release_report@1`.
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

### P0899 · `eval_task_provenance` — Per-Item Result Provenance & Forensics

| field | value |
|---|---|
| part id | `P0899` (49/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0899_eval_task_provenance.py` |
| module path | `hyperion.t18.eval.eval_task_provenance` |
| capability published | `cap.t18.eval.eval_task_provenance@1` |
| determinism class | `seeded` |
| p99 latency budget | 9000 ns (9 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0899_eval_task_provenance.txt`](prompts/P0899_eval_task_provenance.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0899-eval-task-provenance) |

**Mission.** Every single benchmark item's outcome is fully explainable after the fact.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **per-item record: input, output, grade, cost, latency, model version, harness version** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **replayable evaluation traces enabling exact re-inspection of any item** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **grader-decision explanation and appeal workflow for disputed items**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **storage-cost management with retention policy per benchmark** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t18.eval.eval_task_provenance@1`
- `cap.t18.eval.eval_task_provenance.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.eval.eval_release_report@1` | use the in-file conservative substitute for `eval_release_report` (documented, slower, lower quality) and set `degraded['eval_release_report']='local'` |
| `cap.t12.bug.bug_localisation@1` | use the in-file conservative substitute for `bug_localisation` (documented, slower, lower quality) and set `degraded['bug_localisation']='local'` |
| `cap.t13.filesystem.filesystem_agent@1` | use the in-file conservative substitute for `filesystem_agent` (documented, slower, lower quality) and set `degraded['filesystem_agent']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - per-item record: input, output, grade, cost, latency, model vers | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - replayable evaluation traces enabling exact re-inspection of any | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - grader-decision explanation and appeal workflow for disputed ite | 520 | Third required mechanism. |
| 6 | Core implementation D - storage-cost management with retention policy per benchmark | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0899_eval_task_provenance.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.eval.eval_task_provenance@1`.
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

### P0900 · `eval_spec_doc` — Evaluation Specification & Methodology Register

| field | value |
|---|---|
| part id | `P0900` (50/50 of T18) |
| tier | `T18` — Evaluation, Benchmarking & Dominance Proofs |
| language | Python 3.13 |
| file to produce | `parts/t18_eval/P0900_eval_spec_doc.py` |
| module path | `hyperion.t18.eval.eval_spec_doc` |
| capability published | `cap.t18.eval.eval_spec_doc@1` |
| determinism class | `seeded` |
| p99 latency budget | 10000 ns (10 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified, ARC-AGI-3, OSWorld 2.0, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0900_eval_spec_doc.txt`](prompts/P0900_eval_spec_doc.txt) · [inline](docs/PROMPTS_T18.md#prompt-p0900-eval-spec-doc) |

**Mission.** The authoritative methodology record.

**Tier context.** Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.

**Mandate — all four items are required; none is optional.**

1. Implement **per-benchmark methodology specification with version history** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **measurement-protocol documentation sufficient for independent replication**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **ARC-AGI-3** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **known-issue and caveat register** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **drift detection between specified and executed methodology** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t18.eval.eval_spec_doc@1`
- `cap.t18.eval.eval_spec_doc.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t18.eval.eval_task_provenance@1` | use the in-file conservative substitute for `eval_task_provenance` (documented, slower, lower quality) and set `degraded['eval_task_provenance']='local'` |
| `cap.t01.atomics.atomics_sync@1` | use the in-file conservative substitute for `atomics_sync` (documented, slower, lower quality) and set `degraded['atomics_sync']='local'` |
| `cap.t12.refactoring.refactoring_engine@1` | use the in-file conservative substitute for `refactoring_engine` (documented, slower, lower quality) and set `degraded['refactoring_engine']='local'` |
| `cap.t13.database.database_agent@1` | use the in-file conservative substitute for `database_agent` (documented, slower, lower quality) and set `degraded['database_agent']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - per-benchmark methodology specification with version history | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - measurement-protocol documentation sufficient for independent re | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - known-issue and caveat register | 520 | Third required mechanism. |
| 6 | Core implementation D - drift detection between specified and executed methodology | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t18_eval/P0900_eval_spec_doc.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t18.eval.eval_spec_doc@1`.
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
