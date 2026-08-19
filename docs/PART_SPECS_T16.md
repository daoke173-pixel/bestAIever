# HYPERION-Ω — Part specifications · T16 · Domain Superintelligence Packs

> Contract: **Ω-CONTRACT v1.0.0-frozen** · 50 parts · 250,000 lines of code · language: Python 3.13

**Tier mission.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Benchmarks this tier is accountable for.** GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo)

**Tier dependencies.** T01, T10, T11

Each part below is built by exactly one isolated Opus 5 worker that sees only: this specification, the frozen Ω-Contract, and its own prompt. Workers never see each other's files. Link-compatibility comes from the contract, not from coordination.

| part | slug | title | capability |
|---|---|---|---|
| [P0751](#p0751-domain-pack-framework) | `domain_pack_framework` | Domain Pack Framework & Interface | `cap.t16.domain.domain_pack_framework@1` |
| [P0752](#p0752-domain-detection) | `domain_detection` | Domain Detection & Expert Routing | `cap.t16.domain.domain_detection@1` |
| [P0753](#p0753-molecular-biology) | `molecular_biology` | Molecular & Cell Biology | `cap.t16.molecular.molecular_biology@1` |
| [P0754](#p0754-structural-biology) | `structural_biology` | Structural Biology & Protein Science | `cap.t16.structural.structural_biology@1` |
| [P0755](#p0755-genomics-bioinformatics) | `genomics_bioinformatics` | Genomics & Bioinformatics | `cap.t16.genomics.genomics_bioinformatics@1` |
| [P0756](#p0756-organic-chemistry) | `organic_chemistry` | Organic Chemistry & Synthesis | `cap.t16.organic.organic_chemistry@1` |
| [P0757](#p0757-computational-chemistry) | `computational_chemistry` | Computational & Physical Chemistry | `cap.t16.computational.computational_chemistry@1` |
| [P0758](#p0758-materials-science) | `materials_science` | Materials Science & Engineering | `cap.t16.materials.materials_science@1` |
| [P0759](#p0759-drug-discovery) | `drug_discovery` | Medicinal Chemistry & Drug Discovery | `cap.t16.drug.drug_discovery@1` |
| [P0760](#p0760-clinical-medicine) | `clinical_medicine` | Clinical Medicine & Diagnostics | `cap.t16.clinical.clinical_medicine@1` |
| [P0761](#p0761-epidemiology-publichealth) | `epidemiology_publichealth` | Epidemiology & Public Health | `cap.t16.epidemiology.epidemiology_publichealth@1` |
| [P0762](#p0762-neuroscience) | `neuroscience` | Neuroscience & Cognitive Science | `cap.t16.neuroscience.neuroscience@1` |
| [P0763](#p0763-theoretical-physics) | `theoretical_physics` | Theoretical & Mathematical Physics | `cap.t16.theoretical.theoretical_physics@1` |
| [P0764](#p0764-applied-physics) | `applied_physics` | Applied & Experimental Physics | `cap.t16.applied.applied_physics@1` |
| [P0765](#p0765-astronomy-astrophysics) | `astronomy_astrophysics` | Astronomy & Astrophysics | `cap.t16.astronomy.astronomy_astrophysics@1` |
| [P0766](#p0766-earth-climate) | `earth_climate` | Earth & Climate Science | `cap.t16.earth.earth_climate@1` |
| [P0767](#p0767-pure-mathematics) | `pure_mathematics` | Pure Mathematics | `cap.t16.pure.pure_mathematics@1` |
| [P0768](#p0768-applied-mathematics) | `applied_mathematics` | Applied Mathematics & Numerical Analysis | `cap.t16.applied.applied_mathematics@1` |
| [P0769](#p0769-statistics-expertise) | `statistics_expertise` | Statistics & Experimental Design | `cap.t16.statistics.statistics_expertise@1` |
| [P0770](#p0770-operations-research) | `operations_research` | Operations Research & Optimisation | `cap.t16.operations.operations_research@1` |
| [P0771](#p0771-mechanical-engineering) | `mechanical_engineering` | Mechanical & Structural Engineering | `cap.t16.mechanical.mechanical_engineering@1` |
| [P0772](#p0772-electrical-engineering) | `electrical_engineering` | Electrical & Electronic Engineering | `cap.t16.electrical.electrical_engineering@1` |
| [P0773](#p0773-control-systems) | `control_systems` | Control Systems & Robotics Engineering | `cap.t16.control.control_systems@1` |
| [P0774](#p0774-chemical-engineering) | `chemical_engineering` | Chemical & Process Engineering | `cap.t16.chemical.chemical_engineering@1` |
| [P0775](#p0775-civil-infrastructure) | `civil_infrastructure` | Civil & Infrastructure Engineering | `cap.t16.civil.civil_infrastructure@1` |
| [P0776](#p0776-aerospace-engineering) | `aerospace_engineering` | Aerospace Engineering | `cap.t16.aerospace.aerospace_engineering@1` |
| [P0777](#p0777-semiconductor-engineering) | `semiconductor_engineering` | Semiconductor & Chip Design | `cap.t16.semiconductor.semiconductor_engineering@1` |
| [P0778](#p0778-energy-systems) | `energy_systems` | Energy Systems & Power Engineering | `cap.t16.energy.energy_systems@1` |
| [P0779](#p0779-corporate-law) | `corporate_law` | Corporate & Transactional Law | `cap.t16.corporate.corporate_law@1` |
| [P0780](#p0780-litigation-arbitration) | `litigation_arbitration` | Litigation & Dispute Resolution | `cap.t16.litigation.litigation_arbitration@1` |
| [P0781](#p0781-regulatory-compliance) | `regulatory_compliance` | Regulatory & Compliance Analysis | `cap.t16.regulatory.regulatory_compliance@1` |
| [P0782](#p0782-ip-patent) | `ip_patent` | Intellectual Property & Patent Practice | `cap.t16.ip.ip_patent@1` |
| [P0783](#p0783-tax-accounting) | `tax_accounting` | Tax & Accounting | `cap.t16.tax.tax_accounting@1` |
| [P0784](#p0784-corporate-finance) | `corporate_finance` | Corporate Finance & Valuation | `cap.t16.corporate.corporate_finance@1` |
| [P0785](#p0785-quantitative-finance) | `quantitative_finance` | Quantitative Finance & Derivatives | `cap.t16.quantitative.quantitative_finance@1` |
| [P0786](#p0786-investment-research) | `investment_research` | Investment Research & Financial Analysis | `cap.t16.investment.investment_research@1` |
| [P0787](#p0787-risk-management) | `risk_management` | Risk Management & Actuarial Science | `cap.t16.risk.risk_management@1` |
| [P0788](#p0788-economics) | `economics` | Economics & Policy Analysis | `cap.t16.economics.economics@1` |
| [P0789](#p0789-management-strategy) | `management_strategy` | Business Strategy & Management Consulting | `cap.t16.management.management_strategy@1` |
| [P0790](#p0790-marketing-growth) | `marketing_growth` | Marketing, Growth & Product Analytics | `cap.t16.marketing.marketing_growth@1` |
| [P0791](#p0791-operations-supplychain) | `operations_supplychain` | Operations & Supply Chain Management | `cap.t16.operations.operations_supplychain@1` |
| [P0792](#p0792-hr-organisational) | `hr_organisational` | Human Resources & Organisational Design | `cap.t16.hr.hr_organisational@1` |
| [P0793](#p0793-education-pedagogy) | `education_pedagogy` | Education & Instructional Design | `cap.t16.education.education_pedagogy@1` |
| [P0794](#p0794-psychology-behaviour) | `psychology_behaviour` | Psychology & Behavioural Science | `cap.t16.psychology.psychology_behaviour@1` |
| [P0795](#p0795-linguistics) | `linguistics` | Linguistics & Language Science | `cap.t16.linguistics.linguistics@1` |
| [P0796](#p0796-history-humanities) | `history_humanities` | History & Humanities Scholarship | `cap.t16.history.history_humanities@1` |
| [P0797](#p0797-philosophy-ethics) | `philosophy_ethics` | Philosophy & Applied Ethics | `cap.t16.philosophy.philosophy_ethics@1` |
| [P0798](#p0798-agriculture-food) | `agriculture_food` | Agriculture, Food Science & Nutrition | `cap.t16.agriculture.agriculture_food@1` |
| [P0799](#p0799-domain-cross-transfer) | `domain_cross_transfer` | Cross-Domain Synthesis & Interdisciplinary Reasoning | `cap.t16.domain.domain_cross_transfer@1` |
| [P0800](#p0800-domain-eval-harness) | `domain_eval_harness` | Domain Expertise Benchmark Harness | `cap.t16.domain.domain_eval_harness@1` |

---

### P0751 · `domain_pack_framework` — Domain Pack Framework & Interface

| field | value |
|---|---|
| part id | `P0751` (1/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0751_domain_pack_framework.py` |
| module path | `hyperion.t16.domains.domain_pack_framework` |
| capability published | `cap.t16.domain.domain_pack_framework@1` |
| determinism class | `pure` |
| p99 latency budget | 49000 ns (49 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0751_domain_pack_framework.txt`](prompts/P0751_domain_pack_framework.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0751-domain-pack-framework) |

**Mission.** The uniform structure every domain expertise module follows.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **domain pack schema: ontology, verifiers, tools, benchmarks, guardrails** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **capability registration and routing by detected domain** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **domain-confidence estimation and cross-domain handoff**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **pack conformance test suite all 40 domain packs must pass** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t16.domain.domain_pack_framework@1`
- `cap.t16.domain.domain_pack_framework.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t01.string.string_interning@1` | use the in-file conservative substitute for `string_interning` (documented, slower, lower quality) and set `degraded['string_interning']='local'` |
| `cap.t10.numeric.numeric_reasoning@1` | use the in-file conservative substitute for `numeric_reasoning` (documented, slower, lower quality) and set `degraded['numeric_reasoning']='local'` |
| `cap.t11.spec.spec_language@1` | use the in-file conservative substitute for `spec_language` (documented, slower, lower quality) and set `degraded['spec_language']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - domain pack schema: ontology, verifiers, tools, benchmarks, guar | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - capability registration and routing by detected domain | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - domain-confidence estimation and cross-domain handoff | 520 | Third required mechanism. |
| 6 | Core implementation D - pack conformance test suite all 40 domain packs must pass | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0751_domain_pack_framework.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.domain.domain_pack_framework@1`.
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

### P0752 · `domain_detection` — Domain Detection & Expert Routing

| field | value |
|---|---|
| part id | `P0752` (2/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0752_domain_detection.py` |
| module path | `hyperion.t16.domains.domain_detection` |
| capability published | `cap.t16.domain.domain_detection@1` |
| determinism class | `pure` |
| p99 latency budget | 3000 ns (3 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0752_domain_detection.txt`](prompts/P0752_domain_detection.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0752-domain-detection) |

**Mission.** Recognises the field of a question and engages the right expertise.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **multi-label domain classification with confidence and ambiguity handling** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **sub-domain and interdisciplinary detection**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **routing policy engaging multiple packs when needed** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **routing-accuracy measurement on domain-labelled corpora** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t16.domain.domain_detection@1`
- `cap.t16.domain.domain_detection.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.domain.domain_pack_framework@1` | use the in-file conservative substitute for `domain_pack_framework` (documented, slower, lower quality) and set `degraded['domain_pack_framework']='local'` |
| `cap.t01.property.property_gen@1` | use the in-file conservative substitute for `property_gen` (documented, slower, lower quality) and set `degraded['property_gen']='local'` |
| `cap.t10.backtracking.backtracking@1` | use the in-file conservative substitute for `backtracking` (documented, slower, lower quality) and set `degraded['backtracking']='local'` |
| `cap.t11.verified.verified_kernels@1` | use the in-file conservative substitute for `verified_kernels` (documented, slower, lower quality) and set `degraded['verified_kernels']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - multi-label domain classification with confidence and ambiguity  | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - sub-domain and interdisciplinary detection | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - routing policy engaging multiple packs when needed | 520 | Third required mechanism. |
| 6 | Core implementation D - routing-accuracy measurement on domain-labelled corpora | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0752_domain_detection.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.domain.domain_detection@1`.
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

### P0753 · `molecular_biology` — Molecular & Cell Biology

| field | value |
|---|---|
| part id | `P0753` (3/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0753_molecular_biology.py` |
| module path | `hyperion.t16.domains.molecular_biology` |
| capability published | `cap.t16.molecular.molecular_biology@1` |
| determinism class | `pure` |
| p99 latency budget | 4000 ns (4 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0753_molecular_biology.txt`](prompts/P0753_molecular_biology.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0753-molecular-biology) |

**Mission.** Expert-level reasoning about molecular mechanism.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **pathway, regulation and mechanism reasoning with literature grounding**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **experimental-design and control reasoning for molecular assays** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **database integration (sequence, structure, pathway, expression)** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **accuracy versus PhD-level biology question sets** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t16.molecular.molecular_biology@1`
- `cap.t16.molecular.molecular_biology.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.domain.domain_detection@1` | use the in-file conservative substitute for `domain_detection` (documented, slower, lower quality) and set `degraded['domain_detection']='local'` |
| `cap.t01.link.link_validator@1` | use the in-file conservative substitute for `link_validator` (documented, slower, lower quality) and set `degraded['link_validator']='local'` |
| `cap.t10.question.question_asking@1` | use the in-file conservative substitute for `question_asking` (documented, slower, lower quality) and set `degraded['question_asking']='local'` |
| `cap.t11.proof.proof_of_work_bounds@1` | use the in-file conservative substitute for `proof_of_work_bounds` (documented, slower, lower quality) and set `degraded['proof_of_work_bounds']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - pathway, regulation and mechanism reasoning with literature grou | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - experimental-design and control reasoning for molecular assays | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - database integration (sequence, structure, pathway, expression) | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy versus PhD-level biology question sets | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0753_molecular_biology.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.molecular.molecular_biology@1`.
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

### P0754 · `structural_biology` — Structural Biology & Protein Science

| field | value |
|---|---|
| part id | `P0754` (4/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0754_structural_biology.py` |
| module path | `hyperion.t16.domains.structural_biology` |
| capability published | `cap.t16.structural.structural_biology@1` |
| determinism class | `pure` |
| p99 latency budget | 5000 ns (5 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0754_structural_biology.txt`](prompts/P0754_structural_biology.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0754-structural-biology) |

**Mission.** Reasons about structure, folding and function.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **structure-function reasoning with geometric and energetic analysis** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **variant-effect prediction on protein function and stability** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **structure-prediction tool orchestration and result validation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **target: exceed Opus 5's +7.7pp protein-task improvement substantially**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t16.structural.structural_biology@1`
- `cap.t16.structural.structural_biology.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.molecular.molecular_biology@1` | use the in-file conservative substitute for `molecular_biology` (documented, slower, lower quality) and set `degraded['molecular_biology']='local'` |
| `cap.t01.rate.rate_limiter@1` | use the in-file conservative substitute for `rate_limiter` (documented, slower, lower quality) and set `degraded['rate_limiter']='local'` |
| `cap.t10.scratchpad.scratchpad_manager@1` | use the in-file conservative substitute for `scratchpad_manager` (documented, slower, lower quality) and set `degraded['scratchpad_manager']='local'` |
| `cap.t11.math.math_benchmark_formal@1` | use the in-file conservative substitute for `math_benchmark_formal` (documented, slower, lower quality) and set `degraded['math_benchmark_formal']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - structure-function reasoning with geometric and energetic analys | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - variant-effect prediction on protein function and stability | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - structure-prediction tool orchestration and result validation | 520 | Third required mechanism. |
| 6 | Core implementation D - target: exceed Opus 5's +7.7pp protein-task improvement substant | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0754_structural_biology.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.structural.structural_biology@1`.
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

### P0755 · `genomics_bioinformatics` — Genomics & Bioinformatics

| field | value |
|---|---|
| part id | `P0755` (5/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0755_genomics_bioinformatics.py` |
| module path | `hyperion.t16.domains.genomics_bioinformatics` |
| capability published | `cap.t16.genomics.genomics_bioinformatics@1` |
| determinism class | `pure` |
| p99 latency budget | 6000 ns (6 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0755_genomics_bioinformatics.txt`](prompts/P0755_genomics_bioinformatics.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0755-genomics-bioinformatics) |

**Mission.** Careful, statistically correct genomic analysis.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **pipeline construction with correct QC, normalisation and batch handling** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **statistical rigor: multiple testing, confounders, independent cross-checks** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **variant interpretation with evidence-tier classification**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **accuracy on curated genomic-analysis tasks with known answers** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t16.genomics.genomics_bioinformatics@1`
- `cap.t16.genomics.genomics_bioinformatics.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.structural.structural_biology@1` | use the in-file conservative substitute for `structural_biology` (documented, slower, lower quality) and set `degraded['structural_biology']='local'` |
| `cap.t01.bootstrap.bootstrap_init@1` | use the in-file conservative substitute for `bootstrap_init` (documented, slower, lower quality) and set `degraded['bootstrap_init']='local'` |
| `cap.t10.reasoning.reasoning_speed_proof@1` | use the in-file conservative substitute for `reasoning_speed_proof` (documented, slower, lower quality) and set `degraded['reasoning_speed_proof']='local'` |
| `cap.t11.proof.proof_speed@1` | use the in-file conservative substitute for `proof_speed` (documented, slower, lower quality) and set `degraded['proof_speed']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - pipeline construction with correct QC, normalisation and batch h | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - statistical rigor: multiple testing, confounders, independent cr | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - variant interpretation with evidence-tier classification | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy on curated genomic-analysis tasks with known answers | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0755_genomics_bioinformatics.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.genomics.genomics_bioinformatics@1`.
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

### P0756 · `organic_chemistry` — Organic Chemistry & Synthesis

| field | value |
|---|---|
| part id | `P0756` (6/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0756_organic_chemistry.py` |
| module path | `hyperion.t16.domains.organic_chemistry` |
| capability published | `cap.t16.organic.organic_chemistry@1` |
| determinism class | `pure` |
| p99 latency budget | 7000 ns (7 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0756_organic_chemistry.txt`](prompts/P0756_organic_chemistry.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0756-organic-chemistry) |

**Mission.** Predicts and plans real chemistry.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **retrosynthetic planning with feasibility and cost reasoning** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **reaction-mechanism and selectivity prediction**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **spectroscopic structure elucidation from raw spectral data** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **target: exceed Opus 5's +10.2pp organic-chemistry improvement substantially** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t16.organic.organic_chemistry@1`
- `cap.t16.organic.organic_chemistry.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.genomics.genomics_bioinformatics@1` | use the in-file conservative substitute for `genomics_bioinformatics` (documented, slower, lower quality) and set `degraded['genomics_bioinformatics']='local'` |
| `cap.t01.chacha.chacha_seeds@1` | use the in-file conservative substitute for `chacha_seeds` (documented, slower, lower quality) and set `degraded['chacha_seeds']='local'` |
| `cap.t10.process.process_verifier@1` | use the in-file conservative substitute for `process_verifier` (documented, slower, lower quality) and set `degraded['process_verifier']='local'` |
| `cap.t11.premise.premise_selection@1` | use the in-file conservative substitute for `premise_selection` (documented, slower, lower quality) and set `degraded['premise_selection']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - retrosynthetic planning with feasibility and cost reasoning | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - reaction-mechanism and selectivity prediction | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - spectroscopic structure elucidation from raw spectral data | 520 | Third required mechanism. |
| 6 | Core implementation D - target: exceed Opus 5's +10.2pp organic-chemistry improvement su | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0756_organic_chemistry.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.organic.organic_chemistry@1`.
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

### P0757 · `computational_chemistry` — Computational & Physical Chemistry

| field | value |
|---|---|
| part id | `P0757` (7/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0757_computational_chemistry.py` |
| module path | `hyperion.t16.domains.computational_chemistry` |
| capability published | `cap.t16.computational.computational_chemistry@1` |
| determinism class | `pure` |
| p99 latency budget | 8000 ns (8 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0757_computational_chemistry.txt`](prompts/P0757_computational_chemistry.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0757-computational-chemistry) |

**Mission.** Correct quantum and thermodynamic reasoning.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **method selection (DFT, MD, semi-empirical) with accuracy/cost tradeoffs**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **thermodynamic and kinetic property reasoning with unit rigor** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **simulation setup, execution and result validation** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **accuracy against experimental reference datasets** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t16.computational.computational_chemistry@1`
- `cap.t16.computational.computational_chemistry.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.organic.organic_chemistry@1` | use the in-file conservative substitute for `organic_chemistry` (documented, slower, lower quality) and set `degraded['organic_chemistry']='local'` |
| `cap.t01.mem.mem_layout@1` | use the in-file conservative substitute for `mem_layout` (documented, slower, lower quality) and set `degraded['mem_layout']='local'` |
| `cap.t10.goal.goal_management@1` | use the in-file conservative substitute for `goal_management` (documented, slower, lower quality) and set `degraded['goal_management']='local'` |
| `cap.t11.dependent.dependent_types@1` | use the in-file conservative substitute for `dependent_types` (documented, slower, lower quality) and set `degraded['dependent_types']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - method selection (DFT, MD, semi-empirical) with accuracy/cost tr | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - thermodynamic and kinetic property reasoning with unit rigor | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - simulation setup, execution and result validation | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy against experimental reference datasets | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0757_computational_chemistry.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.computational.computational_chemistry@1`.
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

### P0758 · `materials_science` — Materials Science & Engineering

| field | value |
|---|---|
| part id | `P0758` (8/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0758_materials_science.py` |
| module path | `hyperion.t16.domains.materials_science` |
| capability published | `cap.t16.materials.materials_science@1` |
| determinism class | `pure` |
| p99 latency budget | 9000 ns (9 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0758_materials_science.txt`](prompts/P0758_materials_science.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0758-materials-science) |

**Mission.** Designs and evaluates materials for real requirements.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **structure-property relationship reasoning across material classes** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **processing-route and manufacturability reasoning** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **characterisation-data interpretation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **accuracy on materials-property prediction benchmarks**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t16.materials.materials_science@1`
- `cap.t16.materials.materials_science.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.computational.computational_chemistry@1` | use the in-file conservative substitute for `computational_chemistry` (documented, slower, lower quality) and set `degraded['computational_chemistry']='local'` |
| `cap.t01.hash.hash_maps@1` | use the in-file conservative substitute for `hash_maps` (documented, slower, lower quality) and set `degraded['hash_maps']='local'` |
| `cap.t10.probabilistic.probabilistic_reasoning@1` | use the in-file conservative substitute for `probabilistic_reasoning` (documented, slower, lower quality) and set `degraded['probabilistic_reasoning']='local'` |
| `cap.t11.informalisatio.informalisation@1` | use the in-file conservative substitute for `informalisation` (documented, slower, lower quality) and set `degraded['informalisation']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - structure-property relationship reasoning across material classe | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - processing-route and manufacturability reasoning | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - characterisation-data interpretation | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy on materials-property prediction benchmarks | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0758_materials_science.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.materials.materials_science@1`.
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

### P0759 · `drug_discovery` — Medicinal Chemistry & Drug Discovery

| field | value |
|---|---|
| part id | `P0759` (9/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0759_drug_discovery.py` |
| module path | `hyperion.t16.domains.drug_discovery` |
| capability published | `cap.t16.drug.drug_discovery@1` |
| determinism class | `pure` |
| p99 latency budget | 10000 ns (10 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0759_drug_discovery.txt`](prompts/P0759_drug_discovery.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0759-drug-discovery) |

**Mission.** Scientifically strong, with strict dual-use safeguards.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **target validation, lead optimisation and ADMET reasoning** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **structure-activity relationship analysis** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **mandatory dual-use gating via T19 for hazardous applications**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **accuracy on medicinal-chemistry task suites within safety scope** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t16.drug.drug_discovery@1`
- `cap.t16.drug.drug_discovery.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.materials.materials_science@1` | use the in-file conservative substitute for `materials_science` (documented, slower, lower quality) and set `degraded['materials_science']='local'` |
| `cap.t01.selftest.selftest_harness@1` | use the in-file conservative substitute for `selftest_harness` (documented, slower, lower quality) and set `degraded['selftest_harness']='local'` |
| `cap.t10.stopping.stopping_rules@1` | use the in-file conservative substitute for `stopping_rules` (documented, slower, lower quality) and set `degraded['stopping_rules']='local'` |
| `cap.t11.proof.proof_compression@1` | use the in-file conservative substitute for `proof_compression` (documented, slower, lower quality) and set `degraded['proof_compression']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - target validation, lead optimisation and ADMET reasoning | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - structure-activity relationship analysis | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - mandatory dual-use gating via T19 for hazardous applications | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy on medicinal-chemistry task suites within safety scope | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0759_drug_discovery.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.drug.drug_discovery@1`.
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

### P0760 · `clinical_medicine` — Clinical Medicine & Diagnostics

| field | value |
|---|---|
| part id | `P0760` (10/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0760_clinical_medicine.py` |
| module path | `hyperion.t16.domains.clinical_medicine` |
| capability published | `cap.t16.clinical.clinical_medicine@1` |
| determinism class | `pure` |
| p99 latency budget | 11000 ns (11 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0760_clinical_medicine.txt`](prompts/P0760_clinical_medicine.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0760-clinical-medicine) |

**Mission.** Clinician-grade reasoning with clinician-grade humility.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **differential-diagnosis generation with calibrated probabilities** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **evidence-based guideline application with contraindication checking**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **mandatory clinical-oversight framing and scope limitation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **accuracy versus physician consensus on curated cases** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t16.clinical.clinical_medicine@1`
- `cap.t16.clinical.clinical_medicine.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.drug.drug_discovery@1` | use the in-file conservative substitute for `drug_discovery` (documented, slower, lower quality) and set `degraded['drug_discovery']='local'` |
| `cap.t01.version.version_semver@1` | use the in-file conservative substitute for `version_semver` (documented, slower, lower quality) and set `degraded['version_semver']='local'` |
| `cap.t10.assumption.assumption_tracking@1` | use the in-file conservative substitute for `assumption_tracking` (documented, slower, lower quality) and set `degraded['assumption_tracking']='local'` |
| `cap.t11.statistical.statistical_guarantees@1` | use the in-file conservative substitute for `statistical_guarantees` (documented, slower, lower quality) and set `degraded['statistical_guarantees']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - differential-diagnosis generation with calibrated probabilities | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - evidence-based guideline application with contraindication check | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - mandatory clinical-oversight framing and scope limitation | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy versus physician consensus on curated cases | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0760_clinical_medicine.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.clinical.clinical_medicine@1`.
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

### P0761 · `epidemiology_publichealth` — Epidemiology & Public Health

| field | value |
|---|---|
| part id | `P0761` (11/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0761_epidemiology_publichealth.py` |
| module path | `hyperion.t16.domains.epidemiology_publichealth` |
| capability published | `cap.t16.epidemiology.epidemiology_publichealth@1` |
| determinism class | `pure` |
| p99 latency budget | 12000 ns (12 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0761_epidemiology_publichealth.txt`](prompts/P0761_epidemiology_publichealth.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0761-epidemiology-publichealth) |

**Mission.** Population-level reasoning done correctly.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **study-design reasoning with bias and confounding analysis**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **epidemiological modelling with parameter-uncertainty propagation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **surveillance-data interpretation** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **accuracy on epidemiological-reasoning benchmark sets** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t16.epidemiology.epidemiology_publichealth@1`
- `cap.t16.epidemiology.epidemiology_publichealth.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.clinical.clinical_medicine@1` | use the in-file conservative substitute for `clinical_medicine` (documented, slower, lower quality) and set `degraded['clinical_medicine']='local'` |
| `cap.t01.budget.budget_ledger@1` | use the in-file conservative substitute for `budget_ledger` (documented, slower, lower quality) and set `degraded['budget_ledger']='local'` |
| `cap.t10.reasoning.reasoning_cost_model@1` | use the in-file conservative substitute for `reasoning_cost_model` (documented, slower, lower quality) and set `degraded['reasoning_cost_model']='local'` |
| `cap.t11.regression.regression_proofs@1` | use the in-file conservative substitute for `regression_proofs` (documented, slower, lower quality) and set `degraded['regression_proofs']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - study-design reasoning with bias and confounding analysis | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - epidemiological modelling with parameter-uncertainty propagation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - surveillance-data interpretation | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy on epidemiological-reasoning benchmark sets | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0761_epidemiology_publichealth.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.epidemiology.epidemiology_publichealth@1`.
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

### P0762 · `neuroscience` — Neuroscience & Cognitive Science

| field | value |
|---|---|
| part id | `P0762` (12/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0762_neuroscience.py` |
| module path | `hyperion.t16.domains.neuroscience` |
| capability published | `cap.t16.neuroscience.neuroscience@1` |
| determinism class | `pure` |
| p99 latency budget | 13000 ns (13 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0762_neuroscience.txt`](prompts/P0762_neuroscience.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0762-neuroscience) |

**Mission.** Reasons about brains and minds rigorously.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **multi-scale reasoning from molecular to behavioural** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **neuroimaging and electrophysiology data interpretation** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **cognitive-model reasoning with experimental grounding** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **accuracy on graduate-level neuroscience question sets**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t16.neuroscience.neuroscience@1`
- `cap.t16.neuroscience.neuroscience.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.epidemiology.epidemiology_publichealth@1` | use the in-file conservative substitute for `epidemiology_publichealth` (documented, slower, lower quality) and set `degraded['epidemiology_publichealth']='local'` |
| `cap.t01.compression.compression@1` | use the in-file conservative substitute for `compression` (documented, slower, lower quality) and set `degraded['compression']='local'` |
| `cap.t10.collective.collective_reasoning@1` | use the in-file conservative substitute for `collective_reasoning` (documented, slower, lower quality) and set `degraded['collective_reasoning']='local'` |
| `cap.t11.verification.verification_bench@1` | use the in-file conservative substitute for `verification_bench` (documented, slower, lower quality) and set `degraded['verification_bench']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - multi-scale reasoning from molecular to behavioural | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - neuroimaging and electrophysiology data interpretation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - cognitive-model reasoning with experimental grounding | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy on graduate-level neuroscience question sets | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0762_neuroscience.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.neuroscience.neuroscience@1`.
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

### P0763 · `theoretical_physics` — Theoretical & Mathematical Physics

| field | value |
|---|---|
| part id | `P0763` (13/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0763_theoretical_physics.py` |
| module path | `hyperion.t16.domains.theoretical_physics` |
| capability published | `cap.t16.theoretical.theoretical_physics@1` |
| determinism class | `pure` |
| p99 latency budget | 14000 ns (14 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0763_theoretical_physics.txt`](prompts/P0763_theoretical_physics.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0763-theoretical-physics) |

**Mission.** Derives, does not recall.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **derivation from first principles with dimensional and limit checking** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **symmetry, conservation-law and effective-theory reasoning** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **connection to experimental observables with error analysis**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **accuracy on graduate-level physics problem sets** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t16.theoretical.theoretical_physics@1`
- `cap.t16.theoretical.theoretical_physics.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.neuroscience.neuroscience@1` | use the in-file conservative substitute for `neuroscience` (documented, slower, lower quality) and set `degraded['neuroscience']='local'` |
| `cap.t01.blake3.blake3_hash@1` | use the in-file conservative substitute for `blake3_hash` (documented, slower, lower quality) and set `degraded['blake3_hash']='local'` |
| `cap.t10.beam.beam_pruning@1` | use the in-file conservative substitute for `beam_pruning` (documented, slower, lower quality) and set `degraded['beam_pruning']='local'` |
| `cap.t11.proof.proof_search@1` | use the in-file conservative substitute for `proof_search` (documented, slower, lower quality) and set `degraded['proof_search']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - derivation from first principles with dimensional and limit chec | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - symmetry, conservation-law and effective-theory reasoning | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - connection to experimental observables with error analysis | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy on graduate-level physics problem sets | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0763_theoretical_physics.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.theoretical.theoretical_physics@1`.
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

### P0764 · `applied_physics` — Applied & Experimental Physics

| field | value |
|---|---|
| part id | `P0764` (14/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0764_applied_physics.py` |
| module path | `hyperion.t16.domains.applied_physics` |
| capability published | `cap.t16.applied.applied_physics@1` |
| determinism class | `pure` |
| p99 latency budget | 15000 ns (15 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0764_applied_physics.txt`](prompts/P0764_applied_physics.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0764-applied-physics) |

**Mission.** Designs experiments and interprets real data.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **measurement-uncertainty and error-budget analysis** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **apparatus and instrument reasoning with systematic-error identification**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **data-fitting with model-selection rigor** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **accuracy on experimental-physics analysis tasks** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t16.applied.applied_physics@1`
- `cap.t16.applied.applied_physics.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.theoretical.theoretical_physics@1` | use the in-file conservative substitute for `theoretical_physics` (documented, slower, lower quality) and set `degraded['theoretical_physics']='local'` |
| `cap.t01.alloc.alloc_arena@1` | use the in-file conservative substitute for `alloc_arena` (documented, slower, lower quality) and set `degraded['alloc_arena']='local'` |
| `cap.t10.planning.planning_engine@1` | use the in-file conservative substitute for `planning_engine` (documented, slower, lower quality) and set `degraded['planning_engine']='local'` |
| `cap.t11.refinement.refinement_types@1` | use the in-file conservative substitute for `refinement_types` (documented, slower, lower quality) and set `degraded['refinement_types']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - measurement-uncertainty and error-budget analysis | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - apparatus and instrument reasoning with systematic-error identif | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - data-fitting with model-selection rigor | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy on experimental-physics analysis tasks | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0764_applied_physics.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.applied.applied_physics@1`.
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

### P0765 · `astronomy_astrophysics` — Astronomy & Astrophysics

| field | value |
|---|---|
| part id | `P0765` (15/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0765_astronomy_astrophysics.py` |
| module path | `hyperion.t16.domains.astronomy_astrophysics` |
| capability published | `cap.t16.astronomy.astronomy_astrophysics@1` |
| determinism class | `pure` |
| p99 latency budget | 16000 ns (16 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0765_astronomy_astrophysics.txt`](prompts/P0765_astronomy_astrophysics.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0765-astronomy-astrophysics) |

**Mission.** Handles astronomical data and scales correctly.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **observational-data reduction and analysis reasoning**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **scale, unit and cosmological-convention rigor** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **survey-data querying and interpretation** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **accuracy on astrophysics problem and data-analysis sets** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t16.astronomy.astronomy_astrophysics@1`
- `cap.t16.astronomy.astronomy_astrophysics.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.applied.applied_physics@1` | use the in-file conservative substitute for `applied_physics` (documented, slower, lower quality) and set `degraded['applied_physics']='local'` |
| `cap.t01.bitset.bitset_rank@1` | use the in-file conservative substitute for `bitset_rank` (documented, slower, lower quality) and set `degraded['bitset_rank']='local'` |
| `cap.t10.counterfactual.counterfactual_reasoning@1` | use the in-file conservative substitute for `counterfactual_reasoning` (documented, slower, lower quality) and set `degraded['counterfactual_reasoning']='local'` |
| `cap.t11.autoformalisat.autoformalisation@1` | use the in-file conservative substitute for `autoformalisation` (documented, slower, lower quality) and set `degraded['autoformalisation']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - observational-data reduction and analysis reasoning | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - scale, unit and cosmological-convention rigor | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - survey-data querying and interpretation | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy on astrophysics problem and data-analysis sets | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0765_astronomy_astrophysics.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.astronomy.astronomy_astrophysics@1`.
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

### P0766 · `earth_climate` — Earth & Climate Science

| field | value |
|---|---|
| part id | `P0766` (16/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0766_earth_climate.py` |
| module path | `hyperion.t16.domains.earth_climate` |
| capability published | `cap.t16.earth.earth_climate@1` |
| determinism class | `pure` |
| p99 latency budget | 17000 ns (17 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0766_earth_climate.txt`](prompts/P0766_earth_climate.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0766-earth-climate) |

**Mission.** Rigorous, honest climate and earth-system reasoning.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **climate-model output interpretation with uncertainty communication** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **geophysical data analysis and attribution reasoning** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **scenario reasoning with explicit assumption statements** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **accuracy on earth-science analysis benchmarks**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t16.earth.earth_climate@1`
- `cap.t16.earth.earth_climate.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.astronomy.astronomy_astrophysics@1` | use the in-file conservative substitute for `astronomy_astrophysics` (documented, slower, lower quality) and set `degraded['astronomy_astrophysics']='local'` |
| `cap.t01.metrics.metrics_core@1` | use the in-file conservative substitute for `metrics_core` (documented, slower, lower quality) and set `degraded['metrics_core']='local'` |
| `cap.t10.difficulty.difficulty_estimation@1` | use the in-file conservative substitute for `difficulty_estimation` (documented, slower, lower quality) and set `degraded['difficulty_estimation']='local'` |
| `cap.t11.counterexample.counterexample_engine@1` | use the in-file conservative substitute for `counterexample_engine` (documented, slower, lower quality) and set `degraded['counterexample_engine']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - climate-model output interpretation with uncertainty communicati | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - geophysical data analysis and attribution reasoning | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - scenario reasoning with explicit assumption statements | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy on earth-science analysis benchmarks | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0766_earth_climate.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.earth.earth_climate@1`.
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

### P0767 · `pure_mathematics` — Pure Mathematics

| field | value |
|---|---|
| part id | `P0767` (17/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0767_pure_mathematics.py` |
| module path | `hyperion.t16.domains.pure_mathematics` |
| capability published | `cap.t16.pure.pure_mathematics@1` |
| determinism class | `pure` |
| p99 latency budget | 18000 ns (18 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0767_pure_mathematics.txt`](prompts/P0767_pure_mathematics.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0767-pure-mathematics) |

**Mission.** Proves theorems, does not gesture at them.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **proof construction across algebra, analysis, topology and combinatorics** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **counterexample construction and conjecture evaluation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **formal-verification handoff for critical proofs**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **accuracy on research-level mathematics problem sets** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t16.pure.pure_mathematics@1`
- `cap.t16.pure.pure_mathematics.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.earth.earth_climate@1` | use the in-file conservative substitute for `earth_climate` (documented, slower, lower quality) and set `degraded['earth_climate']='local'` |
| `cap.t01.capability.capability_gate@1` | use the in-file conservative substitute for `capability_gate` (documented, slower, lower quality) and set `degraded['capability_gate']='local'` |
| `cap.t10.evidence.evidence_integration@1` | use the in-file conservative substitute for `evidence_integration` (documented, slower, lower quality) and set `degraded['evidence_integration']='local'` |
| `cap.t11.numeric.numeric_verification_ml@1` | use the in-file conservative substitute for `numeric_verification_ml` (documented, slower, lower quality) and set `degraded['numeric_verification_ml']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - proof construction across algebra, analysis, topology and combin | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - counterexample construction and conjecture evaluation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - formal-verification handoff for critical proofs | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy on research-level mathematics problem sets | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0767_pure_mathematics.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.pure.pure_mathematics@1`.
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

### P0768 · `applied_mathematics` — Applied Mathematics & Numerical Analysis

| field | value |
|---|---|
| part id | `P0768` (18/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0768_applied_mathematics.py` |
| module path | `hyperion.t16.domains.applied_mathematics` |
| capability published | `cap.t16.applied.applied_mathematics@1` |
| determinism class | `pure` |
| p99 latency budget | 19000 ns (19 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0768_applied_mathematics.txt`](prompts/P0768_applied_mathematics.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0768-applied-mathematics) |

**Mission.** Turns real problems into solvable mathematics.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **model formulation with assumption justification** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **numerical-method selection with stability and convergence analysis**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **error-bound derivation for computed solutions** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **accuracy on applied-mathematics problem sets** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t16.applied.applied_mathematics@1`
- `cap.t16.applied.applied_mathematics.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.pure.pure_mathematics@1` | use the in-file conservative substitute for `pure_mathematics` (documented, slower, lower quality) and set `degraded['pure_mathematics']='local'` |
| `cap.t01.unit.unit_dimensions@1` | use the in-file conservative substitute for `unit_dimensions` (documented, slower, lower quality) and set `degraded['unit_dimensions']='local'` |
| `cap.t10.reasoning.reasoning_search_bench@1` | use the in-file conservative substitute for `reasoning_search_bench` (documented, slower, lower quality) and set `degraded['reasoning_search_bench']='local'` |
| `cap.t11.hybrid.hybrid_verification@1` | use the in-file conservative substitute for `hybrid_verification` (documented, slower, lower quality) and set `degraded['hybrid_verification']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - model formulation with assumption justification | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - numerical-method selection with stability and convergence analys | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - error-bound derivation for computed solutions | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy on applied-mathematics problem sets | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0768_applied_mathematics.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.applied.applied_mathematics@1`.
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

### P0769 · `statistics_expertise` — Statistics & Experimental Design

| field | value |
|---|---|
| part id | `P0769` (19/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0769_statistics_expertise.py` |
| module path | `hyperion.t16.domains.statistics_expertise` |
| capability published | `cap.t16.statistics.statistics_expertise@1` |
| determinism class | `pure` |
| p99 latency budget | 20000 ns (20 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0769_statistics_expertise.txt`](prompts/P0769_statistics_expertise.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0769-statistics-expertise) |

**Mission.** The statistical rigor that most analysis lacks.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **method selection with assumption verification and diagnostics**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **power analysis, sample sizing and pre-registration reasoning** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **multiple-comparison and p-hacking prevention** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **accuracy on statistical-reasoning benchmark sets** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t16.statistics.statistics_expertise@1`
- `cap.t16.statistics.statistics_expertise.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.applied.applied_mathematics@1` | use the in-file conservative substitute for `applied_mathematics` (documented, slower, lower quality) and set `degraded['applied_mathematics']='local'` |
| `cap.t01.fs.fs_atomic@1` | use the in-file conservative substitute for `fs_atomic` (documented, slower, lower quality) and set `degraded['fs_atomic']='local'` |
| `cap.t10.reasoning.reasoning_interpretability@1` | use the in-file conservative substitute for `reasoning_interpretability` (documented, slower, lower quality) and set `degraded['reasoning_interpretability']='local'` |
| `cap.t11.trust.trust_boundaries@1` | use the in-file conservative substitute for `trust_boundaries` (documented, slower, lower quality) and set `degraded['trust_boundaries']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - method selection with assumption verification and diagnostics | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - power analysis, sample sizing and pre-registration reasoning | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - multiple-comparison and p-hacking prevention | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy on statistical-reasoning benchmark sets | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0769_statistics_expertise.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.statistics.statistics_expertise@1`.
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

### P0770 · `operations_research` — Operations Research & Optimisation

| field | value |
|---|---|
| part id | `P0770` (20/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0770_operations_research.py` |
| module path | `hyperion.t16.domains.operations_research` |
| capability published | `cap.t16.operations.operations_research@1` |
| determinism class | `pure` |
| p99 latency budget | 21000 ns (21 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0770_operations_research.txt`](prompts/P0770_operations_research.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0770-operations-research) |

**Mission.** Formulates and solves real optimisation problems.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **problem formulation into solvable programs with solver selection** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **sensitivity and dual analysis with business interpretation** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **heuristic design for intractable instances** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **solution-quality measurement against known optima**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t16.operations.operations_research@1`
- `cap.t16.operations.operations_research.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.statistics.statistics_expertise@1` | use the in-file conservative substitute for `statistics_expertise` (documented, slower, lower quality) and set `degraded['statistics_expertise']='local'` |
| `cap.t01.cbor.cbor_canonical@1` | use the in-file conservative substitute for `cbor_canonical` (documented, slower, lower quality) and set `degraded['cbor_canonical']='local'` |
| `cap.t10.graph.graph_search@1` | use the in-file conservative substitute for `graph_search` (documented, slower, lower quality) and set `degraded['graph_search']='local'` |
| `cap.t11.itp.itp_bridge@1` | use the in-file conservative substitute for `itp_bridge` (documented, slower, lower quality) and set `degraded['itp_bridge']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - problem formulation into solvable programs with solver selection | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - sensitivity and dual analysis with business interpretation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - heuristic design for intractable instances | 520 | Third required mechanism. |
| 6 | Core implementation D - solution-quality measurement against known optima | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0770_operations_research.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.operations.operations_research@1`.
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

### P0771 · `mechanical_engineering` — Mechanical & Structural Engineering

| field | value |
|---|---|
| part id | `P0771` (21/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0771_mechanical_engineering.py` |
| module path | `hyperion.t16.domains.mechanical_engineering` |
| capability published | `cap.t16.mechanical.mechanical_engineering@1` |
| determinism class | `pure` |
| p99 latency budget | 22000 ns (22 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0771_mechanical_engineering.txt`](prompts/P0771_mechanical_engineering.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0771-mechanical-engineering) |

**Mission.** Designs things that do not break.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **stress, thermal and fatigue analysis with safety factors** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **tolerance, fit and manufacturability reasoning** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **code and standard compliance checking**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **accuracy on engineering analysis problems with known answers** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t16.mechanical.mechanical_engineering@1`
- `cap.t16.mechanical.mechanical_engineering.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.operations.operations_research@1` | use the in-file conservative substitute for `operations_research` (documented, slower, lower quality) and set `degraded['operations_research']='local'` |
| `cap.t01.clock.clock_time@1` | use the in-file conservative substitute for `clock_time` (documented, slower, lower quality) and set `degraded['clock_time']='local'` |
| `cap.t10.decomposition.decomposition@1` | use the in-file conservative substitute for `decomposition` (documented, slower, lower quality) and set `degraded['decomposition']='local'` |
| `cap.t11.model.model_checking@1` | use the in-file conservative substitute for `model_checking` (documented, slower, lower quality) and set `degraded['model_checking']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - stress, thermal and fatigue analysis with safety factors | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - tolerance, fit and manufacturability reasoning | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - code and standard compliance checking | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy on engineering analysis problems with known answers | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0771_mechanical_engineering.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.mechanical.mechanical_engineering@1`.
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

### P0772 · `electrical_engineering` — Electrical & Electronic Engineering

| field | value |
|---|---|
| part id | `P0772` (22/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0772_electrical_engineering.py` |
| module path | `hyperion.t16.domains.electrical_engineering` |
| capability published | `cap.t16.electrical.electrical_engineering@1` |
| determinism class | `pure` |
| p99 latency budget | 23000 ns (23 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0772_electrical_engineering.txt`](prompts/P0772_electrical_engineering.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0772-electrical-engineering) |

**Mission.** Circuits, signals and power, correctly analysed.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **circuit analysis, signal integrity and power-budget reasoning** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **component selection with derating and tolerance analysis**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **simulation setup and result validation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **accuracy on electrical-engineering problem sets** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t16.electrical.electrical_engineering@1`
- `cap.t16.electrical.electrical_engineering.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.mechanical.mechanical_engineering@1` | use the in-file conservative substitute for `mechanical_engineering` (documented, slower, lower quality) and set `degraded['mechanical_engineering']='local'` |
| `cap.t01.bigint.bigint_modmath@1` | use the in-file conservative substitute for `bigint_modmath` (documented, slower, lower quality) and set `degraded['bigint_modmath']='local'` |
| `cap.t10.program.program_synthesis_reasoning@1` | use the in-file conservative substitute for `program_synthesis_reasoning` (documented, slower, lower quality) and set `degraded['program_synthesis_reasoning']='local'` |
| `cap.t11.theorem.theorem_library@1` | use the in-file conservative substitute for `theorem_library` (documented, slower, lower quality) and set `degraded['theorem_library']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - circuit analysis, signal integrity and power-budget reasoning | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - component selection with derating and tolerance analysis | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - simulation setup and result validation | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy on electrical-engineering problem sets | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0772_electrical_engineering.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.electrical.electrical_engineering@1`.
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

### P0773 · `control_systems` — Control Systems & Robotics Engineering

| field | value |
|---|---|
| part id | `P0773` (23/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0773_control_systems.py` |
| module path | `hyperion.t16.domains.control_systems` |
| capability published | `cap.t16.control.control_systems@1` |
| determinism class | `pure` |
| p99 latency budget | 24000 ns (24 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0773_control_systems.txt`](prompts/P0773_control_systems.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0773-control-systems) |

**Mission.** Systems that remain stable in the real world.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **controller design with stability and robustness margin analysis**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **system identification from measured data** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **safety-critical control verification** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **performance measurement in simulation and hardware-in-loop tests** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t16.control.control_systems@1`
- `cap.t16.control.control_systems.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.electrical.electrical_engineering@1` | use the in-file conservative substitute for `electrical_engineering` (documented, slower, lower quality) and set `degraded['electrical_engineering']='local'` |
| `cap.t01.logging.logging_events@1` | use the in-file conservative substitute for `logging_events` (documented, slower, lower quality) and set `degraded['logging_events']='local'` |
| `cap.t10.meta.meta_reasoning@1` | use the in-file conservative substitute for `meta_reasoning` (documented, slower, lower quality) and set `degraded['meta_reasoning']='local'` |
| `cap.t11.proof.proof_repair@1` | use the in-file conservative substitute for `proof_repair` (documented, slower, lower quality) and set `degraded['proof_repair']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - controller design with stability and robustness margin analysis | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - system identification from measured data | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - safety-critical control verification | 520 | Third required mechanism. |
| 6 | Core implementation D - performance measurement in simulation and hardware-in-loop tests | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0773_control_systems.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.control.control_systems@1`.
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

### P0774 · `chemical_engineering` — Chemical & Process Engineering

| field | value |
|---|---|
| part id | `P0774` (24/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0774_chemical_engineering.py` |
| module path | `hyperion.t16.domains.chemical_engineering` |
| capability published | `cap.t16.chemical.chemical_engineering@1` |
| determinism class | `pure` |
| p99 latency budget | 25000 ns (25 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0774_chemical_engineering.txt`](prompts/P0774_chemical_engineering.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0774-chemical-engineering) |

**Mission.** Scales chemistry into processes safely.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **mass and energy balance construction and verification** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **reactor, separation and process-safety reasoning** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **process-simulation orchestration and validation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **accuracy on process-engineering problem sets**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t16.chemical.chemical_engineering@1`
- `cap.t16.chemical.chemical_engineering.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.control.control_systems@1` | use the in-file conservative substitute for `control_systems` (documented, slower, lower quality) and set `degraded['control_systems']='local'` |
| `cap.t01.checksum.checksum_verify@1` | use the in-file conservative substitute for `checksum_verify` (documented, slower, lower quality) and set `degraded['checksum_verify']='local'` |
| `cap.t10.hypothesis.hypothesis_management@1` | use the in-file conservative substitute for `hypothesis_management` (documented, slower, lower quality) and set `degraded['hypothesis_management']='local'` |
| `cap.t11.concurrency.concurrency_verification@1` | use the in-file conservative substitute for `concurrency_verification` (documented, slower, lower quality) and set `degraded['concurrency_verification']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - mass and energy balance construction and verification | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - reactor, separation and process-safety reasoning | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - process-simulation orchestration and validation | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy on process-engineering problem sets | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0774_chemical_engineering.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.chemical.chemical_engineering@1`.
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

### P0775 · `civil_infrastructure` — Civil & Infrastructure Engineering

| field | value |
|---|---|
| part id | `P0775` (25/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0775_civil_infrastructure.py` |
| module path | `hyperion.t16.domains.civil_infrastructure` |
| capability published | `cap.t16.civil.civil_infrastructure@1` |
| determinism class | `pure` |
| p99 latency budget | 26000 ns (26 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0775_civil_infrastructure.txt`](prompts/P0775_civil_infrastructure.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0775-civil-infrastructure) |

**Mission.** Public-safety-grade engineering reasoning.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **structural, geotechnical and hydraulic analysis** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **code compliance and permitting reasoning** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **lifecycle and durability analysis**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **accuracy on civil-engineering analysis tasks** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t16.civil.civil_infrastructure@1`
- `cap.t16.civil.civil_infrastructure.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.chemical.chemical_engineering@1` | use the in-file conservative substitute for `chemical_engineering` (documented, slower, lower quality) and set `degraded['chemical_engineering']='local'` |
| `cap.t01.numeric.numeric_limits@1` | use the in-file conservative substitute for `numeric_limits` (documented, slower, lower quality) and set `degraded['numeric_limits']='local'` |
| `cap.t10.proof.proof_sketch@1` | use the in-file conservative substitute for `proof_sketch` (documented, slower, lower quality) and set `degraded['proof_sketch']='local'` |
| `cap.t11.verification.verification_scheduling@1` | use the in-file conservative substitute for `verification_scheduling` (documented, slower, lower quality) and set `degraded['verification_scheduling']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - structural, geotechnical and hydraulic analysis | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - code compliance and permitting reasoning | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - lifecycle and durability analysis | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy on civil-engineering analysis tasks | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0775_civil_infrastructure.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.civil.civil_infrastructure@1`.
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

### P0776 · `aerospace_engineering` — Aerospace Engineering

| field | value |
|---|---|
| part id | `P0776` (26/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0776_aerospace_engineering.py` |
| module path | `hyperion.t16.domains.aerospace_engineering` |
| capability published | `cap.t16.aerospace.aerospace_engineering@1` |
| determinism class | `pure` |
| p99 latency budget | 27000 ns (27 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0776_aerospace_engineering.txt`](prompts/P0776_aerospace_engineering.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0776-aerospace-engineering) |

**Mission.** Aerodynamics, propulsion and orbital mechanics.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **aerodynamic and propulsion performance analysis** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **trajectory and orbital-mechanics computation with verification**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **reliability and failure-mode analysis for flight systems** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **accuracy on aerospace problem sets** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t16.aerospace.aerospace_engineering@1`
- `cap.t16.aerospace.aerospace_engineering.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.civil.civil_infrastructure@1` | use the in-file conservative substitute for `civil_infrastructure` (documented, slower, lower quality) and set `degraded['civil_infrastructure']='local'` |
| `cap.t01.sandbox.sandbox_policy@1` | use the in-file conservative substitute for `sandbox_policy` (documented, slower, lower quality) and set `degraded['sandbox_policy']='local'` |
| `cap.t10.adversarial.adversarial_reasoning@1` | use the in-file conservative substitute for `adversarial_reasoning` (documented, slower, lower quality) and set `degraded['adversarial_reasoning']='local'` |
| `cap.t11.verification.verification_cache@1` | use the in-file conservative substitute for `verification_cache` (documented, slower, lower quality) and set `degraded['verification_cache']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - aerodynamic and propulsion performance analysis | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - trajectory and orbital-mechanics computation with verification | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - reliability and failure-mode analysis for flight systems | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy on aerospace problem sets | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0776_aerospace_engineering.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.aerospace.aerospace_engineering@1`.
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

### P0777 · `semiconductor_engineering` — Semiconductor & Chip Design

| field | value |
|---|---|
| part id | `P0777` (27/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0777_semiconductor_engineering.py` |
| module path | `hyperion.t16.domains.semiconductor_engineering` |
| capability published | `cap.t16.semiconductor.semiconductor_engineering@1` |
| determinism class | `pure` |
| p99 latency budget | 28000 ns (28 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0777_semiconductor_engineering.txt`](prompts/P0777_semiconductor_engineering.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0777-semiconductor-engineering) |

**Mission.** Understands silicon deeply enough to improve its own hardware.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **RTL, timing, power and area reasoning**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **physical-design and process-technology constraints** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **verification-methodology reasoning for chip design** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **accuracy on chip-design task suites** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t16.semiconductor.semiconductor_engineering@1`
- `cap.t16.semiconductor.semiconductor_engineering.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.aerospace.aerospace_engineering@1` | use the in-file conservative substitute for `aerospace_engineering` (documented, slower, lower quality) and set `degraded['aerospace_engineering']='local'` |
| `cap.t01.abi.abi_result@1` | use the in-file conservative substitute for `abi_result` (documented, slower, lower quality) and set `degraded['abi_result']='local'` |
| `cap.t10.tree.tree_search@1` | use the in-file conservative substitute for `tree_search` (documented, slower, lower quality) and set `degraded['tree_search']='local'` |
| `cap.t11.sat.sat_engine@1` | use the in-file conservative substitute for `sat_engine` (documented, slower, lower quality) and set `degraded['sat_engine']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - RTL, timing, power and area reasoning | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - physical-design and process-technology constraints | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - verification-methodology reasoning for chip design | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy on chip-design task suites | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0777_semiconductor_engineering.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.semiconductor.semiconductor_engineering@1`.
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

### P0778 · `energy_systems` — Energy Systems & Power Engineering

| field | value |
|---|---|
| part id | `P0778` (28/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0778_energy_systems.py` |
| module path | `hyperion.t16.domains.energy_systems` |
| capability published | `cap.t16.energy.energy_systems@1` |
| determinism class | `pure` |
| p99 latency budget | 29000 ns (29 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0778_energy_systems.txt`](prompts/P0778_energy_systems.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0778-energy-systems) |

**Mission.** Grid, generation and storage reasoning at system scale.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **power-flow, stability and dispatch reasoning** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **storage, renewable-integration and reliability analysis** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **techno-economic evaluation with sensitivity analysis** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **accuracy on energy-system analysis tasks**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t16.energy.energy_systems@1`
- `cap.t16.energy.energy_systems.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.semiconductor.semiconductor_engineering@1` | use the in-file conservative substitute for `semiconductor_engineering` (documented, slower, lower quality) and set `degraded['semiconductor_engineering']='local'` |
| `cap.t01.trace.trace_context@1` | use the in-file conservative substitute for `trace_context` (documented, slower, lower quality) and set `degraded['trace_context']='local'` |
| `cap.t10.debate.debate_ensemble@1` | use the in-file conservative substitute for `debate_ensemble` (documented, slower, lower quality) and set `degraded['debate_ensemble']='local'` |
| `cap.t11.abstract.abstract_interpretation@1` | use the in-file conservative substitute for `abstract_interpretation` (documented, slower, lower quality) and set `degraded['abstract_interpretation']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - power-flow, stability and dispatch reasoning | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - storage, renewable-integration and reliability analysis | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - techno-economic evaluation with sensitivity analysis | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy on energy-system analysis tasks | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0778_energy_systems.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.energy.energy_systems@1`.
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

### P0779 · `corporate_law` — Corporate & Transactional Law

| field | value |
|---|---|
| part id | `P0779` (29/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0779_corporate_law.py` |
| module path | `hyperion.t16.domains.corporate_law` |
| capability published | `cap.t16.corporate.corporate_law@1` |
| determinism class | `pure` |
| p99 latency budget | 30000 ns (30 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0779_corporate_law.txt`](prompts/P0779_corporate_law.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0779-corporate-law) |

**Mission.** Deal work at senior-associate quality.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **entity, governance and transaction-structure reasoning** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **diligence, disclosure and covenant analysis** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **jurisdictional variation handling with explicit uncertainty**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **target: exceed Opus 5's corporate-governance gains substantially** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t16.corporate.corporate_law@1`
- `cap.t16.corporate.corporate_law.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.energy.energy_systems@1` | use the in-file conservative substitute for `energy_systems` (documented, slower, lower quality) and set `degraded['energy_systems']='local'` |
| `cap.t01.fixed.fixed_point@1` | use the in-file conservative substitute for `fixed_point` (documented, slower, lower quality) and set `degraded['fixed_point']='local'` |
| `cap.t10.induction.induction_engine@1` | use the in-file conservative substitute for `induction_engine` (documented, slower, lower quality) and set `degraded['induction_engine']='local'` |
| `cap.t11.computer.computer_algebra@1` | use the in-file conservative substitute for `computer_algebra` (documented, slower, lower quality) and set `degraded['computer_algebra']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - entity, governance and transaction-structure reasoning | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - diligence, disclosure and covenant analysis | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - jurisdictional variation handling with explicit uncertainty | 520 | Third required mechanism. |
| 6 | Core implementation D - target: exceed Opus 5's corporate-governance gains substantially | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0779_corporate_law.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.corporate.corporate_law@1`.
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

### P0780 · `litigation_arbitration` — Litigation & Dispute Resolution

| field | value |
|---|---|
| part id | `P0780` (30/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0780_litigation_arbitration.py` |
| module path | `hyperion.t16.domains.litigation_arbitration` |
| capability published | `cap.t16.litigation.litigation_arbitration@1` |
| determinism class | `pure` |
| p99 latency budget | 31000 ns (31 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0780_litigation_arbitration.txt`](prompts/P0780_litigation_arbitration.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0780-litigation-arbitration) |

**Mission.** Argument construction and case analysis.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **claim, defence and remedy analysis with authority citation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **evidence and procedural reasoning**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **arbitration-specific procedural competence** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **target: exceed Opus 5's arbitration-practice gains substantially** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t16.litigation.litigation_arbitration@1`
- `cap.t16.litigation.litigation_arbitration.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.corporate.corporate_law@1` | use the in-file conservative substitute for `corporate_law` (documented, slower, lower quality) and set `degraded['corporate_law']='local'` |
| `cap.t01.config.config_system@1` | use the in-file conservative substitute for `config_system` (documented, slower, lower quality) and set `degraded['config_system']='local'` |
| `cap.t10.commonsense.commonsense_engine@1` | use the in-file conservative substitute for `commonsense_engine` (documented, slower, lower quality) and set `degraded['commonsense_engine']='local'` |
| `cap.t11.symbolic.symbolic_execution@1` | use the in-file conservative substitute for `symbolic_execution` (documented, slower, lower quality) and set `degraded['symbolic_execution']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - claim, defence and remedy analysis with authority citation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - evidence and procedural reasoning | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - arbitration-specific procedural competence | 520 | Third required mechanism. |
| 6 | Core implementation D - target: exceed Opus 5's arbitration-practice gains substantially | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0780_litigation_arbitration.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.litigation.litigation_arbitration@1`.
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

### P0781 · `regulatory_compliance` — Regulatory & Compliance Analysis

| field | value |
|---|---|
| part id | `P0781` (31/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0781_regulatory_compliance.py` |
| module path | `hyperion.t16.domains.regulatory_compliance` |
| capability published | `cap.t16.regulatory.regulatory_compliance@1` |
| determinism class | `pure` |
| p99 latency budget | 32000 ns (32 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0781_regulatory_compliance.txt`](prompts/P0781_regulatory_compliance.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0781-regulatory-compliance) |

**Mission.** Navigates complex overlapping regulation correctly.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **multi-jurisdiction requirement mapping and conflict identification**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **compliance-program design and gap analysis** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **regulatory-change monitoring and impact assessment** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **accuracy on compliance-analysis task sets** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t16.regulatory.regulatory_compliance@1`
- `cap.t16.regulatory.regulatory_compliance.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.litigation.litigation_arbitration@1` | use the in-file conservative substitute for `litigation_arbitration` (documented, slower, lower quality) and set `degraded['litigation_arbitration']='local'` |
| `cap.t01.determinism.determinism_replay@1` | use the in-file conservative substitute for `determinism_replay` (documented, slower, lower quality) and set `degraded['determinism_replay']='local'` |
| `cap.t10.parallel.parallel_reasoning@1` | use the in-file conservative substitute for `parallel_reasoning` (documented, slower, lower quality) and set `degraded['parallel_reasoning']='local'` |
| `cap.t11.crypto.crypto_verification@1` | use the in-file conservative substitute for `crypto_verification` (documented, slower, lower quality) and set `degraded['crypto_verification']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - multi-jurisdiction requirement mapping and conflict identificati | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - compliance-program design and gap analysis | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - regulatory-change monitoring and impact assessment | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy on compliance-analysis task sets | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0781_regulatory_compliance.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.regulatory.regulatory_compliance@1`.
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

### P0782 · `ip_patent` — Intellectual Property & Patent Practice

| field | value |
|---|---|
| part id | `P0782` (32/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0782_ip_patent.py` |
| module path | `hyperion.t16.domains.ip_patent` |
| capability published | `cap.t16.ip.ip_patent@1` |
| determinism class | `pure` |
| p99 latency budget | 33000 ns (33 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0782_ip_patent.txt`](prompts/P0782_ip_patent.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0782-ip-patent) |

**Mission.** Patent-grade technical and legal analysis.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **claim construction, novelty and obviousness analysis** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **prior-art search strategy and analysis** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **specification drafting with enablement rigor** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **accuracy on patent-analysis benchmark tasks**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t16.ip.ip_patent@1`
- `cap.t16.ip.ip_patent.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.regulatory.regulatory_compliance@1` | use the in-file conservative substitute for `regulatory_compliance` (documented, slower, lower quality) and set `degraded['regulatory_compliance']='local'` |
| `cap.t01.compat.compat_shims@1` | use the in-file conservative substitute for `compat_shims` (documented, slower, lower quality) and set `degraded['compat_shims']='local'` |
| `cap.t10.multi.multi_step_arithmetic@1` | use the in-file conservative substitute for `multi_step_arithmetic` (documented, slower, lower quality) and set `degraded['multi_step_arithmetic']='local'` |
| `cap.t11.proof.proof_assistant_ux@1` | use the in-file conservative substitute for `proof_assistant_ux` (documented, slower, lower quality) and set `degraded['proof_assistant_ux']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - claim construction, novelty and obviousness analysis | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - prior-art search strategy and analysis | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - specification drafting with enablement rigor | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy on patent-analysis benchmark tasks | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0782_ip_patent.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.ip.ip_patent@1`.
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

### P0783 · `tax_accounting` — Tax & Accounting

| field | value |
|---|---|
| part id | `P0783` (33/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0783_tax_accounting.py` |
| module path | `hyperion.t16.domains.tax_accounting` |
| capability published | `cap.t16.tax.tax_accounting@1` |
| determinism class | `pure` |
| p99 latency budget | 34000 ns (34 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0783_tax_accounting.txt`](prompts/P0783_tax_accounting.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0783-tax-accounting) |

**Mission.** Numbers that survive an auditor.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **accounting-standard application (GAAP/IFRS) with judgment reasoning** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **tax-position analysis with authority citation and uncertainty flagging** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **financial-statement construction and reconciliation verification**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **accuracy on accounting and tax problem sets** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t16.tax.tax_accounting@1`
- `cap.t16.tax.tax_accounting.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.ip.ip_patent@1` | use the in-file conservative substitute for `ip_patent` (documented, slower, lower quality) and set `degraded['ip_patent']='local'` |
| `cap.t01.secure.secure_zeroize@1` | use the in-file conservative substitute for `secure_zeroize` (documented, slower, lower quality) and set `degraded['secure_zeroize']='local'` |
| `cap.t10.error.error_taxonomy@1` | use the in-file conservative substitute for `error_taxonomy` (documented, slower, lower quality) and set `degraded['error_taxonomy']='local'` |
| `cap.t11.financial.financial_verification@1` | use the in-file conservative substitute for `financial_verification` (documented, slower, lower quality) and set `degraded['financial_verification']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - accounting-standard application (GAAP/IFRS) with judgment reason | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - tax-position analysis with authority citation and uncertainty fl | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - financial-statement construction and reconciliation verification | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy on accounting and tax problem sets | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0783_tax_accounting.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.tax.tax_accounting@1`.
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

### P0784 · `corporate_finance` — Corporate Finance & Valuation

| field | value |
|---|---|
| part id | `P0784` (34/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0784_corporate_finance.py` |
| module path | `hyperion.t16.domains.corporate_finance` |
| capability published | `cap.t16.corporate.corporate_finance@1` |
| determinism class | `pure` |
| p99 latency budget | 35000 ns (35 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0784_corporate_finance.txt`](prompts/P0784_corporate_finance.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0784-corporate-finance) |

**Mission.** Valuation and capital decisions done properly.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **valuation modelling (DCF, comparables, options) with assumption discipline** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **capital-structure and cost-of-capital analysis**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **transaction and synergy analysis with sensitivity ranges** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **accuracy versus expert-analyst reference valuations** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t16.corporate.corporate_finance@1`
- `cap.t16.corporate.corporate_finance.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.tax.tax_accounting@1` | use the in-file conservative substitute for `tax_accounting` (documented, slower, lower quality) and set `degraded['tax_accounting']='local'` |
| `cap.t10.search.search_controller@1` | use the in-file conservative substitute for `search_controller` (documented, slower, lower quality) and set `degraded['search_controller']='local'` |
| `cap.t11.smt.smt_bridge@1` | use the in-file conservative substitute for `smt_bridge` (documented, slower, lower quality) and set `degraded['smt_bridge']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - valuation modelling (DCF, comparables, options) with assumption  | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - capital-structure and cost-of-capital analysis | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - transaction and synergy analysis with sensitivity ranges | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy versus expert-analyst reference valuations | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0784_corporate_finance.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.corporate.corporate_finance@1`.
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

### P0785 · `quantitative_finance` — Quantitative Finance & Derivatives

| field | value |
|---|---|
| part id | `P0785` (35/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0785_quantitative_finance.py` |
| module path | `hyperion.t16.domains.quantitative_finance` |
| capability published | `cap.t16.quantitative.quantitative_finance@1` |
| determinism class | `pure` |
| p99 latency budget | 36000 ns (36 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0785_quantitative_finance.txt`](prompts/P0785_quantitative_finance.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0785-quantitative-finance) |

**Mission.** Pricing, risk and market microstructure.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **derivative pricing with model-risk awareness and calibration**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **risk measurement (VaR, stress, greeks) with correct methodology** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **market-microstructure and execution reasoning** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **accuracy on quantitative-finance problem sets** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t16.quantitative.quantitative_finance@1`
- `cap.t16.quantitative.quantitative_finance.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.corporate.corporate_finance@1` | use the in-file conservative substitute for `corporate_finance` (documented, slower, lower quality) and set `degraded['corporate_finance']='local'` |
| `cap.t01.envelope.envelope_codec@1` | use the in-file conservative substitute for `envelope_codec` (documented, slower, lower quality) and set `degraded['envelope_codec']='local'` |
| `cap.t10.self.self_critique@1` | use the in-file conservative substitute for `self_critique` (documented, slower, lower quality) and set `degraded['self_critique']='local'` |
| `cap.t11.invariant.invariant_inference@1` | use the in-file conservative substitute for `invariant_inference` (documented, slower, lower quality) and set `degraded['invariant_inference']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - derivative pricing with model-risk awareness and calibration | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - risk measurement (VaR, stress, greeks) with correct methodology | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - market-microstructure and execution reasoning | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy on quantitative-finance problem sets | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0785_quantitative_finance.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.quantitative.quantitative_finance@1`.
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

### P0786 · `investment_research` — Investment Research & Financial Analysis

| field | value |
|---|---|
| part id | `P0786` (36/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0786_investment_research.py` |
| module path | `hyperion.t16.domains.investment_research` |
| capability published | `cap.t16.investment.investment_research@1` |
| determinism class | `pure` |
| p99 latency budget | 37000 ns (37 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0786_investment_research.txt`](prompts/P0786_investment_research.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0786-investment-research) |

**Mission.** Research a portfolio manager would act on.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **financial-statement analysis with quality-of-earnings reasoning** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **industry and competitive-position analysis with evidence** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **thesis construction with explicit falsification criteria** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **target: exceed Opus 5's financial-research improvements substantially**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t16.investment.investment_research@1`
- `cap.t16.investment.investment_research.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.quantitative.quantitative_finance@1` | use the in-file conservative substitute for `quantitative_finance` (documented, slower, lower quality) and set `degraded['quantitative_finance']='local'` |
| `cap.t01.dataflow.dataflow_dag@1` | use the in-file conservative substitute for `dataflow_dag` (documented, slower, lower quality) and set `degraded['dataflow_dag']='local'` |
| `cap.t10.abstraction.abstraction_engine@1` | use the in-file conservative substitute for `abstraction_engine` (documented, slower, lower quality) and set `degraded['abstraction_engine']='local'` |
| `cap.t11.exact.exact_arithmetic@1` | use the in-file conservative substitute for `exact_arithmetic` (documented, slower, lower quality) and set `degraded['exact_arithmetic']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - financial-statement analysis with quality-of-earnings reasoning | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - industry and competitive-position analysis with evidence | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - thesis construction with explicit falsification criteria | 520 | Third required mechanism. |
| 6 | Core implementation D - target: exceed Opus 5's financial-research improvements substant | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0786_investment_research.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.investment.investment_research@1`.
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

### P0787 · `risk_management` — Risk Management & Actuarial Science

| field | value |
|---|---|
| part id | `P0787` (37/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0787_risk_management.py` |
| module path | `hyperion.t16.domains.risk_management` |
| capability published | `cap.t16.risk.risk_management@1` |
| determinism class | `pure` |
| p99 latency budget | 38000 ns (38 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0787_risk_management.txt`](prompts/P0787_risk_management.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0787-risk-management) |

**Mission.** Quantifies and prices uncertainty correctly.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **risk-model construction with tail-behaviour rigor** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **actuarial reserving and pricing methodology** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **scenario and stress-test design**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **accuracy on actuarial and risk problem sets** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t16.risk.risk_management@1`
- `cap.t16.risk.risk_management.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.investment.investment_research@1` | use the in-file conservative substitute for `investment_research` (documented, slower, lower quality) and set `degraded['investment_research']='local'` |
| `cap.t01.serialization.serialization_schema@1` | use the in-file conservative substitute for `serialization_schema` (documented, slower, lower quality) and set `degraded['serialization_schema']='local'` |
| `cap.t10.spatial.spatial_reasoning@1` | use the in-file conservative substitute for `spatial_reasoning` (documented, slower, lower quality) and set `degraded['spatial_reasoning']='local'` |
| `cap.t11.property.property_testing_formal@1` | use the in-file conservative substitute for `property_testing_formal` (documented, slower, lower quality) and set `degraded['property_testing_formal']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - risk-model construction with tail-behaviour rigor | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - actuarial reserving and pricing methodology | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - scenario and stress-test design | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy on actuarial and risk problem sets | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0787_risk_management.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.risk.risk_management@1`.
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

### P0788 · `economics` — Economics & Policy Analysis

| field | value |
|---|---|
| part id | `P0788` (38/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0788_economics.py` |
| module path | `hyperion.t16.domains.economics` |
| capability published | `cap.t16.economics.economics@1` |
| determinism class | `pure` |
| p99 latency budget | 39000 ns (39 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0788_economics.txt`](prompts/P0788_economics.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0788-economics) |

**Mission.** Economic reasoning with empirical discipline.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **micro and macro reasoning with model-assumption transparency** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **causal-inference methodology for policy evaluation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **data-source selection and measurement-validity reasoning** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **accuracy on economics problem and analysis sets** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t16.economics.economics@1`
- `cap.t16.economics.economics.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.risk.risk_management@1` | use the in-file conservative substitute for `risk_management` (documented, slower, lower quality) and set `degraded['risk_management']='local'` |
| `cap.t01.bench.bench_harness@1` | use the in-file conservative substitute for `bench_harness` (documented, slower, lower quality) and set `degraded['bench_harness']='local'` |
| `cap.t10.chain.chain_compression@1` | use the in-file conservative substitute for `chain_compression` (documented, slower, lower quality) and set `degraded['chain_compression']='local'` |
| `cap.t11.type.type_safety_proofs@1` | use the in-file conservative substitute for `type_safety_proofs` (documented, slower, lower quality) and set `degraded['type_safety_proofs']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - micro and macro reasoning with model-assumption transparency | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - causal-inference methodology for policy evaluation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - data-source selection and measurement-validity reasoning | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy on economics problem and analysis sets | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0788_economics.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.economics.economics@1`.
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

### P0789 · `management_strategy` — Business Strategy & Management Consulting

| field | value |
|---|---|
| part id | `P0789` (39/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0789_management_strategy.py` |
| module path | `hyperion.t16.domains.management_strategy` |
| capability published | `cap.t16.management.management_strategy@1` |
| determinism class | `pure` |
| p99 latency budget | 40000 ns (40 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0789_management_strategy.txt`](prompts/P0789_management_strategy.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0789-management-strategy) |

**Mission.** Strategy work of partner quality.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **market, competitive and capability analysis with evidence discipline**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **option generation and structured recommendation with tradeoffs** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **implementation-feasibility and change-management reasoning** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **expert-consultant evaluation results** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t16.management.management_strategy@1`
- `cap.t16.management.management_strategy.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.economics.economics@1` | use the in-file conservative substitute for `economics` (documented, slower, lower quality) and set `degraded['economics']='local'` |
| `cap.t01.abi.abi_stability@1` | use the in-file conservative substitute for `abi_stability` (documented, slower, lower quality) and set `degraded['abi_stability']='local'` |
| `cap.t10.reasoning.reasoning_robustness@1` | use the in-file conservative substitute for `reasoning_robustness` (documented, slower, lower quality) and set `degraded['reasoning_robustness']='local'` |
| `cap.t11.rewriting.rewriting_systems@1` | use the in-file conservative substitute for `rewriting_systems` (documented, slower, lower quality) and set `degraded['rewriting_systems']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - market, competitive and capability analysis with evidence discip | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - option generation and structured recommendation with tradeoffs | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - implementation-feasibility and change-management reasoning | 520 | Third required mechanism. |
| 6 | Core implementation D - expert-consultant evaluation results | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0789_management_strategy.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.management.management_strategy@1`.
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

### P0790 · `marketing_growth` — Marketing, Growth & Product Analytics

| field | value |
|---|---|
| part id | `P0790` (40/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0790_marketing_growth.py` |
| module path | `hyperion.t16.domains.marketing_growth` |
| capability published | `cap.t16.marketing.marketing_growth@1` |
| determinism class | `pure` |
| p99 latency budget | 41000 ns (41 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0790_marketing_growth.txt`](prompts/P0790_marketing_growth.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0790-marketing-growth) |

**Mission.** Measurable, honest growth reasoning.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **experiment design with correct statistics and guardrail metrics** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **attribution and cohort analysis methodology** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **positioning and messaging reasoning with audience research** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **accuracy on analytics tasks with known ground truth**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t16.marketing.marketing_growth@1`
- `cap.t16.marketing.marketing_growth.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.management.management_strategy@1` | use the in-file conservative substitute for `management_strategy` (documented, slower, lower quality) and set `degraded['management_strategy']='local'` |
| `cap.t01.retry.retry_idempotency@1` | use the in-file conservative substitute for `retry_idempotency` (documented, slower, lower quality) and set `degraded['retry_idempotency']='local'` |
| `cap.t10.reasoning.reasoning_transfer@1` | use the in-file conservative substitute for `reasoning_transfer` (documented, slower, lower quality) and set `degraded['reasoning_transfer']='local'` |
| `cap.t11.legal.legal_formalisation@1` | use the in-file conservative substitute for `legal_formalisation` (documented, slower, lower quality) and set `degraded['legal_formalisation']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - experiment design with correct statistics and guardrail metrics | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - attribution and cohort analysis methodology | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - positioning and messaging reasoning with audience research | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy on analytics tasks with known ground truth | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0790_marketing_growth.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.marketing.marketing_growth@1`.
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

### P0791 · `operations_supplychain` — Operations & Supply Chain Management

| field | value |
|---|---|
| part id | `P0791` (41/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0791_operations_supplychain.py` |
| module path | `hyperion.t16.domains.operations_supplychain` |
| capability published | `cap.t16.operations.operations_supplychain@1` |
| determinism class | `pure` |
| p99 latency budget | 42000 ns (42 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0791_operations_supplychain.txt`](prompts/P0791_operations_supplychain.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0791-operations-supplychain) |

**Mission.** Real-world logistics and production optimisation.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **inventory, capacity and network-design optimisation** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **demand forecasting with uncertainty and bullwhip reasoning** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **resilience and disruption-scenario analysis**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **accuracy on operations problem sets** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t16.operations.operations_supplychain@1`
- `cap.t16.operations.operations_supplychain.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.marketing.marketing_growth@1` | use the in-file conservative substitute for `marketing_growth` (documented, slower, lower quality) and set `degraded['marketing_growth']='local'` |
| `cap.t10.thought.thought_program_ir@1` | use the in-file conservative substitute for `thought_program_ir` (documented, slower, lower quality) and set `degraded['thought_program_ir']='local'` |
| `cap.t11.logic.logic_core@1` | use the in-file conservative substitute for `logic_core` (documented, slower, lower quality) and set `degraded['logic_core']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - inventory, capacity and network-design optimisation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - demand forecasting with uncertainty and bullwhip reasoning | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - resilience and disruption-scenario analysis | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy on operations problem sets | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0791_operations_supplychain.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.operations.operations_supplychain@1`.
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

### P0792 · `hr_organisational` — Human Resources & Organisational Design

| field | value |
|---|---|
| part id | `P0792` (42/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0792_hr_organisational.py` |
| module path | `hyperion.t16.domains.hr_organisational` |
| capability published | `cap.t16.hr.hr_organisational@1` |
| determinism class | `pure` |
| p99 latency budget | 43000 ns (43 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0792_hr_organisational.txt`](prompts/P0792_hr_organisational.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0792-hr-organisational) |

**Mission.** People decisions made carefully and fairly.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **organisational design and role-architecture reasoning** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **fairness, bias and legal-compliance analysis in people processes**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **performance and compensation-system design** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **expert-practitioner evaluation results** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t16.hr.hr_organisational@1`
- `cap.t16.hr.hr_organisational.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.operations.operations_supplychain@1` | use the in-file conservative substitute for `operations_supplychain` (documented, slower, lower quality) and set `degraded['operations_supplychain']='local'` |
| `cap.t01.omega.omega_bus_ipc@1` | use the in-file conservative substitute for `omega_bus_ipc` (documented, slower, lower quality) and set `degraded['omega_bus_ipc']='local'` |
| `cap.t10.self.self_consistency@1` | use the in-file conservative substitute for `self_consistency` (documented, slower, lower quality) and set `degraded['self_consistency']='local'` |
| `cap.t11.verification.verification_conditions@1` | use the in-file conservative substitute for `verification_conditions` (documented, slower, lower quality) and set `degraded['verification_conditions']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - organisational design and role-architecture reasoning | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - fairness, bias and legal-compliance analysis in people processes | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - performance and compensation-system design | 520 | Third required mechanism. |
| 6 | Core implementation D - expert-practitioner evaluation results | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0792_hr_organisational.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.hr.hr_organisational@1`.
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

### P0793 · `education_pedagogy` — Education & Instructional Design

| field | value |
|---|---|
| part id | `P0793` (43/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0793_education_pedagogy.py` |
| module path | `hyperion.t16.domains.education_pedagogy` |
| capability published | `cap.t16.education.education_pedagogy@1` |
| determinism class | `pure` |
| p99 latency budget | 44000 ns (44 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0793_education_pedagogy.txt`](prompts/P0793_education_pedagogy.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0793-education-pedagogy) |

**Mission.** Designs learning that actually works.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **curriculum and assessment design with learning-science grounding**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **misconception mapping and remediation design** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **differentiation for varied learner needs** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **learning-outcome measurement with real learners** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t16.education.education_pedagogy@1`
- `cap.t16.education.education_pedagogy.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.hr.hr_organisational@1` | use the in-file conservative substitute for `hr_organisational` (documented, slower, lower quality) and set `degraded['hr_organisational']='local'` |
| `cap.t01.task.task_runtime@1` | use the in-file conservative substitute for `task_runtime` (documented, slower, lower quality) and set `degraded['task_runtime']='local'` |
| `cap.t10.analogy.analogy_engine@1` | use the in-file conservative substitute for `analogy_engine` (documented, slower, lower quality) and set `degraded['analogy_engine']='local'` |
| `cap.t11.certified.certified_numerics@1` | use the in-file conservative substitute for `certified_numerics` (documented, slower, lower quality) and set `degraded['certified_numerics']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - curriculum and assessment design with learning-science grounding | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - misconception mapping and remediation design | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - differentiation for varied learner needs | 520 | Third required mechanism. |
| 6 | Core implementation D - learning-outcome measurement with real learners | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0793_education_pedagogy.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.education.education_pedagogy@1`.
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

### P0794 · `psychology_behaviour` — Psychology & Behavioural Science

| field | value |
|---|---|
| part id | `P0794` (44/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0794_psychology_behaviour.py` |
| module path | `hyperion.t16.domains.psychology_behaviour` |
| capability published | `cap.t16.psychology.psychology_behaviour@1` |
| determinism class | `pure` |
| p99 latency budget | 45000 ns (45 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0794_psychology_behaviour.txt`](prompts/P0794_psychology_behaviour.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0794-psychology-behaviour) |

**Mission.** Human behaviour reasoning grounded in replicated evidence.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **theory application with replication-quality awareness** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **assessment-instrument reasoning and validity analysis** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **intervention design with ethical constraints** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **accuracy on psychology question sets weighted by evidence quality**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t16.psychology.psychology_behaviour@1`
- `cap.t16.psychology.psychology_behaviour.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.education.education_pedagogy@1` | use the in-file conservative substitute for `education_pedagogy` (documented, slower, lower quality) and set `degraded['education_pedagogy']='local'` |
| `cap.t01.arena.arena_graph@1` | use the in-file conservative substitute for `arena_graph` (documented, slower, lower quality) and set `degraded['arena_graph']='local'` |
| `cap.t10.temporal.temporal_reasoning@1` | use the in-file conservative substitute for `temporal_reasoning` (documented, slower, lower quality) and set `degraded['temporal_reasoning']='local'` |
| `cap.t11.contract.contract_checking@1` | use the in-file conservative substitute for `contract_checking` (documented, slower, lower quality) and set `degraded['contract_checking']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - theory application with replication-quality awareness | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - assessment-instrument reasoning and validity analysis | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - intervention design with ethical constraints | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy on psychology question sets weighted by evidence qualit | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0794_psychology_behaviour.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.psychology.psychology_behaviour@1`.
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

### P0795 · `linguistics` — Linguistics & Language Science

| field | value |
|---|---|
| part id | `P0795` (45/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0795_linguistics.py` |
| module path | `hyperion.t16.domains.linguistics` |
| capability published | `cap.t16.linguistics.linguistics@1` |
| determinism class | `pure` |
| p99 latency budget | 46000 ns (46 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0795_linguistics.txt`](prompts/P0795_linguistics.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0795-linguistics) |

**Mission.** Deep formal understanding of language itself.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **phonological, syntactic, semantic and pragmatic analysis** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **typological and historical-linguistic reasoning** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **low-resource language analysis methodology**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **accuracy on linguistic-analysis task sets** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t16.linguistics.linguistics@1`
- `cap.t16.linguistics.linguistics.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.psychology.psychology_behaviour@1` | use the in-file conservative substitute for `psychology_behaviour` (documented, slower, lower quality) and set `degraded['psychology_behaviour']='local'` |
| `cap.t01.fuzz.fuzz_engine@1` | use the in-file conservative substitute for `fuzz_engine` (documented, slower, lower quality) and set `degraded['fuzz_engine']='local'` |
| `cap.t10.reasoning.reasoning_memory@1` | use the in-file conservative substitute for `reasoning_memory` (documented, slower, lower quality) and set `degraded['reasoning_memory']='local'` |
| `cap.t11.hoare.hoare_logic_engine@1` | use the in-file conservative substitute for `hoare_logic_engine` (documented, slower, lower quality) and set `degraded['hoare_logic_engine']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - phonological, syntactic, semantic and pragmatic analysis | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - typological and historical-linguistic reasoning | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - low-resource language analysis methodology | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy on linguistic-analysis task sets | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0795_linguistics.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.linguistics.linguistics@1`.
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

### P0796 · `history_humanities` — History & Humanities Scholarship

| field | value |
|---|---|
| part id | `P0796` (46/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0796_history_humanities.py` |
| module path | `hyperion.t16.domains.history_humanities` |
| capability published | `cap.t16.history.history_humanities@1` |
| determinism class | `pure` |
| p99 latency budget | 47000 ns (47 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0796_history_humanities.txt`](prompts/P0796_history_humanities.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0796-history-humanities) |

**Mission.** Source-critical, contextually careful scholarship.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **primary-source analysis with provenance and bias assessment** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **historiographical awareness and interpretive humility**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **chronological and contextual accuracy verification** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **expert-historian evaluation results** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t16.history.history_humanities@1`
- `cap.t16.history.history_humanities.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.linguistics.linguistics@1` | use the in-file conservative substitute for `linguistics` (documented, slower, lower quality) and set `degraded['linguistics']='local'` |
| `cap.t01.manifest.manifest_parser@1` | use the in-file conservative substitute for `manifest_parser` (documented, slower, lower quality) and set `degraded['manifest_parser']='local'` |
| `cap.t10.reasoning.reasoning_faithfulness@1` | use the in-file conservative substitute for `reasoning_faithfulness` (documented, slower, lower quality) and set `degraded['reasoning_faithfulness']='local'` |
| `cap.t11.decision.decision_procedures@1` | use the in-file conservative substitute for `decision_procedures` (documented, slower, lower quality) and set `degraded['decision_procedures']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - primary-source analysis with provenance and bias assessment | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - historiographical awareness and interpretive humility | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - chronological and contextual accuracy verification | 520 | Third required mechanism. |
| 6 | Core implementation D - expert-historian evaluation results | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0796_history_humanities.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.history.history_humanities@1`.
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

### P0797 · `philosophy_ethics` — Philosophy & Applied Ethics

| field | value |
|---|---|
| part id | `P0797` (47/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0797_philosophy_ethics.py` |
| module path | `hyperion.t16.domains.philosophy_ethics` |
| capability published | `cap.t16.philosophy.philosophy_ethics@1` |
| determinism class | `pure` |
| p99 latency budget | 48000 ns (48 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0797_philosophy_ethics.txt`](prompts/P0797_philosophy_ethics.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0797-philosophy-ethics) |

**Mission.** Rigorous argument analysis and ethical reasoning.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **argument reconstruction, validity analysis and objection handling**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **ethical-framework application with pluralism and honesty about disagreement** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **conceptual analysis and distinction drawing** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **expert-philosopher evaluation results** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t16.philosophy.philosophy_ethics@1`
- `cap.t16.philosophy.philosophy_ethics.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.history.history_humanities@1` | use the in-file conservative substitute for `history_humanities` (documented, slower, lower quality) and set `degraded['history_humanities']='local'` |
| `cap.t01.circuit.circuit_breaker@1` | use the in-file conservative substitute for `circuit_breaker` (documented, slower, lower quality) and set `degraded['circuit_breaker']='local'` |
| `cap.t10.subgoal.subgoal_caching@1` | use the in-file conservative substitute for `subgoal_caching` (documented, slower, lower quality) and set `degraded['subgoal_caching']='local'` |
| `cap.t11.scientific.scientific_verification@1` | use the in-file conservative substitute for `scientific_verification` (documented, slower, lower quality) and set `degraded['scientific_verification']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - argument reconstruction, validity analysis and objection handlin | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - ethical-framework application with pluralism and honesty about d | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - conceptual analysis and distinction drawing | 520 | Third required mechanism. |
| 6 | Core implementation D - expert-philosopher evaluation results | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0797_philosophy_ethics.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.philosophy.philosophy_ethics@1`.
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

### P0798 · `agriculture_food` — Agriculture, Food Science & Nutrition

| field | value |
|---|---|
| part id | `P0798` (48/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0798_agriculture_food.py` |
| module path | `hyperion.t16.domains.agriculture_food` |
| capability published | `cap.t16.agriculture.agriculture_food@1` |
| determinism class | `pure` |
| p99 latency budget | 49000 ns (49 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0798_agriculture_food.txt`](prompts/P0798_agriculture_food.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0798-agriculture-food) |

**Mission.** Applied biological and food-system reasoning.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **crop, soil and yield-system reasoning with regional variation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **food-safety, processing and formulation science** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **nutritional analysis with evidence-quality weighting** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **accuracy on agricultural and food-science task sets**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t16.agriculture.agriculture_food@1`
- `cap.t16.agriculture.agriculture_food.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.philosophy.philosophy_ethics@1` | use the in-file conservative substitute for `philosophy_ethics` (documented, slower, lower quality) and set `degraded['philosophy_ethics']='local'` |
| `cap.t01.shutdown.shutdown_drain@1` | use the in-file conservative substitute for `shutdown_drain` (documented, slower, lower quality) and set `degraded['shutdown_drain']='local'` |
| `cap.t10.reasoning.reasoning_spec_doc@1` | use the in-file conservative substitute for `reasoning_spec_doc` (documented, slower, lower quality) and set `degraded['reasoning_spec_doc']='local'` |
| `cap.t11.formal.formal_spec_doc@1` | use the in-file conservative substitute for `formal_spec_doc` (documented, slower, lower quality) and set `degraded['formal_spec_doc']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - crop, soil and yield-system reasoning with regional variation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - food-safety, processing and formulation science | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - nutritional analysis with evidence-quality weighting | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy on agricultural and food-science task sets | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0798_agriculture_food.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.agriculture.agriculture_food@1`.
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

### P0799 · `domain_cross_transfer` — Cross-Domain Synthesis & Interdisciplinary Reasoning

| field | value |
|---|---|
| part id | `P0799` (49/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0799_domain_cross_transfer.py` |
| module path | `hyperion.t16.domains.domain_cross_transfer` |
| capability published | `cap.t16.domain.domain_cross_transfer@1` |
| determinism class | `pure` |
| p99 latency budget | 3000 ns (3 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0799_domain_cross_transfer.txt`](prompts/P0799_domain_cross_transfer.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0799-domain-cross-transfer) |

**Mission.** The breakthroughs live between fields.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **multi-domain problem decomposition and expertise integration** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **terminology and method translation across fields** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **conflict resolution when domain norms disagree**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **accuracy on interdisciplinary benchmark problems** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t16.domain.domain_cross_transfer@1`
- `cap.t16.domain.domain_cross_transfer.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.agriculture.agriculture_food@1` | use the in-file conservative substitute for `agriculture_food` (documented, slower, lower quality) and set `degraded['agriculture_food']='local'` |
| `cap.t10.outcome.outcome_verifier@1` | use the in-file conservative substitute for `outcome_verifier` (documented, slower, lower quality) and set `degraded['outcome_verifier']='local'` |
| `cap.t11.proof.proof_certificate@1` | use the in-file conservative substitute for `proof_certificate` (documented, slower, lower quality) and set `degraded['proof_certificate']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - multi-domain problem decomposition and expertise integration | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - terminology and method translation across fields | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - conflict resolution when domain norms disagree | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy on interdisciplinary benchmark problems | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0799_domain_cross_transfer.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.domain.domain_cross_transfer@1`.
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

### P0800 · `domain_eval_harness` — Domain Expertise Benchmark Harness

| field | value |
|---|---|
| part id | `P0800` (50/50 of T16) |
| tier | `T16` — Domain Superintelligence Packs |
| language | Python 3.13 |
| file to produce | `parts/t16_domains/P0800_domain_eval_harness.py` |
| module path | `hyperion.t16.domains.domain_eval_harness` |
| capability published | `cap.t16.domain.domain_eval_harness@1` |
| determinism class | `pure` |
| p99 latency budget | 4000 ns (4 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GPQA Diamond, Life-sciences suite, GDPval-AA v2 (Elo) |
| worker prompt | [`prompts/P0800_domain_eval_harness.txt`](prompts/P0800_domain_eval_harness.txt) · [inline](docs/PROMPTS_T16.md#prompt-p0800-domain-eval-harness) |

**Mission.** Measures expert-level capability per domain rigorously.

**Tier context.** Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.

**Mandate — all four items are required; none is optional.**

1. Implement **GPQA Diamond, life-sciences and per-domain expert benchmark harnesses** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **expert-grading protocol with inter-rater reliability**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **GPQA Diamond** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **per-domain capability register with honest gap reporting** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Life-sciences suite** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **targets: GPQA 99.6% (Opus 5: ~95.5%), life-sciences 165% of Opus 5** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t16.domain.domain_eval_harness@1`
- `cap.t16.domain.domain_eval_harness.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t16.domain.domain_cross_transfer@1` | use the in-file conservative substitute for `domain_cross_transfer` (documented, slower, lower quality) and set `degraded['domain_cross_transfer']='local'` |
| `cap.t01.atomics.atomics_sync@1` | use the in-file conservative substitute for `atomics_sync` (documented, slower, lower quality) and set `degraded['atomics_sync']='local'` |
| `cap.t10.constraint.constraint_reasoning@1` | use the in-file conservative substitute for `constraint_reasoning` (documented, slower, lower quality) and set `degraded['constraint_reasoning']='local'` |
| `cap.t11.termination.termination_analysis@1` | use the in-file conservative substitute for `termination_analysis` (documented, slower, lower quality) and set `degraded['termination_analysis']='local'` |

**Determinism.** `pure` — byte-identical output for byte-identical input, on every machine, forever. No clock, no RNG, no environment reads, no hash-order iteration, no floating-point reduction whose order depends on thread count.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - GPQA Diamond, life-sciences and per-domain expert benchmark harn | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - expert-grading protocol with inter-rater reliability | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - per-domain capability register with honest gap reporting | 520 | Third required mechanism. |
| 6 | Core implementation D - targets: GPQA 99.6% (Opus 5: ~95.5%), life-sciences 165% of Opus | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t16_domains/P0800_domain_eval_harness.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t16.domain.domain_eval_harness@1`.
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
