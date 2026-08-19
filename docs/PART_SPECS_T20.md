# HYPERION-Ω — Part specifications · T20 · Platform, SDK, Ops & Distributed Assembly

> Contract: **Ω-CONTRACT v1.0.0-frozen** · 50 parts · 250,000 lines of code · language: TypeScript 5.7

**Tier mission.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Benchmarks this tier is accountable for.** CursorBench 3.2, Zapier AutomationBench

**Tier dependencies.** T01, T08, T09, T18

Each part below is built by exactly one isolated Opus 5 worker that sees only: this specification, the frozen Ω-Contract, and its own prompt. Workers never see each other's files. Link-compatibility comes from the contract, not from coordination.

| part | slug | title | capability |
|---|---|---|---|
| [P0951](#p0951-assembly-manifest) | `assembly_manifest` | Assembly Manifest & 1000-Part Registry | `cap.t20.assembly.assembly_manifest@1` |
| [P0952](#p0952-assembly-linker) | `assembly_linker` | Runtime Assembly & Capability Wiring | `cap.t20.assembly.assembly_linker@1` |
| [P0953](#p0953-assembly-validation) | `assembly_validation` | Assembly Integration Validation | `cap.t20.assembly.assembly_validation@1` |
| [P0954](#p0954-integration-test-matrix) | `integration_test_matrix` | Cross-Part Integration Test Matrix | `cap.t20.integration.integration_test_matrix@1` |
| [P0955](#p0955-contract-conformance) | `contract_conformance` | Ω-Contract Conformance Checker | `cap.t20.contract.contract_conformance@1` |
| [P0956](#p0956-public-api) | `public_api` | Public API Surface Definition | `cap.t20.public.public_api@1` |
| [P0957](#p0957-sdk-typescript) | `sdk_typescript` | TypeScript / JavaScript SDK | `cap.t20.sdk.sdk_typescript@1` |
| [P0958](#p0958-sdk-python) | `sdk_python` | Python SDK | `cap.t20.sdk.sdk_python@1` |
| [P0959](#p0959-sdk-other-languages) | `sdk_other_languages` | Additional Language SDKs | `cap.t20.sdk.sdk_other_languages@1` |
| [P0960](#p0960-cli-tool) | `cli_tool` | Command Line Interface & Developer Tooling | `cap.t20.cli.cli_tool@1` |
| [P0961](#p0961-ide-integration) | `ide_integration` | IDE & Editor Integration | `cap.t20.ide.ide_integration@1` |
| [P0962](#p0962-mcp-interop) | `mcp_interop` | Tool Protocol Interoperability | `cap.t20.mcp.mcp_interop@1` |
| [P0963](#p0963-webhook-events) | `webhook_events` | Webhooks, Events & Async Delivery | `cap.t20.webhook.webhook_events@1` |
| [P0964](#p0964-batch-api) | `batch_api` | Batch & Asynchronous Job API | `cap.t20.batch.batch_api@1` |
| [P0965](#p0965-auth-identity) | `auth_identity` | Authentication, Authorisation & Identity | `cap.t20.auth.auth_identity@1` |
| [P0966](#p0966-tenancy-isolation) | `tenancy_isolation` | Multi-Tenant Isolation Guarantees | `cap.t20.tenancy.tenancy_isolation@1` |
| [P0967](#p0967-quota-billing) | `quota_billing` | Quotas, Metering & Billing | `cap.t20.quota.quota_billing@1` |
| [P0968](#p0968-pricing-engine) | `pricing_engine` | Pricing Model & Cost Transparency | `cap.t20.pricing.pricing_engine@1` |
| [P0969](#p0969-rate-limits-public) | `rate_limits_public` | Public Rate Limiting & Fair Use | `cap.t20.rate.rate_limits_public@1` |
| [P0970](#p0970-deployment-pipeline) | `deployment_pipeline` | Build, Test & Deployment Pipeline | `cap.t20.deployment.deployment_pipeline@1` |
| [P0971](#p0971-release-management) | `release_management` | Release Management & Versioning | `cap.t20.release.release_management@1` |
| [P0972](#p0972-canary-deployment) | `canary_deployment` | Canary & Progressive Delivery | `cap.t20.canary.canary_deployment@1` |
| [P0973](#p0973-feature-flags-platform) | `feature_flags_platform` | Feature Flag & Experiment Platform | `cap.t20.feature.feature_flags_platform@1` |
| [P0974](#p0974-config-management-platform) | `config_management_platform` | Fleet Configuration Management | `cap.t20.config.config_management_platform@1` |
| [P0975](#p0975-observability-platform) | `observability_platform` | Observability Platform: Metrics, Traces, Logs | `cap.t20.observability.observability_platform@1` |
| [P0976](#p0976-alerting-oncall) | `alerting_oncall` | Alerting, Escalation & On-Call Operations | `cap.t20.alerting.alerting_oncall@1` |
| [P0977](#p0977-incident-management) | `incident_management` | Incident Management & Postmortem Process | `cap.t20.incident.incident_management@1` |
| [P0978](#p0978-runbook-automation) | `runbook_automation` | Runbook Automation & Self-Healing | `cap.t20.runbook.runbook_automation@1` |
| [P0979](#p0979-chaos-engineering) | `chaos_engineering` | Chaos Engineering & Resilience Verification | `cap.t20.chaos.chaos_engineering@1` |
| [P0980](#p0980-disaster-recovery) | `disaster_recovery` | Disaster Recovery & Business Continuity | `cap.t20.disaster.disaster_recovery@1` |
| [P0981](#p0981-capacity-operations) | `capacity_operations` | Capacity Operations & Demand Management | `cap.t20.capacity.capacity_operations@1` |
| [P0982](#p0982-cost-operations) | `cost_operations` | Cost Operations & Efficiency Programme | `cap.t20.cost.cost_operations@1` |
| [P0983](#p0983-edge-deployment) | `edge_deployment` | Edge & Regional Deployment | `cap.t20.edge.edge_deployment@1` |
| [P0984](#p0984-on-prem-deployment) | `on_prem_deployment` | Self-Hosted & Air-Gapped Deployment | `cap.t20.on.on_prem_deployment@1` |
| [P0985](#p0985-container-orchestration) | `container_orchestration` | Container & Orchestration Integration | `cap.t20.container.container_orchestration@1` |
| [P0986](#p0986-infrastructure-as-code) | `infrastructure_as_code` | Infrastructure as Code & Environment Definition | `cap.t20.infrastructure.infrastructure_as_code@1` |
| [P0987](#p0987-secrets-management) | `secrets_management` | Secrets Management & Key Rotation | `cap.t20.secrets.secrets_management@1` |
| [P0988](#p0988-compliance-platform) | `compliance_platform` | Compliance & Certification Support | `cap.t20.compliance.compliance_platform@1` |
| [P0989](#p0989-data-residency) | `data_residency` | Data Residency & Sovereignty Controls | `cap.t20.data.data_residency@1` |
| [P0990](#p0990-customer-support-tooling) | `customer_support_tooling` | Support Tooling & Diagnostics | `cap.t20.customer.customer_support_tooling@1` |
| [P0991](#p0991-documentation-platform) | `documentation_platform` | Documentation Platform & Content | `cap.t20.documentation.documentation_platform@1` |
| [P0992](#p0992-developer-onboarding) | `developer_onboarding` | Developer Onboarding & Examples | `cap.t20.developer.developer_onboarding@1` |
| [P0993](#p0993-playground-console) | `playground_console` | Interactive Console & Playground | `cap.t20.playground.playground_console@1` |
| [P0994](#p0994-model-registry-platform) | `model_registry_platform` | Model & Artifact Registry | `cap.t20.model.model_registry_platform@1` |
| [P0995](#p0995-evaluation-integration) | `evaluation_integration` | Continuous Evaluation in the Deployment Pipeline | `cap.t20.evaluation.evaluation_integration@1` |
| [P0996](#p0996-distributed-dev-workflow) | `distributed_dev_workflow` | 1000-Worker Distributed Development Workflow | `cap.t20.distributed.distributed_dev_workflow@1` |
| [P0997](#p0997-part-submission-gate) | `part_submission_gate` | Part Submission Validation Gate | `cap.t20.part.part_submission_gate@1` |
| [P0998](#p0998-assembly-dashboard) | `assembly_dashboard` | Assembly Progress & Health Data Products | `cap.t20.assembly.assembly_dashboard@1` |
| [P0999](#p0999-platform-bench) | `platform_bench` | Platform Benchmark & SLO Verification | `cap.t20.platform.platform_bench@1` |
| [P1000](#p1000-platform-spec-doc) | `platform_spec_doc` | Platform Specification, README & Master Index | `cap.t20.platform.platform_spec_doc@1` |

---

### P0951 · `assembly_manifest` — Assembly Manifest & 1000-Part Registry

| field | value |
|---|---|
| part id | `P0951` (1/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0951_assembly_manifest.ts` |
| module path | `hyperion.t20.platform.assembly_manifest` |
| capability published | `cap.t20.assembly.assembly_manifest@1` |
| determinism class | `io` |
| p99 latency budget | 14000 ns (14 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0951_assembly_manifest.txt`](prompts/P0951_assembly_manifest.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0951-assembly-manifest) |

**Mission.** The single index of all 1000 parts and their capabilities.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **manifest aggregation from all 1000 part files with validation** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **capability index with provider/consumer cross-references** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **completeness verification (all 1000 present, all requires satisfied)**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **assembly-report artifact consumed by the build and deploy pipeline** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t20.assembly.assembly_manifest@1`
- `cap.t20.assembly.assembly_manifest.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t01.string.string_interning@1` | use the in-file conservative substitute for `string_interning` (documented, slower, lower quality) and set `degraded['string_interning']='local'` |
| `cap.t08.stop.stop_conditions@1` | use the in-file conservative substitute for `stop_conditions` (documented, slower, lower quality) and set `degraded['stop_conditions']='local'` |
| `cap.t09.edge.edge_inference@1` | use the in-file conservative substitute for `edge_inference` (documented, slower, lower quality) and set `degraded['edge_inference']='local'` |
| `cap.t18.gdpval.gdpval_eval@1` | use the in-file conservative substitute for `gdpval_eval` (documented, slower, lower quality) and set `degraded['gdpval_eval']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - manifest aggregation from all 1000 part files with validation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - capability index with provider/consumer cross-references | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - completeness verification (all 1000 present, all requires satisf | 520 | Third required mechanism. |
| 6 | Core implementation D - assembly-report artifact consumed by the build and deploy pipeli | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0951_assembly_manifest.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.assembly.assembly_manifest@1`.
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

### P0952 · `assembly_linker` — Runtime Assembly & Capability Wiring

| field | value |
|---|---|
| part id | `P0952` (2/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0952_assembly_linker.ts` |
| module path | `hyperion.t20.platform.assembly_linker` |
| capability published | `cap.t20.assembly.assembly_linker@1` |
| determinism class | `io` |
| p99 latency budget | 15000 ns (15 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0952_assembly_linker.txt`](prompts/P0952_assembly_linker.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0952-assembly-linker) |

**Mission.** Fuses 1000 independently authored files into one working system.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **dependency-ordered registration with parallel waves** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **capability resolution with fallback ladders for missing parts**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **partial-assembly operation (system works with parts missing, degraded)** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured startup time and degradation behaviour per missing part** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t20.assembly.assembly_linker@1`
- `cap.t20.assembly.assembly_linker.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.assembly.assembly_manifest@1` | use the in-file conservative substitute for `assembly_manifest` (documented, slower, lower quality) and set `degraded['assembly_manifest']='local'` |
| `cap.t01.property.property_gen@1` | use the in-file conservative substitute for `property_gen` (documented, slower, lower quality) and set `degraded['property_gen']='local'` |
| `cap.t08.adapter.adapter_serving@1` | use the in-file conservative substitute for `adapter_serving` (documented, slower, lower quality) and set `degraded['adapter_serving']='local'` |
| `cap.t09.lock.lock_free_paths@1` | use the in-file conservative substitute for `lock_free_paths` (documented, slower, lower quality) and set `degraded['lock_free_paths']='local'` |
| `cap.t18.robustness.robustness_eval@1` | use the in-file conservative substitute for `robustness_eval` (documented, slower, lower quality) and set `degraded['robustness_eval']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - dependency-ordered registration with parallel waves | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - capability resolution with fallback ladders for missing parts | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - partial-assembly operation (system works with parts missing, deg | 520 | Third required mechanism. |
| 6 | Core implementation D - measured startup time and degradation behaviour per missing part | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0952_assembly_linker.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.assembly.assembly_linker@1`.
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

### P0953 · `assembly_validation` — Assembly Integration Validation

| field | value |
|---|---|
| part id | `P0953` (3/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0953_assembly_validation.ts` |
| module path | `hyperion.t20.platform.assembly_validation` |
| capability published | `cap.t20.assembly.assembly_validation@1` |
| determinism class | `io` |
| p99 latency budget | 16000 ns (16 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0953_assembly_validation.txt`](prompts/P0953_assembly_validation.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0953-assembly-validation) |

**Mission.** Proves the whole is coherent, not just the parts.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **cross-part contract conformance verification at runtime**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **integration smoke suite exercising every capability boundary** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **version and schema compatibility verification across all parts** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **validation report required before any deployment** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t20.assembly.assembly_validation@1`
- `cap.t20.assembly.assembly_validation.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.assembly.assembly_linker@1` | use the in-file conservative substitute for `assembly_linker` (documented, slower, lower quality) and set `degraded['assembly_linker']='local'` |
| `cap.t01.link.link_validator@1` | use the in-file conservative substitute for `link_validator` (documented, slower, lower quality) and set `degraded['link_validator']='local'` |
| `cap.t08.engine.engine_telemetry@1` | use the in-file conservative substitute for `engine_telemetry` (documented, slower, lower quality) and set `degraded['engine_telemetry']='local'` |
| `cap.t09.flamegraph.flamegraph_tooling@1` | use the in-file conservative substitute for `flamegraph_tooling` (documented, slower, lower quality) and set `degraded['flamegraph_tooling']='local'` |
| `cap.t18.canary.canary_eval@1` | use the in-file conservative substitute for `canary_eval` (documented, slower, lower quality) and set `degraded['canary_eval']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - cross-part contract conformance verification at runtime | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - integration smoke suite exercising every capability boundary | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - version and schema compatibility verification across all parts | 520 | Third required mechanism. |
| 6 | Core implementation D - validation report required before any deployment | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0953_assembly_validation.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.assembly.assembly_validation@1`.
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

### P0954 · `integration_test_matrix` — Cross-Part Integration Test Matrix

| field | value |
|---|---|
| part id | `P0954` (4/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0954_integration_test_matrix.ts` |
| module path | `hyperion.t20.platform.integration_test_matrix` |
| capability published | `cap.t20.integration.integration_test_matrix@1` |
| determinism class | `io` |
| p99 latency budget | 17000 ns (17 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0954_integration_test_matrix.txt`](prompts/P0954_integration_test_matrix.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0954-integration-test-matrix) |

**Mission.** Tests the interfaces, where independently written code actually breaks.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **pairwise and path-based integration test generation from the capability graph** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **contract-violation detection with precise part attribution** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **coverage measurement over all capability edges** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **matrix execution within a bounded time budget**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t20.integration.integration_test_matrix@1`
- `cap.t20.integration.integration_test_matrix.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.assembly.assembly_validation@1` | use the in-file conservative substitute for `assembly_validation` (documented, slower, lower quality) and set `degraded['assembly_validation']='local'` |
| `cap.t01.rate.rate_limiter@1` | use the in-file conservative substitute for `rate_limiter` (documented, slower, lower quality) and set `degraded['rate_limiter']='local'` |
| `cap.t08.api.api_gateway_runtime@1` | use the in-file conservative substitute for `api_gateway_runtime` (documented, slower, lower quality) and set `degraded['api_gateway_runtime']='local'` |
| `cap.t09.speculation.speculation_budget@1` | use the in-file conservative substitute for `speculation_budget` (documented, slower, lower quality) and set `degraded['speculation_budget']='local'` |
| `cap.t18.dynamic.dynamic_benchmark@1` | use the in-file conservative substitute for `dynamic_benchmark` (documented, slower, lower quality) and set `degraded['dynamic_benchmark']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - pairwise and path-based integration test generation from the cap | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - contract-violation detection with precise part attribution | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - coverage measurement over all capability edges | 520 | Third required mechanism. |
| 6 | Core implementation D - matrix execution within a bounded time budget | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0954_integration_test_matrix.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.integration.integration_test_matrix@1`.
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

### P0955 · `contract_conformance` — Ω-Contract Conformance Checker

| field | value |
|---|---|
| part id | `P0955` (5/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0955_contract_conformance.ts` |
| module path | `hyperion.t20.platform.contract_conformance` |
| capability published | `cap.t20.contract.contract_conformance@1` |
| determinism class | `io` |
| p99 latency budget | 18000 ns (18 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0955_contract_conformance.txt`](prompts/P0955_contract_conformance.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0955-contract-conformance) |

**Mission.** Machine-verifies all twelve contract clauses in every part.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **per-clause automated checking (manifest, symbols, errors, determinism, tests, shape)** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **contract-digest verification detecting header drift** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **conformance scorecard per part with remediation guidance**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **gate blocking non-conformant parts from the assembly** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t20.contract.contract_conformance@1`
- `cap.t20.contract.contract_conformance.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.integration.integration_test_matrix@1` | use the in-file conservative substitute for `integration_test_matrix` (documented, slower, lower quality) and set `degraded['integration_test_matrix']='local'` |
| `cap.t01.bootstrap.bootstrap_init@1` | use the in-file conservative substitute for `bootstrap_init` (documented, slower, lower quality) and set `degraded['bootstrap_init']='local'` |
| `cap.t08.cost.cost_accounting_runtime@1` | use the in-file conservative substitute for `cost_accounting_runtime` (documented, slower, lower quality) and set `degraded['cost_accounting_runtime']='local'` |
| `cap.t09.speed.speed_proof_report@1` | use the in-file conservative substitute for `speed_proof_report` (documented, slower, lower quality) and set `degraded['speed_proof_report']='local'` |
| `cap.t18.eval.eval_task_provenance@1` | use the in-file conservative substitute for `eval_task_provenance` (documented, slower, lower quality) and set `degraded['eval_task_provenance']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - per-clause automated checking (manifest, symbols, errors, determ | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - contract-digest verification detecting header drift | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - conformance scorecard per part with remediation guidance | 520 | Third required mechanism. |
| 6 | Core implementation D - gate blocking non-conformant parts from the assembly | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0955_contract_conformance.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.contract.contract_conformance@1`.
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

### P0956 · `public_api` — Public API Surface Definition

| field | value |
|---|---|
| part id | `P0956` (6/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0956_public_api.ts` |
| module path | `hyperion.t20.platform.public_api` |
| capability published | `cap.t20.public.public_api@1` |
| determinism class | `io` |
| p99 latency budget | 19000 ns (19 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0956_public_api.txt`](prompts/P0956_public_api.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0956-public-api) |

**Mission.** The interface the world uses.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **endpoint, message and error specification with versioning policy** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **compatibility guarantees and deprecation timeline rules**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **OpenAPI-class machine-readable specification generation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **API-conformance test suite** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t20.public.public_api@1`
- `cap.t20.public.public_api.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.contract.contract_conformance@1` | use the in-file conservative substitute for `contract_conformance` (documented, slower, lower quality) and set `degraded['contract_conformance']='local'` |
| `cap.t01.chacha.chacha_seeds@1` | use the in-file conservative substitute for `chacha_seeds` (documented, slower, lower quality) and set `degraded['chacha_seeds']='local'` |
| `cap.t08.cascade.cascade_stage1_draft@1` | use the in-file conservative substitute for `cascade_stage1_draft` (documented, slower, lower quality) and set `degraded['cascade_stage1_draft']='local'` |
| `cap.t09.template.template_cache@1` | use the in-file conservative substitute for `template_cache` (documented, slower, lower quality) and set `degraded['template_cache']='local'` |
| `cap.t18.elo.elo_arena@1` | use the in-file conservative substitute for `elo_arena` (documented, slower, lower quality) and set `degraded['elo_arena']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - endpoint, message and error specification with versioning policy | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - compatibility guarantees and deprecation timeline rules | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - OpenAPI-class machine-readable specification generation | 520 | Third required mechanism. |
| 6 | Core implementation D - API-conformance test suite | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0956_public_api.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.public.public_api@1`.
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

### P0957 · `sdk_typescript` — TypeScript / JavaScript SDK

| field | value |
|---|---|
| part id | `P0957` (7/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0957_sdk_typescript.ts` |
| module path | `hyperion.t20.platform.sdk_typescript` |
| capability published | `cap.t20.sdk.sdk_typescript@1` |
| determinism class | `io` |
| p99 latency budget | 20000 ns (20 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0957_sdk_typescript.txt`](prompts/P0957_sdk_typescript.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0957-sdk-typescript) |

**Mission.** First-class client library for the largest developer ecosystem.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **typed client with streaming, tools, retries and cancellation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **runtime-agnostic implementation (Node, browser, edge, Deno, Bun)** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **zero-dependency implementation with tree-shakeable modules** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **example suite and API-conformance verification** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t20.sdk.sdk_typescript@1`
- `cap.t20.sdk.sdk_typescript.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.public.public_api@1` | use the in-file conservative substitute for `public_api` (documented, slower, lower quality) and set `degraded['public_api']='local'` |
| `cap.t01.mem.mem_layout@1` | use the in-file conservative substitute for `mem_layout` (documented, slower, lower quality) and set `degraded['mem_layout']='local'` |
| `cap.t08.cascade.cascade_rollback@1` | use the in-file conservative substitute for `cascade_rollback` (documented, slower, lower quality) and set `degraded['cascade_rollback']='local'` |
| `cap.t09.dag.dag_critical_path@1` | use the in-file conservative substitute for `dag_critical_path` (documented, slower, lower quality) and set `degraded['dag_critical_path']='local'` |
| `cap.t18.terminal.terminal_bench_eval@1` | use the in-file conservative substitute for `terminal_bench_eval` (documented, slower, lower quality) and set `degraded['terminal_bench_eval']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - typed client with streaming, tools, retries and cancellation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - runtime-agnostic implementation (Node, browser, edge, Deno, Bun) | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - zero-dependency implementation with tree-shakeable modules | 520 | Third required mechanism. |
| 6 | Core implementation D - example suite and API-conformance verification | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0957_sdk_typescript.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.sdk.sdk_typescript@1`.
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

### P0958 · `sdk_python` — Python SDK

| field | value |
|---|---|
| part id | `P0958` (8/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0958_sdk_python.ts` |
| module path | `hyperion.t20.platform.sdk_python` |
| capability published | `cap.t20.sdk.sdk_python@1` |
| determinism class | `io` |
| p99 latency budget | 21000 ns (21 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0958_sdk_python.txt`](prompts/P0958_sdk_python.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0958-sdk-python) |

**Mission.** First-class client library for the AI and data ecosystem.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **sync and async clients with identical semantics** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **streaming, tool-loop and structured-output helpers** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **typed interfaces with strict type-checker compatibility** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **example suite and API-conformance verification**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t20.sdk.sdk_python@1`
- `cap.t20.sdk.sdk_python.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.sdk.sdk_typescript@1` | use the in-file conservative substitute for `sdk_typescript` (documented, slower, lower quality) and set `degraded['sdk_typescript']='local'` |
| `cap.t01.hash.hash_maps@1` | use the in-file conservative substitute for `hash_maps` (documented, slower, lower quality) and set `degraded['hash_maps']='local'` |
| `cap.t08.logit.logit_processor@1` | use the in-file conservative substitute for `logit_processor` (documented, slower, lower quality) and set `degraded['logit_processor']='local'` |
| `cap.t09.network.network_latency@1` | use the in-file conservative substitute for `network_latency` (documented, slower, lower quality) and set `degraded['network_latency']='local'` |
| `cap.t18.automation.automation_bench_eval@1` | use the in-file conservative substitute for `automation_bench_eval` (documented, slower, lower quality) and set `degraded['automation_bench_eval']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - sync and async clients with identical semantics | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - streaming, tool-loop and structured-output helpers | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - typed interfaces with strict type-checker compatibility | 520 | Third required mechanism. |
| 6 | Core implementation D - example suite and API-conformance verification | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0958_sdk_python.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.sdk.sdk_python@1`.
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

### P0959 · `sdk_other_languages` — Additional Language SDKs

| field | value |
|---|---|
| part id | `P0959` (9/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0959_sdk_other_languages.ts` |
| module path | `hyperion.t20.platform.sdk_other_languages` |
| capability published | `cap.t20.sdk.sdk_other_languages@1` |
| determinism class | `io` |
| p99 latency budget | 22000 ns (22 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0959_sdk_other_languages.txt`](prompts/P0959_sdk_other_languages.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0959-sdk-other-languages) |

**Mission.** Go, Rust, Java, C# and mobile clients from one specification.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **specification-driven client generation with idiomatic hand-tuning** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **cross-SDK behavioural equivalence testing** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **language-specific concurrency and error idioms**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **conformance verification across all SDKs** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t20.sdk.sdk_other_languages@1`
- `cap.t20.sdk.sdk_other_languages.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.sdk.sdk_python@1` | use the in-file conservative substitute for `sdk_python` (documented, slower, lower quality) and set `degraded['sdk_python']='local'` |
| `cap.t01.selftest.selftest_harness@1` | use the in-file conservative substitute for `selftest_harness` (documented, slower, lower quality) and set `degraded['selftest_harness']='local'` |
| `cap.t08.multi.multi_model_serving@1` | use the in-file conservative substitute for `multi_model_serving` (documented, slower, lower quality) and set `degraded['multi_model_serving']='local'` |
| `cap.t09.hot.hot_cold_split@1` | use the in-file conservative substitute for `hot_cold_split` (documented, slower, lower quality) and set `degraded['hot_cold_split']='local'` |
| `cap.t18.calibration.calibration_eval@1` | use the in-file conservative substitute for `calibration_eval` (documented, slower, lower quality) and set `degraded['calibration_eval']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - specification-driven client generation with idiomatic hand-tunin | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - cross-SDK behavioural equivalence testing | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - language-specific concurrency and error idioms | 520 | Third required mechanism. |
| 6 | Core implementation D - conformance verification across all SDKs | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0959_sdk_other_languages.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.sdk.sdk_other_languages@1`.
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

### P0960 · `cli_tool` — Command Line Interface & Developer Tooling

| field | value |
|---|---|
| part id | `P0960` (10/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0960_cli_tool.ts` |
| module path | `hyperion.t20.platform.cli_tool` |
| capability published | `cap.t20.cli.cli_tool@1` |
| determinism class | `io` |
| p99 latency budget | 23000 ns (23 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0960_cli_tool.txt`](prompts/P0960_cli_tool.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0960-cli-tool) |

**Mission.** The terminal-native way to use and operate the system.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **interactive and scriptable modes with structured output options** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **session, project and configuration management**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **shell completion, help quality and error-message clarity** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **usability validation with real developer workflows** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t20.cli.cli_tool@1`
- `cap.t20.cli.cli_tool.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.sdk.sdk_other_languages@1` | use the in-file conservative substitute for `sdk_other_languages` (documented, slower, lower quality) and set `degraded['sdk_other_languages']='local'` |
| `cap.t01.version.version_semver@1` | use the in-file conservative substitute for `version_semver` (documented, slower, lower quality) and set `degraded['version_semver']='local'` |
| `cap.t08.output.output_verification_loop@1` | use the in-file conservative substitute for `output_verification_loop` (documented, slower, lower quality) and set `degraded['output_verification_loop']='local'` |
| `cap.t09.perf.perf_ci@1` | use the in-file conservative substitute for `perf_ci` (documented, slower, lower quality) and set `degraded['perf_ci']='local'` |
| `cap.t18.regression.regression_suite@1` | use the in-file conservative substitute for `regression_suite` (documented, slower, lower quality) and set `degraded['regression_suite']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - interactive and scriptable modes with structured output options | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - session, project and configuration management | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - shell completion, help quality and error-message clarity | 520 | Third required mechanism. |
| 6 | Core implementation D - usability validation with real developer workflows | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0960_cli_tool.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.cli.cli_tool@1`.
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

### P0961 · `ide_integration` — IDE & Editor Integration

| field | value |
|---|---|
| part id | `P0961` (11/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0961_ide_integration.ts` |
| module path | `hyperion.t20.platform.ide_integration` |
| capability published | `cap.t20.ide.ide_integration@1` |
| determinism class | `io` |
| p99 latency budget | 24000 ns (24 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0961_ide_integration.txt`](prompts/P0961_ide_integration.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0961-ide-integration) |

**Mission.** Where developers actually work.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **language-server-protocol integration with incremental context**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **inline suggestion, chat and agent-task interfaces** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **workspace-context management with privacy controls** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **latency budget for interactive editor operations** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t20.ide.ide_integration@1`
- `cap.t20.ide.ide_integration.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.cli.cli_tool@1` | use the in-file conservative substitute for `cli_tool` (documented, slower, lower quality) and set `degraded['cli_tool']='local'` |
| `cap.t01.budget.budget_ledger@1` | use the in-file conservative substitute for `budget_ledger` (documented, slower, lower quality) and set `degraded['budget_ledger']='local'` |
| `cap.t08.engine.engine_fault_tolerance@1` | use the in-file conservative substitute for `engine_fault_tolerance` (documented, slower, lower quality) and set `degraded['engine_fault_tolerance']='local'` |
| `cap.t09.cache.cache_sizing@1` | use the in-file conservative substitute for `cache_sizing` (documented, slower, lower quality) and set `degraded['cache_sizing']='local'` |
| `cap.t18.benchmark.benchmark_construction@1` | use the in-file conservative substitute for `benchmark_construction` (documented, slower, lower quality) and set `degraded['benchmark_construction']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - language-server-protocol integration with incremental context | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - inline suggestion, chat and agent-task interfaces | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - workspace-context management with privacy controls | 520 | Third required mechanism. |
| 6 | Core implementation D - latency budget for interactive editor operations | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0961_ide_integration.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.ide.ide_integration@1`.
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

### P0962 · `mcp_interop` — Tool Protocol Interoperability

| field | value |
|---|---|
| part id | `P0962` (12/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0962_mcp_interop.ts` |
| module path | `hyperion.t20.platform.mcp_interop` |
| capability published | `cap.t20.mcp.mcp_interop@1` |
| determinism class | `io` |
| p99 latency budget | 25000 ns (25 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0962_mcp_interop.txt`](prompts/P0962_mcp_interop.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0962-mcp-interop) |

**Mission.** Speaks the ecosystem's tool protocols natively.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **standard tool-protocol server and client implementation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **capability negotiation and version compatibility handling** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **security review of protocol-mediated tool access** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **interoperability testing against reference implementations**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t20.mcp.mcp_interop@1`
- `cap.t20.mcp.mcp_interop.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.ide.ide_integration@1` | use the in-file conservative substitute for `ide_integration` (documented, slower, lower quality) and set `degraded['ide_integration']='local'` |
| `cap.t01.compression.compression@1` | use the in-file conservative substitute for `compression` (documented, slower, lower quality) and set `degraded['compression']='local'` |
| `cap.t08.engine.engine_security@1` | use the in-file conservative substitute for `engine_security` (documented, slower, lower quality) and set `degraded['engine_security']='local'` |
| `cap.t09.latency.latency_dashboard@1` | use the in-file conservative substitute for `latency_dashboard` (documented, slower, lower quality) and set `degraded['latency_dashboard']='local'` |
| `cap.t18.eval.eval_release_report@1` | use the in-file conservative substitute for `eval_release_report` (documented, slower, lower quality) and set `degraded['eval_release_report']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - standard tool-protocol server and client implementation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - capability negotiation and version compatibility handling | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - security review of protocol-mediated tool access | 520 | Third required mechanism. |
| 6 | Core implementation D - interoperability testing against reference implementations | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0962_mcp_interop.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.mcp.mcp_interop@1`.
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

### P0963 · `webhook_events` — Webhooks, Events & Async Delivery

| field | value |
|---|---|
| part id | `P0963` (13/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0963_webhook_events.ts` |
| module path | `hyperion.t20.platform.webhook_events` |
| capability published | `cap.t20.webhook.webhook_events@1` |
| determinism class | `io` |
| p99 latency budget | 26000 ns (26 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0963_webhook_events.txt`](prompts/P0963_webhook_events.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0963-webhook-events) |

**Mission.** Reliable notification for long-running work.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **event schema, signing and replay-protection** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **at-least-once delivery with idempotency guidance and retry policy** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **subscription management and filtering**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **delivery-reliability measurement** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t20.webhook.webhook_events@1`
- `cap.t20.webhook.webhook_events.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.mcp.mcp_interop@1` | use the in-file conservative substitute for `mcp_interop` (documented, slower, lower quality) and set `degraded['mcp_interop']='local'` |
| `cap.t01.blake3.blake3_hash@1` | use the in-file conservative substitute for `blake3_hash` (documented, slower, lower quality) and set `degraded['blake3_hash']='local'` |
| `cap.t08.admission.admission_control@1` | use the in-file conservative substitute for `admission_control` (documented, slower, lower quality) and set `degraded['admission_control']='local'` |
| `cap.t09.similarity.similarity_cache@1` | use the in-file conservative substitute for `similarity_cache` (documented, slower, lower quality) and set `degraded['similarity_cache']='local'` |
| `cap.t18.expert.expert_eval@1` | use the in-file conservative substitute for `expert_eval` (documented, slower, lower quality) and set `degraded['expert_eval']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - event schema, signing and replay-protection | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - at-least-once delivery with idempotency guidance and retry polic | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - subscription management and filtering | 520 | Third required mechanism. |
| 6 | Core implementation D - delivery-reliability measurement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0963_webhook_events.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.webhook.webhook_events@1`.
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

### P0964 · `batch_api` — Batch & Asynchronous Job API

| field | value |
|---|---|
| part id | `P0964` (14/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0964_batch_api.ts` |
| module path | `hyperion.t20.platform.batch_api` |
| capability published | `cap.t20.batch.batch_api@1` |
| determinism class | `io` |
| p99 latency budget | 27000 ns (27 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0964_batch_api.txt`](prompts/P0964_batch_api.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0964-batch-api) |

**Mission.** Cheap, high-throughput processing for non-interactive work.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **job submission, status, cancellation and result retrieval** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **cost-reduced scheduling into spare capacity**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **partial-result and per-item error reporting** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **throughput and cost-saving measurement versus synchronous serving** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t20.batch.batch_api@1`
- `cap.t20.batch.batch_api.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.webhook.webhook_events@1` | use the in-file conservative substitute for `webhook_events` (documented, slower, lower quality) and set `degraded['webhook_events']='local'` |
| `cap.t01.alloc.alloc_arena@1` | use the in-file conservative substitute for `alloc_arena` (documented, slower, lower quality) and set `degraded['alloc_arena']='local'` |
| `cap.t08.cascade.cascade_batching@1` | use the in-file conservative substitute for `cascade_batching` (documented, slower, lower quality) and set `degraded['cascade_batching']='local'` |
| `cap.t09.parallel.parallel_horizon@1` | use the in-file conservative substitute for `parallel_horizon` (documented, slower, lower quality) and set `degraded['parallel_horizon']='local'` |
| `cap.t18.frontier.frontier_bench_eval@1` | use the in-file conservative substitute for `frontier_bench_eval` (documented, slower, lower quality) and set `degraded['frontier_bench_eval']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - job submission, status, cancellation and result retrieval | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - cost-reduced scheduling into spare capacity | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - partial-result and per-item error reporting | 520 | Third required mechanism. |
| 6 | Core implementation D - throughput and cost-saving measurement versus synchronous servin | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0964_batch_api.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.batch.batch_api@1`.
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

### P0965 · `auth_identity` — Authentication, Authorisation & Identity

| field | value |
|---|---|
| part id | `P0965` (15/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0965_auth_identity.ts` |
| module path | `hyperion.t20.platform.auth_identity` |
| capability published | `cap.t20.auth.auth_identity@1` |
| determinism class | `io` |
| p99 latency budget | 28000 ns (28 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0965_auth_identity.txt`](prompts/P0965_auth_identity.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0965-auth-identity) |

**Mission.** Correct access control at the platform edge.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **key, token and federated-identity authentication with rotation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **fine-grained authorisation with least-privilege defaults** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **organisation, project and user scope hierarchy** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **authorisation-bypass testing and verification** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t20.auth.auth_identity@1`
- `cap.t20.auth.auth_identity.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.batch.batch_api@1` | use the in-file conservative substitute for `batch_api` (documented, slower, lower quality) and set `degraded['batch_api']='local'` |
| `cap.t01.bitset.bitset_rank@1` | use the in-file conservative substitute for `bitset_rank` (documented, slower, lower quality) and set `degraded['bitset_rank']='local'` |
| `cap.t08.constrained.constrained_decoding@1` | use the in-file conservative substitute for `constrained_decoding` (documented, slower, lower quality) and set `degraded['constrained_decoding']='local'` |
| `cap.t09.syscall.syscall_reduction@1` | use the in-file conservative substitute for `syscall_reduction` (documented, slower, lower quality) and set `degraded['syscall_reduction']='local'` |
| `cap.t18.browsecomp.browsecomp_eval@1` | use the in-file conservative substitute for `browsecomp_eval` (documented, slower, lower quality) and set `degraded['browsecomp_eval']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - key, token and federated-identity authentication with rotation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - fine-grained authorisation with least-privilege defaults | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - organisation, project and user scope hierarchy | 520 | Third required mechanism. |
| 6 | Core implementation D - authorisation-bypass testing and verification | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0965_auth_identity.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.auth.auth_identity@1`.
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

### P0966 · `tenancy_isolation` — Multi-Tenant Isolation Guarantees

| field | value |
|---|---|
| part id | `P0966` (16/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0966_tenancy_isolation.ts` |
| module path | `hyperion.t20.platform.tenancy_isolation` |
| capability published | `cap.t20.tenancy.tenancy_isolation@1` |
| determinism class | `io` |
| p99 latency budget | 29000 ns (29 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0966_tenancy_isolation.txt`](prompts/P0966_tenancy_isolation.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0966-tenancy-isolation) |

**Mission.** One customer can never affect or observe another.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **data, cache, memory and compute isolation enforcement** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **cross-tenant leakage testing across every shared structure** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **per-tenant quota and fairness enforcement** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **isolation-verification report with adversarial test results**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t20.tenancy.tenancy_isolation@1`
- `cap.t20.tenancy.tenancy_isolation.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.auth.auth_identity@1` | use the in-file conservative substitute for `auth_identity` (documented, slower, lower quality) and set `degraded['auth_identity']='local'` |
| `cap.t01.metrics.metrics_core@1` | use the in-file conservative substitute for `metrics_core` (documented, slower, lower quality) and set `degraded['metrics_core']='local'` |
| `cap.t08.weight.weight_hotswap@1` | use the in-file conservative substitute for `weight_hotswap` (documented, slower, lower quality) and set `degraded['weight_hotswap']='local'` |
| `cap.t09.cache.cache_coherence@1` | use the in-file conservative substitute for `cache_coherence` (documented, slower, lower quality) and set `degraded['cache_coherence']='local'` |
| `cap.t18.hallucination.hallucination_eval@1` | use the in-file conservative substitute for `hallucination_eval` (documented, slower, lower quality) and set `degraded['hallucination_eval']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - data, cache, memory and compute isolation enforcement | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - cross-tenant leakage testing across every shared structure | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - per-tenant quota and fairness enforcement | 520 | Third required mechanism. |
| 6 | Core implementation D - isolation-verification report with adversarial test results | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0966_tenancy_isolation.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.tenancy.tenancy_isolation@1`.
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

### P0967 · `quota_billing` — Quotas, Metering & Billing

| field | value |
|---|---|
| part id | `P0967` (17/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0967_quota_billing.ts` |
| module path | `hyperion.t20.platform.quota_billing` |
| capability published | `cap.t20.quota.quota_billing@1` |
| determinism class | `io` |
| p99 latency budget | 30000 ns (30 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0967_quota_billing.txt`](prompts/P0967_quota_billing.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0967-quota-billing) |

**Mission.** Accurate, transparent, disputable-free usage accounting.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **usage metering with billing-grade accuracy verification** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **quota enforcement with clear limit signalling** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **cost attribution by project, feature and request**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **reconciliation testing against independent accounting** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t20.quota.quota_billing@1`
- `cap.t20.quota.quota_billing.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.tenancy.tenancy_isolation@1` | use the in-file conservative substitute for `tenancy_isolation` (documented, slower, lower quality) and set `degraded['tenancy_isolation']='local'` |
| `cap.t01.capability.capability_gate@1` | use the in-file conservative substitute for `capability_gate` (documented, slower, lower quality) and set `degraded['capability_gate']='local'` |
| `cap.t08.parallel.parallel_generation@1` | use the in-file conservative substitute for `parallel_generation` (documented, slower, lower quality) and set `degraded['parallel_generation']='local'` |
| `cap.t09.latency.latency_regression_gate@1` | use the in-file conservative substitute for `latency_regression_gate` (documented, slower, lower quality) and set `degraded['latency_regression_gate']='local'` |
| `cap.t18.speed.speed_eval@1` | use the in-file conservative substitute for `speed_eval` (documented, slower, lower quality) and set `degraded['speed_eval']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - usage metering with billing-grade accuracy verification | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - quota enforcement with clear limit signalling | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - cost attribution by project, feature and request | 520 | Third required mechanism. |
| 6 | Core implementation D - reconciliation testing against independent accounting | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0967_quota_billing.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.quota.quota_billing@1`.
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

### P0968 · `pricing_engine` — Pricing Model & Cost Transparency

| field | value |
|---|---|
| part id | `P0968` (18/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0968_pricing_engine.ts` |
| module path | `hyperion.t20.platform.pricing_engine` |
| capability published | `cap.t20.pricing.pricing_engine@1` |
| determinism class | `io` |
| p99 latency budget | 31000 ns (31 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0968_pricing_engine.txt`](prompts/P0968_pricing_engine.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0968-pricing-engine) |

**Mission.** Users always know what something will cost before running it.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **pre-execution cost estimation with accuracy bounds** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **pricing-model implementation with cache and batch discounts**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **cost-optimisation recommendations for users** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **estimate-versus-actual accuracy measurement** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t20.pricing.pricing_engine@1`
- `cap.t20.pricing.pricing_engine.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.quota.quota_billing@1` | use the in-file conservative substitute for `quota_billing` (documented, slower, lower quality) and set `degraded['quota_billing']='local'` |
| `cap.t01.unit.unit_dimensions@1` | use the in-file conservative substitute for `unit_dimensions` (documented, slower, lower quality) and set `degraded['unit_dimensions']='local'` |
| `cap.t08.quantised.quantised_serving@1` | use the in-file conservative substitute for `quantised_serving` (documented, slower, lower quality) and set `degraded['quantised_serving']='local'` |
| `cap.t09.capacity.capacity_planner@1` | use the in-file conservative substitute for `capacity_planner` (documented, slower, lower quality) and set `degraded['capacity_planner']='local'` |
| `cap.t18.eval.eval_infrastructure@1` | use the in-file conservative substitute for `eval_infrastructure` (documented, slower, lower quality) and set `degraded['eval_infrastructure']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - pre-execution cost estimation with accuracy bounds | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - pricing-model implementation with cache and batch discounts | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - cost-optimisation recommendations for users | 520 | Third required mechanism. |
| 6 | Core implementation D - estimate-versus-actual accuracy measurement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0968_pricing_engine.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.pricing.pricing_engine@1`.
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

### P0969 · `rate_limits_public` — Public Rate Limiting & Fair Use

| field | value |
|---|---|
| part id | `P0969` (19/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0969_rate_limits_public.ts` |
| module path | `hyperion.t20.platform.rate_limits_public` |
| capability published | `cap.t20.rate.rate_limits_public@1` |
| determinism class | `io` |
| p99 latency budget | 32000 ns (32 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0969_rate_limits_public.txt`](prompts/P0969_rate_limits_public.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0969-rate-limits-public) |

**Mission.** Protects the system while treating customers fairly.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **tiered rate limits with burst allowance and clear headers**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **graceful limit responses with retry guidance** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **abuse detection distinguished from legitimate high usage** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **fairness measurement across customer sizes** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t20.rate.rate_limits_public@1`
- `cap.t20.rate.rate_limits_public.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.pricing.pricing_engine@1` | use the in-file conservative substitute for `pricing_engine` (documented, slower, lower quality) and set `degraded['pricing_engine']='local'` |
| `cap.t01.fs.fs_atomic@1` | use the in-file conservative substitute for `fs_atomic` (documented, slower, lower quality) and set `degraded['fs_atomic']='local'` |
| `cap.t08.prompt.prompt_compilation@1` | use the in-file conservative substitute for `prompt_compilation` (documented, slower, lower quality) and set `degraded['prompt_compilation']='local'` |
| `cap.t09.degradation.degradation_ladder@1` | use the in-file conservative substitute for `degradation_ladder` (documented, slower, lower quality) and set `degraded['degradation_ladder']='local'` |
| `cap.t18.safety.safety_eval_bridge@1` | use the in-file conservative substitute for `safety_eval_bridge` (documented, slower, lower quality) and set `degraded['safety_eval_bridge']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - tiered rate limits with burst allowance and clear headers | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - graceful limit responses with retry guidance | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - abuse detection distinguished from legitimate high usage | 520 | Third required mechanism. |
| 6 | Core implementation D - fairness measurement across customer sizes | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0969_rate_limits_public.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.rate.rate_limits_public@1`.
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

### P0970 · `deployment_pipeline` — Build, Test & Deployment Pipeline

| field | value |
|---|---|
| part id | `P0970` (20/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0970_deployment_pipeline.ts` |
| module path | `hyperion.t20.platform.deployment_pipeline` |
| capability published | `cap.t20.deployment.deployment_pipeline@1` |
| determinism class | `io` |
| p99 latency budget | 33000 ns (33 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0970_deployment_pipeline.txt`](prompts/P0970_deployment_pipeline.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0970-deployment-pipeline) |

**Mission.** 1000 parts to production, safely, repeatedly.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **hermetic reproducible build of the full assembly** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **staged pipeline with automated gates at every stage** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **artifact signing, provenance and promotion workflow** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured deployment frequency and change-failure rate**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t20.deployment.deployment_pipeline@1`
- `cap.t20.deployment.deployment_pipeline.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.rate.rate_limits_public@1` | use the in-file conservative substitute for `rate_limits_public` (documented, slower, lower quality) and set `degraded['rate_limits_public']='local'` |
| `cap.t01.cbor.cbor_canonical@1` | use the in-file conservative substitute for `cbor_canonical` (documented, slower, lower quality) and set `degraded['cbor_canonical']='local'` |
| `cap.t08.prefill.prefill_decode_split@1` | use the in-file conservative substitute for `prefill_decode_split` (documented, slower, lower quality) and set `degraded['prefill_decode_split']='local'` |
| `cap.t09.exact.exact_cache@1` | use the in-file conservative substitute for `exact_cache` (documented, slower, lower quality) and set `degraded['exact_cache']='local'` |
| `cap.t18.human.human_eval_protocol@1` | use the in-file conservative substitute for `human_eval_protocol` (documented, slower, lower quality) and set `degraded['human_eval_protocol']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - hermetic reproducible build of the full assembly | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - staged pipeline with automated gates at every stage | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - artifact signing, provenance and promotion workflow | 520 | Third required mechanism. |
| 6 | Core implementation D - measured deployment frequency and change-failure rate | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0970_deployment_pipeline.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.deployment.deployment_pipeline@1`.
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

### P0971 · `release_management` — Release Management & Versioning

| field | value |
|---|---|
| part id | `P0971` (21/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0971_release_management.ts` |
| module path | `hyperion.t20.platform.release_management` |
| capability published | `cap.t20.release.release_management@1` |
| determinism class | `io` |
| p99 latency budget | 34000 ns (34 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0971_release_management.txt`](prompts/P0971_release_management.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0971-release-management) |

**Mission.** Every release identified, documented and reversible.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **semantic versioning policy for the assembly and its API** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **release-note generation from part-level change data** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **rollback procedure with verified data compatibility**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured rollback success rate in drills** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t20.release.release_management@1`
- `cap.t20.release.release_management.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.deployment.deployment_pipeline@1` | use the in-file conservative substitute for `deployment_pipeline` (documented, slower, lower quality) and set `degraded['deployment_pipeline']='local'` |
| `cap.t01.clock.clock_time@1` | use the in-file conservative substitute for `clock_time` (documented, slower, lower quality) and set `degraded['clock_time']='local'` |
| `cap.t08.cascade.cascade_scheduler@1` | use the in-file conservative substitute for `cascade_scheduler` (documented, slower, lower quality) and set `degraded['cascade_scheduler']='local'` |
| `cap.t09.prefetch.prefetch_predictor@1` | use the in-file conservative substitute for `prefetch_predictor` (documented, slower, lower quality) and set `degraded['prefetch_predictor']='local'` |
| `cap.t18.swe.swe_pro_eval@1` | use the in-file conservative substitute for `swe_pro_eval` (documented, slower, lower quality) and set `degraded['swe_pro_eval']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - semantic versioning policy for the assembly and its API | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - release-note generation from part-level change data | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - rollback procedure with verified data compatibility | 520 | Third required mechanism. |
| 6 | Core implementation D - measured rollback success rate in drills | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0971_release_management.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.release.release_management@1`.
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

### P0972 · `canary_deployment` — Canary & Progressive Delivery

| field | value |
|---|---|
| part id | `P0972` (22/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0972_canary_deployment.ts` |
| module path | `hyperion.t20.platform.canary_deployment` |
| capability published | `cap.t20.canary.canary_deployment@1` |
| determinism class | `io` |
| p99 latency budget | 35000 ns (35 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0972_canary_deployment.txt`](prompts/P0972_canary_deployment.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0972-canary-deployment) |

**Mission.** Every change proves itself on a small slice first.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **traffic-splitting with cohort selection and guardrail metrics** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **automatic promotion and rollback decision logic**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **blast-radius limitation per stage** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured incident prevention from canary detection** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t20.canary.canary_deployment@1`
- `cap.t20.canary.canary_deployment.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.release.release_management@1` | use the in-file conservative substitute for `release_management` (documented, slower, lower quality) and set `degraded['release_management']='local'` |
| `cap.t01.bigint.bigint_modmath@1` | use the in-file conservative substitute for `bigint_modmath` (documented, slower, lower quality) and set `degraded['bigint_modmath']='local'` |
| `cap.t08.sampler.sampler_engine@1` | use the in-file conservative substitute for `sampler_engine` (documented, slower, lower quality) and set `degraded['sampler_engine']='local'` |
| `cap.t09.gc.gc_pause_control@1` | use the in-file conservative substitute for `gc_pause_control` (documented, slower, lower quality) and set `degraded['gc_pause_control']='local'` |
| `cap.t18.osworld.osworld_eval@1` | use the in-file conservative substitute for `osworld_eval` (documented, slower, lower quality) and set `degraded['osworld_eval']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - traffic-splitting with cohort selection and guardrail metrics | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - automatic promotion and rollback decision logic | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - blast-radius limitation per stage | 520 | Third required mechanism. |
| 6 | Core implementation D - measured incident prevention from canary detection | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0972_canary_deployment.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.canary.canary_deployment@1`.
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

### P0973 · `feature_flags_platform` — Feature Flag & Experiment Platform

| field | value |
|---|---|
| part id | `P0973` (23/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0973_feature_flags_platform.ts` |
| module path | `hyperion.t20.platform.feature_flags_platform` |
| capability published | `cap.t20.feature.feature_flags_platform@1` |
| determinism class | `io` |
| p99 latency budget | 36000 ns (36 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0973_feature_flags_platform.txt`](prompts/P0973_feature_flags_platform.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0973-feature-flags-platform) |

**Mission.** Ship code continuously, enable behaviour deliberately.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **flag lifecycle with owner, expiry and kill-switch requirements**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **experiment assignment with correct randomisation and analysis** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **flag-state consistency across a distributed fleet** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **flag-debt monitoring and cleanup enforcement** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t20.feature.feature_flags_platform@1`
- `cap.t20.feature.feature_flags_platform.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.canary.canary_deployment@1` | use the in-file conservative substitute for `canary_deployment` (documented, slower, lower quality) and set `degraded['canary_deployment']='local'` |
| `cap.t01.logging.logging_events@1` | use the in-file conservative substitute for `logging_events` (documented, slower, lower quality) and set `degraded['logging_events']='local'` |
| `cap.t08.model.model_loading@1` | use the in-file conservative substitute for `model_loading` (documented, slower, lower quality) and set `degraded['model_loading']='local'` |
| `cap.t09.speculative.speculative_ui@1` | use the in-file conservative substitute for `speculative_ui` (documented, slower, lower quality) and set `degraded['speculative_ui']='local'` |
| `cap.t18.instruction.instruction_following_eval@1` | use the in-file conservative substitute for `instruction_following_eval` (documented, slower, lower quality) and set `degraded['instruction_following_eval']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - flag lifecycle with owner, expiry and kill-switch requirements | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - experiment assignment with correct randomisation and analysis | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - flag-state consistency across a distributed fleet | 520 | Third required mechanism. |
| 6 | Core implementation D - flag-debt monitoring and cleanup enforcement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0973_feature_flags_platform.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.feature.feature_flags_platform@1`.
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

### P0974 · `config_management_platform` — Fleet Configuration Management

| field | value |
|---|---|
| part id | `P0974` (24/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0974_config_management_platform.ts` |
| module path | `hyperion.t20.platform.config_management_platform` |
| capability published | `cap.t20.config.config_management_platform@1` |
| determinism class | `io` |
| p99 latency budget | 37000 ns (37 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0974_config_management_platform.txt`](prompts/P0974_config_management_platform.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0974-config-management-platform) |

**Mission.** One coherent configuration across thousands of machines.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **versioned configuration with staged rollout and validation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **drift detection and reconciliation across the fleet** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **emergency-override path with audit requirements** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured configuration-convergence time**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t20.config.config_management_platform@1`
- `cap.t20.config.config_management_platform.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.feature.feature_flags_platform@1` | use the in-file conservative substitute for `feature_flags_platform` (documented, slower, lower quality) and set `degraded['feature_flags_platform']='local'` |
| `cap.t01.checksum.checksum_verify@1` | use the in-file conservative substitute for `checksum_verify` (documented, slower, lower quality) and set `degraded['checksum_verify']='local'` |
| `cap.t08.speculative.speculative_tools@1` | use the in-file conservative substitute for `speculative_tools` (documented, slower, lower quality) and set `degraded['speculative_tools']='local'` |
| `cap.t09.slo.slo_manager@1` | use the in-file conservative substitute for `slo_manager` (documented, slower, lower quality) and set `degraded['slo_manager']='local'` |
| `cap.t18.efficiency.efficiency_eval@1` | use the in-file conservative substitute for `efficiency_eval` (documented, slower, lower quality) and set `degraded['efficiency_eval']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - versioned configuration with staged rollout and validation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - drift detection and reconciliation across the fleet | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - emergency-override path with audit requirements | 520 | Third required mechanism. |
| 6 | Core implementation D - measured configuration-convergence time | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0974_config_management_platform.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.config.config_management_platform@1`.
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

### P0975 · `observability_platform` — Observability Platform: Metrics, Traces, Logs

| field | value |
|---|---|
| part id | `P0975` (25/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0975_observability_platform.ts` |
| module path | `hyperion.t20.platform.observability_platform` |
| capability published | `cap.t20.observability.observability_platform@1` |
| determinism class | `io` |
| p99 latency budget | 38000 ns (38 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0975_observability_platform.txt`](prompts/P0975_observability_platform.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0975-observability-platform) |

**Mission.** Full visibility into a 1000-part distributed system.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **unified telemetry pipeline with cardinality and cost control** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **cross-part trace stitching with capability-level spans** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **query interface for incident investigation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured telemetry cost per request and its reduction** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t20.observability.observability_platform@1`
- `cap.t20.observability.observability_platform.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.config.config_management_platform@1` | use the in-file conservative substitute for `config_management_platform` (documented, slower, lower quality) and set `degraded['config_management_platform']='local'` |
| `cap.t01.numeric.numeric_limits@1` | use the in-file conservative substitute for `numeric_limits` (documented, slower, lower quality) and set `degraded['numeric_limits']='local'` |
| `cap.t08.kv.kv_offload_runtime@1` | use the in-file conservative substitute for `kv_offload_runtime` (documented, slower, lower quality) and set `degraded['kv_offload_runtime']='local'` |
| `cap.t09.cost.cost_optimiser@1` | use the in-file conservative substitute for `cost_optimiser` (documented, slower, lower quality) and set `degraded['cost_optimiser']='local'` |
| `cap.t18.eval.eval_cost_control@1` | use the in-file conservative substitute for `eval_cost_control` (documented, slower, lower quality) and set `degraded['eval_cost_control']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - unified telemetry pipeline with cardinality and cost control | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - cross-part trace stitching with capability-level spans | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - query interface for incident investigation | 520 | Third required mechanism. |
| 6 | Core implementation D - measured telemetry cost per request and its reduction | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0975_observability_platform.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.observability.observability_platform@1`.
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

### P0976 · `alerting_oncall` — Alerting, Escalation & On-Call Operations

| field | value |
|---|---|
| part id | `P0976` (26/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0976_alerting_oncall.ts` |
| module path | `hyperion.t20.platform.alerting_oncall` |
| capability published | `cap.t20.alerting.alerting_oncall@1` |
| determinism class | `io` |
| p99 latency budget | 39000 ns (39 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0976_alerting_oncall.txt`](prompts/P0976_alerting_oncall.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0976-alerting-oncall) |

**Mission.** Humans learn about problems before customers do.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **symptom-based alerting with actionable runbook links** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **alert-quality management (precision, actionability, fatigue reduction)**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **escalation policy and paging integration** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured alert precision and mean-time-to-acknowledge** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t20.alerting.alerting_oncall@1`
- `cap.t20.alerting.alerting_oncall.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.observability.observability_platform@1` | use the in-file conservative substitute for `observability_platform` (documented, slower, lower quality) and set `degraded['observability_platform']='local'` |
| `cap.t01.sandbox.sandbox_policy@1` | use the in-file conservative substitute for `sandbox_policy` (documented, slower, lower quality) and set `degraded['sandbox_policy']='local'` |
| `cap.t08.tokenizer.tokenizer_runtime@1` | use the in-file conservative substitute for `tokenizer_runtime` (documented, slower, lower quality) and set `degraded['tokenizer_runtime']='local'` |
| `cap.t09.burst.burst_handling@1` | use the in-file conservative substitute for `burst_handling` (documented, slower, lower quality) and set `degraded['burst_handling']='local'` |
| `cap.t18.eval.eval_meta@1` | use the in-file conservative substitute for `eval_meta` (documented, slower, lower quality) and set `degraded['eval_meta']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - symptom-based alerting with actionable runbook links | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - alert-quality management (precision, actionability, fatigue redu | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - escalation policy and paging integration | 520 | Third required mechanism. |
| 6 | Core implementation D - measured alert precision and mean-time-to-acknowledge | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0976_alerting_oncall.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.alerting.alerting_oncall@1`.
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

### P0977 · `incident_management` — Incident Management & Postmortem Process

| field | value |
|---|---|
| part id | `P0977` (27/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0977_incident_management.ts` |
| module path | `hyperion.t20.platform.incident_management` |
| capability published | `cap.t20.incident.incident_management@1` |
| determinism class | `io` |
| p99 latency budget | 40000 ns (40 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0977_incident_management.txt`](prompts/P0977_incident_management.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0977-incident-management) |

**Mission.** Every outage makes the system stronger.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **incident lifecycle with severity, roles and communication templates**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **timeline reconstruction from telemetry and audit logs** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **blameless postmortem with tracked action items** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured recurrence rate of postmortem-covered causes** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t20.incident.incident_management@1`
- `cap.t20.incident.incident_management.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.alerting.alerting_oncall@1` | use the in-file conservative substitute for `alerting_oncall` (documented, slower, lower quality) and set `degraded['alerting_oncall']='local'` |
| `cap.t01.abi.abi_result@1` | use the in-file conservative substitute for `abi_result` (documented, slower, lower quality) and set `degraded['abi_result']='local'` |
| `cap.t08.chunked.chunked_prefill@1` | use the in-file conservative substitute for `chunked_prefill` (documented, slower, lower quality) and set `degraded['chunked_prefill']='local'` |
| `cap.t09.memoize.memoize_core@1` | use the in-file conservative substitute for `memoize_core` (documented, slower, lower quality) and set `degraded['memoize_core']='local'` |
| `cap.t18.grading.grading_engine@1` | use the in-file conservative substitute for `grading_engine` (documented, slower, lower quality) and set `degraded['grading_engine']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - incident lifecycle with severity, roles and communication templa | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - timeline reconstruction from telemetry and audit logs | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - blameless postmortem with tracked action items | 520 | Third required mechanism. |
| 6 | Core implementation D - measured recurrence rate of postmortem-covered causes | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0977_incident_management.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.incident.incident_management@1`.
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

### P0978 · `runbook_automation` — Runbook Automation & Self-Healing

| field | value |
|---|---|
| part id | `P0978` (28/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0978_runbook_automation.ts` |
| module path | `hyperion.t20.platform.runbook_automation` |
| capability published | `cap.t20.runbook.runbook_automation@1` |
| determinism class | `io` |
| p99 latency budget | 41000 ns (41 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0978_runbook_automation.txt`](prompts/P0978_runbook_automation.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0978-runbook-automation) |

**Mission.** The system fixes its own routine problems.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **automated remediation for known failure signatures** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **safety guards preventing automation from worsening incidents** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **human-approval requirements for risky remediations** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured fraction of incidents auto-remediated**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t20.runbook.runbook_automation@1`
- `cap.t20.runbook.runbook_automation.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.incident.incident_management@1` | use the in-file conservative substitute for `incident_management` (documented, slower, lower quality) and set `degraded['incident_management']='local'` |
| `cap.t01.trace.trace_context@1` | use the in-file conservative substitute for `trace_context` (documented, slower, lower quality) and set `degraded['trace_context']='local'` |
| `cap.t08.cascade.cascade_acceptance@1` | use the in-file conservative substitute for `cascade_acceptance` (documented, slower, lower quality) and set `degraded['cascade_acceptance']='local'` |
| `cap.t09.precompute.precompute_engine@1` | use the in-file conservative substitute for `precompute_engine` (documented, slower, lower quality) and set `degraded['precompute_engine']='local'` |
| `cap.t18.swe.swe_verified_eval@1` | use the in-file conservative substitute for `swe_verified_eval` (documented, slower, lower quality) and set `degraded['swe_verified_eval']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - automated remediation for known failure signatures | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - safety guards preventing automation from worsening incidents | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - human-approval requirements for risky remediations | 520 | Third required mechanism. |
| 6 | Core implementation D - measured fraction of incidents auto-remediated | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0978_runbook_automation.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.runbook.runbook_automation@1`.
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

### P0979 · `chaos_engineering` — Chaos Engineering & Resilience Verification

| field | value |
|---|---|
| part id | `P0979` (29/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0979_chaos_engineering.ts` |
| module path | `hyperion.t20.platform.chaos_engineering` |
| capability published | `cap.t20.chaos.chaos_engineering@1` |
| determinism class | `io` |
| p99 latency budget | 42000 ns (42 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0979_chaos_engineering.txt`](prompts/P0979_chaos_engineering.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0979-chaos-engineering) |

**Mission.** Breaks itself on purpose, in production, safely.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **fault-injection experiment framework with blast-radius controls** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **hypothesis-driven experiment design and result analysis** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **experiment catalogue covering every dependency and failure mode**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured resilience improvement from findings** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t20.chaos.chaos_engineering@1`
- `cap.t20.chaos.chaos_engineering.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.runbook.runbook_automation@1` | use the in-file conservative substitute for `runbook_automation` (documented, slower, lower quality) and set `degraded['runbook_automation']='local'` |
| `cap.t01.fixed.fixed_point@1` | use the in-file conservative substitute for `fixed_point` (documented, slower, lower quality) and set `degraded['fixed_point']='local'` |
| `cap.t08.session.session_affinity@1` | use the in-file conservative substitute for `session_affinity` (documented, slower, lower quality) and set `degraded['session_affinity']='local'` |
| `cap.t09.warmup.warmup_manager@1` | use the in-file conservative substitute for `warmup_manager` (documented, slower, lower quality) and set `degraded['warmup_manager']='local'` |
| `cap.t18.mmmu.mmmu_eval@1` | use the in-file conservative substitute for `mmmu_eval` (documented, slower, lower quality) and set `degraded['mmmu_eval']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - fault-injection experiment framework with blast-radius controls | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - hypothesis-driven experiment design and result analysis | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - experiment catalogue covering every dependency and failure mode | 520 | Third required mechanism. |
| 6 | Core implementation D - measured resilience improvement from findings | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0979_chaos_engineering.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.chaos.chaos_engineering@1`.
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

### P0980 · `disaster_recovery` — Disaster Recovery & Business Continuity

| field | value |
|---|---|
| part id | `P0980` (30/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0980_disaster_recovery.ts` |
| module path | `hyperion.t20.platform.disaster_recovery` |
| capability published | `cap.t20.disaster.disaster_recovery@1` |
| determinism class | `io` |
| p99 latency budget | 43000 ns (43 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0980_disaster_recovery.txt`](prompts/P0980_disaster_recovery.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0980-disaster-recovery) |

**Mission.** Survives losing a region, with proven recovery times.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **recovery objective definitions per system component** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **backup, replication and restore procedures with integrity verification**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **regular recovery drills with measured RTO and RPO** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **drill-result documentation and gap remediation** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t20.disaster.disaster_recovery@1`
- `cap.t20.disaster.disaster_recovery.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.chaos.chaos_engineering@1` | use the in-file conservative substitute for `chaos_engineering` (documented, slower, lower quality) and set `degraded['chaos_engineering']='local'` |
| `cap.t01.config.config_system@1` | use the in-file conservative substitute for `config_system` (documented, slower, lower quality) and set `degraded['config_system']='local'` |
| `cap.t08.multi.multi_gpu_runtime@1` | use the in-file conservative substitute for `multi_gpu_runtime` (documented, slower, lower quality) and set `degraded['multi_gpu_runtime']='local'` |
| `cap.t09.priority.priority_lanes@1` | use the in-file conservative substitute for `priority_lanes` (documented, slower, lower quality) and set `degraded['priority_lanes']='local'` |
| `cap.t18.longcontext.longcontext_eval@1` | use the in-file conservative substitute for `longcontext_eval` (documented, slower, lower quality) and set `degraded['longcontext_eval']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - recovery objective definitions per system component | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - backup, replication and restore procedures with integrity verifi | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - regular recovery drills with measured RTO and RPO | 520 | Third required mechanism. |
| 6 | Core implementation D - drill-result documentation and gap remediation | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0980_disaster_recovery.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.disaster.disaster_recovery@1`.
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

### P0981 · `capacity_operations` — Capacity Operations & Demand Management

| field | value |
|---|---|
| part id | `P0981` (31/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0981_capacity_operations.ts` |
| module path | `hyperion.t20.platform.capacity_operations` |
| capability published | `cap.t20.capacity.capacity_operations@1` |
| determinism class | `io` |
| p99 latency budget | 44000 ns (44 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0981_capacity_operations.txt`](prompts/P0981_capacity_operations.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0981-capacity-operations) |

**Mission.** Never runs out, never wastes.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **demand forecasting with uncertainty and lead-time awareness**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **procurement and allocation planning across hardware generations** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **utilisation and headroom monitoring with automated recommendations** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured forecast accuracy and utilisation improvement** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t20.capacity.capacity_operations@1`
- `cap.t20.capacity.capacity_operations.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.disaster.disaster_recovery@1` | use the in-file conservative substitute for `disaster_recovery` (documented, slower, lower quality) and set `degraded['disaster_recovery']='local'` |
| `cap.t01.determinism.determinism_replay@1` | use the in-file conservative substitute for `determinism_replay` (documented, slower, lower quality) and set `degraded['determinism_replay']='local'` |
| `cap.t08.deadline.deadline_scheduling@1` | use the in-file conservative substitute for `deadline_scheduling` (documented, slower, lower quality) and set `degraded['deadline_scheduling']='local'` |
| `cap.t09.adaptive.adaptive_quality@1` | use the in-file conservative substitute for `adaptive_quality` (documented, slower, lower quality) and set `degraded['adaptive_quality']='local'` |
| `cap.t18.multilingual.multilingual_eval@1` | use the in-file conservative substitute for `multilingual_eval` (documented, slower, lower quality) and set `degraded['multilingual_eval']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - demand forecasting with uncertainty and lead-time awareness | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - procurement and allocation planning across hardware generations | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - utilisation and headroom monitoring with automated recommendatio | 520 | Third required mechanism. |
| 6 | Core implementation D - measured forecast accuracy and utilisation improvement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0981_capacity_operations.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.capacity.capacity_operations@1`.
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

### P0982 · `cost_operations` — Cost Operations & Efficiency Programme

| field | value |
|---|---|
| part id | `P0982` (32/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0982_cost_operations.ts` |
| module path | `hyperion.t20.platform.cost_operations` |
| capability published | `cap.t20.cost.cost_operations@1` |
| determinism class | `io` |
| p99 latency budget | 45000 ns (45 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0982_cost_operations.txt`](prompts/P0982_cost_operations.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0982-cost-operations) |

**Mission.** Continuous, measured cost reduction.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **cost attribution across parts, features and customers** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **efficiency-opportunity identification with projected savings** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **savings verification after implementation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured cost-per-request trend**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t20.cost.cost_operations@1`
- `cap.t20.cost.cost_operations.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.capacity.capacity_operations@1` | use the in-file conservative substitute for `capacity_operations` (documented, slower, lower quality) and set `degraded['capacity_operations']='local'` |
| `cap.t01.compat.compat_shims@1` | use the in-file conservative substitute for `compat_shims` (documented, slower, lower quality) and set `degraded['compat_shims']='local'` |
| `cap.t08.engine.engine_determinism@1` | use the in-file conservative substitute for `engine_determinism` (documented, slower, lower quality) and set `degraded['engine_determinism']='local'` |
| `cap.t09.energy.energy_efficiency@1` | use the in-file conservative substitute for `energy_efficiency` (documented, slower, lower quality) and set `degraded['energy_efficiency']='local'` |
| `cap.t18.competitor.competitor_tracking@1` | use the in-file conservative substitute for `competitor_tracking` (documented, slower, lower quality) and set `degraded['competitor_tracking']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - cost attribution across parts, features and customers | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - efficiency-opportunity identification with projected savings | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - savings verification after implementation | 520 | Third required mechanism. |
| 6 | Core implementation D - measured cost-per-request trend | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0982_cost_operations.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.cost.cost_operations@1`.
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

### P0983 · `edge_deployment` — Edge & Regional Deployment

| field | value |
|---|---|
| part id | `P0983` (33/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0983_edge_deployment.ts` |
| module path | `hyperion.t20.platform.edge_deployment` |
| capability published | `cap.t20.edge.edge_deployment@1` |
| determinism class | `io` |
| p99 latency budget | 46000 ns (46 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0983_edge_deployment.txt`](prompts/P0983_edge_deployment.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0983-edge-deployment) |

**Mission.** Low latency and data residency worldwide.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **regional deployment topology with data-residency enforcement** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **edge caching and request-routing policy** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **per-region capability and compliance differences handling**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured latency improvement per region** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t20.edge.edge_deployment@1`
- `cap.t20.edge.edge_deployment.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.cost.cost_operations@1` | use the in-file conservative substitute for `cost_operations` (documented, slower, lower quality) and set `degraded['cost_operations']='local'` |
| `cap.t01.secure.secure_zeroize@1` | use the in-file conservative substitute for `secure_zeroize` (documented, slower, lower quality) and set `degraded['secure_zeroize']='local'` |
| `cap.t08.engine.engine_config_tuning@1` | use the in-file conservative substitute for `engine_config_tuning` (documented, slower, lower quality) and set `degraded['engine_config_tuning']='local'` |
| `cap.t09.realtime.realtime_mode@1` | use the in-file conservative substitute for `realtime_mode` (documented, slower, lower quality) and set `degraded['realtime_mode']='local'` |
| `cap.t18.eval.eval_dashboard@1` | use the in-file conservative substitute for `eval_dashboard` (documented, slower, lower quality) and set `degraded['eval_dashboard']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - regional deployment topology with data-residency enforcement | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - edge caching and request-routing policy | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - per-region capability and compliance differences handling | 520 | Third required mechanism. |
| 6 | Core implementation D - measured latency improvement per region | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0983_edge_deployment.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.edge.edge_deployment@1`.
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

### P0984 · `on_prem_deployment` — Self-Hosted & Air-Gapped Deployment

| field | value |
|---|---|
| part id | `P0984` (34/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0984_on_prem_deployment.ts` |
| module path | `hyperion.t20.platform.on_prem_deployment` |
| capability published | `cap.t20.on.on_prem_deployment@1` |
| determinism class | `io` |
| p99 latency budget | 47000 ns (47 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0984_on_prem_deployment.txt`](prompts/P0984_on_prem_deployment.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0984-on-prem-deployment) |

**Mission.** Runs inside customer environments, fully disconnected.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **deployment packaging with dependency vendoring** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **air-gapped licensing, updating and telemetry-free operation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **hardware-requirement specification and validation tooling** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **installation success rate across target environments** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t20.on.on_prem_deployment@1`
- `cap.t20.on.on_prem_deployment.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.edge.edge_deployment@1` | use the in-file conservative substitute for `edge_deployment` (documented, slower, lower quality) and set `degraded['edge_deployment']='local'` |
| `cap.t08.continuous.continuous_batching@1` | use the in-file conservative substitute for `continuous_batching` (documented, slower, lower quality) and set `degraded['continuous_batching']='local'` |
| `cap.t09.speed.speed_law_model@1` | use the in-file conservative substitute for `speed_law_model` (documented, slower, lower quality) and set `degraded['speed_law_model']='local'` |
| `cap.t18.eval.eval_registry@1` | use the in-file conservative substitute for `eval_registry` (documented, slower, lower quality) and set `degraded['eval_registry']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - deployment packaging with dependency vendoring | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - air-gapped licensing, updating and telemetry-free operation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - hardware-requirement specification and validation tooling | 520 | Third required mechanism. |
| 6 | Core implementation D - installation success rate across target environments | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0984_on_prem_deployment.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.on.on_prem_deployment@1`.
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

### P0985 · `container_orchestration` — Container & Orchestration Integration

| field | value |
|---|---|
| part id | `P0985` (35/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0985_container_orchestration.ts` |
| module path | `hyperion.t20.platform.container_orchestration` |
| capability published | `cap.t20.container.container_orchestration@1` |
| determinism class | `io` |
| p99 latency budget | 48000 ns (48 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0985_container_orchestration.txt`](prompts/P0985_container_orchestration.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0985-container-orchestration) |

**Mission.** Native operation in modern infrastructure.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **container images with minimal surface and reproducible builds**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **orchestrator manifests with correct probes, limits and topology hints** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **graceful startup, drain and termination behaviour** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **verified operation across major orchestration platforms** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t20.container.container_orchestration@1`
- `cap.t20.container.container_orchestration.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.on.on_prem_deployment@1` | use the in-file conservative substitute for `on_prem_deployment` (documented, slower, lower quality) and set `degraded['on_prem_deployment']='local'` |
| `cap.t01.envelope.envelope_codec@1` | use the in-file conservative substitute for `envelope_codec` (documented, slower, lower quality) and set `degraded['envelope_codec']='local'` |
| `cap.t08.cascade.cascade_tree_verify@1` | use the in-file conservative substitute for `cascade_tree_verify` (documented, slower, lower quality) and set `degraded['cascade_tree_verify']='local'` |
| `cap.t09.distill.distill_fast_paths@1` | use the in-file conservative substitute for `distill_fast_paths` (documented, slower, lower quality) and set `degraded['distill_fast_paths']='local'` |
| `cap.t18.contamination.contamination_audit@1` | use the in-file conservative substitute for `contamination_audit` (documented, slower, lower quality) and set `degraded['contamination_audit']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - container images with minimal surface and reproducible builds | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - orchestrator manifests with correct probes, limits and topology  | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - graceful startup, drain and termination behaviour | 520 | Third required mechanism. |
| 6 | Core implementation D - verified operation across major orchestration platforms | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0985_container_orchestration.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.container.container_orchestration@1`.
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

### P0986 · `infrastructure_as_code` — Infrastructure as Code & Environment Definition

| field | value |
|---|---|
| part id | `P0986` (36/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0986_infrastructure_as_code.ts` |
| module path | `hyperion.t20.platform.infrastructure_as_code` |
| capability published | `cap.t20.infrastructure.infrastructure_as_code@1` |
| determinism class | `io` |
| p99 latency budget | 49000 ns (49 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0986_infrastructure_as_code.txt`](prompts/P0986_infrastructure_as_code.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0986-infrastructure-as-code) |

**Mission.** Every environment reproducible from source.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **declarative infrastructure definitions for all environments** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **drift detection between declared and actual infrastructure** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **environment parity verification (dev, staging, production)** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured environment-provisioning time and reliability**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t20.infrastructure.infrastructure_as_code@1`
- `cap.t20.infrastructure.infrastructure_as_code.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.container.container_orchestration@1` | use the in-file conservative substitute for `container_orchestration` (documented, slower, lower quality) and set `degraded['container_orchestration']='local'` |
| `cap.t01.dataflow.dataflow_dag@1` | use the in-file conservative substitute for `dataflow_dag` (documented, slower, lower quality) and set `degraded['dataflow_dag']='local'` |
| `cap.t08.prefix.prefix_cache_runtime@1` | use the in-file conservative substitute for `prefix_cache_runtime` (documented, slower, lower quality) and set `degraded['prefix_cache_runtime']='local'` |
| `cap.t09.jitter.jitter_control@1` | use the in-file conservative substitute for `jitter_control` (documented, slower, lower quality) and set `degraded['jitter_control']='local'` |
| `cap.t18.math.math_eval@1` | use the in-file conservative substitute for `math_eval` (documented, slower, lower quality) and set `degraded['math_eval']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - declarative infrastructure definitions for all environments | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - drift detection between declared and actual infrastructure | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - environment parity verification (dev, staging, production) | 520 | Third required mechanism. |
| 6 | Core implementation D - measured environment-provisioning time and reliability | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0986_infrastructure_as_code.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.infrastructure.infrastructure_as_code@1`.
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

### P0987 · `secrets_management` — Secrets Management & Key Rotation

| field | value |
|---|---|
| part id | `P0987` (37/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0987_secrets_management.ts` |
| module path | `hyperion.t20.platform.secrets_management` |
| capability published | `cap.t20.secrets.secrets_management@1` |
| determinism class | `io` |
| p99 latency budget | 3000 ns (3 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0987_secrets_management.txt`](prompts/P0987_secrets_management.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0987-secrets-management) |

**Mission.** Operational secret hygiene, enforced.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **central secret storage with scoped access and audit** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **automatic rotation without service interruption** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **secret-scanning in code, configs, logs and model outputs**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **verified zero-secret-exposure across all channels** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t20.secrets.secrets_management@1`
- `cap.t20.secrets.secrets_management.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.infrastructure.infrastructure_as_code@1` | use the in-file conservative substitute for `infrastructure_as_code` (documented, slower, lower quality) and set `degraded['infrastructure_as_code']='local'` |
| `cap.t01.serialization.serialization_schema@1` | use the in-file conservative substitute for `serialization_schema` (documented, slower, lower quality) and set `degraded['serialization_schema']='local'` |
| `cap.t08.batch.batch_invariance@1` | use the in-file conservative substitute for `batch_invariance` (documented, slower, lower quality) and set `degraded['batch_invariance']='local'` |
| `cap.t09.batch.batch_latency_tradeoff@1` | use the in-file conservative substitute for `batch_latency_tradeoff` (documented, slower, lower quality) and set `degraded['batch_latency_tradeoff']='local'` |
| `cap.t18.security.security_eval@1` | use the in-file conservative substitute for `security_eval` (documented, slower, lower quality) and set `degraded['security_eval']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - central secret storage with scoped access and audit | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - automatic rotation without service interruption | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - secret-scanning in code, configs, logs and model outputs | 520 | Third required mechanism. |
| 6 | Core implementation D - verified zero-secret-exposure across all channels | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0987_secrets_management.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.secrets.secrets_management@1`.
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

### P0988 · `compliance_platform` — Compliance & Certification Support

| field | value |
|---|---|
| part id | `P0988` (38/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0988_compliance_platform.ts` |
| module path | `hyperion.t20.platform.compliance_platform` |
| capability published | `cap.t20.compliance.compliance_platform@1` |
| determinism class | `io` |
| p99 latency budget | 4000 ns (4 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0988_compliance_platform.txt`](prompts/P0988_compliance_platform.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0988-compliance-platform) |

**Mission.** Meets the standards enterprises require.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **control mapping to major frameworks with evidence collection** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **continuous control monitoring and exception tracking**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **audit-evidence package generation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **certification-readiness assessment reporting** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t20.compliance.compliance_platform@1`
- `cap.t20.compliance.compliance_platform.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.secrets.secrets_management@1` | use the in-file conservative substitute for `secrets_management` (documented, slower, lower quality) and set `degraded['secrets_management']='local'` |
| `cap.t01.bench.bench_harness@1` | use the in-file conservative substitute for `bench_harness` (documented, slower, lower quality) and set `degraded['bench_harness']='local'` |
| `cap.t08.cancellation.cancellation@1` | use the in-file conservative substitute for `cancellation` (documented, slower, lower quality) and set `degraded['cancellation']='local'` |
| `cap.t09.io.io_scheduling@1` | use the in-file conservative substitute for `io_scheduling` (documented, slower, lower quality) and set `degraded['io_scheduling']='local'` |
| `cap.t18.bias.bias_fairness_eval@1` | use the in-file conservative substitute for `bias_fairness_eval` (documented, slower, lower quality) and set `degraded['bias_fairness_eval']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - control mapping to major frameworks with evidence collection | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - continuous control monitoring and exception tracking | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - audit-evidence package generation | 520 | Third required mechanism. |
| 6 | Core implementation D - certification-readiness assessment reporting | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0988_compliance_platform.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.compliance.compliance_platform@1`.
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

### P0989 · `data_residency` — Data Residency & Sovereignty Controls

| field | value |
|---|---|
| part id | `P0989` (39/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0989_data_residency.ts` |
| module path | `hyperion.t20.platform.data_residency` |
| capability published | `cap.t20.data.data_residency@1` |
| determinism class | `io` |
| p99 latency budget | 5000 ns (5 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0989_data_residency.txt`](prompts/P0989_data_residency.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0989-data-residency) |

**Mission.** Data stays where it is legally required to stay.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **per-request and per-tenant residency policy enforcement**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **cross-border transfer prevention with verification** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **regional key management and processing isolation** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **residency-compliance verification testing** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t20.data.data_residency@1`
- `cap.t20.data.data_residency.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.compliance.compliance_platform@1` | use the in-file conservative substitute for `compliance_platform` (documented, slower, lower quality) and set `degraded['compliance_platform']='local'` |
| `cap.t01.abi.abi_stability@1` | use the in-file conservative substitute for `abi_stability` (documented, slower, lower quality) and set `degraded['abi_stability']='local'` |
| `cap.t08.overload.overload_shedding@1` | use the in-file conservative substitute for `overload_shedding` (documented, slower, lower quality) and set `degraded['overload_shedding']='local'` |
| `cap.t09.throughput.throughput_optimiser@1` | use the in-file conservative substitute for `throughput_optimiser` (documented, slower, lower quality) and set `degraded['throughput_optimiser']='local'` |
| `cap.t18.capability.capability_map@1` | use the in-file conservative substitute for `capability_map` (documented, slower, lower quality) and set `degraded['capability_map']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - per-request and per-tenant residency policy enforcement | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - cross-border transfer prevention with verification | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - regional key management and processing isolation | 520 | Third required mechanism. |
| 6 | Core implementation D - residency-compliance verification testing | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0989_data_residency.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.data.data_residency@1`.
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

### P0990 · `customer_support_tooling` — Support Tooling & Diagnostics

| field | value |
|---|---|
| part id | `P0990` (40/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0990_customer_support_tooling.ts` |
| module path | `hyperion.t20.platform.customer_support_tooling` |
| capability published | `cap.t20.customer.customer_support_tooling@1` |
| determinism class | `io` |
| p99 latency budget | 6000 ns (6 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0990_customer_support_tooling.txt`](prompts/P0990_customer_support_tooling.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0990-customer-support-tooling) |

**Mission.** Support can answer 'what happened to my request' precisely.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **request-lookup tooling with privacy-preserving access controls** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **diagnostic bundle generation for customer issues** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **known-issue matching and resolution suggestion** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured first-contact resolution rate**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t20.customer.customer_support_tooling@1`
- `cap.t20.customer.customer_support_tooling.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.data.data_residency@1` | use the in-file conservative substitute for `data_residency` (documented, slower, lower quality) and set `degraded['data_residency']='local'` |
| `cap.t01.retry.retry_idempotency@1` | use the in-file conservative substitute for `retry_idempotency` (documented, slower, lower quality) and set `degraded['retry_idempotency']='local'` |
| `cap.t08.cascade.cascade_speed_proof@1` | use the in-file conservative substitute for `cascade_speed_proof` (documented, slower, lower quality) and set `degraded['cascade_speed_proof']='local'` |
| `cap.t09.benchmark.benchmark_speed_public@1` | use the in-file conservative substitute for `benchmark_speed_public` (documented, slower, lower quality) and set `degraded['benchmark_speed_public']='local'` |
| `cap.t18.dominance.dominance_proof@1` | use the in-file conservative substitute for `dominance_proof` (documented, slower, lower quality) and set `degraded['dominance_proof']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - request-lookup tooling with privacy-preserving access controls | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - diagnostic bundle generation for customer issues | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - known-issue matching and resolution suggestion | 520 | Third required mechanism. |
| 6 | Core implementation D - measured first-contact resolution rate | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0990_customer_support_tooling.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.customer.customer_support_tooling@1`.
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

### P0991 · `documentation_platform` — Documentation Platform & Content

| field | value |
|---|---|
| part id | `P0991` (41/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0991_documentation_platform.ts` |
| module path | `hyperion.t20.platform.documentation_platform` |
| capability published | `cap.t20.documentation.documentation_platform@1` |
| determinism class | `io` |
| p99 latency budget | 7000 ns (7 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0991_documentation_platform.txt`](prompts/P0991_documentation_platform.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0991-documentation-platform) |

**Mission.** Documentation that makes the system usable.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **API reference generation from specifications with example verification** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **conceptual guides, tutorials and cookbook content** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **documentation testing (every example executes correctly)**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured developer time-to-first-success** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t20.documentation.documentation_platform@1`
- `cap.t20.documentation.documentation_platform.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.customer.customer_support_tooling@1` | use the in-file conservative substitute for `customer_support_tooling` (documented, slower, lower quality) and set `degraded['customer_support_tooling']='local'` |
| `cap.t08.engine.engine_core@1` | use the in-file conservative substitute for `engine_core` (documented, slower, lower quality) and set `degraded['engine_core']='local'` |
| `cap.t09.latency.latency_accounting@1` | use the in-file conservative substitute for `latency_accounting` (documented, slower, lower quality) and set `degraded['latency_accounting']='local'` |
| `cap.t18.eval.eval_framework@1` | use the in-file conservative substitute for `eval_framework` (documented, slower, lower quality) and set `degraded['eval_framework']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - API reference generation from specifications with example verifi | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - conceptual guides, tutorials and cookbook content | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - documentation testing (every example executes correctly) | 520 | Third required mechanism. |
| 6 | Core implementation D - measured developer time-to-first-success | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0991_documentation_platform.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.documentation.documentation_platform@1`.
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

### P0992 · `developer_onboarding` — Developer Onboarding & Examples

| field | value |
|---|---|
| part id | `P0992` (42/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0992_developer_onboarding.ts` |
| module path | `hyperion.t20.platform.developer_onboarding` |
| capability published | `cap.t20.developer.developer_onboarding@1` |
| determinism class | `io` |
| p99 latency budget | 8000 ns (8 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0992_developer_onboarding.txt`](prompts/P0992_developer_onboarding.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0992-developer-onboarding) |

**Mission.** From zero to working integration in minutes.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **quickstart paths per language and use case** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **example application suite with automated verification**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **common-mistake detection and guidance** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured onboarding completion rate and time** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t20.developer.developer_onboarding@1`
- `cap.t20.developer.developer_onboarding.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.documentation.documentation_platform@1` | use the in-file conservative substitute for `documentation_platform` (documented, slower, lower quality) and set `degraded['documentation_platform']='local'` |
| `cap.t01.omega.omega_bus_ipc@1` | use the in-file conservative substitute for `omega_bus_ipc` (documented, slower, lower quality) and set `degraded['omega_bus_ipc']='local'` |
| `cap.t08.cascade.cascade_stage3_draft@1` | use the in-file conservative substitute for `cascade_stage3_draft` (documented, slower, lower quality) and set `degraded['cascade_stage3_draft']='local'` |
| `cap.t09.early.early_exit_runtime@1` | use the in-file conservative substitute for `early_exit_runtime` (documented, slower, lower quality) and set `degraded['early_exit_runtime']='local'` |
| `cap.t18.variance.variance_control@1` | use the in-file conservative substitute for `variance_control` (documented, slower, lower quality) and set `degraded['variance_control']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - quickstart paths per language and use case | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - example application suite with automated verification | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - common-mistake detection and guidance | 520 | Third required mechanism. |
| 6 | Core implementation D - measured onboarding completion rate and time | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0992_developer_onboarding.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.developer.developer_onboarding@1`.
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

### P0993 · `playground_console` — Interactive Console & Playground

| field | value |
|---|---|
| part id | `P0993` (43/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0993_playground_console.ts` |
| module path | `hyperion.t20.platform.playground_console` |
| capability published | `cap.t20.playground.playground_console@1` |
| determinism class | `io` |
| p99 latency budget | 9000 ns (9 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0993_playground_console.txt`](prompts/P0993_playground_console.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0993-playground-console) |

**Mission.** Try everything before writing code.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **interactive request construction with parameter exploration**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **cost and latency display before and after execution** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **code-export in every supported SDK** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **usability validation with new developers** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t20.playground.playground_console@1`
- `cap.t20.playground.playground_console.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.developer.developer_onboarding@1` | use the in-file conservative substitute for `developer_onboarding` (documented, slower, lower quality) and set `degraded['developer_onboarding']='local'` |
| `cap.t01.task.task_runtime@1` | use the in-file conservative substitute for `task_runtime` (documented, slower, lower quality) and set `degraded['task_runtime']='local'` |
| `cap.t08.paged.paged_attention_runtime@1` | use the in-file conservative substitute for `paged_attention_runtime` (documented, slower, lower quality) and set `degraded['paged_attention_runtime']='local'` |
| `cap.t09.tail.tail_latency@1` | use the in-file conservative substitute for `tail_latency` (documented, slower, lower quality) and set `degraded['tail_latency']='local'` |
| `cap.t18.gpqa.gpqa_eval@1` | use the in-file conservative substitute for `gpqa_eval` (documented, slower, lower quality) and set `degraded['gpqa_eval']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - interactive request construction with parameter exploration | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - cost and latency display before and after execution | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - code-export in every supported SDK | 520 | Third required mechanism. |
| 6 | Core implementation D - usability validation with new developers | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0993_playground_console.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.playground.playground_console@1`.
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

### P0994 · `model_registry_platform` — Model & Artifact Registry

| field | value |
|---|---|
| part id | `P0994` (44/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0994_model_registry_platform.ts` |
| module path | `hyperion.t20.platform.model_registry_platform` |
| capability published | `cap.t20.model.model_registry_platform@1` |
| determinism class | `io` |
| p99 latency budget | 10000 ns (10 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0994_model_registry_platform.txt`](prompts/P0994_model_registry_platform.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0994-model-registry-platform) |

**Mission.** Every deployed model version tracked and reproducible.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **model artifact storage with lineage, evaluation results and approvals** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **deployment-to-version mapping with audit history** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **artifact integrity and signature verification** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **registry completeness and correctness auditing**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t20.model.model_registry_platform@1`
- `cap.t20.model.model_registry_platform.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.playground.playground_console@1` | use the in-file conservative substitute for `playground_console` (documented, slower, lower quality) and set `degraded['playground_console']='local'` |
| `cap.t01.arena.arena_graph@1` | use the in-file conservative substitute for `arena_graph` (documented, slower, lower quality) and set `degraded['arena_graph']='local'` |
| `cap.t08.streaming.streaming_output@1` | use the in-file conservative substitute for `streaming_output` (documented, slower, lower quality) and set `degraded['streaming_output']='local'` |
| `cap.t09.compression.compression_latency@1` | use the in-file conservative substitute for `compression_latency` (documented, slower, lower quality) and set `degraded['compression_latency']='local'` |
| `cap.t18.lifescience.lifescience_eval@1` | use the in-file conservative substitute for `lifescience_eval` (documented, slower, lower quality) and set `degraded['lifescience_eval']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - model artifact storage with lineage, evaluation results and appr | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - deployment-to-version mapping with audit history | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - artifact integrity and signature verification | 520 | Third required mechanism. |
| 6 | Core implementation D - registry completeness and correctness auditing | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0994_model_registry_platform.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.model.model_registry_platform@1`.
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

### P0995 · `evaluation_integration` — Continuous Evaluation in the Deployment Pipeline

| field | value |
|---|---|
| part id | `P0995` (45/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0995_evaluation_integration.ts` |
| module path | `hyperion.t20.platform.evaluation_integration` |
| capability published | `cap.t20.evaluation.evaluation_integration@1` |
| determinism class | `io` |
| p99 latency budget | 11000 ns (11 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0995_evaluation_integration.txt`](prompts/P0995_evaluation_integration.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0995-evaluation-integration) |

**Mission.** Quality gates automated into every deploy.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **pre-deployment benchmark execution with pass criteria** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **post-deployment online quality monitoring** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **automatic rollback on quality regression**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured quality-regression escape rate** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t20.evaluation.evaluation_integration@1`
- `cap.t20.evaluation.evaluation_integration.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.model.model_registry_platform@1` | use the in-file conservative substitute for `model_registry_platform` (documented, slower, lower quality) and set `degraded['model_registry_platform']='local'` |
| `cap.t01.fuzz.fuzz_engine@1` | use the in-file conservative substitute for `fuzz_engine` (documented, slower, lower quality) and set `degraded['fuzz_engine']='local'` |
| `cap.t08.request.request_lifecycle@1` | use the in-file conservative substitute for `request_lifecycle` (documented, slower, lower quality) and set `degraded['request_lifecycle']='local'` |
| `cap.t09.numa.numa_latency@1` | use the in-file conservative substitute for `numa_latency` (documented, slower, lower quality) and set `degraded['numa_latency']='local'` |
| `cap.t18.adversarial.adversarial_eval@1` | use the in-file conservative substitute for `adversarial_eval` (documented, slower, lower quality) and set `degraded['adversarial_eval']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - pre-deployment benchmark execution with pass criteria | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - post-deployment online quality monitoring | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - automatic rollback on quality regression | 520 | Third required mechanism. |
| 6 | Core implementation D - measured quality-regression escape rate | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0995_evaluation_integration.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.evaluation.evaluation_integration@1`.
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

### P0996 · `distributed_dev_workflow` — 1000-Worker Distributed Development Workflow

| field | value |
|---|---|
| part id | `P0996` (46/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0996_distributed_dev_workflow.ts` |
| module path | `hyperion.t20.platform.distributed_dev_workflow` |
| capability published | `cap.t20.distributed.distributed_dev_workflow@1` |
| determinism class | `io` |
| p99 latency budget | 12000 ns (12 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0996_distributed_dev_workflow.txt`](prompts/P0996_distributed_dev_workflow.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0996-distributed-dev-workflow) |

**Mission.** The process that lets 1000 isolated authors produce one system.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **work-assignment protocol with contract-frozen briefs per part** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **submission validation, conformance checking and acceptance criteria**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **conflict-free integration procedure requiring no shared folders** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured first-submission acceptance rate across parts** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t20.distributed.distributed_dev_workflow@1`
- `cap.t20.distributed.distributed_dev_workflow.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.evaluation.evaluation_integration@1` | use the in-file conservative substitute for `evaluation_integration` (documented, slower, lower quality) and set `degraded['evaluation_integration']='local'` |
| `cap.t01.manifest.manifest_parser@1` | use the in-file conservative substitute for `manifest_parser` (documented, slower, lower quality) and set `degraded['manifest_parser']='local'` |
| `cap.t08.autoscaling.autoscaling@1` | use the in-file conservative substitute for `autoscaling` (documented, slower, lower quality) and set `degraded['autoscaling']='local'` |
| `cap.t09.bottleneck.bottleneck_analyser@1` | use the in-file conservative substitute for `bottleneck_analyser` (documented, slower, lower quality) and set `degraded['bottleneck_analyser']='local'` |
| `cap.t18.failure.failure_taxonomy@1` | use the in-file conservative substitute for `failure_taxonomy` (documented, slower, lower quality) and set `degraded['failure_taxonomy']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - work-assignment protocol with contract-frozen briefs per part | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - submission validation, conformance checking and acceptance crite | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - conflict-free integration procedure requiring no shared folders | 520 | Third required mechanism. |
| 6 | Core implementation D - measured first-submission acceptance rate across parts | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0996_distributed_dev_workflow.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.distributed.distributed_dev_workflow@1`.
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

### P0997 · `part_submission_gate` — Part Submission Validation Gate

| field | value |
|---|---|
| part id | `P0997` (47/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0997_part_submission_gate.ts` |
| module path | `hyperion.t20.platform.part_submission_gate` |
| capability published | `cap.t20.part.part_submission_gate@1` |
| determinism class | `io` |
| p99 latency budget | 13000 ns (13 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0997_part_submission_gate.txt`](prompts/P0997_part_submission_gate.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0997-part-submission-gate) |

**Mission.** Automated acceptance testing for each of the 1000 deliverables.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **line-count, structure and required-symbol verification**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **in-file test execution with pass and coverage requirements** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **contract-clause conformance and manifest validation** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **clear rejection reports enabling one-pass correction** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t20.part.part_submission_gate@1`
- `cap.t20.part.part_submission_gate.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.distributed.distributed_dev_workflow@1` | use the in-file conservative substitute for `distributed_dev_workflow` (documented, slower, lower quality) and set `degraded['distributed_dev_workflow']='local'` |
| `cap.t01.circuit.circuit_breaker@1` | use the in-file conservative substitute for `circuit_breaker` (documented, slower, lower quality) and set `degraded['circuit_breaker']='local'` |
| `cap.t08.engine.engine_bench_serving@1` | use the in-file conservative substitute for `engine_bench_serving` (documented, slower, lower quality) and set `degraded['engine_bench_serving']='local'` |
| `cap.t09.latency.latency_simulator@1` | use the in-file conservative substitute for `latency_simulator` (documented, slower, lower quality) and set `degraded['latency_simulator']='local'` |
| `cap.t18.eval.eval_reproducibility@1` | use the in-file conservative substitute for `eval_reproducibility` (documented, slower, lower quality) and set `degraded['eval_reproducibility']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - line-count, structure and required-symbol verification | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - in-file test execution with pass and coverage requirements | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - contract-clause conformance and manifest validation | 520 | Third required mechanism. |
| 6 | Core implementation D - clear rejection reports enabling one-pass correction | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0997_part_submission_gate.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.part.part_submission_gate@1`.
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

### P0998 · `assembly_dashboard` — Assembly Progress & Health Data Products

| field | value |
|---|---|
| part id | `P0998` (48/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0998_assembly_dashboard.ts` |
| module path | `hyperion.t20.platform.assembly_dashboard` |
| capability published | `cap.t20.assembly.assembly_dashboard@1` |
| determinism class | `io` |
| p99 latency budget | 14000 ns (14 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0998_assembly_dashboard.txt`](prompts/P0998_assembly_dashboard.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0998-assembly-dashboard) |

**Mission.** Live view of 1000 parts: submitted, validated, integrated, degraded.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **per-part status with blocking-dependency identification** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **CursorBench 3.2**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **capability-coverage and integration-health reporting** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **critical-path analysis for remaining work** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **data-product schemas for external dashboards**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t20.assembly.assembly_dashboard@1`
- `cap.t20.assembly.assembly_dashboard.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.part.part_submission_gate@1` | use the in-file conservative substitute for `part_submission_gate` (documented, slower, lower quality) and set `degraded['part_submission_gate']='local'` |
| `cap.t01.shutdown.shutdown_drain@1` | use the in-file conservative substitute for `shutdown_drain` (documented, slower, lower quality) and set `degraded['shutdown_drain']='local'` |
| `cap.t08.engine.engine_spec_doc@1` | use the in-file conservative substitute for `engine_spec_doc` (documented, slower, lower quality) and set `degraded['engine_spec_doc']='local'` |
| `cap.t09.latency.latency_spec_doc@1` | use the in-file conservative substitute for `latency_spec_doc` (documented, slower, lower quality) and set `degraded['latency_spec_doc']='local'` |
| `cap.t18.eval.eval_spec_doc@1` | use the in-file conservative substitute for `eval_spec_doc` (documented, slower, lower quality) and set `degraded['eval_spec_doc']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - per-part status with blocking-dependency identification | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - capability-coverage and integration-health reporting | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - critical-path analysis for remaining work | 520 | Third required mechanism. |
| 6 | Core implementation D - data-product schemas for external dashboards | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0998_assembly_dashboard.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.assembly.assembly_dashboard@1`.
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

### P0999 · `platform_bench` — Platform Benchmark & SLO Verification

| field | value |
|---|---|
| part id | `P0999` (49/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P0999_platform_bench.ts` |
| module path | `hyperion.t20.platform.platform_bench` |
| capability published | `cap.t20.platform.platform_bench@1` |
| determinism class | `io` |
| p99 latency budget | 15000 ns (15 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P0999_platform_bench.txt`](prompts/P0999_platform_bench.txt) · [inline](docs/PROMPTS_T20.md#prompt-p0999-platform-bench) |

**Mission.** Measures the platform layer itself.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **API latency, availability and error-rate measurement** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **SDK overhead measurement across languages** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **deployment pipeline speed and reliability metrics**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **SLO-attainment reporting with error budgets** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t20.platform.platform_bench@1`
- `cap.t20.platform.platform_bench.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.assembly.assembly_dashboard@1` | use the in-file conservative substitute for `assembly_dashboard` (documented, slower, lower quality) and set `degraded['assembly_dashboard']='local'` |
| `cap.t08.cascade.cascade_stage2_draft@1` | use the in-file conservative substitute for `cascade_stage2_draft` (documented, slower, lower quality) and set `degraded['cascade_stage2_draft']='local'` |
| `cap.t09.computation.computation_reuse@1` | use the in-file conservative substitute for `computation_reuse` (documented, slower, lower quality) and set `degraded['computation_reuse']='local'` |
| `cap.t18.statistical.statistical_engine@1` | use the in-file conservative substitute for `statistical_engine` (documented, slower, lower quality) and set `degraded['statistical_engine']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - API latency, availability and error-rate measurement | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - SDK overhead measurement across languages | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - deployment pipeline speed and reliability metrics | 520 | Third required mechanism. |
| 6 | Core implementation D - SLO-attainment reporting with error budgets | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P0999_platform_bench.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.platform.platform_bench@1`.
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

### P1000 · `platform_spec_doc` — Platform Specification, README & Master Index

| field | value |
|---|---|
| part id | `P1000` (50/50 of T20) |
| tier | `T20` — Platform, SDK, Ops & Distributed Assembly |
| language | TypeScript 5.7 |
| file to produce | `parts/t20_platform/P1000_platform_spec_doc.ts` |
| module path | `hyperion.t20.platform.platform_spec_doc` |
| capability published | `cap.t20.platform.platform_spec_doc@1` |
| determinism class | `io` |
| p99 latency budget | 16000 ns (16 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | CursorBench 3.2, Zapier AutomationBench |
| worker prompt | [`prompts/P1000_platform_spec_doc.txt`](prompts/P1000_platform_spec_doc.txt) · [inline](docs/PROMPTS_T20.md#prompt-p1000-platform-spec-doc) |

**Mission.** The authoritative top-level document for the whole system.

**Tier context.** Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.

**Mandate — all four items are required; none is optional.**

1. Implement **assembly overview with tier and part index** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **CursorBench 3.2** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **build, deploy and operate instructions verified by execution**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **guarantee register aggregated from all tiers** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **CursorBench 3.2** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **drift detection across the entire documentation set** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t20.platform.platform_spec_doc@1`
- `cap.t20.platform.platform_spec_doc.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t20.platform.platform_bench@1` | use the in-file conservative substitute for `platform_bench` (documented, slower, lower quality) and set `degraded['platform_bench']='local'` |
| `cap.t01.atomics.atomics_sync@1` | use the in-file conservative substitute for `atomics_sync` (documented, slower, lower quality) and set `degraded['atomics_sync']='local'` |
| `cap.t08.cascade.cascade_tuning@1` | use the in-file conservative substitute for `cascade_tuning` (documented, slower, lower quality) and set `degraded['cascade_tuning']='local'` |
| `cap.t09.async.async_pipeline@1` | use the in-file conservative substitute for `async_pipeline` (documented, slower, lower quality) and set `degraded['async_pipeline']='local'` |
| `cap.t18.arc.arc_agi_eval@1` | use the in-file conservative substitute for `arc_agi_eval` (documented, slower, lower quality) and set `degraded['arc_agi_eval']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - assembly overview with tier and part index | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - build, deploy and operate instructions verified by execution | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - guarantee register aggregated from all tiers | 520 | Third required mechanism. |
| 6 | Core implementation D - drift detection across the entire documentation set | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t20_platform/P1000_platform_spec_doc.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t20.platform.platform_spec_doc@1`.
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
