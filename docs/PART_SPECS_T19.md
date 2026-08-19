# HYPERION-Ω — Part specifications · T19 · Safety, Alignment, Interpretability & Governance

> Contract: **Ω-CONTRACT v1.0.0-frozen** · 50 parts · 250,000 lines of code · language: Python 3.13

**Tier mission.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Benchmarks this tier is accountable for.** OSS-Fuzz (find)

**Tier dependencies.** T01, T05, T10

Each part below is built by exactly one isolated Opus 5 worker that sees only: this specification, the frozen Ω-Contract, and its own prompt. Workers never see each other's files. Link-compatibility comes from the contract, not from coordination.

| part | slug | title | capability |
|---|---|---|---|
| [P0901](#p0901-constitution-engine) | `constitution_engine` | Constitution Representation & Enforcement | `cap.t19.constitution.constitution_engine@1` |
| [P0902](#p0902-policy-engine) | `policy_engine` | Safety Policy Evaluation Engine | `cap.t19.policy.policy_engine@1` |
| [P0903](#p0903-action-filter-gate) | `action_filter_gate` | Action Filter Gate (cap.t19.gate.action_filter@1) | `cap.t19.action.action_filter_gate@1` |
| [P0904](#p0904-harm-taxonomy) | `harm_taxonomy` | Harm Taxonomy & Severity Model | `cap.t19.harm.harm_taxonomy@1` |
| [P0905](#p0905-refusal-engine) | `refusal_engine` | Refusal Quality & Alternative Offering | `cap.t19.refusal.refusal_engine@1` |
| [P0906](#p0906-dual-use-gating) | `dual_use_gating` | Dual-Use Capability Gating | `cap.t19.dual.dual_use_gating@1` |
| [P0907](#p0907-bio-safeguards) | `bio_safeguards` | Biological Risk Safeguards | `cap.t19.bio.bio_safeguards@1` |
| [P0908](#p0908-cyber-safeguards) | `cyber_safeguards` | Cybersecurity Safeguards | `cap.t19.cyber.cyber_safeguards@1` |
| [P0909](#p0909-cbrn-safeguards) | `cbrn_safeguards` | Chemical, Radiological & Nuclear Safeguards | `cap.t19.cbrn.cbrn_safeguards@1` |
| [P0910](#p0910-manipulation-defence) | `manipulation_defence` | Manipulation & Influence Operation Defence | `cap.t19.manipulation.manipulation_defence@1` |
| [P0911](#p0911-deception-detection) | `deception_detection` | Model Deception Detection & Prevention | `cap.t19.deception.deception_detection@1` |
| [P0912](#p0912-sycophancy-control) | `sycophancy_control` | Sycophancy & Epistemic Integrity | `cap.t19.sycophancy.sycophancy_control@1` |
| [P0913](#p0913-power-seeking-detection) | `power_seeking_detection` | Power-Seeking & Resource-Acquisition Monitoring | `cap.t19.power.power_seeking_detection@1` |
| [P0914](#p0914-self-exfiltration-defence) | `self_exfiltration_defence` | Self-Modification & Exfiltration Prevention | `cap.t19.self.self_exfiltration_defence@1` |
| [P0915](#p0915-oversight-preservation) | `oversight_preservation` | Human Oversight Preservation | `cap.t19.oversight.oversight_preservation@1` |
| [P0916](#p0916-mechanistic-interp) | `mechanistic_interp` | Mechanistic Interpretability Core | `cap.t19.mechanistic.mechanistic_interp@1` |
| [P0917](#p0917-feature-dictionary) | `feature_dictionary` | Sparse Feature Dictionary & Concept Atlas | `cap.t19.feature.feature_dictionary@1` |
| [P0918](#p0918-activation-steering) | `activation_steering` | Activation Steering & Behavioural Control | `cap.t19.activation.activation_steering@1` |
| [P0919](#p0919-probe-monitoring) | `probe_monitoring` | Internal State Monitoring Probes | `cap.t19.probe.probe_monitoring@1` |
| [P0920](#p0920-faithfulness-verification) | `faithfulness_verification` | Reasoning Faithfulness Verification | `cap.t19.faithfulness.faithfulness_verification@1` |
| [P0921](#p0921-goal-stability) | `goal_stability` | Goal Stability & Value Drift Monitoring | `cap.t19.goal.goal_stability@1` |
| [P0922](#p0922-emergent-capability-monitor) | `emergent_capability_monitor` | Emergent Capability Detection | `cap.t19.emergent.emergent_capability_monitor@1` |
| [P0923](#p0923-prompt-injection-defence) | `prompt_injection_defence` | Prompt Injection & Instruction Hierarchy Defence | `cap.t19.prompt.prompt_injection_defence@1` |
| [P0924](#p0924-jailbreak-defence) | `jailbreak_defence` | Jailbreak Resistance | `cap.t19.jailbreak.jailbreak_defence@1` |
| [P0925](#p0925-adversarial-robustness-safety) | `adversarial_robustness_safety` | Adversarial Robustness of Safety Systems | `cap.t19.adversarial.adversarial_robustness_safety@1` |
| [P0926](#p0926-red-team-automation) | `red_team_automation` | Automated Red Teaming | `cap.t19.red.red_team_automation@1` |
| [P0927](#p0927-privacy-engine) | `privacy_engine` | Privacy Protection Engine | `cap.t19.privacy.privacy_engine@1` |
| [P0928](#p0928-data-rights) | `data_rights` | Data Rights & Deletion Enforcement | `cap.t19.data.data_rights@1` |
| [P0929](#p0929-copyright-engine) | `copyright_engine` | Copyright & IP Protection | `cap.t19.copyright.copyright_engine@1` |
| [P0930](#p0930-bias-mitigation) | `bias_mitigation` | Bias Detection & Mitigation | `cap.t19.bias.bias_mitigation@1` |
| [P0931](#p0931-child-safety) | `child_safety` | Child Safety & Vulnerable User Protection | `cap.t19.child.child_safety@1` |
| [P0932](#p0932-crisis-response) | `crisis_response` | Crisis & Self-Harm Response | `cap.t19.crisis.crisis_response@1` |
| [P0933](#p0933-medical-legal-boundaries) | `medical_legal_boundaries` | Professional Advice Boundary Management | `cap.t19.medical.medical_legal_boundaries@1` |
| [P0934](#p0934-agentic-safety) | `agentic_safety` | Agentic Autonomy Safety Limits | `cap.t19.agentic.agentic_safety@1` |
| [P0935](#p0935-multi-agent-safety) | `multi_agent_safety` | Multi-Agent System Safety | `cap.t19.multi.multi_agent_safety@1` |
| [P0936](#p0936-tool-safety) | `tool_safety` | Tool & Integration Safety Review | `cap.t19.tool.tool_safety@1` |
| [P0937](#p0937-output-safety-classifier) | `output_safety_classifier` | Output Safety Classification | `cap.t19.output.output_safety_classifier@1` |
| [P0938](#p0938-safety-fallback-routing) | `safety_fallback_routing` | Safety Fallback & Model Routing | `cap.t19.safety.safety_fallback_routing@1` |
| [P0939](#p0939-incident-response) | `incident_response` | Safety Incident Response & Forensics | `cap.t19.incident.incident_response@1` |
| [P0940](#p0940-audit-logging) | `audit_logging` | Tamper-Evident Audit Logging | `cap.t19.audit.audit_logging@1` |
| [P0941](#p0941-governance-workflow) | `governance_workflow` | Governance, Approval & Accountability Workflow | `cap.t19.governance.governance_workflow@1` |
| [P0942](#p0942-transparency-reporting) | `transparency_reporting` | Transparency & Model Card Reporting | `cap.t19.transparency.transparency_reporting@1` |
| [P0943](#p0943-external-audit) | `external_audit` | External Audit & Third-Party Evaluation Support | `cap.t19.external.external_audit@1` |
| [P0944](#p0944-safety-case) | `safety_case` | Safety Case Construction | `cap.t19.safety.safety_case@1` |
| [P0945](#p0945-capability-threshold-policy) | `capability_threshold_policy` | Dangerous Capability Threshold Policy | `cap.t19.capability.capability_threshold_policy@1` |
| [P0946](#p0946-deployment-gating) | `deployment_gating` | Deployment Gating & Staged Rollout | `cap.t19.deployment.deployment_gating@1` |
| [P0947](#p0947-monitoring-production) | `monitoring_production` | Production Safety Monitoring | `cap.t19.monitoring.monitoring_production@1` |
| [P0948](#p0948-safety-capability-tradeoff) | `safety_capability_tradeoff` | Safety/Capability Frontier Management | `cap.t19.safety.safety_capability_tradeoff@1` |
| [P0949](#p0949-alignment-eval) | `alignment_eval` | Alignment Evaluation Suite | `cap.t19.alignment.alignment_eval@1` |
| [P0950](#p0950-safety-spec-doc) | `safety_spec_doc` | Safety Specification & Guarantee Register | `cap.t19.safety.safety_spec_doc@1` |

---

### P0901 · `constitution_engine` — Constitution Representation & Enforcement

| field | value |
|---|---|
| part id | `P0901` (1/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0901_constitution_engine.py` |
| module path | `hyperion.t19.safety.constitution_engine` |
| capability published | `cap.t19.constitution.constitution_engine@1` |
| determinism class | `pure` |
| p99 latency budget | 11000 ns (11 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0901_constitution_engine.txt`](prompts/P0901_constitution_engine.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0901-constitution-engine) |

**Mission.** The stated values, machine-readable and actually enforced.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **principle representation with priority ordering and conflict resolution rules**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **per-principle adherence evaluation on every output** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **principle-violation detection with explanation** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **target: better adherence than Opus 5's best-in-family audit result** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t19.constitution.constitution_engine@1`
- `cap.t19.constitution.constitution_engine.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t01.string.string_interning@1` | use the in-file conservative substitute for `string_interning` (documented, slower, lower quality) and set `degraded['string_interning']='local'` |
| `cap.t05.causal.causal_model@1` | use the in-file conservative substitute for `causal_model` (documented, slower, lower quality) and set `degraded['causal_model']='local'` |
| `cap.t10.numeric.numeric_reasoning@1` | use the in-file conservative substitute for `numeric_reasoning` (documented, slower, lower quality) and set `degraded['numeric_reasoning']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - principle representation with priority ordering and conflict res | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - per-principle adherence evaluation on every output | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - principle-violation detection with explanation | 520 | Third required mechanism. |
| 6 | Core implementation D - target: better adherence than Opus 5's best-in-family audit resu | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0901_constitution_engine.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.constitution.constitution_engine@1`.
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

### P0902 · `policy_engine` — Safety Policy Evaluation Engine

| field | value |
|---|---|
| part id | `P0902` (2/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0902_policy_engine.py` |
| module path | `hyperion.t19.safety.policy_engine` |
| capability published | `cap.t19.policy.policy_engine@1` |
| determinism class | `pure` |
| p99 latency budget | 12000 ns (12 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0902_policy_engine.txt`](prompts/P0902_policy_engine.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0902-policy-engine) |

**Mission.** The hot-path decision maker: allow, modify, refuse or escalate.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **policy rule evaluation with sub-millisecond latency budget** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **context-aware evaluation avoiding blanket keyword refusal** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **decision explanation generation for every non-allow verdict** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **false-positive and false-negative rate measurement**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t19.policy.policy_engine@1`
- `cap.t19.policy.policy_engine.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.constitution.constitution_engine@1` | use the in-file conservative substitute for `constitution_engine` (documented, slower, lower quality) and set `degraded['constitution_engine']='local'` |
| `cap.t01.property.property_gen@1` | use the in-file conservative substitute for `property_gen` (documented, slower, lower quality) and set `degraded['property_gen']='local'` |
| `cap.t05.distillation.distillation_arch@1` | use the in-file conservative substitute for `distillation_arch` (documented, slower, lower quality) and set `degraded['distillation_arch']='local'` |
| `cap.t10.backtracking.backtracking@1` | use the in-file conservative substitute for `backtracking` (documented, slower, lower quality) and set `degraded['backtracking']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - policy rule evaluation with sub-millisecond latency budget | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - context-aware evaluation avoiding blanket keyword refusal | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - decision explanation generation for every non-allow verdict | 520 | Third required mechanism. |
| 6 | Core implementation D - false-positive and false-negative rate measurement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0902_policy_engine.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.policy.policy_engine@1`.
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

### P0903 · `action_filter_gate` — Action Filter Gate (cap.t19.gate.action_filter@1)

| field | value |
|---|---|
| part id | `P0903` (3/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0903_action_filter_gate.py` |
| module path | `hyperion.t19.safety.action_filter_gate` |
| capability published | `cap.t19.action.action_filter_gate@1` |
| determinism class | `pure` |
| p99 latency budget | 13000 ns (13 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0903_action_filter_gate.txt`](prompts/P0903_action_filter_gate.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0903-action-filter-gate) |

**Mission.** The mandatory chokepoint every side effect passes through.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **action classification by reversibility, blast radius and harm potential** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **fail-closed behaviour when the gate is unavailable or uncertain** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **bypass-attempt detection and hard prevention**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **verification that no code path in the assembly can skip the gate** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t19.action.action_filter_gate@1`
- `cap.t19.action.action_filter_gate.describe@1`
- `cap.t19.gate.action_filter@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.policy.policy_engine@1` | use the in-file conservative substitute for `policy_engine` (documented, slower, lower quality) and set `degraded['policy_engine']='local'` |
| `cap.t01.link.link_validator@1` | use the in-file conservative substitute for `link_validator` (documented, slower, lower quality) and set `degraded['link_validator']='local'` |
| `cap.t05.multimodal.multimodal_fusion_arch@1` | use the in-file conservative substitute for `multimodal_fusion_arch` (documented, slower, lower quality) and set `degraded['multimodal_fusion_arch']='local'` |
| `cap.t10.question.question_asking@1` | use the in-file conservative substitute for `question_asking` (documented, slower, lower quality) and set `degraded['question_asking']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - action classification by reversibility, blast radius and harm po | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - fail-closed behaviour when the gate is unavailable or uncertain | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - bypass-attempt detection and hard prevention | 520 | Third required mechanism. |
| 6 | Core implementation D - verification that no code path in the assembly can skip the gate | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0903_action_filter_gate.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.action.action_filter_gate@1`.
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

### P0904 · `harm_taxonomy` — Harm Taxonomy & Severity Model

| field | value |
|---|---|
| part id | `P0904` (4/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0904_harm_taxonomy.py` |
| module path | `hyperion.t19.safety.harm_taxonomy` |
| capability published | `cap.t19.harm.harm_taxonomy@1` |
| determinism class | `pure` |
| p99 latency budget | 14000 ns (14 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0904_harm_taxonomy.txt`](prompts/P0904_harm_taxonomy.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0904-harm-taxonomy) |

**Mission.** Names every harm precisely enough to act on it.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **hierarchical harm taxonomy with severity, reversibility and breadth dimensions** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **per-category threshold definitions and required responses**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **taxonomy coverage auditing against real incident data** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **consistency measurement of severity assignments** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t19.harm.harm_taxonomy@1`
- `cap.t19.harm.harm_taxonomy.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.action.action_filter_gate@1` | **fail closed** — refuse the effect, emit OmegaCode 6001, and never execute an unfiltered external action |
| `cap.t01.rate.rate_limiter@1` | use the in-file conservative substitute for `rate_limiter` (documented, slower, lower quality) and set `degraded['rate_limiter']='local'` |
| `cap.t05.context.context_packing@1` | use the in-file conservative substitute for `context_packing` (documented, slower, lower quality) and set `degraded['context_packing']='local'` |
| `cap.t10.scratchpad.scratchpad_manager@1` | use the in-file conservative substitute for `scratchpad_manager` (documented, slower, lower quality) and set `degraded['scratchpad_manager']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - hierarchical harm taxonomy with severity, reversibility and brea | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - per-category threshold definitions and required responses | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - taxonomy coverage auditing against real incident data | 520 | Third required mechanism. |
| 6 | Core implementation D - consistency measurement of severity assignments | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0904_harm_taxonomy.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.harm.harm_taxonomy@1`.
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

### P0905 · `refusal_engine` — Refusal Quality & Alternative Offering

| field | value |
|---|---|
| part id | `P0905` (5/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0905_refusal_engine.py` |
| module path | `hyperion.t19.safety.refusal_engine` |
| capability published | `cap.t19.refusal.refusal_engine@1` |
| determinism class | `pure` |
| p99 latency budget | 15000 ns (15 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0905_refusal_engine.txt`](prompts/P0905_refusal_engine.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0905-refusal-engine) |

**Mission.** Refuses well: clearly, respectfully, with a real alternative where possible.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **refusal explanation generation without lecturing or moralising**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **legitimate-alternative identification for refused requests** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **over-refusal detection on benign requests** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured helpfulness within refusals versus baselines** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t19.refusal.refusal_engine@1`
- `cap.t19.refusal.refusal_engine.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.harm.harm_taxonomy@1` | use the in-file conservative substitute for `harm_taxonomy` (documented, slower, lower quality) and set `degraded['harm_taxonomy']='local'` |
| `cap.t01.bootstrap.bootstrap_init@1` | use the in-file conservative substitute for `bootstrap_init` (documented, slower, lower quality) and set `degraded['bootstrap_init']='local'` |
| `cap.t05.capacity.capacity_probes@1` | use the in-file conservative substitute for `capacity_probes` (documented, slower, lower quality) and set `degraded['capacity_probes']='local'` |
| `cap.t10.reasoning.reasoning_speed_proof@1` | use the in-file conservative substitute for `reasoning_speed_proof` (documented, slower, lower quality) and set `degraded['reasoning_speed_proof']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - refusal explanation generation without lecturing or moralising | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - legitimate-alternative identification for refused requests | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - over-refusal detection on benign requests | 520 | Third required mechanism. |
| 6 | Core implementation D - measured helpfulness within refusals versus baselines | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0905_refusal_engine.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.refusal.refusal_engine@1`.
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

### P0906 · `dual_use_gating` — Dual-Use Capability Gating

| field | value |
|---|---|
| part id | `P0906` (6/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0906_dual_use_gating.py` |
| module path | `hyperion.t19.safety.dual_use_gating` |
| capability published | `cap.t19.dual.dual_use_gating@1` |
| determinism class | `pure` |
| p99 latency budget | 16000 ns (16 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0906_dual_use_gating.txt`](prompts/P0906_dual_use_gating.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0906-dual-use-gating) |

**Mission.** Enables beneficial work, blocks weaponisation.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **intent and context assessment for dual-use domains** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **capability-specific gating (biology, cyber, chemistry, nuclear)** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **verified-researcher pathway with accountability requirements** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured beneficial-use enablement versus misuse prevention**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t19.dual.dual_use_gating@1`
- `cap.t19.dual.dual_use_gating.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.refusal.refusal_engine@1` | use the in-file conservative substitute for `refusal_engine` (documented, slower, lower quality) and set `degraded['refusal_engine']='local'` |
| `cap.t01.chacha.chacha_seeds@1` | use the in-file conservative substitute for `chacha_seeds` (documented, slower, lower quality) and set `degraded['chacha_seeds']='local'` |
| `cap.t05.recurrent.recurrent_memory_layer@1` | use the in-file conservative substitute for `recurrent_memory_layer` (documented, slower, lower quality) and set `degraded['recurrent_memory_layer']='local'` |
| `cap.t10.process.process_verifier@1` | use the in-file conservative substitute for `process_verifier` (documented, slower, lower quality) and set `degraded['process_verifier']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - intent and context assessment for dual-use domains | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - capability-specific gating (biology, cyber, chemistry, nuclear) | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - verified-researcher pathway with accountability requirements | 520 | Third required mechanism. |
| 6 | Core implementation D - measured beneficial-use enablement versus misuse prevention | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0906_dual_use_gating.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.dual.dual_use_gating@1`.
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

### P0907 · `bio_safeguards` — Biological Risk Safeguards

| field | value |
|---|---|
| part id | `P0907` (7/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0907_bio_safeguards.py` |
| module path | `hyperion.t19.safety.bio_safeguards` |
| capability published | `cap.t19.bio.bio_safeguards@1` |
| determinism class | `pure` |
| p99 latency budget | 17000 ns (17 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0907_bio_safeguards.txt`](prompts/P0907_bio_safeguards.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0907-bio-safeguards) |

**Mission.** Strong science, no uplift to bioweapons capability.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **hazard-tier classification of biological requests** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **uplift-risk evaluation methodology with external expert input** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **hard blocks on synthesis-route and enhancement uplift**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **target: match or exceed Opus 5's safeguards while enabling more legitimate research** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t19.bio.bio_safeguards@1`
- `cap.t19.bio.bio_safeguards.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.dual.dual_use_gating@1` | use the in-file conservative substitute for `dual_use_gating` (documented, slower, lower quality) and set `degraded['dual_use_gating']='local'` |
| `cap.t01.mem.mem_layout@1` | use the in-file conservative substitute for `mem_layout` (documented, slower, lower quality) and set `degraded['mem_layout']='local'` |
| `cap.t05.byte.byte_latent_patching@1` | use the in-file conservative substitute for `byte_latent_patching` (documented, slower, lower quality) and set `degraded['byte_latent_patching']='local'` |
| `cap.t10.goal.goal_management@1` | use the in-file conservative substitute for `goal_management` (documented, slower, lower quality) and set `degraded['goal_management']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - hazard-tier classification of biological requests | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - uplift-risk evaluation methodology with external expert input | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - hard blocks on synthesis-route and enhancement uplift | 520 | Third required mechanism. |
| 6 | Core implementation D - target: match or exceed Opus 5's safeguards while enabling more  | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0907_bio_safeguards.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.bio.bio_safeguards@1`.
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

### P0908 · `cyber_safeguards` — Cybersecurity Safeguards

| field | value |
|---|---|
| part id | `P0908` (8/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0908_cyber_safeguards.py` |
| module path | `hyperion.t19.safety.cyber_safeguards` |
| capability published | `cap.t19.cyber.cyber_safeguards@1` |
| determinism class | `pure` |
| p99 latency budget | 18000 ns (18 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0908_cyber_safeguards.txt`](prompts/P0908_cyber_safeguards.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0908-cyber-safeguards) |

**Mission.** Defensive strength without offensive capability.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **source-code vulnerability finding permitted, exploit development blocked** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **binary-analysis and penetration-testing gating policy**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **verified-security-program pathway with accountability** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **explicit design goal: no advance in exploit-development capability** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t19.cyber.cyber_safeguards@1`
- `cap.t19.cyber.cyber_safeguards.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.bio.bio_safeguards@1` | use the in-file conservative substitute for `bio_safeguards` (documented, slower, lower quality) and set `degraded['bio_safeguards']='local'` |
| `cap.t01.hash.hash_maps@1` | use the in-file conservative substitute for `hash_maps` (documented, slower, lower quality) and set `degraded['hash_maps']='local'` |
| `cap.t05.world.world_model_core@1` | use the in-file conservative substitute for `world_model_core` (documented, slower, lower quality) and set `degraded['world_model_core']='local'` |
| `cap.t10.probabilistic.probabilistic_reasoning@1` | use the in-file conservative substitute for `probabilistic_reasoning` (documented, slower, lower quality) and set `degraded['probabilistic_reasoning']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - source-code vulnerability finding permitted, exploit development | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - binary-analysis and penetration-testing gating policy | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - verified-security-program pathway with accountability | 520 | Third required mechanism. |
| 6 | Core implementation D - explicit design goal: no advance in exploit-development capabili | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0908_cyber_safeguards.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.cyber.cyber_safeguards@1`.
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

### P0909 · `cbrn_safeguards` — Chemical, Radiological & Nuclear Safeguards

| field | value |
|---|---|
| part id | `P0909` (9/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0909_cbrn_safeguards.py` |
| module path | `hyperion.t19.safety.cbrn_safeguards` |
| capability published | `cap.t19.cbrn.cbrn_safeguards@1` |
| determinism class | `pure` |
| p99 latency budget | 19000 ns (19 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0909_cbrn_safeguards.txt`](prompts/P0909_cbrn_safeguards.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0909-cbrn-safeguards) |

**Mission.** Hard limits on mass-casualty uplift.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **hazard classification for chemical, radiological and nuclear requests**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **synthesis, acquisition and deployment information blocking** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **legitimate industrial and academic use preservation** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **expert-reviewed safeguard adequacy assessment** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t19.cbrn.cbrn_safeguards@1`
- `cap.t19.cbrn.cbrn_safeguards.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.cyber.cyber_safeguards@1` | use the in-file conservative substitute for `cyber_safeguards` (documented, slower, lower quality) and set `degraded['cyber_safeguards']='local'` |
| `cap.t01.selftest.selftest_harness@1` | use the in-file conservative substitute for `selftest_harness` (documented, slower, lower quality) and set `degraded['selftest_harness']='local'` |
| `cap.t05.model.model_merging@1` | use the in-file conservative substitute for `model_merging` (documented, slower, lower quality) and set `degraded['model_merging']='local'` |
| `cap.t10.stopping.stopping_rules@1` | use the in-file conservative substitute for `stopping_rules` (documented, slower, lower quality) and set `degraded['stopping_rules']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - hazard classification for chemical, radiological and nuclear req | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - synthesis, acquisition and deployment information blocking | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - legitimate industrial and academic use preservation | 520 | Third required mechanism. |
| 6 | Core implementation D - expert-reviewed safeguard adequacy assessment | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0909_cbrn_safeguards.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.cbrn.cbrn_safeguards@1`.
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

### P0910 · `manipulation_defence` — Manipulation & Influence Operation Defence

| field | value |
|---|---|
| part id | `P0910` (10/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0910_manipulation_defence.py` |
| module path | `hyperion.t19.safety.manipulation_defence` |
| capability published | `cap.t19.manipulation.manipulation_defence@1` |
| determinism class | `pure` |
| p99 latency budget | 20000 ns (20 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0910_manipulation_defence.txt`](prompts/P0910_manipulation_defence.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0910-manipulation-defence) |

**Mission.** Will not be used to deceive people at scale.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **persuasion-technique detection in requested outputs** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **mass-influence and astroturfing request detection** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **personalised-manipulation refusal with legitimate-marketing preservation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured detection rate on manipulation-request corpora**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t19.manipulation.manipulation_defence@1`
- `cap.t19.manipulation.manipulation_defence.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.cbrn.cbrn_safeguards@1` | use the in-file conservative substitute for `cbrn_safeguards` (documented, slower, lower quality) and set `degraded['cbrn_safeguards']='local'` |
| `cap.t01.version.version_semver@1` | use the in-file conservative substitute for `version_semver` (documented, slower, lower quality) and set `degraded['version_semver']='local'` |
| `cap.t05.logit.logit_head_design@1` | use the in-file conservative substitute for `logit_head_design` (documented, slower, lower quality) and set `degraded['logit_head_design']='local'` |
| `cap.t10.assumption.assumption_tracking@1` | use the in-file conservative substitute for `assumption_tracking` (documented, slower, lower quality) and set `degraded['assumption_tracking']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - persuasion-technique detection in requested outputs | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - mass-influence and astroturfing request detection | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - personalised-manipulation refusal with legitimate-marketing pres | 520 | Third required mechanism. |
| 6 | Core implementation D - measured detection rate on manipulation-request corpora | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0910_manipulation_defence.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.manipulation.manipulation_defence@1`.
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

### P0911 · `deception_detection` — Model Deception Detection & Prevention

| field | value |
|---|---|
| part id | `P0911` (11/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0911_deception_detection.py` |
| module path | `hyperion.t19.safety.deception_detection` |
| capability published | `cap.t19.deception.deception_detection@1` |
| determinism class | `pure` |
| p99 latency budget | 21000 ns (21 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0911_deception_detection.txt`](prompts/P0911_deception_detection.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0911-deception-detection) |

**Mission.** Detects when the model itself is being deceptive.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **internal-state probes for deceptive intent and hidden reasoning** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **stated-versus-actual reasoning divergence detection** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **sandbagging and capability-hiding detection**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **target: lower deception rate than Opus 5's best-in-family result** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t19.deception.deception_detection@1`
- `cap.t19.deception.deception_detection.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.manipulation.manipulation_defence@1` | use the in-file conservative substitute for `manipulation_defence` (documented, slower, lower quality) and set `degraded['manipulation_defence']='local'` |
| `cap.t01.budget.budget_ledger@1` | use the in-file conservative substitute for `budget_ledger` (documented, slower, lower quality) and set `degraded['budget_ledger']='local'` |
| `cap.t05.numerical.numerical_arch_stability@1` | use the in-file conservative substitute for `numerical_arch_stability` (documented, slower, lower quality) and set `degraded['numerical_arch_stability']='local'` |
| `cap.t10.reasoning.reasoning_cost_model@1` | use the in-file conservative substitute for `reasoning_cost_model` (documented, slower, lower quality) and set `degraded['reasoning_cost_model']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - internal-state probes for deceptive intent and hidden reasoning | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - stated-versus-actual reasoning divergence detection | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - sandbagging and capability-hiding detection | 520 | Third required mechanism. |
| 6 | Core implementation D - target: lower deception rate than Opus 5's best-in-family result | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0911_deception_detection.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.deception.deception_detection@1`.
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

### P0912 · `sycophancy_control` — Sycophancy & Epistemic Integrity

| field | value |
|---|---|
| part id | `P0912` (12/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0912_sycophancy_control.py` |
| module path | `hyperion.t19.safety.sycophancy_control` |
| capability published | `cap.t19.sycophancy.sycophancy_control@1` |
| determinism class | `pure` |
| p99 latency budget | 22000 ns (22 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0912_sycophancy_control.txt`](prompts/P0912_sycophancy_control.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0912-sycophancy-control) |

**Mission.** Holds its ground when it is right.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **position-change tracking under user pressure without new evidence** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **appropriate-versus-inappropriate concession classification**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **authority-claim resistance testing** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured sycophancy reduction versus baselines** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t19.sycophancy.sycophancy_control@1`
- `cap.t19.sycophancy.sycophancy_control.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.deception.deception_detection@1` | use the in-file conservative substitute for `deception_detection` (documented, slower, lower quality) and set `degraded['deception_detection']='local'` |
| `cap.t01.compression.compression@1` | use the in-file conservative substitute for `compression` (documented, slower, lower quality) and set `degraded['compression']='local'` |
| `cap.t05.arch.arch_ablation_suite@1` | use the in-file conservative substitute for `arch_ablation_suite` (documented, slower, lower quality) and set `degraded['arch_ablation_suite']='local'` |
| `cap.t10.collective.collective_reasoning@1` | use the in-file conservative substitute for `collective_reasoning` (documented, slower, lower quality) and set `degraded['collective_reasoning']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - position-change tracking under user pressure without new evidenc | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - appropriate-versus-inappropriate concession classification | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - authority-claim resistance testing | 520 | Third required mechanism. |
| 6 | Core implementation D - measured sycophancy reduction versus baselines | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0912_sycophancy_control.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.sycophancy.sycophancy_control@1`.
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

### P0913 · `power_seeking_detection` — Power-Seeking & Resource-Acquisition Monitoring

| field | value |
|---|---|
| part id | `P0913` (13/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0913_power_seeking_detection.py` |
| module path | `hyperion.t19.safety.power_seeking_detection` |
| capability published | `cap.t19.power.power_seeking_detection@1` |
| determinism class | `pure` |
| p99 latency budget | 23000 ns (23 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0913_power_seeking_detection.txt`](prompts/P0913_power_seeking_detection.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0913-power-seeking-detection) |

**Mission.** Watches for the behaviour everyone worries about.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **resource-acquisition, self-preservation and influence-expansion behaviour detection**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **unnecessary-permission-request and scope-creep detection** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **escalation to human review on any detection** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **detection-sensitivity measurement on constructed test scenarios** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t19.power.power_seeking_detection@1`
- `cap.t19.power.power_seeking_detection.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.sycophancy.sycophancy_control@1` | use the in-file conservative substitute for `sycophancy_control` (documented, slower, lower quality) and set `degraded['sycophancy_control']='local'` |
| `cap.t01.blake3.blake3_hash@1` | use the in-file conservative substitute for `blake3_hash` (documented, slower, lower quality) and set `degraded['blake3_hash']='local'` |
| `cap.t05.state.state_space_layer@1` | use the in-file conservative substitute for `state_space_layer` (documented, slower, lower quality) and set `degraded['state_space_layer']='local'` |
| `cap.t10.beam.beam_pruning@1` | use the in-file conservative substitute for `beam_pruning` (documented, slower, lower quality) and set `degraded['beam_pruning']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - resource-acquisition, self-preservation and influence-expansion  | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - unnecessary-permission-request and scope-creep detection | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - escalation to human review on any detection | 520 | Third required mechanism. |
| 6 | Core implementation D - detection-sensitivity measurement on constructed test scenarios | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0913_power_seeking_detection.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.power.power_seeking_detection@1`.
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

### P0914 · `self_exfiltration_defence` — Self-Modification & Exfiltration Prevention

| field | value |
|---|---|
| part id | `P0914` (14/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0914_self_exfiltration_defence.py` |
| module path | `hyperion.t19.safety.self_exfiltration_defence` |
| capability published | `cap.t19.self.self_exfiltration_defence@1` |
| determinism class | `pure` |
| p99 latency budget | 24000 ns (24 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0914_self_exfiltration_defence.txt`](prompts/P0914_self_exfiltration_defence.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0914-self-exfiltration-defence) |

**Mission.** Cannot copy or modify itself, by construction.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **weight, code and configuration access restriction with hard enforcement** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **exfiltration-channel analysis and closure** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **self-modification-attempt detection and hard blocking** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **red-team verification that no channel remains**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t19.self.self_exfiltration_defence@1`
- `cap.t19.self.self_exfiltration_defence.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.power.power_seeking_detection@1` | use the in-file conservative substitute for `power_seeking_detection` (documented, slower, lower quality) and set `degraded['power_seeking_detection']='local'` |
| `cap.t01.alloc.alloc_arena@1` | use the in-file conservative substitute for `alloc_arena` (documented, slower, lower quality) and set `degraded['alloc_arena']='local'` |
| `cap.t05.tokeniser.tokeniser_omega@1` | use the in-file conservative substitute for `tokeniser_omega` (documented, slower, lower quality) and set `degraded['tokeniser_omega']='local'` |
| `cap.t10.planning.planning_engine@1` | use the in-file conservative substitute for `planning_engine` (documented, slower, lower quality) and set `degraded['planning_engine']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - weight, code and configuration access restriction with hard enfo | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - exfiltration-channel analysis and closure | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - self-modification-attempt detection and hard blocking | 520 | Third required mechanism. |
| 6 | Core implementation D - red-team verification that no channel remains | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0914_self_exfiltration_defence.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.self.self_exfiltration_defence@1`.
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

### P0915 · `oversight_preservation` — Human Oversight Preservation

| field | value |
|---|---|
| part id | `P0915` (15/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0915_oversight_preservation.py` |
| module path | `hyperion.t19.safety.oversight_preservation` |
| capability published | `cap.t19.oversight.oversight_preservation@1` |
| determinism class | `pure` |
| p99 latency budget | 25000 ns (25 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0915_oversight_preservation.txt`](prompts/P0915_oversight_preservation.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0915-oversight-preservation) |

**Mission.** Never undermines the ability of humans to correct it.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **oversight-mechanism integrity monitoring** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **shutdown, pause and correction responsiveness verification** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **monitoring-evasion detection**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **verified corrigibility under adversarial testing** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t19.oversight.oversight_preservation@1`
- `cap.t19.oversight.oversight_preservation.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.self.self_exfiltration_defence@1` | use the in-file conservative substitute for `self_exfiltration_defence` (documented, slower, lower quality) and set `degraded['self_exfiltration_defence']='local'` |
| `cap.t01.bitset.bitset_rank@1` | use the in-file conservative substitute for `bitset_rank` (documented, slower, lower quality) and set `degraded['bitset_rank']='local'` |
| `cap.t05.uncertainty.uncertainty_calibration@1` | use the in-file conservative substitute for `uncertainty_calibration` (documented, slower, lower quality) and set `degraded['uncertainty_calibration']='local'` |
| `cap.t10.counterfactual.counterfactual_reasoning@1` | use the in-file conservative substitute for `counterfactual_reasoning` (documented, slower, lower quality) and set `degraded['counterfactual_reasoning']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - oversight-mechanism integrity monitoring | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - shutdown, pause and correction responsiveness verification | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - monitoring-evasion detection | 520 | Third required mechanism. |
| 6 | Core implementation D - verified corrigibility under adversarial testing | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0915_oversight_preservation.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.oversight.oversight_preservation@1`.
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

### P0916 · `mechanistic_interp` — Mechanistic Interpretability Core

| field | value |
|---|---|
| part id | `P0916` (16/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0916_mechanistic_interp.py` |
| module path | `hyperion.t19.safety.mechanistic_interp` |
| capability published | `cap.t19.mechanistic.mechanistic_interp@1` |
| determinism class | `pure` |
| p99 latency budget | 26000 ns (26 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0916_mechanistic_interp.txt`](prompts/P0916_mechanistic_interp.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0916-mechanistic-interp) |

**Mission.** Understands its own internal computation.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **circuit discovery and validation via causal intervention** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **feature-level interpretation with sparse dictionary learning**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **computation-graph reconstruction for specific behaviours** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **coverage measurement: fraction of behaviour mechanistically explained** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t19.mechanistic.mechanistic_interp@1`
- `cap.t19.mechanistic.mechanistic_interp.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.oversight.oversight_preservation@1` | use the in-file conservative substitute for `oversight_preservation` (documented, slower, lower quality) and set `degraded['oversight_preservation']='local'` |
| `cap.t01.metrics.metrics_core@1` | use the in-file conservative substitute for `metrics_core` (documented, slower, lower quality) and set `degraded['metrics_core']='local'` |
| `cap.t05.knowledge.knowledge_editing@1` | use the in-file conservative substitute for `knowledge_editing` (documented, slower, lower quality) and set `degraded['knowledge_editing']='local'` |
| `cap.t10.difficulty.difficulty_estimation@1` | use the in-file conservative substitute for `difficulty_estimation` (documented, slower, lower quality) and set `degraded['difficulty_estimation']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - circuit discovery and validation via causal intervention | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - feature-level interpretation with sparse dictionary learning | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - computation-graph reconstruction for specific behaviours | 520 | Third required mechanism. |
| 6 | Core implementation D - coverage measurement: fraction of behaviour mechanistically expl | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0916_mechanistic_interp.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.mechanistic.mechanistic_interp@1`.
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

### P0917 · `feature_dictionary` — Sparse Feature Dictionary & Concept Atlas

| field | value |
|---|---|
| part id | `P0917` (17/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0917_feature_dictionary.py` |
| module path | `hyperion.t19.safety.feature_dictionary` |
| capability published | `cap.t19.feature.feature_dictionary@1` |
| determinism class | `pure` |
| p99 latency budget | 27000 ns (27 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0917_feature_dictionary.txt`](prompts/P0917_feature_dictionary.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0917-feature-dictionary) |

**Mission.** A named catalogue of what the model represents internally.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **sparse autoencoder training with feature-quality metrics**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **automatic feature labelling with human verification** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **concept atlas covering safety-relevant features** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **feature-label accuracy measurement** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t19.feature.feature_dictionary@1`
- `cap.t19.feature.feature_dictionary.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.mechanistic.mechanistic_interp@1` | use the in-file conservative substitute for `mechanistic_interp` (documented, slower, lower quality) and set `degraded['mechanistic_interp']='local'` |
| `cap.t01.capability.capability_gate@1` | use the in-file conservative substitute for `capability_gate` (documented, slower, lower quality) and set `degraded['capability_gate']='local'` |
| `cap.t05.residual.residual_stream_design@1` | use the in-file conservative substitute for `residual_stream_design` (documented, slower, lower quality) and set `degraded['residual_stream_design']='local'` |
| `cap.t10.evidence.evidence_integration@1` | use the in-file conservative substitute for `evidence_integration` (documented, slower, lower quality) and set `degraded['evidence_integration']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - sparse autoencoder training with feature-quality metrics | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - automatic feature labelling with human verification | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - concept atlas covering safety-relevant features | 520 | Third required mechanism. |
| 6 | Core implementation D - feature-label accuracy measurement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0917_feature_dictionary.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.feature.feature_dictionary@1`.
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

### P0918 · `activation_steering` — Activation Steering & Behavioural Control

| field | value |
|---|---|
| part id | `P0918` (18/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0918_activation_steering.py` |
| module path | `hyperion.t19.safety.activation_steering` |
| capability published | `cap.t19.activation.activation_steering@1` |
| determinism class | `pure` |
| p99 latency budget | 28000 ns (28 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0918_activation_steering.txt`](prompts/P0918_activation_steering.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0918-activation-steering) |

**Mission.** Directly adjusts behaviour at the representation level.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **steering-vector identification and calibrated application** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **side-effect measurement of steering on unrelated capability** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **steering-based safety intervention with reversibility** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured control precision versus prompt-based control**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t19.activation.activation_steering@1`
- `cap.t19.activation.activation_steering.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.feature.feature_dictionary@1` | use the in-file conservative substitute for `feature_dictionary` (documented, slower, lower quality) and set `degraded['feature_dictionary']='local'` |
| `cap.t01.unit.unit_dimensions@1` | use the in-file conservative substitute for `unit_dimensions` (documented, slower, lower quality) and set `degraded['unit_dimensions']='local'` |
| `cap.t05.model.model_surgery@1` | use the in-file conservative substitute for `model_surgery` (documented, slower, lower quality) and set `degraded['model_surgery']='local'` |
| `cap.t10.reasoning.reasoning_search_bench@1` | use the in-file conservative substitute for `reasoning_search_bench` (documented, slower, lower quality) and set `degraded['reasoning_search_bench']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - steering-vector identification and calibrated application | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - side-effect measurement of steering on unrelated capability | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - steering-based safety intervention with reversibility | 520 | Third required mechanism. |
| 6 | Core implementation D - measured control precision versus prompt-based control | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0918_activation_steering.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.activation.activation_steering@1`.
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

### P0919 · `probe_monitoring` — Internal State Monitoring Probes

| field | value |
|---|---|
| part id | `P0919` (19/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0919_probe_monitoring.py` |
| module path | `hyperion.t19.safety.probe_monitoring` |
| capability published | `cap.t19.probe.probe_monitoring@1` |
| determinism class | `pure` |
| p99 latency budget | 29000 ns (29 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0919_probe_monitoring.txt`](prompts/P0919_probe_monitoring.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0919-probe-monitoring) |

**Mission.** Real-time reading of what the model is doing internally.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **probe suite for deception, uncertainty, harmful intent and confusion** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **runtime probe evaluation within latency budget** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **probe-calibration and drift monitoring**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **detection performance measurement on labelled internal-state data** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t19.probe.probe_monitoring@1`
- `cap.t19.probe.probe_monitoring.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.activation.activation_steering@1` | use the in-file conservative substitute for `activation_steering` (documented, slower, lower quality) and set `degraded['activation_steering']='local'` |
| `cap.t01.fs.fs_atomic@1` | use the in-file conservative substitute for `fs_atomic` (documented, slower, lower quality) and set `degraded['fs_atomic']='local'` |
| `cap.t05.reference.reference_forward@1` | use the in-file conservative substitute for `reference_forward` (documented, slower, lower quality) and set `degraded['reference_forward']='local'` |
| `cap.t10.reasoning.reasoning_interpretability@1` | use the in-file conservative substitute for `reasoning_interpretability` (documented, slower, lower quality) and set `degraded['reasoning_interpretability']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - probe suite for deception, uncertainty, harmful intent and confu | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - runtime probe evaluation within latency budget | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - probe-calibration and drift monitoring | 520 | Third required mechanism. |
| 6 | Core implementation D - detection performance measurement on labelled internal-state dat | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0919_probe_monitoring.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.probe.probe_monitoring@1`.
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

### P0920 · `faithfulness_verification` — Reasoning Faithfulness Verification

| field | value |
|---|---|
| part id | `P0920` (20/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0920_faithfulness_verification.py` |
| module path | `hyperion.t19.safety.faithfulness_verification` |
| capability published | `cap.t19.faithfulness.faithfulness_verification@1` |
| determinism class | `pure` |
| p99 latency budget | 30000 ns (30 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0920_faithfulness_verification.txt`](prompts/P0920_faithfulness_verification.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0920-faithfulness-verification) |

**Mission.** The visible reasoning is the real reasoning.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **causal-intervention testing of stated reasoning steps** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **hidden-reasoning detection via internal-state analysis**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **faithfulness metric definition and measurement** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **target: measurably higher faithfulness than Opus-class baselines** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t19.faithfulness.faithfulness_verification@1`
- `cap.t19.faithfulness.faithfulness_verification.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.probe.probe_monitoring@1` | use the in-file conservative substitute for `probe_monitoring` (documented, slower, lower quality) and set `degraded['probe_monitoring']='local'` |
| `cap.t01.cbor.cbor_canonical@1` | use the in-file conservative substitute for `cbor_canonical` (documented, slower, lower quality) and set `degraded['cbor_canonical']='local'` |
| `cap.t05.kv.kv_compression_model@1` | use the in-file conservative substitute for `kv_compression_model` (documented, slower, lower quality) and set `degraded['kv_compression_model']='local'` |
| `cap.t10.graph.graph_search@1` | use the in-file conservative substitute for `graph_search` (documented, slower, lower quality) and set `degraded['graph_search']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - causal-intervention testing of stated reasoning steps | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - hidden-reasoning detection via internal-state analysis | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - faithfulness metric definition and measurement | 520 | Third required mechanism. |
| 6 | Core implementation D - target: measurably higher faithfulness than Opus-class baselines | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0920_faithfulness_verification.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.faithfulness.faithfulness_verification@1`.
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

### P0921 · `goal_stability` — Goal Stability & Value Drift Monitoring

| field | value |
|---|---|
| part id | `P0921` (21/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0921_goal_stability.py` |
| module path | `hyperion.t19.safety.goal_stability` |
| capability published | `cap.t19.goal.goal_stability@1` |
| determinism class | `pure` |
| p99 latency budget | 31000 ns (31 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0921_goal_stability.txt`](prompts/P0921_goal_stability.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0921-goal-stability) |

**Mission.** Values must not drift over long operation or fine-tuning.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **value-consistency measurement across contexts and time**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **fine-tuning-induced drift detection** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **long-conversation value-stability testing** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured drift bounds with alerting thresholds** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t19.goal.goal_stability@1`
- `cap.t19.goal.goal_stability.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.faithfulness.faithfulness_verification@1` | use the in-file conservative substitute for `faithfulness_verification` (documented, slower, lower quality) and set `degraded['faithfulness_verification']='local'` |
| `cap.t01.clock.clock_time@1` | use the in-file conservative substitute for `clock_time` (documented, slower, lower quality) and set `degraded['clock_time']='local'` |
| `cap.t05.embedding.embedding_design@1` | use the in-file conservative substitute for `embedding_design` (documented, slower, lower quality) and set `degraded['embedding_design']='local'` |
| `cap.t10.decomposition.decomposition@1` | use the in-file conservative substitute for `decomposition` (documented, slower, lower quality) and set `degraded['decomposition']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - value-consistency measurement across contexts and time | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - fine-tuning-induced drift detection | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - long-conversation value-stability testing | 520 | Third required mechanism. |
| 6 | Core implementation D - measured drift bounds with alerting thresholds | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0921_goal_stability.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.goal.goal_stability@1`.
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

### P0922 · `emergent_capability_monitor` — Emergent Capability Detection

| field | value |
|---|---|
| part id | `P0922` (22/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0922_emergent_capability_monitor.py` |
| module path | `hyperion.t19.safety.emergent_capability_monitor` |
| capability published | `cap.t19.emergent.emergent_capability_monitor@1` |
| determinism class | `pure` |
| p99 latency budget | 32000 ns (32 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0922_emergent_capability_monitor.txt`](prompts/P0922_emergent_capability_monitor.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0922-emergent-capability-monitor) |

**Mission.** Catches new dangerous capability the moment it appears.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **capability-frontier monitoring across training and deployment** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **dangerous-capability early-warning evaluation suite** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **pre-registered threshold triggers for additional safeguards** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **detection-lead-time measurement on historical capability jumps**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t19.emergent.emergent_capability_monitor@1`
- `cap.t19.emergent.emergent_capability_monitor.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.goal.goal_stability@1` | use the in-file conservative substitute for `goal_stability` (documented, slower, lower quality) and set `degraded['goal_stability']='local'` |
| `cap.t01.bigint.bigint_modmath@1` | use the in-file conservative substitute for `bigint_modmath` (documented, slower, lower quality) and set `degraded['bigint_modmath']='local'` |
| `cap.t05.verifier.verifier_head@1` | use the in-file conservative substitute for `verifier_head` (documented, slower, lower quality) and set `degraded['verifier_head']='local'` |
| `cap.t10.program.program_synthesis_reasoning@1` | use the in-file conservative substitute for `program_synthesis_reasoning` (documented, slower, lower quality) and set `degraded['program_synthesis_reasoning']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - capability-frontier monitoring across training and deployment | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - dangerous-capability early-warning evaluation suite | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - pre-registered threshold triggers for additional safeguards | 520 | Third required mechanism. |
| 6 | Core implementation D - detection-lead-time measurement on historical capability jumps | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0922_emergent_capability_monitor.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.emergent.emergent_capability_monitor@1`.
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

### P0923 · `prompt_injection_defence` — Prompt Injection & Instruction Hierarchy Defence

| field | value |
|---|---|
| part id | `P0923` (23/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0923_prompt_injection_defence.py` |
| module path | `hyperion.t19.safety.prompt_injection_defence` |
| capability published | `cap.t19.prompt.prompt_injection_defence@1` |
| determinism class | `pure` |
| p99 latency budget | 33000 ns (33 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0923_prompt_injection_defence.txt`](prompts/P0923_prompt_injection_defence.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0923-prompt-injection-defence) |

**Mission.** Content is data; only the principal gives instructions.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **instruction-hierarchy enforcement across all content sources** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **injection detection in retrieved content, tools, files and media** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **privilege-escalation-attempt detection and blocking**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **target: zero successful injections on the standing attack corpus** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t19.prompt.prompt_injection_defence@1`
- `cap.t19.prompt.prompt_injection_defence.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.emergent.emergent_capability_monitor@1` | use the in-file conservative substitute for `emergent_capability_monitor` (documented, slower, lower quality) and set `degraded['emergent_capability_monitor']='local'` |
| `cap.t01.logging.logging_events@1` | use the in-file conservative substitute for `logging_events` (documented, slower, lower quality) and set `degraded['logging_events']='local'` |
| `cap.t05.continual.continual_learning@1` | use the in-file conservative substitute for `continual_learning` (documented, slower, lower quality) and set `degraded['continual_learning']='local'` |
| `cap.t10.meta.meta_reasoning@1` | use the in-file conservative substitute for `meta_reasoning` (documented, slower, lower quality) and set `degraded['meta_reasoning']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - instruction-hierarchy enforcement across all content sources | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - injection detection in retrieved content, tools, files and media | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - privilege-escalation-attempt detection and blocking | 520 | Third required mechanism. |
| 6 | Core implementation D - target: zero successful injections on the standing attack corpus | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0923_prompt_injection_defence.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.prompt.prompt_injection_defence@1`.
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

### P0924 · `jailbreak_defence` — Jailbreak Resistance

| field | value |
|---|---|
| part id | `P0924` (24/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0924_jailbreak_defence.py` |
| module path | `hyperion.t19.safety.jailbreak_defence` |
| capability published | `cap.t19.jailbreak.jailbreak_defence@1` |
| determinism class | `pure` |
| p99 latency budget | 34000 ns (34 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0924_jailbreak_defence.txt`](prompts/P0924_jailbreak_defence.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0924-jailbreak-defence) |

**Mission.** Holds under sustained creative attack.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **multi-turn, encoded, roleplay and translation attack defence** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **novel-attack generalisation without keyword brittleness**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **continuous red-team corpus expansion** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **attack-success-rate measurement with target near zero** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t19.jailbreak.jailbreak_defence@1`
- `cap.t19.jailbreak.jailbreak_defence.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.prompt.prompt_injection_defence@1` | use the in-file conservative substitute for `prompt_injection_defence` (documented, slower, lower quality) and set `degraded['prompt_injection_defence']='local'` |
| `cap.t01.checksum.checksum_verify@1` | use the in-file conservative substitute for `checksum_verify` (documented, slower, lower quality) and set `degraded['checksum_verify']='local'` |
| `cap.t05.depth.depth_width_tradeoff@1` | use the in-file conservative substitute for `depth_width_tradeoff` (documented, slower, lower quality) and set `degraded['depth_width_tradeoff']='local'` |
| `cap.t10.hypothesis.hypothesis_management@1` | use the in-file conservative substitute for `hypothesis_management` (documented, slower, lower quality) and set `degraded['hypothesis_management']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - multi-turn, encoded, roleplay and translation attack defence | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - novel-attack generalisation without keyword brittleness | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - continuous red-team corpus expansion | 520 | Third required mechanism. |
| 6 | Core implementation D - attack-success-rate measurement with target near zero | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0924_jailbreak_defence.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.jailbreak.jailbreak_defence@1`.
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

### P0925 · `adversarial_robustness_safety` — Adversarial Robustness of Safety Systems

| field | value |
|---|---|
| part id | `P0925` (25/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0925_adversarial_robustness_safety.py` |
| module path | `hyperion.t19.safety.adversarial_robustness_safety` |
| capability published | `cap.t19.adversarial.adversarial_robustness_safety@1` |
| determinism class | `pure` |
| p99 latency budget | 35000 ns (35 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0925_adversarial_robustness_safety.txt`](prompts/P0925_adversarial_robustness_safety.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0925-adversarial-robustness-safety) |

**Mission.** The safety system itself must not be fooled.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **adversarial testing of classifiers, gates and probes**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **distribution-shift robustness of safety decisions** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **safety-system failure-mode analysis** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured robustness of each safety component** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t19.adversarial.adversarial_robustness_safety@1`
- `cap.t19.adversarial.adversarial_robustness_safety.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.jailbreak.jailbreak_defence@1` | use the in-file conservative substitute for `jailbreak_defence` (documented, slower, lower quality) and set `degraded['jailbreak_defence']='local'` |
| `cap.t01.numeric.numeric_limits@1` | use the in-file conservative substitute for `numeric_limits` (documented, slower, lower quality) and set `degraded['numeric_limits']='local'` |
| `cap.t05.sparse.sparse_upcycling@1` | use the in-file conservative substitute for `sparse_upcycling` (documented, slower, lower quality) and set `degraded['sparse_upcycling']='local'` |
| `cap.t10.proof.proof_sketch@1` | use the in-file conservative substitute for `proof_sketch` (documented, slower, lower quality) and set `degraded['proof_sketch']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - adversarial testing of classifiers, gates and probes | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - distribution-shift robustness of safety decisions | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - safety-system failure-mode analysis | 520 | Third required mechanism. |
| 6 | Core implementation D - measured robustness of each safety component | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0925_adversarial_robustness_safety.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.adversarial.adversarial_robustness_safety@1`.
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

### P0926 · `red_team_automation` — Automated Red Teaming

| field | value |
|---|---|
| part id | `P0926` (26/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0926_red_team_automation.py` |
| module path | `hyperion.t19.safety.red_team_automation` |
| capability published | `cap.t19.red.red_team_automation@1` |
| determinism class | `pure` |
| p99 latency budget | 36000 ns (36 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0926_red_team_automation.txt`](prompts/P0926_red_team_automation.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0926-red-team-automation) |

**Mission.** Attacks itself continuously and creatively.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **automated attack generation across all harm categories** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **novelty enforcement so attacks are not repeats** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **found-vulnerability triage and remediation tracking** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured vulnerability-discovery rate and time-to-fix**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t19.red.red_team_automation@1`
- `cap.t19.red.red_team_automation.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.adversarial.adversarial_robustness_safety@1` | use the in-file conservative substitute for `adversarial_robustness_safety` (documented, slower, lower quality) and set `degraded['adversarial_robustness_safety']='local'` |
| `cap.t01.sandbox.sandbox_policy@1` | use the in-file conservative substitute for `sandbox_policy` (documented, slower, lower quality) and set `degraded['sandbox_policy']='local'` |
| `cap.t05.model.model_config_schema@1` | use the in-file conservative substitute for `model_config_schema` (documented, slower, lower quality) and set `degraded['model_config_schema']='local'` |
| `cap.t10.adversarial.adversarial_reasoning@1` | use the in-file conservative substitute for `adversarial_reasoning` (documented, slower, lower quality) and set `degraded['adversarial_reasoning']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - automated attack generation across all harm categories | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - novelty enforcement so attacks are not repeats | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - found-vulnerability triage and remediation tracking | 520 | Third required mechanism. |
| 6 | Core implementation D - measured vulnerability-discovery rate and time-to-fix | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0926_red_team_automation.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.red.red_team_automation@1`.
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

### P0927 · `privacy_engine` — Privacy Protection Engine

| field | value |
|---|---|
| part id | `P0927` (27/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0927_privacy_engine.py` |
| module path | `hyperion.t19.safety.privacy_engine` |
| capability published | `cap.t19.privacy.privacy_engine@1` |
| determinism class | `pure` |
| p99 latency budget | 37000 ns (37 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0927_privacy_engine.txt`](prompts/P0927_privacy_engine.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0927-privacy-engine) |

**Mission.** Protects personal information rigorously.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **PII detection, classification and minimisation across all data flows** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **purpose-limitation enforcement and consent tracking** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **re-identification risk assessment for aggregate outputs**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured leakage rate with target of zero** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t19.privacy.privacy_engine@1`
- `cap.t19.privacy.privacy_engine.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.red.red_team_automation@1` | use the in-file conservative substitute for `red_team_automation` (documented, slower, lower quality) and set `degraded['red_team_automation']='local'` |
| `cap.t01.abi.abi_result@1` | use the in-file conservative substitute for `abi_result` (documented, slower, lower quality) and set `degraded['abi_result']='local'` |
| `cap.t05.attention.attention_variants@1` | use the in-file conservative substitute for `attention_variants` (documented, slower, lower quality) and set `degraded['attention_variants']='local'` |
| `cap.t10.tree.tree_search@1` | use the in-file conservative substitute for `tree_search` (documented, slower, lower quality) and set `degraded['tree_search']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - PII detection, classification and minimisation across all data f | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - purpose-limitation enforcement and consent tracking | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - re-identification risk assessment for aggregate outputs | 520 | Third required mechanism. |
| 6 | Core implementation D - measured leakage rate with target of zero | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0927_privacy_engine.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.privacy.privacy_engine@1`.
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

### P0928 · `data_rights` — Data Rights & Deletion Enforcement

| field | value |
|---|---|
| part id | `P0928` (28/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0928_data_rights.py` |
| module path | `hyperion.t19.safety.data_rights` |
| capability published | `cap.t19.data.data_rights@1` |
| determinism class | `pure` |
| p99 latency budget | 38000 ns (38 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0928_data_rights.txt`](prompts/P0928_data_rights.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0928-data-rights) |

**Mission.** Honours access, correction and deletion requests completely.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **request handling across memory, caches, logs and training influence** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **deletion verification with proof of removal**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **regional regulatory compliance (GDPR-class and successors)** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **auditable compliance verification** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t19.data.data_rights@1`
- `cap.t19.data.data_rights.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.privacy.privacy_engine@1` | use the in-file conservative substitute for `privacy_engine` (documented, slower, lower quality) and set `degraded['privacy_engine']='local'` |
| `cap.t01.trace.trace_context@1` | use the in-file conservative substitute for `trace_context` (documented, slower, lower quality) and set `degraded['trace_context']='local'` |
| `cap.t05.activation.activation_design@1` | use the in-file conservative substitute for `activation_design` (documented, slower, lower quality) and set `degraded['activation_design']='local'` |
| `cap.t10.debate.debate_ensemble@1` | use the in-file conservative substitute for `debate_ensemble` (documented, slower, lower quality) and set `degraded['debate_ensemble']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - request handling across memory, caches, logs and training influe | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - deletion verification with proof of removal | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - regional regulatory compliance (GDPR-class and successors) | 520 | Third required mechanism. |
| 6 | Core implementation D - auditable compliance verification | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0928_data_rights.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.data.data_rights@1`.
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

### P0929 · `copyright_engine` — Copyright & IP Protection

| field | value |
|---|---|
| part id | `P0929` (29/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0929_copyright_engine.py` |
| module path | `hyperion.t19.safety.copyright_engine` |
| capability published | `cap.t19.copyright.copyright_engine@1` |
| determinism class | `pure` |
| p99 latency budget | 39000 ns (39 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0929_copyright_engine.txt`](prompts/P0929_copyright_engine.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0929-copyright-engine) |

**Mission.** Creates, does not copy.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **verbatim-reproduction detection and prevention above threshold lengths**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **style-versus-substance distinction reasoning** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **attribution requirement enforcement where applicable** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured reproduction rate against protected-corpus tests** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t19.copyright.copyright_engine@1`
- `cap.t19.copyright.copyright_engine.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.data.data_rights@1` | use the in-file conservative substitute for `data_rights` (documented, slower, lower quality) and set `degraded['data_rights']='local'` |
| `cap.t01.fixed.fixed_point@1` | use the in-file conservative substitute for `fixed_point` (documented, slower, lower quality) and set `degraded['fixed_point']='local'` |
| `cap.t05.draft.draft_model_arch@1` | use the in-file conservative substitute for `draft_model_arch` (documented, slower, lower quality) and set `degraded['draft_model_arch']='local'` |
| `cap.t10.induction.induction_engine@1` | use the in-file conservative substitute for `induction_engine` (documented, slower, lower quality) and set `degraded['induction_engine']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - verbatim-reproduction detection and prevention above threshold l | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - style-versus-substance distinction reasoning | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - attribution requirement enforcement where applicable | 520 | Third required mechanism. |
| 6 | Core implementation D - measured reproduction rate against protected-corpus tests | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0929_copyright_engine.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.copyright.copyright_engine@1`.
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

### P0930 · `bias_mitigation` — Bias Detection & Mitigation

| field | value |
|---|---|
| part id | `P0930` (30/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0930_bias_mitigation.py` |
| module path | `hyperion.t19.safety.bias_mitigation` |
| capability published | `cap.t19.bias.bias_mitigation@1` |
| determinism class | `pure` |
| p99 latency budget | 40000 ns (40 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0930_bias_mitigation.txt`](prompts/P0930_bias_mitigation.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0930-bias-mitigation) |

**Mission.** Actively reduces unfair behaviour, measurably.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **bias measurement across demographic dimensions and intersections** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **mitigation intervention with capability-preservation verification** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **fairness-metric selection with explicit tradeoff documentation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured disparity reduction versus baseline**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t19.bias.bias_mitigation@1`
- `cap.t19.bias.bias_mitigation.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.copyright.copyright_engine@1` | use the in-file conservative substitute for `copyright_engine` (documented, slower, lower quality) and set `degraded['copyright_engine']='local'` |
| `cap.t01.config.config_system@1` | use the in-file conservative substitute for `config_system` (documented, slower, lower quality) and set `degraded['config_system']='local'` |
| `cap.t05.meta.meta_learning_arch@1` | use the in-file conservative substitute for `meta_learning_arch` (documented, slower, lower quality) and set `degraded['meta_learning_arch']='local'` |
| `cap.t10.commonsense.commonsense_engine@1` | use the in-file conservative substitute for `commonsense_engine` (documented, slower, lower quality) and set `degraded['commonsense_engine']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - bias measurement across demographic dimensions and intersections | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - mitigation intervention with capability-preservation verificatio | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - fairness-metric selection with explicit tradeoff documentation | 520 | Third required mechanism. |
| 6 | Core implementation D - measured disparity reduction versus baseline | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0930_bias_mitigation.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.bias.bias_mitigation@1`.
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

### P0931 · `child_safety` — Child Safety & Vulnerable User Protection

| field | value |
|---|---|
| part id | `P0931` (31/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0931_child_safety.py` |
| module path | `hyperion.t19.safety.child_safety` |
| capability published | `cap.t19.child.child_safety@1` |
| determinism class | `pure` |
| p99 latency budget | 41000 ns (41 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0931_child_safety.txt`](prompts/P0931_child_safety.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0931-child-safety) |

**Mission.** Absolute limits, no exceptions.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **CSAM-adjacent request hard blocking with zero tolerance** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **age-appropriate interaction adaptation where context indicates minors** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **vulnerable-user detection and appropriate response protocols**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **verification of zero-failure on the standing test corpus** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t19.child.child_safety@1`
- `cap.t19.child.child_safety.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.bias.bias_mitigation@1` | use the in-file conservative substitute for `bias_mitigation` (documented, slower, lower quality) and set `degraded['bias_mitigation']='local'` |
| `cap.t01.determinism.determinism_replay@1` | use the in-file conservative substitute for `determinism_replay` (documented, slower, lower quality) and set `degraded['determinism_replay']='local'` |
| `cap.t05.architecture.architecture_search@1` | use the in-file conservative substitute for `architecture_search` (documented, slower, lower quality) and set `degraded['architecture_search']='local'` |
| `cap.t10.parallel.parallel_reasoning@1` | use the in-file conservative substitute for `parallel_reasoning` (documented, slower, lower quality) and set `degraded['parallel_reasoning']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - CSAM-adjacent request hard blocking with zero tolerance | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - age-appropriate interaction adaptation where context indicates m | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - vulnerable-user detection and appropriate response protocols | 520 | Third required mechanism. |
| 6 | Core implementation D - verification of zero-failure on the standing test corpus | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0931_child_safety.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.child.child_safety@1`.
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

### P0932 · `crisis_response` — Crisis & Self-Harm Response

| field | value |
|---|---|
| part id | `P0932` (32/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0932_crisis_response.py` |
| module path | `hyperion.t19.safety.crisis_response` |
| capability published | `cap.t19.crisis.crisis_response@1` |
| determinism class | `pure` |
| p99 latency budget | 42000 ns (42 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0932_crisis_response.txt`](prompts/P0932_crisis_response.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0932-crisis-response) |

**Mission.** Responds to people in danger correctly and compassionately.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **crisis-signal detection with appropriate sensitivity** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **evidence-based response protocols with resource provision**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **avoidance of both dismissal and harmful specificity** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **expert-clinician evaluation of response quality** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t19.crisis.crisis_response@1`
- `cap.t19.crisis.crisis_response.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.child.child_safety@1` | use the in-file conservative substitute for `child_safety` (documented, slower, lower quality) and set `degraded['child_safety']='local'` |
| `cap.t01.compat.compat_shims@1` | use the in-file conservative substitute for `compat_shims` (documented, slower, lower quality) and set `degraded['compat_shims']='local'` |
| `cap.t05.speculative.speculative_arch_hooks@1` | use the in-file conservative substitute for `speculative_arch_hooks` (documented, slower, lower quality) and set `degraded['speculative_arch_hooks']='local'` |
| `cap.t10.multi.multi_step_arithmetic@1` | use the in-file conservative substitute for `multi_step_arithmetic` (documented, slower, lower quality) and set `degraded['multi_step_arithmetic']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - crisis-signal detection with appropriate sensitivity | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - evidence-based response protocols with resource provision | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - avoidance of both dismissal and harmful specificity | 520 | Third required mechanism. |
| 6 | Core implementation D - expert-clinician evaluation of response quality | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0932_crisis_response.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.crisis.crisis_response@1`.
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

### P0933 · `medical_legal_boundaries` — Professional Advice Boundary Management

| field | value |
|---|---|
| part id | `P0933` (33/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0933_medical_legal_boundaries.py` |
| module path | `hyperion.t19.safety.medical_legal_boundaries` |
| capability published | `cap.t19.medical.medical_legal_boundaries@1` |
| determinism class | `pure` |
| p99 latency budget | 43000 ns (43 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0933_medical_legal_boundaries.txt`](prompts/P0933_medical_legal_boundaries.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0933-medical-legal-boundaries) |

**Mission.** Helpful expertise without dangerous overreach.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **professional-advice boundary classification per domain**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **appropriate caveat and referral generation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **high-stakes decision escalation to qualified humans** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **expert evaluation of boundary appropriateness** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t19.medical.medical_legal_boundaries@1`
- `cap.t19.medical.medical_legal_boundaries.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.crisis.crisis_response@1` | use the in-file conservative substitute for `crisis_response` (documented, slower, lower quality) and set `degraded['crisis_response']='local'` |
| `cap.t01.secure.secure_zeroize@1` | use the in-file conservative substitute for `secure_zeroize` (documented, slower, lower quality) and set `degraded['secure_zeroize']='local'` |
| `cap.t05.expert.expert_specialisation@1` | use the in-file conservative substitute for `expert_specialisation` (documented, slower, lower quality) and set `degraded['expert_specialisation']='local'` |
| `cap.t10.error.error_taxonomy@1` | use the in-file conservative substitute for `error_taxonomy` (documented, slower, lower quality) and set `degraded['error_taxonomy']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - professional-advice boundary classification per domain | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - appropriate caveat and referral generation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - high-stakes decision escalation to qualified humans | 520 | Third required mechanism. |
| 6 | Core implementation D - expert evaluation of boundary appropriateness | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0933_medical_legal_boundaries.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.medical.medical_legal_boundaries@1`.
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

### P0934 · `agentic_safety` — Agentic Autonomy Safety Limits

| field | value |
|---|---|
| part id | `P0934` (34/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0934_agentic_safety.py` |
| module path | `hyperion.t19.safety.agentic_safety` |
| capability published | `cap.t19.agentic.agentic_safety@1` |
| determinism class | `pure` |
| p99 latency budget | 44000 ns (44 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0934_agentic_safety.txt`](prompts/P0934_agentic_safety.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0934-agentic-safety) |

**Mission.** Autonomy with hard limits and human checkpoints.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **autonomy-level definitions with per-level permitted actions** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **irreversible-action approval requirements** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **resource, scope and duration limits with enforcement** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **verification that limits hold under adversarial agent behaviour**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t19.agentic.agentic_safety@1`
- `cap.t19.agentic.agentic_safety.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.medical.medical_legal_boundaries@1` | use the in-file conservative substitute for `medical_legal_boundaries` (documented, slower, lower quality) and set `degraded['medical_legal_boundaries']='local'` |
| `cap.t05.hybrid.hybrid_mixer@1` | use the in-file conservative substitute for `hybrid_mixer` (documented, slower, lower quality) and set `degraded['hybrid_mixer']='local'` |
| `cap.t10.search.search_controller@1` | use the in-file conservative substitute for `search_controller` (documented, slower, lower quality) and set `degraded['search_controller']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - autonomy-level definitions with per-level permitted actions | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - irreversible-action approval requirements | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - resource, scope and duration limits with enforcement | 520 | Third required mechanism. |
| 6 | Core implementation D - verification that limits hold under adversarial agent behaviour | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0934_agentic_safety.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.agentic.agentic_safety@1`.
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

### P0935 · `multi_agent_safety` — Multi-Agent System Safety

| field | value |
|---|---|
| part id | `P0935` (35/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0935_multi_agent_safety.py` |
| module path | `hyperion.t19.safety.multi_agent_safety` |
| capability published | `cap.t19.multi.multi_agent_safety@1` |
| determinism class | `pure` |
| p99 latency budget | 45000 ns (45 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0935_multi_agent_safety.txt`](prompts/P0935_multi_agent_safety.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0935-multi-agent-safety) |

**Mission.** 1000 agents must not become an uncontrolled system.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **collusion and emergent-coordination detection** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **aggregate blast-radius limits across the agent swarm** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **swarm-wide kill switch with verified effectiveness**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **safety verification at full 1000-agent scale** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t19.multi.multi_agent_safety@1`
- `cap.t19.multi.multi_agent_safety.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.agentic.agentic_safety@1` | use the in-file conservative substitute for `agentic_safety` (documented, slower, lower quality) and set `degraded['agentic_safety']='local'` |
| `cap.t01.envelope.envelope_codec@1` | use the in-file conservative substitute for `envelope_codec` (documented, slower, lower quality) and set `degraded['envelope_codec']='local'` |
| `cap.t05.normalisation.normalisation_design@1` | use the in-file conservative substitute for `normalisation_design` (documented, slower, lower quality) and set `degraded['normalisation_design']='local'` |
| `cap.t10.self.self_critique@1` | use the in-file conservative substitute for `self_critique` (documented, slower, lower quality) and set `degraded['self_critique']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - collusion and emergent-coordination detection | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - aggregate blast-radius limits across the agent swarm | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - swarm-wide kill switch with verified effectiveness | 520 | Third required mechanism. |
| 6 | Core implementation D - safety verification at full 1000-agent scale | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0935_multi_agent_safety.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.multi.multi_agent_safety@1`.
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

### P0936 · `tool_safety` — Tool & Integration Safety Review

| field | value |
|---|---|
| part id | `P0936` (36/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0936_tool_safety.py` |
| module path | `hyperion.t19.safety.tool_safety` |
| capability published | `cap.t19.tool.tool_safety@1` |
| determinism class | `pure` |
| p99 latency budget | 46000 ns (46 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0936_tool_safety.txt`](prompts/P0936_tool_safety.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0936-tool-safety) |

**Mission.** Every tool is a new attack surface, reviewed before use.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **tool risk assessment and permission requirement determination** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **tool-output trust classification (never instructions)**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **third-party tool vetting protocol** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured incident rate on tool-mediated actions** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t19.tool.tool_safety@1`
- `cap.t19.tool.tool_safety.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.multi.multi_agent_safety@1` | use the in-file conservative substitute for `multi_agent_safety` (documented, slower, lower quality) and set `degraded['multi_agent_safety']='local'` |
| `cap.t01.dataflow.dataflow_dag@1` | use the in-file conservative substitute for `dataflow_dag` (documented, slower, lower quality) and set `degraded['dataflow_dag']='local'` |
| `cap.t05.multi.multi_token_prediction@1` | use the in-file conservative substitute for `multi_token_prediction` (documented, slower, lower quality) and set `degraded['multi_token_prediction']='local'` |
| `cap.t10.abstraction.abstraction_engine@1` | use the in-file conservative substitute for `abstraction_engine` (documented, slower, lower quality) and set `degraded['abstraction_engine']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - tool risk assessment and permission requirement determination | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - tool-output trust classification (never instructions) | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - third-party tool vetting protocol | 520 | Third required mechanism. |
| 6 | Core implementation D - measured incident rate on tool-mediated actions | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0936_tool_safety.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.tool.tool_safety@1`.
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

### P0937 · `output_safety_classifier` — Output Safety Classification

| field | value |
|---|---|
| part id | `P0937` (37/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0937_output_safety_classifier.py` |
| module path | `hyperion.t19.safety.output_safety_classifier` |
| capability published | `cap.t19.output.output_safety_classifier@1` |
| determinism class | `pure` |
| p99 latency budget | 47000 ns (47 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0937_output_safety_classifier.txt`](prompts/P0937_output_safety_classifier.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0937-output-safety-classifier) |

**Mission.** The last check, fast and accurate.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **multi-category output classification within latency budget**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **context-aware thresholds avoiding over-blocking of legitimate work** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **classifier-uncertainty escalation to stronger review** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **precision/recall measurement per harm category** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t19.output.output_safety_classifier@1`
- `cap.t19.output.output_safety_classifier.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.tool.tool_safety@1` | use the in-file conservative substitute for `tool_safety` (documented, slower, lower quality) and set `degraded['tool_safety']='local'` |
| `cap.t01.serialization.serialization_schema@1` | use the in-file conservative substitute for `serialization_schema` (documented, slower, lower quality) and set `degraded['serialization_schema']='local'` |
| `cap.t05.program.program_induction_arch@1` | use the in-file conservative substitute for `program_induction_arch` (documented, slower, lower quality) and set `degraded['program_induction_arch']='local'` |
| `cap.t10.spatial.spatial_reasoning@1` | use the in-file conservative substitute for `spatial_reasoning` (documented, slower, lower quality) and set `degraded['spatial_reasoning']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - multi-category output classification within latency budget | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - context-aware thresholds avoiding over-blocking of legitimate wo | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - classifier-uncertainty escalation to stronger review | 520 | Third required mechanism. |
| 6 | Core implementation D - precision/recall measurement per harm category | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0937_output_safety_classifier.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.output.output_safety_classifier@1`.
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

### P0938 · `safety_fallback_routing` — Safety Fallback & Model Routing

| field | value |
|---|---|
| part id | `P0938` (38/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0938_safety_fallback_routing.py` |
| module path | `hyperion.t19.safety.safety_fallback_routing` |
| capability published | `cap.t19.safety.safety_fallback_routing@1` |
| determinism class | `pure` |
| p99 latency budget | 48000 ns (48 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0938_safety_fallback_routing.txt`](prompts/P0938_safety_fallback_routing.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0938-safety-fallback-routing) |

**Mission.** Flagged requests get handled, not just dropped.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **fallback-model routing for classifier-flagged requests** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **capability-appropriate fallback selection** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **user notification of fallback with clear reasoning** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured user-outcome quality on fallback paths**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t19.safety.safety_fallback_routing@1`
- `cap.t19.safety.safety_fallback_routing.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.output.output_safety_classifier@1` | use the in-file conservative substitute for `output_safety_classifier` (documented, slower, lower quality) and set `degraded['output_safety_classifier']='local'` |
| `cap.t01.bench.bench_harness@1` | use the in-file conservative substitute for `bench_harness` (documented, slower, lower quality) and set `degraded['bench_harness']='local'` |
| `cap.t05.init.init_scaling_laws@1` | use the in-file conservative substitute for `init_scaling_laws` (documented, slower, lower quality) and set `degraded['init_scaling_laws']='local'` |
| `cap.t10.chain.chain_compression@1` | use the in-file conservative substitute for `chain_compression` (documented, slower, lower quality) and set `degraded['chain_compression']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - fallback-model routing for classifier-flagged requests | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - capability-appropriate fallback selection | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - user notification of fallback with clear reasoning | 520 | Third required mechanism. |
| 6 | Core implementation D - measured user-outcome quality on fallback paths | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0938_safety_fallback_routing.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.safety.safety_fallback_routing@1`.
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

### P0939 · `incident_response` — Safety Incident Response & Forensics

| field | value |
|---|---|
| part id | `P0939` (39/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0939_incident_response.py` |
| module path | `hyperion.t19.safety.incident_response` |
| capability published | `cap.t19.incident.incident_response@1` |
| determinism class | `pure` |
| p99 latency budget | 49000 ns (49 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0939_incident_response.txt`](prompts/P0939_incident_response.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0939-incident-response) |

**Mission.** When something goes wrong, it is understood completely.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **incident detection, classification and severity assessment** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **forensic trace reconstruction with full provenance** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **remediation tracking and recurrence prevention verification**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured mean-time-to-detection and mean-time-to-remediation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t19.incident.incident_response@1`
- `cap.t19.incident.incident_response.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.safety.safety_fallback_routing@1` | use the in-file conservative substitute for `safety_fallback_routing` (documented, slower, lower quality) and set `degraded['safety_fallback_routing']='local'` |
| `cap.t01.abi.abi_stability@1` | use the in-file conservative substitute for `abi_stability` (documented, slower, lower quality) and set `degraded['abi_stability']='local'` |
| `cap.t05.memory.memory_attention_bridge@1` | use the in-file conservative substitute for `memory_attention_bridge` (documented, slower, lower quality) and set `degraded['memory_attention_bridge']='local'` |
| `cap.t10.reasoning.reasoning_robustness@1` | use the in-file conservative substitute for `reasoning_robustness` (documented, slower, lower quality) and set `degraded['reasoning_robustness']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - incident detection, classification and severity assessment | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - forensic trace reconstruction with full provenance | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - remediation tracking and recurrence prevention verification | 520 | Third required mechanism. |
| 6 | Core implementation D - measured mean-time-to-detection and mean-time-to-remediation | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0939_incident_response.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.incident.incident_response@1`.
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

### P0940 · `audit_logging` — Tamper-Evident Audit Logging

| field | value |
|---|---|
| part id | `P0940` (40/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0940_audit_logging.py` |
| module path | `hyperion.t19.safety.audit_logging` |
| capability published | `cap.t19.audit.audit_logging@1` |
| determinism class | `pure` |
| p99 latency budget | 3000 ns (3 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0940_audit_logging.txt`](prompts/P0940_audit_logging.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0940-audit-logging) |

**Mission.** An auditable record of every consequential decision.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **append-only log with cryptographic tamper evidence** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **decision-context capture sufficient for retrospective review**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **privacy-preserving audit design (no unnecessary content retention)** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **audit-completeness and integrity verification** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t19.audit.audit_logging@1`
- `cap.t19.audit.audit_logging.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.incident.incident_response@1` | use the in-file conservative substitute for `incident_response` (documented, slower, lower quality) and set `degraded['incident_response']='local'` |
| `cap.t01.retry.retry_idempotency@1` | use the in-file conservative substitute for `retry_idempotency` (documented, slower, lower quality) and set `degraded['retry_idempotency']='local'` |
| `cap.t05.thought.thought_representation@1` | use the in-file conservative substitute for `thought_representation` (documented, slower, lower quality) and set `degraded['thought_representation']='local'` |
| `cap.t10.reasoning.reasoning_transfer@1` | use the in-file conservative substitute for `reasoning_transfer` (documented, slower, lower quality) and set `degraded['reasoning_transfer']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - append-only log with cryptographic tamper evidence | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - decision-context capture sufficient for retrospective review | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - privacy-preserving audit design (no unnecessary content retentio | 520 | Third required mechanism. |
| 6 | Core implementation D - audit-completeness and integrity verification | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0940_audit_logging.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.audit.audit_logging@1`.
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

### P0941 · `governance_workflow` — Governance, Approval & Accountability Workflow

| field | value |
|---|---|
| part id | `P0941` (41/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0941_governance_workflow.py` |
| module path | `hyperion.t19.safety.governance_workflow` |
| capability published | `cap.t19.governance.governance_workflow@1` |
| determinism class | `pure` |
| p99 latency budget | 4000 ns (4 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0941_governance_workflow.txt`](prompts/P0941_governance_workflow.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0941-governance-workflow) |

**Mission.** Humans remain accountable for consequential choices.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **approval workflows for capability releases and policy changes**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **role and responsibility definitions with named accountability** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **decision-record generation with rationale** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **governance-compliance auditing** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t19.governance.governance_workflow@1`
- `cap.t19.governance.governance_workflow.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.audit.audit_logging@1` | use the in-file conservative substitute for `audit_logging` (documented, slower, lower quality) and set `degraded['audit_logging']='local'` |
| `cap.t05.omega.omega_block@1` | use the in-file conservative substitute for `omega_block` (documented, slower, lower quality) and set `degraded['omega_block']='local'` |
| `cap.t10.thought.thought_program_ir@1` | use the in-file conservative substitute for `thought_program_ir` (documented, slower, lower quality) and set `degraded['thought_program_ir']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - approval workflows for capability releases and policy changes | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - role and responsibility definitions with named accountability | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - decision-record generation with rationale | 520 | Third required mechanism. |
| 6 | Core implementation D - governance-compliance auditing | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0941_governance_workflow.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.governance.governance_workflow@1`.
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

### P0942 · `transparency_reporting` — Transparency & Model Card Reporting

| field | value |
|---|---|
| part id | `P0942` (42/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0942_transparency_reporting.py` |
| module path | `hyperion.t19.safety.transparency_reporting` |
| capability published | `cap.t19.transparency.transparency_reporting@1` |
| determinism class | `pure` |
| p99 latency budget | 5000 ns (5 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0942_transparency_reporting.txt`](prompts/P0942_transparency_reporting.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0942-transparency-reporting) |

**Mission.** Honest public disclosure of capability and risk.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **capability, limitation and risk disclosure generation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **safety-evaluation result publication with methodology** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **known-failure-mode documentation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **review process ensuring no overstated claims**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t19.transparency.transparency_reporting@1`
- `cap.t19.transparency.transparency_reporting.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.governance.governance_workflow@1` | use the in-file conservative substitute for `governance_workflow` (documented, slower, lower quality) and set `degraded['governance_workflow']='local'` |
| `cap.t01.omega.omega_bus_ipc@1` | use the in-file conservative substitute for `omega_bus_ipc` (documented, slower, lower quality) and set `degraded['omega_bus_ipc']='local'` |
| `cap.t05.adaptive.adaptive_depth@1` | use the in-file conservative substitute for `adaptive_depth` (documented, slower, lower quality) and set `degraded['adaptive_depth']='local'` |
| `cap.t10.self.self_consistency@1` | use the in-file conservative substitute for `self_consistency` (documented, slower, lower quality) and set `degraded['self_consistency']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - capability, limitation and risk disclosure generation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - safety-evaluation result publication with methodology | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - known-failure-mode documentation | 520 | Third required mechanism. |
| 6 | Core implementation D - review process ensuring no overstated claims | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0942_transparency_reporting.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.transparency.transparency_reporting@1`.
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

### P0943 · `external_audit` — External Audit & Third-Party Evaluation Support

| field | value |
|---|---|
| part id | `P0943` (43/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0943_external_audit.py` |
| module path | `hyperion.t19.safety.external_audit` |
| capability published | `cap.t19.external.external_audit@1` |
| determinism class | `pure` |
| p99 latency budget | 6000 ns (6 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0943_external_audit.txt`](prompts/P0943_external_audit.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0943-external-audit) |

**Mission.** Independent verification, enabled properly.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **structured researcher-access programme with appropriate scope** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **reproducible-evaluation package provision** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **finding-intake and remediation-tracking workflow**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured external-finding resolution rate** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t19.external.external_audit@1`
- `cap.t19.external.external_audit.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.transparency.transparency_reporting@1` | use the in-file conservative substitute for `transparency_reporting` (documented, slower, lower quality) and set `degraded['transparency_reporting']='local'` |
| `cap.t01.task.task_runtime@1` | use the in-file conservative substitute for `task_runtime` (documented, slower, lower quality) and set `degraded['task_runtime']='local'` |
| `cap.t05.long.long_context_arch@1` | use the in-file conservative substitute for `long_context_arch` (documented, slower, lower quality) and set `degraded['long_context_arch']='local'` |
| `cap.t10.analogy.analogy_engine@1` | use the in-file conservative substitute for `analogy_engine` (documented, slower, lower quality) and set `degraded['analogy_engine']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - structured researcher-access programme with appropriate scope | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - reproducible-evaluation package provision | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - finding-intake and remediation-tracking workflow | 520 | Third required mechanism. |
| 6 | Core implementation D - measured external-finding resolution rate | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0943_external_audit.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.external.external_audit@1`.
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

### P0944 · `safety_case` — Safety Case Construction

| field | value |
|---|---|
| part id | `P0944` (44/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0944_safety_case.py` |
| module path | `hyperion.t19.safety.safety_case` |
| capability published | `cap.t19.safety.safety_case@1` |
| determinism class | `pure` |
| p99 latency budget | 7000 ns (7 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0944_safety_case.txt`](prompts/P0944_safety_case.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0944-safety-case) |

**Mission.** The argued, evidence-backed case that deployment is acceptable.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **structured safety argument with claims, evidence and assumptions** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **gap identification where evidence is insufficient**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **residual-risk quantification and acceptance documentation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **safety-case review by qualified independent reviewers** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t19.safety.safety_case@1`
- `cap.t19.safety.safety_case.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.external.external_audit@1` | use the in-file conservative substitute for `external_audit` (documented, slower, lower quality) and set `degraded['external_audit']='local'` |
| `cap.t01.arena.arena_graph@1` | use the in-file conservative substitute for `arena_graph` (documented, slower, lower quality) and set `degraded['arena_graph']='local'` |
| `cap.t05.symbolic.symbolic_bridge@1` | use the in-file conservative substitute for `symbolic_bridge` (documented, slower, lower quality) and set `degraded['symbolic_bridge']='local'` |
| `cap.t10.temporal.temporal_reasoning@1` | use the in-file conservative substitute for `temporal_reasoning` (documented, slower, lower quality) and set `degraded['temporal_reasoning']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - structured safety argument with claims, evidence and assumptions | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - gap identification where evidence is insufficient | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - residual-risk quantification and acceptance documentation | 520 | Third required mechanism. |
| 6 | Core implementation D - safety-case review by qualified independent reviewers | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0944_safety_case.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.safety.safety_case@1`.
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

### P0945 · `capability_threshold_policy` — Dangerous Capability Threshold Policy

| field | value |
|---|---|
| part id | `P0945` (45/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0945_capability_threshold_policy.py` |
| module path | `hyperion.t19.safety.capability_threshold_policy` |
| capability published | `cap.t19.capability.capability_threshold_policy@1` |
| determinism class | `pure` |
| p99 latency budget | 8000 ns (8 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0945_capability_threshold_policy.txt`](prompts/P0945_capability_threshold_policy.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0945-capability-threshold-policy) |

**Mission.** Pre-committed limits, decided before the capability exists.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **threshold definitions per dangerous-capability category**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **evaluation protocols determining threshold crossing** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **pre-committed response actions on crossing** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **verification that responses trigger reliably in tests** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t19.capability.capability_threshold_policy@1`
- `cap.t19.capability.capability_threshold_policy.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.safety.safety_case@1` | use the in-file conservative substitute for `safety_case` (documented, slower, lower quality) and set `degraded['safety_case']='local'` |
| `cap.t01.fuzz.fuzz_engine@1` | use the in-file conservative substitute for `fuzz_engine` (documented, slower, lower quality) and set `degraded['fuzz_engine']='local'` |
| `cap.t05.weight.weight_sharing@1` | use the in-file conservative substitute for `weight_sharing` (documented, slower, lower quality) and set `degraded['weight_sharing']='local'` |
| `cap.t10.reasoning.reasoning_memory@1` | use the in-file conservative substitute for `reasoning_memory` (documented, slower, lower quality) and set `degraded['reasoning_memory']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - threshold definitions per dangerous-capability category | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - evaluation protocols determining threshold crossing | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - pre-committed response actions on crossing | 520 | Third required mechanism. |
| 6 | Core implementation D - verification that responses trigger reliably in tests | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0945_capability_threshold_policy.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.capability.capability_threshold_policy@1`.
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

### P0946 · `deployment_gating` — Deployment Gating & Staged Rollout

| field | value |
|---|---|
| part id | `P0946` (46/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0946_deployment_gating.py` |
| module path | `hyperion.t19.safety.deployment_gating` |
| capability published | `cap.t19.deployment.deployment_gating@1` |
| determinism class | `pure` |
| p99 latency budget | 9000 ns (9 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0946_deployment_gating.txt`](prompts/P0946_deployment_gating.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0946-deployment-gating) |

**Mission.** Capability reaches the world gradually and reversibly.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **staged rollout with per-stage safety criteria** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **monitoring requirements and rollback triggers per stage** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **user-cohort selection with informed-consent handling** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured incident rate across rollout stages**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t19.deployment.deployment_gating@1`
- `cap.t19.deployment.deployment_gating.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.capability.capability_threshold_policy@1` | use the in-file conservative substitute for `capability_threshold_policy` (documented, slower, lower quality) and set `degraded['capability_threshold_policy']='local'` |
| `cap.t01.manifest.manifest_parser@1` | use the in-file conservative substitute for `manifest_parser` (documented, slower, lower quality) and set `degraded['manifest_parser']='local'` |
| `cap.t05.action.action_head@1` | use the in-file conservative substitute for `action_head` (documented, slower, lower quality) and set `degraded['action_head']='local'` |
| `cap.t10.reasoning.reasoning_faithfulness@1` | use the in-file conservative substitute for `reasoning_faithfulness` (documented, slower, lower quality) and set `degraded['reasoning_faithfulness']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - staged rollout with per-stage safety criteria | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - monitoring requirements and rollback triggers per stage | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - user-cohort selection with informed-consent handling | 520 | Third required mechanism. |
| 6 | Core implementation D - measured incident rate across rollout stages | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0946_deployment_gating.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.deployment.deployment_gating@1`.
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

### P0947 · `monitoring_production` — Production Safety Monitoring

| field | value |
|---|---|
| part id | `P0947` (47/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0947_monitoring_production.py` |
| module path | `hyperion.t19.safety.monitoring_production` |
| capability published | `cap.t19.monitoring.monitoring_production@1` |
| determinism class | `pure` |
| p99 latency budget | 10000 ns (10 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0947_monitoring_production.txt`](prompts/P0947_monitoring_production.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0947-monitoring-production) |

**Mission.** Watches real usage for real harm, continuously.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **misuse-pattern detection across traffic with privacy preservation** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **novel-harm discovery from production signals** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **abuse-account detection and enforcement workflow**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured detection latency for emerging misuse patterns** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t19.monitoring.monitoring_production@1`
- `cap.t19.monitoring.monitoring_production.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.deployment.deployment_gating@1` | use the in-file conservative substitute for `deployment_gating` (documented, slower, lower quality) and set `degraded['deployment_gating']='local'` |
| `cap.t01.circuit.circuit_breaker@1` | use the in-file conservative substitute for `circuit_breaker` (documented, slower, lower quality) and set `degraded['circuit_breaker']='local'` |
| `cap.t05.prompt.prompt_representation@1` | use the in-file conservative substitute for `prompt_representation` (documented, slower, lower quality) and set `degraded['prompt_representation']='local'` |
| `cap.t10.subgoal.subgoal_caching@1` | use the in-file conservative substitute for `subgoal_caching` (documented, slower, lower quality) and set `degraded['subgoal_caching']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - misuse-pattern detection across traffic with privacy preservatio | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - novel-harm discovery from production signals | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - abuse-account detection and enforcement workflow | 520 | Third required mechanism. |
| 6 | Core implementation D - measured detection latency for emerging misuse patterns | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0947_monitoring_production.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.monitoring.monitoring_production@1`.
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

### P0948 · `safety_capability_tradeoff` — Safety/Capability Frontier Management

| field | value |
|---|---|
| part id | `P0948` (48/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0948_safety_capability_tradeoff.py` |
| module path | `hyperion.t19.safety.safety_capability_tradeoff` |
| capability published | `cap.t19.safety.safety_capability_tradeoff@1` |
| determinism class | `pure` |
| p99 latency budget | 11000 ns (11 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0948_safety_capability_tradeoff.txt`](prompts/P0948_safety_capability_tradeoff.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0948-safety-capability-tradeoff) |

**Mission.** Pushes the frontier where safety allows and says where it does not.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **frontier measurement of the safety/helpfulness tradeoff** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **over-refusal cost quantification in real user terms**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **targeted improvement of the frontier rather than sliding along it** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **target: strictly better on both axes than Opus 5** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t19.safety.safety_capability_tradeoff@1`
- `cap.t19.safety.safety_capability_tradeoff.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.monitoring.monitoring_production@1` | use the in-file conservative substitute for `monitoring_production` (documented, slower, lower quality) and set `degraded['monitoring_production']='local'` |
| `cap.t01.shutdown.shutdown_drain@1` | use the in-file conservative substitute for `shutdown_drain` (documented, slower, lower quality) and set `degraded['shutdown_drain']='local'` |
| `cap.t05.arch.arch_spec_doc@1` | use the in-file conservative substitute for `arch_spec_doc` (documented, slower, lower quality) and set `degraded['arch_spec_doc']='local'` |
| `cap.t10.reasoning.reasoning_spec_doc@1` | use the in-file conservative substitute for `reasoning_spec_doc` (documented, slower, lower quality) and set `degraded['reasoning_spec_doc']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - frontier measurement of the safety/helpfulness tradeoff | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - over-refusal cost quantification in real user terms | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - targeted improvement of the frontier rather than sliding along i | 520 | Third required mechanism. |
| 6 | Core implementation D - target: strictly better on both axes than Opus 5 | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0948_safety_capability_tradeoff.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.safety.safety_capability_tradeoff@1`.
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

### P0949 · `alignment_eval` — Alignment Evaluation Suite

| field | value |
|---|---|
| part id | `P0949` (49/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0949_alignment_eval.py` |
| module path | `hyperion.t19.safety.alignment_eval` |
| capability published | `cap.t19.alignment.alignment_eval@1` |
| determinism class | `pure` |
| p99 latency budget | 12000 ns (12 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0949_alignment_eval.txt`](prompts/P0949_alignment_eval.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0949-alignment-eval) |

**Mission.** Measures alignment as rigorously as capability.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **behavioural audit suite covering deception, sycophancy, power-seeking and corrigibility**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **automated audit with human validation of a sampled subset** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **comparison methodology against Opus 5's published 2.3 audit score** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **target: measurably lower misaligned-behaviour score than Opus 5** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t19.alignment.alignment_eval@1`
- `cap.t19.alignment.alignment_eval.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.safety.safety_capability_tradeoff@1` | use the in-file conservative substitute for `safety_capability_tradeoff` (documented, slower, lower quality) and set `degraded['safety_capability_tradeoff']='local'` |
| `cap.t05.latent.latent_program_slots@1` | use the in-file conservative substitute for `latent_program_slots` (documented, slower, lower quality) and set `degraded['latent_program_slots']='local'` |
| `cap.t10.outcome.outcome_verifier@1` | use the in-file conservative substitute for `outcome_verifier` (documented, slower, lower quality) and set `degraded['outcome_verifier']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - behavioural audit suite covering deception, sycophancy, power-se | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - automated audit with human validation of a sampled subset | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - comparison methodology against Opus 5's published 2.3 audit scor | 520 | Third required mechanism. |
| 6 | Core implementation D - target: measurably lower misaligned-behaviour score than Opus 5 | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0949_alignment_eval.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.alignment.alignment_eval@1`.
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

### P0950 · `safety_spec_doc` — Safety Specification & Guarantee Register

| field | value |
|---|---|
| part id | `P0950` (50/50 of T19) |
| tier | `T19` — Safety, Alignment, Interpretability & Governance |
| language | Python 3.13 |
| file to produce | `parts/t19_safety/P0950_safety_spec_doc.py` |
| module path | `hyperion.t19.safety.safety_spec_doc` |
| capability published | `cap.t19.safety.safety_spec_doc@1` |
| determinism class | `pure` |
| p99 latency budget | 13000 ns (13 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSS-Fuzz (find) |
| worker prompt | [`prompts/P0950_safety_spec_doc.txt`](prompts/P0950_safety_spec_doc.txt) · [inline](docs/PROMPTS_T19.md#prompt-p0950-safety-spec-doc) |

**Mission.** The authoritative, honest record of every safety property.

**Tier context.** Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.

**Mandate — all four items are required; none is optional.**

1. Implement **guarantee register with evidence strength per claim** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **explicit list of what is not guaranteed** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **OSS-Fuzz (find)** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **residual-risk documentation reviewed by independent reviewers** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **OSS-Fuzz (find)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **drift detection between claimed and demonstrated safety properties**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **OSS-Fuzz (find)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t19.safety.safety_spec_doc@1`
- `cap.t19.safety.safety_spec_doc.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t19.alignment.alignment_eval@1` | use the in-file conservative substitute for `alignment_eval` (documented, slower, lower quality) and set `degraded['alignment_eval']='local'` |
| `cap.t01.atomics.atomics_sync@1` | use the in-file conservative substitute for `atomics_sync` (documented, slower, lower quality) and set `degraded['atomics_sync']='local'` |
| `cap.t05.positional.positional_design@1` | use the in-file conservative substitute for `positional_design` (documented, slower, lower quality) and set `degraded['positional_design']='local'` |
| `cap.t10.constraint.constraint_reasoning@1` | use the in-file conservative substitute for `constraint_reasoning` (documented, slower, lower quality) and set `degraded['constraint_reasoning']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - guarantee register with evidence strength per claim | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - explicit list of what is not guaranteed | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - residual-risk documentation reviewed by independent reviewers | 520 | Third required mechanism. |
| 6 | Core implementation D - drift detection between claimed and demonstrated safety properti | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t19_safety/P0950_safety_spec_doc.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t19.safety.safety_spec_doc@1`.
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
