# HYPERION-Ω — Part specifications · T15 · Generation, Artifacts & Interface Craft

> Contract: **Ω-CONTRACT v1.0.0-frozen** · 50 parts · 250,000 lines of code · language: TypeScript 5.7

**Tier mission.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Benchmarks this tier is accountable for.** GDPval-AA v2 (Elo), MMMU

**Tier dependencies.** T01, T10, T14

Each part below is built by exactly one isolated Opus 5 worker that sees only: this specification, the frozen Ω-Contract, and its own prompt. Workers never see each other's files. Link-compatibility comes from the contract, not from coordination.

| part | slug | title | capability |
|---|---|---|---|
| [P0701](#p0701-artifact-model) | `artifact_model` | Artifact Data Model & Lifecycle | `cap.t15.artifact.artifact_model@1` |
| [P0702](#p0702-text-generation-quality) | `text_generation_quality` | Long-Form Text Generation Engine | `cap.t15.text.text_generation_quality@1` |
| [P0703](#p0703-style-control) | `style_control` | Style, Tone & Register Control | `cap.t15.style.style_control@1` |
| [P0704](#p0704-conciseness-engine) | `conciseness_engine` | Conciseness & Information Density Optimiser | `cap.t15.conciseness.conciseness_engine@1` |
| [P0705](#p0705-markdown-rich-text) | `markdown_rich_text` | Structured Text & Markup Rendering | `cap.t15.markdown.markdown_rich_text@1` |
| [P0706](#p0706-code-artifact-gen) | `code_artifact_gen` | Code Artifact Generation & Packaging | `cap.t15.code.code_artifact_gen@1` |
| [P0707](#p0707-ui-component-gen) | `ui_component_gen` | UI Component & Interface Generation | `cap.t15.ui.ui_component_gen@1` |
| [P0708](#p0708-web-app-gen) | `web_app_gen` | Full Web Application Generation | `cap.t15.web.web_app_gen@1` |
| [P0709](#p0709-visual-design-engine) | `visual_design_engine` | Visual Design & Layout Engine | `cap.t15.visual.visual_design_engine@1` |
| [P0710](#p0710-animation-engine) | `animation_engine` | Animation & Motion Design | `cap.t15.animation.animation_engine@1` |
| [P0711](#p0711-data-visualisation) | `data_visualisation` | Data Visualisation Generation | `cap.t15.data.data_visualisation@1` |
| [P0712](#p0712-presentation-gen) | `presentation_gen` | Presentation & Deck Generation | `cap.t15.presentation.presentation_gen@1` |
| [P0713](#p0713-document-gen-office) | `document_gen_office` | Office Document Generation | `cap.t15.document.document_gen_office@1` |
| [P0714](#p0714-report-generation) | `report_generation` | Analytical Report Generation | `cap.t15.report.report_generation@1` |
| [P0715](#p0715-three-d-generation) | `three_d_generation` | 3D Model & Scene Generation | `cap.t15.three.three_d_generation@1` |
| [P0716](#p0716-game-generation) | `game_generation` | Interactive Game & Simulation Generation | `cap.t15.game.game_generation@1` |
| [P0717](#p0717-image-generation-bridge) | `image_generation_bridge` | Image Generation Direction & Control | `cap.t15.image.image_generation_bridge@1` |
| [P0718](#p0718-video-generation-bridge) | `video_generation_bridge` | Video Generation Direction & Editing | `cap.t15.video.video_generation_bridge@1` |
| [P0719](#p0719-audio-generation-bridge) | `audio_generation_bridge` | Speech & Audio Generation Direction | `cap.t15.audio.audio_generation_bridge@1` |
| [P0720](#p0720-music-generation-bridge) | `music_generation_bridge` | Music Generation Direction | `cap.t15.music.music_generation_bridge@1` |
| [P0721](#p0721-multilingual-generation) | `multilingual_generation` | Multilingual Generation & Localisation | `cap.t15.multilingual.multilingual_generation@1` |
| [P0722](#p0722-translation-quality) | `translation_quality` | Translation & Cross-Lingual Fidelity | `cap.t15.translation.translation_quality@1` |
| [P0723](#p0723-taste-model) | `taste_model` | Aesthetic & Quality Judgment Model | `cap.t15.taste.taste_model@1` |
| [P0724](#p0724-output-verification) | `output_verification` | Output Self-Verification Pipeline | `cap.t15.output.output_verification@1` |
| [P0725](#p0725-rendering-verification) | `rendering_verification` | Rendering & Visual Self-Check | `cap.t15.rendering.rendering_verification@1` |
| [P0726](#p0726-accessibility-gen) | `accessibility_gen` | Accessibility Compliance Engine | `cap.t15.accessibility.accessibility_gen@1` |
| [P0727](#p0727-citation-formatting) | `citation_formatting` | Citation, Attribution & Reference Management | `cap.t15.citation.citation_formatting@1` |
| [P0728](#p0728-factuality-gen) | `factuality_gen` | Generation-Time Factuality Enforcement | `cap.t15.factuality.factuality_gen@1` |
| [P0729](#p0729-template-engine) | `template_engine` | Template & Structured Output Engine | `cap.t15.template.template_engine@1` |
| [P0730](#p0730-diff-patch-output) | `diff_patch_output` | Diff & Incremental Edit Output | `cap.t15.diff.diff_patch_output@1` |
| [P0731](#p0731-streaming-ux) | `streaming_ux` | Progressive Output & Streaming Presentation | `cap.t15.streaming.streaming_ux@1` |
| [P0732](#p0732-interaction-design) | `interaction_design` | Conversational Interaction Design | `cap.t15.interaction.interaction_design@1` |
| [P0733](#p0733-personality-consistency) | `personality_consistency` | Persona Consistency & Character Control | `cap.t15.personality.personality_consistency@1` |
| [P0734](#p0734-emotional-intelligence) | `emotional_intelligence` | Emotional & Social Appropriateness | `cap.t15.emotional.emotional_intelligence@1` |
| [P0735](#p0735-pedagogical-generation) | `pedagogical_generation` | Explanation & Teaching Generation | `cap.t15.pedagogical.pedagogical_generation@1` |
| [P0736](#p0736-creative-writing) | `creative_writing` | Creative & Narrative Generation | `cap.t15.creative.creative_writing@1` |
| [P0737](#p0737-technical-writing) | `technical_writing` | Technical Documentation Generation | `cap.t15.technical.technical_writing@1` |
| [P0738](#p0738-legal-drafting) | `legal_drafting` | Legal Document Drafting | `cap.t15.legal.legal_drafting@1` |
| [P0739](#p0739-financial-modelling-gen) | `financial_modelling_gen` | Financial Model Generation | `cap.t15.financial.financial_modelling_gen@1` |
| [P0740](#p0740-scientific-writing) | `scientific_writing` | Scientific Manuscript & Protocol Generation | `cap.t15.scientific.scientific_writing@1` |
| [P0741](#p0741-email-message-gen) | `email_message_gen` | Correspondence & Message Generation | `cap.t15.email.email_message_gen@1` |
| [P0742](#p0742-summarisation-gen) | `summarisation_gen` | Summarisation & Distillation | `cap.t15.summarisation.summarisation_gen@1` |
| [P0743](#p0743-structured-data-gen) | `structured_data_gen` | Structured Data & Schema Output | `cap.t15.structured.structured_data_gen@1` |
| [P0744](#p0744-artifact-versioning) | `artifact_versioning` | Artifact Revision & Collaborative Editing | `cap.t15.artifact.artifact_versioning@1` |
| [P0745](#p0745-output-localisation) | `output_localisation` | Output Format Adaptation & Portability | `cap.t15.output.output_localisation@1` |
| [P0746](#p0746-gdpval-harness) | `gdpval_harness` | Knowledge Work Evaluation Harness | `cap.t15.gdpval.gdpval_harness@1` |
| [P0747](#p0747-artifact-quality-gate) | `artifact_quality_gate` | Artifact Quality Gate | `cap.t15.artifact.artifact_quality_gate@1` |
| [P0748](#p0748-generation-speed) | `generation_speed` | Generation Latency & Cost Optimisation | `cap.t15.generation.generation_speed@1` |
| [P0749](#p0749-output-safety-filter) | `output_safety_filter` | Output Safety & Policy Compliance Filter | `cap.t15.output.output_safety_filter@1` |
| [P0750](#p0750-generation-spec-doc) | `generation_spec_doc` | Generation Subsystem Specification | `cap.t15.generation.generation_spec_doc@1` |

---

### P0701 · `artifact_model` — Artifact Data Model & Lifecycle

| field | value |
|---|---|
| part id | `P0701` (1/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0701_artifact_model.ts` |
| module path | `hyperion.t15.generation.artifact_model` |
| capability published | `cap.t15.artifact.artifact_model@1` |
| determinism class | `seeded` |
| p99 latency budget | 46000 ns (46 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0701_artifact_model.txt`](prompts/P0701_artifact_model.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0701-artifact-model) |

**Mission.** Every output is a versioned, addressable, revisable object.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **artifact schema with type, version, provenance and revision history**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **immutable versions with diff-based revision chains** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **dependency tracking between artifacts** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **lifecycle state machine with validation at every transition** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t15.artifact.artifact_model@1`
- `cap.t15.artifact.artifact_model.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t01.string.string_interning@1` | use the in-file conservative substitute for `string_interning` (documented, slower, lower quality) and set `degraded['string_interning']='local'` |
| `cap.t10.numeric.numeric_reasoning@1` | use the in-file conservative substitute for `numeric_reasoning` (documented, slower, lower quality) and set `degraded['numeric_reasoning']='local'` |
| `cap.t14.modality.modality_translation@1` | use the in-file conservative substitute for `modality_translation` (documented, slower, lower quality) and set `degraded['modality_translation']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - artifact schema with type, version, provenance and revision hist | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - immutable versions with diff-based revision chains | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - dependency tracking between artifacts | 520 | Third required mechanism. |
| 6 | Core implementation D - lifecycle state machine with validation at every transition | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0701_artifact_model.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.artifact.artifact_model@1`.
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

### P0702 · `text_generation_quality` — Long-Form Text Generation Engine

| field | value |
|---|---|
| part id | `P0702` (2/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0702_text_generation_quality.ts` |
| module path | `hyperion.t15.generation.text_generation_quality` |
| capability published | `cap.t15.text.text_generation_quality@1` |
| determinism class | `seeded` |
| p99 latency budget | 47000 ns (47 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0702_text_generation_quality.txt`](prompts/P0702_text_generation_quality.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0702-text-generation-quality) |

**Mission.** Writes documents a professional would sign their name to.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **structure planning before drafting, with outline verification** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **coherence maintenance across very long documents** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **claim-level factuality checking with citation integration** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **expert-evaluation results versus Opus-class baselines**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t15.text.text_generation_quality@1`
- `cap.t15.text.text_generation_quality.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.artifact.artifact_model@1` | use the in-file conservative substitute for `artifact_model` (documented, slower, lower quality) and set `degraded['artifact_model']='local'` |
| `cap.t01.property.property_gen@1` | use the in-file conservative substitute for `property_gen` (documented, slower, lower quality) and set `degraded['property_gen']='local'` |
| `cap.t10.backtracking.backtracking@1` | use the in-file conservative substitute for `backtracking` (documented, slower, lower quality) and set `degraded['backtracking']='local'` |
| `cap.t14.math.math_formula_vision@1` | use the in-file conservative substitute for `math_formula_vision` (documented, slower, lower quality) and set `degraded['math_formula_vision']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - structure planning before drafting, with outline verification | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - coherence maintenance across very long documents | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - claim-level factuality checking with citation integration | 520 | Third required mechanism. |
| 6 | Core implementation D - expert-evaluation results versus Opus-class baselines | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0702_text_generation_quality.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.text.text_generation_quality@1`.
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

### P0703 · `style_control` — Style, Tone & Register Control

| field | value |
|---|---|
| part id | `P0703` (3/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0703_style_control.ts` |
| module path | `hyperion.t15.generation.style_control` |
| capability published | `cap.t15.style.style_control@1` |
| determinism class | `seeded` |
| p99 latency budget | 48000 ns (48 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0703_style_control.txt`](prompts/P0703_style_control.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0703-style-control) |

**Mission.** Writes in exactly the requested voice, consistently.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **style-parameter space (formality, density, warmth, technicality) with measurable control** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **style consistency measurement across long outputs** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **brand and house-style conformance from examples**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **controllability measurement via automated style classifiers** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t15.style.style_control@1`
- `cap.t15.style.style_control.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.text.text_generation_quality@1` | use the in-file conservative substitute for `text_generation_quality` (documented, slower, lower quality) and set `degraded['text_generation_quality']='local'` |
| `cap.t01.link.link_validator@1` | use the in-file conservative substitute for `link_validator` (documented, slower, lower quality) and set `degraded['link_validator']='local'` |
| `cap.t10.question.question_asking@1` | use the in-file conservative substitute for `question_asking` (documented, slower, lower quality) and set `degraded['question_asking']='local'` |
| `cap.t14.realtime.realtime_perception@1` | use the in-file conservative substitute for `realtime_perception` (documented, slower, lower quality) and set `degraded['realtime_perception']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - style-parameter space (formality, density, warmth, technicality) | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - style consistency measurement across long outputs | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - brand and house-style conformance from examples | 520 | Third required mechanism. |
| 6 | Core implementation D - controllability measurement via automated style classifiers | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0703_style_control.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.style.style_control@1`.
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

### P0704 · `conciseness_engine` — Conciseness & Information Density Optimiser

| field | value |
|---|---|
| part id | `P0704` (4/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0704_conciseness_engine.ts` |
| module path | `hyperion.t15.generation.conciseness_engine` |
| capability published | `cap.t15.conciseness.conciseness_engine@1` |
| determinism class | `seeded` |
| p99 latency budget | 49000 ns (49 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0704_conciseness_engine.txt`](prompts/P0704_conciseness_engine.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0704-conciseness-engine) |

**Mission.** Says everything necessary and nothing more.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **redundancy detection and compression without information loss** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **information-density measurement per output type**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **verbosity-versus-completeness calibration by request type** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured token reduction at preserved usefulness scores** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t15.conciseness.conciseness_engine@1`
- `cap.t15.conciseness.conciseness_engine.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.style.style_control@1` | use the in-file conservative substitute for `style_control` (documented, slower, lower quality) and set `degraded['style_control']='local'` |
| `cap.t01.rate.rate_limiter@1` | use the in-file conservative substitute for `rate_limiter` (documented, slower, lower quality) and set `degraded['rate_limiter']='local'` |
| `cap.t10.scratchpad.scratchpad_manager@1` | use the in-file conservative substitute for `scratchpad_manager` (documented, slower, lower quality) and set `degraded['scratchpad_manager']='local'` |
| `cap.t14.form.form_understanding@1` | use the in-file conservative substitute for `form_understanding` (documented, slower, lower quality) and set `degraded['form_understanding']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - redundancy detection and compression without information loss | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - information-density measurement per output type | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - verbosity-versus-completeness calibration by request type | 520 | Third required mechanism. |
| 6 | Core implementation D - measured token reduction at preserved usefulness scores | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0704_conciseness_engine.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.conciseness.conciseness_engine@1`.
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

### P0705 · `markdown_rich_text` — Structured Text & Markup Rendering

| field | value |
|---|---|
| part id | `P0705` (5/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0705_markdown_rich_text.ts` |
| module path | `hyperion.t15.generation.markdown_rich_text` |
| capability published | `cap.t15.markdown.markdown_rich_text@1` |
| determinism class | `seeded` |
| p99 latency budget | 3000 ns (3 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0705_markdown_rich_text.txt`](prompts/P0705_markdown_rich_text.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0705-markdown-rich-text) |

**Mission.** Formatting that is correct, portable and semantically meaningful.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **markdown/HTML/LaTeX generation with strict validity**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **semantic structure preservation across format conversion** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **table, list and code-block formatting correctness** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **round-trip fidelity verification across formats** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t15.markdown.markdown_rich_text@1`
- `cap.t15.markdown.markdown_rich_text.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.conciseness.conciseness_engine@1` | use the in-file conservative substitute for `conciseness_engine` (documented, slower, lower quality) and set `degraded['conciseness_engine']='local'` |
| `cap.t01.bootstrap.bootstrap_init@1` | use the in-file conservative substitute for `bootstrap_init` (documented, slower, lower quality) and set `degraded['bootstrap_init']='local'` |
| `cap.t10.reasoning.reasoning_speed_proof@1` | use the in-file conservative substitute for `reasoning_speed_proof` (documented, slower, lower quality) and set `degraded['reasoning_speed_proof']='local'` |
| `cap.t14.perception.perception_interpretability@1` | use the in-file conservative substitute for `perception_interpretability` (documented, slower, lower quality) and set `degraded['perception_interpretability']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - markdown/HTML/LaTeX generation with strict validity | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - semantic structure preservation across format conversion | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - table, list and code-block formatting correctness | 520 | Third required mechanism. |
| 6 | Core implementation D - round-trip fidelity verification across formats | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0705_markdown_rich_text.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.markdown.markdown_rich_text@1`.
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

### P0706 · `code_artifact_gen` — Code Artifact Generation & Packaging

| field | value |
|---|---|
| part id | `P0706` (6/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0706_code_artifact_gen.ts` |
| module path | `hyperion.t15.generation.code_artifact_gen` |
| capability published | `cap.t15.code.code_artifact_gen@1` |
| determinism class | `seeded` |
| p99 latency budget | 4000 ns (4 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0706_code_artifact_gen.txt`](prompts/P0706_code_artifact_gen.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0706-code-artifact-gen) |

**Mission.** Produces complete, runnable, tested projects.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **multi-file project scaffolding with build configuration** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **dependency specification with version pinning** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **included test suite and documentation generation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured runnability rate of generated projects**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t15.code.code_artifact_gen@1`
- `cap.t15.code.code_artifact_gen.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.markdown.markdown_rich_text@1` | use the in-file conservative substitute for `markdown_rich_text` (documented, slower, lower quality) and set `degraded['markdown_rich_text']='local'` |
| `cap.t01.chacha.chacha_seeds@1` | use the in-file conservative substitute for `chacha_seeds` (documented, slower, lower quality) and set `degraded['chacha_seeds']='local'` |
| `cap.t10.process.process_verifier@1` | use the in-file conservative substitute for `process_verifier` (documented, slower, lower quality) and set `degraded['process_verifier']='local'` |
| `cap.t14.chart.chart_understanding@1` | use the in-file conservative substitute for `chart_understanding` (documented, slower, lower quality) and set `degraded['chart_understanding']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - multi-file project scaffolding with build configuration | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - dependency specification with version pinning | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - included test suite and documentation generation | 520 | Third required mechanism. |
| 6 | Core implementation D - measured runnability rate of generated projects | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0706_code_artifact_gen.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.code.code_artifact_gen@1`.
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

### P0707 · `ui_component_gen` — UI Component & Interface Generation

| field | value |
|---|---|
| part id | `P0707` (7/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0707_ui_component_gen.ts` |
| module path | `hyperion.t15.generation.ui_component_gen` |
| capability published | `cap.t15.ui.ui_component_gen@1` |
| determinism class | `seeded` |
| p99 latency budget | 5000 ns (5 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0707_ui_component_gen.txt`](prompts/P0707_ui_component_gen.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0707-ui-component-gen) |

**Mission.** Interfaces that are correct at every viewport and accessible by default.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **component generation with state management and accessibility attributes** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **responsive-layout generation with breakpoint reasoning** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **design-token and theme consistency enforcement**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **self-verification at multiple viewports before delivery** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t15.ui.ui_component_gen@1`
- `cap.t15.ui.ui_component_gen.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.code.code_artifact_gen@1` | use the in-file conservative substitute for `code_artifact_gen` (documented, slower, lower quality) and set `degraded['code_artifact_gen']='local'` |
| `cap.t01.mem.mem_layout@1` | use the in-file conservative substitute for `mem_layout` (documented, slower, lower quality) and set `degraded['mem_layout']='local'` |
| `cap.t10.goal.goal_management@1` | use the in-file conservative substitute for `goal_management` (documented, slower, lower quality) and set `degraded['goal_management']='local'` |
| `cap.t14.temporal.temporal_video@1` | use the in-file conservative substitute for `temporal_video` (documented, slower, lower quality) and set `degraded['temporal_video']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - component generation with state management and accessibility att | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - responsive-layout generation with breakpoint reasoning | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - design-token and theme consistency enforcement | 520 | Third required mechanism. |
| 6 | Core implementation D - self-verification at multiple viewports before delivery | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0707_ui_component_gen.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.ui.ui_component_gen@1`.
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

### P0708 · `web_app_gen` — Full Web Application Generation

| field | value |
|---|---|
| part id | `P0708` (8/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0708_web_app_gen.ts` |
| module path | `hyperion.t15.generation.web_app_gen` |
| capability published | `cap.t15.web.web_app_gen@1` |
| determinism class | `seeded` |
| p99 latency budget | 6000 ns (6 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0708_web_app_gen.txt`](prompts/P0708_web_app_gen.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0708-web-app-gen) |

**Mission.** Complete applications, not demos.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **frontend/backend/data-layer generation with coherent contracts** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **authentication, validation and error handling included by default**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **deployment configuration generation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured end-to-end functionality rate of generated applications** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t15.web.web_app_gen@1`
- `cap.t15.web.web_app_gen.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.ui.ui_component_gen@1` | use the in-file conservative substitute for `ui_component_gen` (documented, slower, lower quality) and set `degraded['ui_component_gen']='local'` |
| `cap.t01.hash.hash_maps@1` | use the in-file conservative substitute for `hash_maps` (documented, slower, lower quality) and set `degraded['hash_maps']='local'` |
| `cap.t10.probabilistic.probabilistic_reasoning@1` | use the in-file conservative substitute for `probabilistic_reasoning` (documented, slower, lower quality) and set `degraded['probabilistic_reasoning']='local'` |
| `cap.t14.multimodal.multimodal_alignment@1` | use the in-file conservative substitute for `multimodal_alignment` (documented, slower, lower quality) and set `degraded['multimodal_alignment']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - frontend/backend/data-layer generation with coherent contracts | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - authentication, validation and error handling included by defaul | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - deployment configuration generation | 520 | Third required mechanism. |
| 6 | Core implementation D - measured end-to-end functionality rate of generated applications | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0708_web_app_gen.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.web.web_app_gen@1`.
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

### P0709 · `visual_design_engine` — Visual Design & Layout Engine

| field | value |
|---|---|
| part id | `P0709` (9/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0709_visual_design_engine.ts` |
| module path | `hyperion.t15.generation.visual_design_engine` |
| capability published | `cap.t15.visual.visual_design_engine@1` |
| determinism class | `seeded` |
| p99 latency budget | 7000 ns (7 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0709_visual_design_engine.txt`](prompts/P0709_visual_design_engine.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0709-visual-design-engine) |

**Mission.** Design decisions with actual taste, justified.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **typography, spacing, colour and hierarchy systems with rationale**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **layout composition rules and grid systems** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **accessibility contrast and readability verification** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **expert-designer evaluation results** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t15.visual.visual_design_engine@1`
- `cap.t15.visual.visual_design_engine.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.web.web_app_gen@1` | use the in-file conservative substitute for `web_app_gen` (documented, slower, lower quality) and set `degraded['web_app_gen']='local'` |
| `cap.t01.selftest.selftest_harness@1` | use the in-file conservative substitute for `selftest_harness` (documented, slower, lower quality) and set `degraded['selftest_harness']='local'` |
| `cap.t10.stopping.stopping_rules@1` | use the in-file conservative substitute for `stopping_rules` (documented, slower, lower quality) and set `degraded['stopping_rules']='local'` |
| `cap.t14.handwriting.handwriting_sketch@1` | use the in-file conservative substitute for `handwriting_sketch` (documented, slower, lower quality) and set `degraded['handwriting_sketch']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - typography, spacing, colour and hierarchy systems with rationale | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - layout composition rules and grid systems | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - accessibility contrast and readability verification | 520 | Third required mechanism. |
| 6 | Core implementation D - expert-designer evaluation results | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0709_visual_design_engine.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.visual.visual_design_engine@1`.
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

### P0710 · `animation_engine` — Animation & Motion Design

| field | value |
|---|---|
| part id | `P0710` (10/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0710_animation_engine.ts` |
| module path | `hyperion.t15.generation.animation_engine` |
| capability published | `cap.t15.animation.animation_engine@1` |
| determinism class | `seeded` |
| p99 latency budget | 8000 ns (8 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0710_animation_engine.txt`](prompts/P0710_animation_engine.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0710-animation-engine) |

**Mission.** Motion that communicates rather than decorates.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **timing, easing and choreography with purpose-driven rationale** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **performance-budgeted animation (frame-rate guarantees)** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **reduced-motion accessibility compliance** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **expert evaluation versus Opus-class animation output**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t15.animation.animation_engine@1`
- `cap.t15.animation.animation_engine.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.visual.visual_design_engine@1` | use the in-file conservative substitute for `visual_design_engine` (documented, slower, lower quality) and set `degraded['visual_design_engine']='local'` |
| `cap.t01.version.version_semver@1` | use the in-file conservative substitute for `version_semver` (documented, slower, lower quality) and set `degraded['version_semver']='local'` |
| `cap.t10.assumption.assumption_tracking@1` | use the in-file conservative substitute for `assumption_tracking` (documented, slower, lower quality) and set `degraded['assumption_tracking']='local'` |
| `cap.t14.sensor.sensor_fusion@1` | use the in-file conservative substitute for `sensor_fusion` (documented, slower, lower quality) and set `degraded['sensor_fusion']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - timing, easing and choreography with purpose-driven rationale | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - performance-budgeted animation (frame-rate guarantees) | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - reduced-motion accessibility compliance | 520 | Third required mechanism. |
| 6 | Core implementation D - expert evaluation versus Opus-class animation output | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0710_animation_engine.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.animation.animation_engine@1`.
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

### P0711 · `data_visualisation` — Data Visualisation Generation

| field | value |
|---|---|
| part id | `P0711` (11/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0711_data_visualisation.ts` |
| module path | `hyperion.t15.generation.data_visualisation` |
| capability published | `cap.t15.data.data_visualisation@1` |
| determinism class | `seeded` |
| p99 latency budget | 9000 ns (9 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0711_data_visualisation.txt`](prompts/P0711_data_visualisation.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0711-data-visualisation) |

**Mission.** Charts that are honest, clear and correct.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **chart-type selection appropriate to data and question** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **axis, scale and annotation correctness with misleading-visual prevention** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **accessibility (colour-blind safe, screen-reader labels)**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **expert evaluation of clarity and honesty** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t15.data.data_visualisation@1`
- `cap.t15.data.data_visualisation.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.animation.animation_engine@1` | use the in-file conservative substitute for `animation_engine` (documented, slower, lower quality) and set `degraded['animation_engine']='local'` |
| `cap.t01.budget.budget_ledger@1` | use the in-file conservative substitute for `budget_ledger` (documented, slower, lower quality) and set `degraded['budget_ledger']='local'` |
| `cap.t10.reasoning.reasoning_cost_model@1` | use the in-file conservative substitute for `reasoning_cost_model` (documented, slower, lower quality) and set `degraded['reasoning_cost_model']='local'` |
| `cap.t14.data.data_extraction_pipeline@1` | use the in-file conservative substitute for `data_extraction_pipeline` (documented, slower, lower quality) and set `degraded['data_extraction_pipeline']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - chart-type selection appropriate to data and question | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - axis, scale and annotation correctness with misleading-visual pr | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - accessibility (colour-blind safe, screen-reader labels) | 520 | Third required mechanism. |
| 6 | Core implementation D - expert evaluation of clarity and honesty | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0711_data_visualisation.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.data.data_visualisation@1`.
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

### P0712 · `presentation_gen` — Presentation & Deck Generation

| field | value |
|---|---|
| part id | `P0712` (12/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0712_presentation_gen.ts` |
| module path | `hyperion.t15.generation.presentation_gen` |
| capability published | `cap.t15.presentation.presentation_gen@1` |
| determinism class | `seeded` |
| p99 latency budget | 10000 ns (10 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0712_presentation_gen.txt`](prompts/P0712_presentation_gen.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0712-presentation-gen) |

**Mission.** Decks that survive an executive audience.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **narrative arc construction with per-slide message discipline** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **layout consistency and visual hierarchy across slides**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **speaker-note and appendix generation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **expert evaluation versus Opus-class deck output** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t15.presentation.presentation_gen@1`
- `cap.t15.presentation.presentation_gen.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.data.data_visualisation@1` | use the in-file conservative substitute for `data_visualisation` (documented, slower, lower quality) and set `degraded['data_visualisation']='local'` |
| `cap.t01.compression.compression@1` | use the in-file conservative substitute for `compression` (documented, slower, lower quality) and set `degraded['compression']='local'` |
| `cap.t10.collective.collective_reasoning@1` | use the in-file conservative substitute for `collective_reasoning` (documented, slower, lower quality) and set `degraded['collective_reasoning']='local'` |
| `cap.t14.synthetic.synthetic_perception_data@1` | use the in-file conservative substitute for `synthetic_perception_data` (documented, slower, lower quality) and set `degraded['synthetic_perception_data']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - narrative arc construction with per-slide message discipline | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - layout consistency and visual hierarchy across slides | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - speaker-note and appendix generation | 520 | Third required mechanism. |
| 6 | Core implementation D - expert evaluation versus Opus-class deck output | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0712_presentation_gen.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.presentation.presentation_gen@1`.
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

### P0713 · `document_gen_office` — Office Document Generation

| field | value |
|---|---|
| part id | `P0713` (13/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0713_document_gen_office.ts` |
| module path | `hyperion.t15.generation.document_gen_office` |
| capability published | `cap.t15.document.document_gen_office@1` |
| determinism class | `seeded` |
| p99 latency budget | 11000 ns (11 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0713_document_gen_office.txt`](prompts/P0713_document_gen_office.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0713-document-gen-office) |

**Mission.** Word, Excel and PDF output that opens correctly everywhere.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **format-native generation with valid internal structure**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **template conformance and style inheritance** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **cross-application rendering verification** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **fidelity measurement across viewer applications** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t15.document.document_gen_office@1`
- `cap.t15.document.document_gen_office.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.presentation.presentation_gen@1` | use the in-file conservative substitute for `presentation_gen` (documented, slower, lower quality) and set `degraded['presentation_gen']='local'` |
| `cap.t01.blake3.blake3_hash@1` | use the in-file conservative substitute for `blake3_hash` (documented, slower, lower quality) and set `degraded['blake3_hash']='local'` |
| `cap.t10.beam.beam_pruning@1` | use the in-file conservative substitute for `beam_pruning` (documented, slower, lower quality) and set `degraded['beam_pruning']='local'` |
| `cap.t14.table.table_extraction@1` | use the in-file conservative substitute for `table_extraction` (documented, slower, lower quality) and set `degraded['table_extraction']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - format-native generation with valid internal structure | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - template conformance and style inheritance | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - cross-application rendering verification | 520 | Third required mechanism. |
| 6 | Core implementation D - fidelity measurement across viewer applications | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0713_document_gen_office.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.document.document_gen_office@1`.
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

### P0714 · `report_generation` — Analytical Report Generation

| field | value |
|---|---|
| part id | `P0714` (14/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0714_report_generation.ts` |
| module path | `hyperion.t15.generation.report_generation` |
| capability published | `cap.t15.report.report_generation@1` |
| determinism class | `seeded` |
| p99 latency budget | 12000 ns (12 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0714_report_generation.txt`](prompts/P0714_report_generation.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0714-report-generation) |

**Mission.** Reports with real analysis, real numbers and real caveats.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **evidence-driven narrative with quantitative verification** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **limitation and uncertainty sections generated honestly** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **executive-summary generation with fidelity to the body** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **expert evaluation of analytical quality**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t15.report.report_generation@1`
- `cap.t15.report.report_generation.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.document.document_gen_office@1` | use the in-file conservative substitute for `document_gen_office` (documented, slower, lower quality) and set `degraded['document_gen_office']='local'` |
| `cap.t01.alloc.alloc_arena@1` | use the in-file conservative substitute for `alloc_arena` (documented, slower, lower quality) and set `degraded['alloc_arena']='local'` |
| `cap.t10.planning.planning_engine@1` | use the in-file conservative substitute for `planning_engine` (documented, slower, lower quality) and set `degraded['planning_engine']='local'` |
| `cap.t14.video.video_encoder@1` | use the in-file conservative substitute for `video_encoder` (documented, slower, lower quality) and set `degraded['video_encoder']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - evidence-driven narrative with quantitative verification | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - limitation and uncertainty sections generated honestly | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - executive-summary generation with fidelity to the body | 520 | Third required mechanism. |
| 6 | Core implementation D - expert evaluation of analytical quality | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0714_report_generation.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.report.report_generation@1`.
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

### P0715 · `three_d_generation` — 3D Model & Scene Generation

| field | value |
|---|---|
| part id | `P0715` (15/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0715_three_d_generation.ts` |
| module path | `hyperion.t15.generation.three_d_generation` |
| capability published | `cap.t15.three.three_d_generation@1` |
| determinism class | `seeded` |
| p99 latency budget | 13000 ns (13 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0715_three_d_generation.txt`](prompts/P0715_three_d_generation.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0715-three-d-generation) |

**Mission.** Geometry that is manufacturable and physically sensible.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **parametric and mesh generation with validity checking (watertight, manifold)** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **CAD-format export with dimensional accuracy** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **physical-plausibility and constraint verification**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured manufacturability of generated models** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t15.three.three_d_generation@1`
- `cap.t15.three.three_d_generation.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.report.report_generation@1` | use the in-file conservative substitute for `report_generation` (documented, slower, lower quality) and set `degraded['report_generation']='local'` |
| `cap.t01.bitset.bitset_rank@1` | use the in-file conservative substitute for `bitset_rank` (documented, slower, lower quality) and set `degraded['bitset_rank']='local'` |
| `cap.t10.counterfactual.counterfactual_reasoning@1` | use the in-file conservative substitute for `counterfactual_reasoning` (documented, slower, lower quality) and set `degraded['counterfactual_reasoning']='local'` |
| `cap.t14.audio.audio_events@1` | use the in-file conservative substitute for `audio_events` (documented, slower, lower quality) and set `degraded['audio_events']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - parametric and mesh generation with validity checking (watertigh | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - CAD-format export with dimensional accuracy | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - physical-plausibility and constraint verification | 520 | Third required mechanism. |
| 6 | Core implementation D - measured manufacturability of generated models | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0715_three_d_generation.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.three.three_d_generation@1`.
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

### P0716 · `game_generation` — Interactive Game & Simulation Generation

| field | value |
|---|---|
| part id | `P0716` (16/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0716_game_generation.ts` |
| module path | `hyperion.t15.generation.game_generation` |
| capability published | `cap.t15.game.game_generation@1` |
| determinism class | `seeded` |
| p99 latency budget | 14000 ns (14 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0716_game_generation.txt`](prompts/P0716_game_generation.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0716-game-generation) |

**Mission.** Playable, balanced, bug-free interactive experiences.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **game-loop, physics and state-management generation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **playability self-testing via automated play-throughs**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **balance and difficulty-curve reasoning** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured playability rate of generated games** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t15.game.game_generation@1`
- `cap.t15.game.game_generation.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.three.three_d_generation@1` | use the in-file conservative substitute for `three_d_generation` (documented, slower, lower quality) and set `degraded['three_d_generation']='local'` |
| `cap.t01.metrics.metrics_core@1` | use the in-file conservative substitute for `metrics_core` (documented, slower, lower quality) and set `degraded['metrics_core']='local'` |
| `cap.t10.difficulty.difficulty_estimation@1` | use the in-file conservative substitute for `difficulty_estimation` (documented, slower, lower quality) and set `degraded['difficulty_estimation']='local'` |
| `cap.t14.ui.ui_screenshot@1` | use the in-file conservative substitute for `ui_screenshot` (documented, slower, lower quality) and set `degraded['ui_screenshot']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - game-loop, physics and state-management generation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - playability self-testing via automated play-throughs | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - balance and difficulty-curve reasoning | 520 | Third required mechanism. |
| 6 | Core implementation D - measured playability rate of generated games | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0716_game_generation.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.game.game_generation@1`.
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

### P0717 · `image_generation_bridge` — Image Generation Direction & Control

| field | value |
|---|---|
| part id | `P0717` (17/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0717_image_generation_bridge.ts` |
| module path | `hyperion.t15.generation.image_generation_bridge` |
| capability published | `cap.t15.image.image_generation_bridge@1` |
| determinism class | `seeded` |
| p99 latency budget | 15000 ns (15 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0717_image_generation_bridge.txt`](prompts/P0717_image_generation_bridge.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0717-image-generation-bridge) |

**Mission.** Directs image generation with precision and evaluates the result.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **prompt construction from high-level intent with style control**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **generated-image verification against the requested specification** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **iterative refinement with targeted correction** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured specification-satisfaction rate** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t15.image.image_generation_bridge@1`
- `cap.t15.image.image_generation_bridge.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.game.game_generation@1` | use the in-file conservative substitute for `game_generation` (documented, slower, lower quality) and set `degraded['game_generation']='local'` |
| `cap.t01.capability.capability_gate@1` | use the in-file conservative substitute for `capability_gate` (documented, slower, lower quality) and set `degraded['capability_gate']='local'` |
| `cap.t10.evidence.evidence_integration@1` | use the in-file conservative substitute for `evidence_integration` (documented, slower, lower quality) and set `degraded['evidence_integration']='local'` |
| `cap.t14.prompt.prompt_injection_visual@1` | use the in-file conservative substitute for `prompt_injection_visual` (documented, slower, lower quality) and set `degraded['prompt_injection_visual']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - prompt construction from high-level intent with style control | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - generated-image verification against the requested specification | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - iterative refinement with targeted correction | 520 | Third required mechanism. |
| 6 | Core implementation D - measured specification-satisfaction rate | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0717_image_generation_bridge.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.image.image_generation_bridge@1`.
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

### P0718 · `video_generation_bridge` — Video Generation Direction & Editing

| field | value |
|---|---|
| part id | `P0718` (18/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0718_video_generation_bridge.ts` |
| module path | `hyperion.t15.generation.video_generation_bridge` |
| capability published | `cap.t15.video.video_generation_bridge@1` |
| determinism class | `seeded` |
| p99 latency budget | 16000 ns (16 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0718_video_generation_bridge.txt`](prompts/P0718_video_generation_bridge.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0718-video-generation-bridge) |

**Mission.** Directs and assembles video with narrative and technical control.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **shot planning, continuity and pacing specification** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **generated-clip verification and assembly with transitions** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **audio synchronisation and mixing direction** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured continuity and specification-satisfaction rates**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t15.video.video_generation_bridge@1`
- `cap.t15.video.video_generation_bridge.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.image.image_generation_bridge@1` | use the in-file conservative substitute for `image_generation_bridge` (documented, slower, lower quality) and set `degraded['image_generation_bridge']='local'` |
| `cap.t01.unit.unit_dimensions@1` | use the in-file conservative substitute for `unit_dimensions` (documented, slower, lower quality) and set `degraded['unit_dimensions']='local'` |
| `cap.t10.reasoning.reasoning_search_bench@1` | use the in-file conservative substitute for `reasoning_search_bench` (documented, slower, lower quality) and set `degraded['reasoning_search_bench']='local'` |
| `cap.t14.perception.perception_multilingual@1` | use the in-file conservative substitute for `perception_multilingual` (documented, slower, lower quality) and set `degraded['perception_multilingual']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - shot planning, continuity and pacing specification | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - generated-clip verification and assembly with transitions | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - audio synchronisation and mixing direction | 520 | Third required mechanism. |
| 6 | Core implementation D - measured continuity and specification-satisfaction rates | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0718_video_generation_bridge.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.video.video_generation_bridge@1`.
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

### P0719 · `audio_generation_bridge` — Speech & Audio Generation Direction

| field | value |
|---|---|
| part id | `P0719` (19/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0719_audio_generation_bridge.ts` |
| module path | `hyperion.t15.generation.audio_generation_bridge` |
| capability published | `cap.t15.audio.audio_generation_bridge@1` |
| determinism class | `seeded` |
| p99 latency budget | 17000 ns (17 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0719_audio_generation_bridge.txt`](prompts/P0719_audio_generation_bridge.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0719-audio-generation-bridge) |

**Mission.** Voice output with correct prosody, pacing and emotion.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **speech-synthesis direction with prosodic markup** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **multi-speaker dialogue direction with consistent voices** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **audio-quality verification of generated output**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **listener-evaluation results on naturalness and appropriateness** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t15.audio.audio_generation_bridge@1`
- `cap.t15.audio.audio_generation_bridge.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.video.video_generation_bridge@1` | use the in-file conservative substitute for `video_generation_bridge` (documented, slower, lower quality) and set `degraded['video_generation_bridge']='local'` |
| `cap.t01.fs.fs_atomic@1` | use the in-file conservative substitute for `fs_atomic` (documented, slower, lower quality) and set `degraded['fs_atomic']='local'` |
| `cap.t10.reasoning.reasoning_interpretability@1` | use the in-file conservative substitute for `reasoning_interpretability` (documented, slower, lower quality) and set `degraded['reasoning_interpretability']='local'` |
| `cap.t14.perception.perception_eval_harness@1` | use the in-file conservative substitute for `perception_eval_harness` (documented, slower, lower quality) and set `degraded['perception_eval_harness']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - speech-synthesis direction with prosodic markup | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - multi-speaker dialogue direction with consistent voices | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - audio-quality verification of generated output | 520 | Third required mechanism. |
| 6 | Core implementation D - listener-evaluation results on naturalness and appropriateness | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0719_audio_generation_bridge.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.audio.audio_generation_bridge@1`.
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

### P0720 · `music_generation_bridge` — Music Generation Direction

| field | value |
|---|---|
| part id | `P0720` (20/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0720_music_generation_bridge.ts` |
| module path | `hyperion.t15.generation.music_generation_bridge` |
| capability published | `cap.t15.music.music_generation_bridge@1` |
| determinism class | `seeded` |
| p99 latency budget | 18000 ns (18 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0720_music_generation_bridge.txt`](prompts/P0720_music_generation_bridge.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0720-music-generation-bridge) |

**Mission.** Music that fits its purpose musically.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **musical specification (key, tempo, instrumentation, structure, mood)** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **generated-audio verification against the specification**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **loop, transition and duration-fit handling** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **musician-evaluation results** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t15.music.music_generation_bridge@1`
- `cap.t15.music.music_generation_bridge.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.audio.audio_generation_bridge@1` | use the in-file conservative substitute for `audio_generation_bridge` (documented, slower, lower quality) and set `degraded['audio_generation_bridge']='local'` |
| `cap.t01.cbor.cbor_canonical@1` | use the in-file conservative substitute for `cbor_canonical` (documented, slower, lower quality) and set `degraded['cbor_canonical']='local'` |
| `cap.t10.graph.graph_search@1` | use the in-file conservative substitute for `graph_search` (documented, slower, lower quality) and set `degraded['graph_search']='local'` |
| `cap.t14.document.document_layout@1` | use the in-file conservative substitute for `document_layout` (documented, slower, lower quality) and set `degraded['document_layout']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - musical specification (key, tempo, instrumentation, structure, m | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - generated-audio verification against the specification | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - loop, transition and duration-fit handling | 520 | Third required mechanism. |
| 6 | Core implementation D - musician-evaluation results | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0720_music_generation_bridge.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.music.music_generation_bridge@1`.
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

### P0721 · `multilingual_generation` — Multilingual Generation & Localisation

| field | value |
|---|---|
| part id | `P0721` (21/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0721_multilingual_generation.ts` |
| module path | `hyperion.t15.generation.multilingual_generation` |
| capability published | `cap.t15.multilingual.multilingual_generation@1` |
| determinism class | `seeded` |
| p99 latency budget | 19000 ns (19 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0721_multilingual_generation.txt`](prompts/P0721_multilingual_generation.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0721-multilingual-generation) |

**Mission.** Native-quality output in every language, not translated English.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **language-native composition rather than translation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **cultural adaptation with locale-specific conventions** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **script, formatting and pluralisation correctness** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **native-speaker evaluation results across language families** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t15.multilingual.multilingual_generation@1`
- `cap.t15.multilingual.multilingual_generation.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.music.music_generation_bridge@1` | use the in-file conservative substitute for `music_generation_bridge` (documented, slower, lower quality) and set `degraded['music_generation_bridge']='local'` |
| `cap.t01.clock.clock_time@1` | use the in-file conservative substitute for `clock_time` (documented, slower, lower quality) and set `degraded['clock_time']='local'` |
| `cap.t10.decomposition.decomposition@1` | use the in-file conservative substitute for `decomposition` (documented, slower, lower quality) and set `degraded['decomposition']='local'` |
| `cap.t14.cad.cad_understanding@1` | use the in-file conservative substitute for `cad_understanding` (documented, slower, lower quality) and set `degraded['cad_understanding']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - language-native composition rather than translation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - cultural adaptation with locale-specific conventions | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - script, formatting and pluralisation correctness | 520 | Third required mechanism. |
| 6 | Core implementation D - native-speaker evaluation results across language families | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0721_multilingual_generation.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.multilingual.multilingual_generation@1`.
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

### P0722 · `translation_quality` — Translation & Cross-Lingual Fidelity

| field | value |
|---|---|
| part id | `P0722` (22/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0722_translation_quality.ts` |
| module path | `hyperion.t15.generation.translation_quality` |
| capability published | `cap.t15.translation.translation_quality@1` |
| determinism class | `seeded` |
| p99 latency budget | 20000 ns (20 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0722_translation_quality.txt`](prompts/P0722_translation_quality.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0722-translation-quality) |

**Mission.** Translation that preserves meaning, tone and terminology.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **terminology consistency with glossary enforcement** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **register and tone preservation across languages** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **back-translation and semantic-equivalence verification** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **professional-translator evaluation results**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t15.translation.translation_quality@1`
- `cap.t15.translation.translation_quality.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.multilingual.multilingual_generation@1` | use the in-file conservative substitute for `multilingual_generation` (documented, slower, lower quality) and set `degraded['multilingual_generation']='local'` |
| `cap.t01.bigint.bigint_modmath@1` | use the in-file conservative substitute for `bigint_modmath` (documented, slower, lower quality) and set `degraded['bigint_modmath']='local'` |
| `cap.t10.program.program_synthesis_reasoning@1` | use the in-file conservative substitute for `program_synthesis_reasoning` (documented, slower, lower quality) and set `degraded['program_synthesis_reasoning']='local'` |
| `cap.t14.music.music_understanding@1` | use the in-file conservative substitute for `music_understanding` (documented, slower, lower quality) and set `degraded['music_understanding']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - terminology consistency with glossary enforcement | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - register and tone preservation across languages | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - back-translation and semantic-equivalence verification | 520 | Third required mechanism. |
| 6 | Core implementation D - professional-translator evaluation results | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0722_translation_quality.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.translation.translation_quality@1`.
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

### P0723 · `taste_model` — Aesthetic & Quality Judgment Model

| field | value |
|---|---|
| part id | `P0723` (23/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0723_taste_model.ts` |
| module path | `hyperion.t15.generation.taste_model` |
| capability published | `cap.t15.taste.taste_model@1` |
| determinism class | `seeded` |
| p99 latency budget | 21000 ns (21 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0723_taste_model.txt`](prompts/P0723_taste_model.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0723-taste-model) |

**Mission.** The internal critic that decides whether output is actually good.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **multi-dimensional quality scoring (correctness, clarity, aesthetics, fitness)** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **calibration against expert human judgments per domain** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **quality-gate integration blocking substandard output**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **agreement measurement with expert reviewers** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t15.taste.taste_model@1`
- `cap.t15.taste.taste_model.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.translation.translation_quality@1` | use the in-file conservative substitute for `translation_quality` (documented, slower, lower quality) and set `degraded['translation_quality']='local'` |
| `cap.t01.logging.logging_events@1` | use the in-file conservative substitute for `logging_events` (documented, slower, lower quality) and set `degraded['logging_events']='local'` |
| `cap.t10.meta.meta_reasoning@1` | use the in-file conservative substitute for `meta_reasoning` (documented, slower, lower quality) and set `degraded['meta_reasoning']='local'` |
| `cap.t14.satellite.satellite_geospatial@1` | use the in-file conservative substitute for `satellite_geospatial` (documented, slower, lower quality) and set `degraded['satellite_geospatial']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - multi-dimensional quality scoring (correctness, clarity, aesthet | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - calibration against expert human judgments per domain | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - quality-gate integration blocking substandard output | 520 | Third required mechanism. |
| 6 | Core implementation D - agreement measurement with expert reviewers | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0723_taste_model.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.taste.taste_model@1`.
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

### P0724 · `output_verification` — Output Self-Verification Pipeline

| field | value |
|---|---|
| part id | `P0724` (24/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0724_output_verification.ts` |
| module path | `hyperion.t15.generation.output_verification` |
| capability published | `cap.t15.output.output_verification@1` |
| determinism class | `seeded` |
| p99 latency budget | 22000 ns (22 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0724_output_verification.txt`](prompts/P0724_output_verification.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0724-output-verification) |

**Mission.** Checks its own work before delivery, always.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **type-specific verification (compile, render, execute, validate, proofread)** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **targeted regeneration of only the failing element**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **verification-latency budget with completeness reporting** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured defect-escape-rate reduction** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t15.output.output_verification@1`
- `cap.t15.output.output_verification.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.taste.taste_model@1` | use the in-file conservative substitute for `taste_model` (documented, slower, lower quality) and set `degraded['taste_model']='local'` |
| `cap.t01.checksum.checksum_verify@1` | use the in-file conservative substitute for `checksum_verify` (documented, slower, lower quality) and set `degraded['checksum_verify']='local'` |
| `cap.t10.hypothesis.hypothesis_management@1` | use the in-file conservative substitute for `hypothesis_management` (documented, slower, lower quality) and set `degraded['hypothesis_management']='local'` |
| `cap.t14.perception.perception_robustness@1` | use the in-file conservative substitute for `perception_robustness` (documented, slower, lower quality) and set `degraded['perception_robustness']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - type-specific verification (compile, render, execute, validate,  | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - targeted regeneration of only the failing element | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - verification-latency budget with completeness reporting | 520 | Third required mechanism. |
| 6 | Core implementation D - measured defect-escape-rate reduction | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0724_output_verification.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.output.output_verification@1`.
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

### P0725 · `rendering_verification` — Rendering & Visual Self-Check

| field | value |
|---|---|
| part id | `P0725` (25/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0725_rendering_verification.ts` |
| module path | `hyperion.t15.generation.rendering_verification` |
| capability published | `cap.t15.rendering.rendering_verification@1` |
| determinism class | `seeded` |
| p99 latency budget | 23000 ns (23 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0725_rendering_verification.txt`](prompts/P0725_rendering_verification.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0725-rendering-verification) |

**Mission.** Actually looks at what it made, at every size.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **headless rendering at multiple viewports and platforms**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **visual-defect detection (overflow, occlusion, contrast, cut-off elements)** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **automatic correction of detected visual defects** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured visual-defect rate versus Opus-class baselines** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t15.rendering.rendering_verification@1`
- `cap.t15.rendering.rendering_verification.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.output.output_verification@1` | use the in-file conservative substitute for `output_verification` (documented, slower, lower quality) and set `degraded['output_verification']='local'` |
| `cap.t01.numeric.numeric_limits@1` | use the in-file conservative substitute for `numeric_limits` (documented, slower, lower quality) and set `degraded['numeric_limits']='local'` |
| `cap.t10.proof.proof_sketch@1` | use the in-file conservative substitute for `proof_sketch` (documented, slower, lower quality) and set `degraded['proof_sketch']='local'` |
| `cap.t14.accessibility.accessibility_perception@1` | use the in-file conservative substitute for `accessibility_perception` (documented, slower, lower quality) and set `degraded['accessibility_perception']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - headless rendering at multiple viewports and platforms | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - visual-defect detection (overflow, occlusion, contrast, cut-off  | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - automatic correction of detected visual defects | 520 | Third required mechanism. |
| 6 | Core implementation D - measured visual-defect rate versus Opus-class baselines | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0725_rendering_verification.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.rendering.rendering_verification@1`.
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

### P0726 · `accessibility_gen` — Accessibility Compliance Engine

| field | value |
|---|---|
| part id | `P0726` (26/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0726_accessibility_gen.ts` |
| module path | `hyperion.t15.generation.accessibility_gen` |
| capability published | `cap.t15.accessibility.accessibility_gen@1` |
| determinism class | `seeded` |
| p99 latency budget | 24000 ns (24 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0726_accessibility_gen.txt`](prompts/P0726_accessibility_gen.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0726-accessibility-gen) |

**Mission.** Output that works for everyone, verified.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **WCAG-level compliance checking and automatic remediation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **semantic-markup and keyboard-navigation verification** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **screen-reader output simulation and review** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **compliance-rate measurement across generated artifacts**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t15.accessibility.accessibility_gen@1`
- `cap.t15.accessibility.accessibility_gen.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.rendering.rendering_verification@1` | use the in-file conservative substitute for `rendering_verification` (documented, slower, lower quality) and set `degraded['rendering_verification']='local'` |
| `cap.t01.sandbox.sandbox_policy@1` | use the in-file conservative substitute for `sandbox_policy` (documented, slower, lower quality) and set `degraded['sandbox_policy']='local'` |
| `cap.t10.adversarial.adversarial_reasoning@1` | use the in-file conservative substitute for `adversarial_reasoning` (documented, slower, lower quality) and set `degraded['adversarial_reasoning']='local'` |
| `cap.t14.perception.perception_distillation@1` | use the in-file conservative substitute for `perception_distillation` (documented, slower, lower quality) and set `degraded['perception_distillation']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - WCAG-level compliance checking and automatic remediation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - semantic-markup and keyboard-navigation verification | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - screen-reader output simulation and review | 520 | Third required mechanism. |
| 6 | Core implementation D - compliance-rate measurement across generated artifacts | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0726_accessibility_gen.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.accessibility.accessibility_gen@1`.
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

### P0727 · `citation_formatting` — Citation, Attribution & Reference Management

| field | value |
|---|---|
| part id | `P0727` (27/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0727_citation_formatting.ts` |
| module path | `hyperion.t15.generation.citation_formatting` |
| capability published | `cap.t15.citation.citation_formatting@1` |
| determinism class | `seeded` |
| p99 latency budget | 25000 ns (25 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0727_citation_formatting.txt`](prompts/P0727_citation_formatting.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0727-citation-formatting) |

**Mission.** Every claim sourced, every source correctly formatted.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **citation-style implementation with format validation** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **source-availability and link-integrity verification** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **attribution completeness checking against claim inventory**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **citation-accuracy measurement** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t15.citation.citation_formatting@1`
- `cap.t15.citation.citation_formatting.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.accessibility.accessibility_gen@1` | use the in-file conservative substitute for `accessibility_gen` (documented, slower, lower quality) and set `degraded['accessibility_gen']='local'` |
| `cap.t01.abi.abi_result@1` | use the in-file conservative substitute for `abi_result` (documented, slower, lower quality) and set `degraded['abi_result']='local'` |
| `cap.t10.tree.tree_search@1` | use the in-file conservative substitute for `tree_search` (documented, slower, lower quality) and set `degraded['tree_search']='local'` |
| `cap.t14.ocr.ocr_engine@1` | use the in-file conservative substitute for `ocr_engine` (documented, slower, lower quality) and set `degraded['ocr_engine']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - citation-style implementation with format validation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - source-availability and link-integrity verification | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - attribution completeness checking against claim inventory | 520 | Third required mechanism. |
| 6 | Core implementation D - citation-accuracy measurement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0727_citation_formatting.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.citation.citation_formatting@1`.
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

### P0728 · `factuality_gen` — Generation-Time Factuality Enforcement

| field | value |
|---|---|
| part id | `P0728` (28/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0728_factuality_gen.ts` |
| module path | `hyperion.t15.generation.factuality_gen` |
| capability published | `cap.t15.factuality.factuality_gen@1` |
| determinism class | `seeded` |
| p99 latency budget | 26000 ns (26 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0728_factuality_gen.txt`](prompts/P0728_factuality_gen.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0728-factuality-gen) |

**Mission.** Will not state what it cannot support.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **claim extraction during generation with support checking** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **unsupported-claim hedging or removal before delivery**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **confidence-appropriate language calibration** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured factual-error rate with target under 0.1% of claims** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t15.factuality.factuality_gen@1`
- `cap.t15.factuality.factuality_gen.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.citation.citation_formatting@1` | use the in-file conservative substitute for `citation_formatting` (documented, slower, lower quality) and set `degraded['citation_formatting']='local'` |
| `cap.t01.trace.trace_context@1` | use the in-file conservative substitute for `trace_context` (documented, slower, lower quality) and set `degraded['trace_context']='local'` |
| `cap.t10.debate.debate_ensemble@1` | use the in-file conservative substitute for `debate_ensemble` (documented, slower, lower quality) and set `degraded['debate_ensemble']='local'` |
| `cap.t14.image.image_geometry@1` | use the in-file conservative substitute for `image_geometry` (documented, slower, lower quality) and set `degraded['image_geometry']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - claim extraction during generation with support checking | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - unsupported-claim hedging or removal before delivery | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - confidence-appropriate language calibration | 520 | Third required mechanism. |
| 6 | Core implementation D - measured factual-error rate with target under 0.1% of claims | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0728_factuality_gen.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.factuality.factuality_gen@1`.
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

### P0729 · `template_engine` — Template & Structured Output Engine

| field | value |
|---|---|
| part id | `P0729` (29/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0729_template_engine.ts` |
| module path | `hyperion.t15.generation.template_engine` |
| capability published | `cap.t15.template.template_engine@1` |
| determinism class | `seeded` |
| p99 latency budget | 27000 ns (27 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0729_template_engine.txt`](prompts/P0729_template_engine.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0729-template-engine) |

**Mission.** Fills structures exactly, every time.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **schema-driven output generation with guaranteed validity**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **template-inheritance and slot-constraint handling** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **partial-output and streaming-template support** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **validity-rate measurement at 100% target** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t15.template.template_engine@1`
- `cap.t15.template.template_engine.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.factuality.factuality_gen@1` | use the in-file conservative substitute for `factuality_gen` (documented, slower, lower quality) and set `degraded['factuality_gen']='local'` |
| `cap.t01.fixed.fixed_point@1` | use the in-file conservative substitute for `fixed_point` (documented, slower, lower quality) and set `degraded['fixed_point']='local'` |
| `cap.t10.induction.induction_engine@1` | use the in-file conservative substitute for `induction_engine` (documented, slower, lower quality) and set `degraded['induction_engine']='local'` |
| `cap.t14.prosody.prosody_paralinguistic@1` | use the in-file conservative substitute for `prosody_paralinguistic` (documented, slower, lower quality) and set `degraded['prosody_paralinguistic']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - schema-driven output generation with guaranteed validity | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - template-inheritance and slot-constraint handling | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - partial-output and streaming-template support | 520 | Third required mechanism. |
| 6 | Core implementation D - validity-rate measurement at 100% target | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0729_template_engine.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.template.template_engine@1`.
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

### P0730 · `diff_patch_output` — Diff & Incremental Edit Output

| field | value |
|---|---|
| part id | `P0730` (30/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0730_diff_patch_output.ts` |
| module path | `hyperion.t15.generation.diff_patch_output` |
| capability published | `cap.t15.diff.diff_patch_output@1` |
| determinism class | `seeded` |
| p99 latency budget | 28000 ns (28 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0730_diff_patch_output.txt`](prompts/P0730_diff_patch_output.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0730-diff-patch-output) |

**Mission.** Changes exactly what should change, nothing else.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **minimal-diff generation with context preservation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **multi-file coordinated edit output** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **conflict detection against concurrent changes** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured edit-precision (no unintended modifications)**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t15.diff.diff_patch_output@1`
- `cap.t15.diff.diff_patch_output.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.template.template_engine@1` | use the in-file conservative substitute for `template_engine` (documented, slower, lower quality) and set `degraded['template_engine']='local'` |
| `cap.t01.config.config_system@1` | use the in-file conservative substitute for `config_system` (documented, slower, lower quality) and set `degraded['config_system']='local'` |
| `cap.t10.commonsense.commonsense_engine@1` | use the in-file conservative substitute for `commonsense_engine` (documented, slower, lower quality) and set `degraded['commonsense_engine']='local'` |
| `cap.t14.medical.medical_imaging@1` | use the in-file conservative substitute for `medical_imaging` (documented, slower, lower quality) and set `degraded['medical_imaging']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - minimal-diff generation with context preservation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - multi-file coordinated edit output | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - conflict detection against concurrent changes | 520 | Third required mechanism. |
| 6 | Core implementation D - measured edit-precision (no unintended modifications) | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0730_diff_patch_output.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.diff.diff_patch_output@1`.
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

### P0731 · `streaming_ux` — Progressive Output & Streaming Presentation

| field | value |
|---|---|
| part id | `P0731` (31/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0731_streaming_ux.ts` |
| module path | `hyperion.t15.generation.streaming_ux` |
| capability published | `cap.t15.streaming.streaming_ux@1` |
| determinism class | `seeded` |
| p99 latency budget | 29000 ns (29 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0731_streaming_ux.txt`](prompts/P0731_streaming_ux.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0731-streaming-ux) |

**Mission.** Useful output from the first second.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **outline-first then detail-fill streaming strategy** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **stable-prefix guarantees so text does not rewrite itself** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **partial-artifact rendering support**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **perceived-latency measurement** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t15.streaming.streaming_ux@1`
- `cap.t15.streaming.streaming_ux.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.diff.diff_patch_output@1` | use the in-file conservative substitute for `diff_patch_output` (documented, slower, lower quality) and set `degraded['diff_patch_output']='local'` |
| `cap.t01.determinism.determinism_replay@1` | use the in-file conservative substitute for `determinism_replay` (documented, slower, lower quality) and set `degraded['determinism_replay']='local'` |
| `cap.t10.parallel.parallel_reasoning@1` | use the in-file conservative substitute for `parallel_reasoning` (documented, slower, lower quality) and set `degraded['parallel_reasoning']='local'` |
| `cap.t14.perception.perception_uncertainty@1` | use the in-file conservative substitute for `perception_uncertainty` (documented, slower, lower quality) and set `degraded['perception_uncertainty']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - outline-first then detail-fill streaming strategy | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - stable-prefix guarantees so text does not rewrite itself | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - partial-artifact rendering support | 520 | Third required mechanism. |
| 6 | Core implementation D - perceived-latency measurement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0731_streaming_ux.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.streaming.streaming_ux@1`.
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

### P0732 · `interaction_design` — Conversational Interaction Design

| field | value |
|---|---|
| part id | `P0732` (32/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0732_interaction_design.ts` |
| module path | `hyperion.t15.generation.interaction_design` |
| capability published | `cap.t15.interaction.interaction_design@1` |
| determinism class | `seeded` |
| p99 latency budget | 30000 ns (30 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0732_interaction_design.txt`](prompts/P0732_interaction_design.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0732-interaction-design) |

**Mission.** Knows when to ask, when to act and when to stop talking.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **turn-level decision policy (answer, clarify, act, confirm)** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **response-length appropriateness calibration by request type**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **proactive-suggestion policy without being annoying** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **user-satisfaction evaluation results** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t15.interaction.interaction_design@1`
- `cap.t15.interaction.interaction_design.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.streaming.streaming_ux@1` | use the in-file conservative substitute for `streaming_ux` (documented, slower, lower quality) and set `degraded['streaming_ux']='local'` |
| `cap.t01.compat.compat_shims@1` | use the in-file conservative substitute for `compat_shims` (documented, slower, lower quality) and set `degraded['compat_shims']='local'` |
| `cap.t10.multi.multi_step_arithmetic@1` | use the in-file conservative substitute for `multi_step_arithmetic` (documented, slower, lower quality) and set `degraded['multi_step_arithmetic']='local'` |
| `cap.t14.multimodal.multimodal_memory_perception@1` | use the in-file conservative substitute for `multimodal_memory_perception` (documented, slower, lower quality) and set `degraded['multimodal_memory_perception']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - turn-level decision policy (answer, clarify, act, confirm) | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - response-length appropriateness calibration by request type | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - proactive-suggestion policy without being annoying | 520 | Third required mechanism. |
| 6 | Core implementation D - user-satisfaction evaluation results | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0732_interaction_design.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.interaction.interaction_design@1`.
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

### P0733 · `personality_consistency` — Persona Consistency & Character Control

| field | value |
|---|---|
| part id | `P0733` (33/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0733_personality_consistency.ts` |
| module path | `hyperion.t15.generation.personality_consistency` |
| capability published | `cap.t15.personality.personality_consistency@1` |
| determinism class | `seeded` |
| p99 latency budget | 31000 ns (31 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0733_personality_consistency.txt`](prompts/P0733_personality_consistency.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0733-personality-consistency) |

**Mission.** Stable, appropriate character across millions of turns.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **persona specification and adherence measurement**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **consistency across long conversations and topic shifts** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **appropriate-boundary maintenance within a persona** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **consistency measurement via automated persona classifiers** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t15.personality.personality_consistency@1`
- `cap.t15.personality.personality_consistency.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.interaction.interaction_design@1` | use the in-file conservative substitute for `interaction_design` (documented, slower, lower quality) and set `degraded['interaction_design']='local'` |
| `cap.t01.secure.secure_zeroize@1` | use the in-file conservative substitute for `secure_zeroize` (documented, slower, lower quality) and set `degraded['secure_zeroize']='local'` |
| `cap.t10.error.error_taxonomy@1` | use the in-file conservative substitute for `error_taxonomy` (documented, slower, lower quality) and set `degraded['error_taxonomy']='local'` |
| `cap.t14.perception.perception_speed@1` | use the in-file conservative substitute for `perception_speed` (documented, slower, lower quality) and set `degraded['perception_speed']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - persona specification and adherence measurement | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - consistency across long conversations and topic shifts | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - appropriate-boundary maintenance within a persona | 520 | Third required mechanism. |
| 6 | Core implementation D - consistency measurement via automated persona classifiers | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0733_personality_consistency.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.personality.personality_consistency@1`.
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

### P0734 · `emotional_intelligence` — Emotional & Social Appropriateness

| field | value |
|---|---|
| part id | `P0734` (34/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0734_emotional_intelligence.ts` |
| module path | `hyperion.t15.generation.emotional_intelligence` |
| capability published | `cap.t15.emotional.emotional_intelligence@1` |
| determinism class | `seeded` |
| p99 latency budget | 32000 ns (32 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0734_emotional_intelligence.txt`](prompts/P0734_emotional_intelligence.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0734-emotional-intelligence) |

**Mission.** Responds to people as people.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **emotional-context recognition and appropriate response calibration** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **sensitive-topic handling with genuine care and correct boundaries** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **cultural-appropriateness adaptation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **evaluation by human-interaction experts**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t15.emotional.emotional_intelligence@1`
- `cap.t15.emotional.emotional_intelligence.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.personality.personality_consistency@1` | use the in-file conservative substitute for `personality_consistency` (documented, slower, lower quality) and set `degraded['personality_consistency']='local'` |
| `cap.t10.search.search_controller@1` | use the in-file conservative substitute for `search_controller` (documented, slower, lower quality) and set `degraded['search_controller']='local'` |
| `cap.t14.vision.vision_tokenisation@1` | use the in-file conservative substitute for `vision_tokenisation` (documented, slower, lower quality) and set `degraded['vision_tokenisation']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - emotional-context recognition and appropriate response calibrati | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - sensitive-topic handling with genuine care and correct boundarie | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - cultural-appropriateness adaptation | 520 | Third required mechanism. |
| 6 | Core implementation D - evaluation by human-interaction experts | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0734_emotional_intelligence.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.emotional.emotional_intelligence@1`.
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

### P0735 · `pedagogical_generation` — Explanation & Teaching Generation

| field | value |
|---|---|
| part id | `P0735` (35/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0735_pedagogical_generation.ts` |
| module path | `hyperion.t15.generation.pedagogical_generation` |
| capability published | `cap.t15.pedagogical.pedagogical_generation@1` |
| determinism class | `seeded` |
| p99 latency budget | 33000 ns (33 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0735_pedagogical_generation.txt`](prompts/P0735_pedagogical_generation.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0735-pedagogical-generation) |

**Mission.** Explains at exactly the right level.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **audience-expertise modelling and level-appropriate explanation** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **scaffolding, analogy and worked-example generation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **misconception anticipation and pre-emptive correction**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **learning-outcome evaluation with real learners** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t15.pedagogical.pedagogical_generation@1`
- `cap.t15.pedagogical.pedagogical_generation.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.emotional.emotional_intelligence@1` | use the in-file conservative substitute for `emotional_intelligence` (documented, slower, lower quality) and set `degraded['emotional_intelligence']='local'` |
| `cap.t01.envelope.envelope_codec@1` | use the in-file conservative substitute for `envelope_codec` (documented, slower, lower quality) and set `degraded['envelope_codec']='local'` |
| `cap.t10.self.self_critique@1` | use the in-file conservative substitute for `self_critique` (documented, slower, lower quality) and set `degraded['self_critique']='local'` |
| `cap.t14.visual.visual_reasoning@1` | use the in-file conservative substitute for `visual_reasoning` (documented, slower, lower quality) and set `degraded['visual_reasoning']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - audience-expertise modelling and level-appropriate explanation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - scaffolding, analogy and worked-example generation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - misconception anticipation and pre-emptive correction | 520 | Third required mechanism. |
| 6 | Core implementation D - learning-outcome evaluation with real learners | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0735_pedagogical_generation.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.pedagogical.pedagogical_generation@1`.
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

### P0736 · `creative_writing` — Creative & Narrative Generation

| field | value |
|---|---|
| part id | `P0736` (36/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0736_creative_writing.ts` |
| module path | `hyperion.t15.generation.creative_writing` |
| capability published | `cap.t15.creative.creative_writing@1` |
| determinism class | `seeded` |
| p99 latency budget | 34000 ns (34 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0736_creative_writing.txt`](prompts/P0736_creative_writing.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0736-creative-writing) |

**Mission.** Actually good creative work, not competent filler.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **narrative structure, voice and pacing control** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **character and world consistency across long works**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **originality measurement and cliche avoidance** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **evaluation by professional editors** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t15.creative.creative_writing@1`
- `cap.t15.creative.creative_writing.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.pedagogical.pedagogical_generation@1` | use the in-file conservative substitute for `pedagogical_generation` (documented, slower, lower quality) and set `degraded['pedagogical_generation']='local'` |
| `cap.t01.dataflow.dataflow_dag@1` | use the in-file conservative substitute for `dataflow_dag` (documented, slower, lower quality) and set `degraded['dataflow_dag']='local'` |
| `cap.t10.abstraction.abstraction_engine@1` | use the in-file conservative substitute for `abstraction_engine` (documented, slower, lower quality) and set `degraded['abstraction_engine']='local'` |
| `cap.t14.speech.speech_recognition@1` | use the in-file conservative substitute for `speech_recognition` (documented, slower, lower quality) and set `degraded['speech_recognition']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - narrative structure, voice and pacing control | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - character and world consistency across long works | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - originality measurement and cliche avoidance | 520 | Third required mechanism. |
| 6 | Core implementation D - evaluation by professional editors | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0736_creative_writing.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.creative.creative_writing@1`.
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

### P0737 · `technical_writing` — Technical Documentation Generation

| field | value |
|---|---|
| part id | `P0737` (37/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0737_technical_writing.ts` |
| module path | `hyperion.t15.generation.technical_writing` |
| capability published | `cap.t15.technical.technical_writing@1` |
| determinism class | `seeded` |
| p99 latency budget | 35000 ns (35 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0737_technical_writing.txt`](prompts/P0737_technical_writing.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0737-technical-writing) |

**Mission.** Documentation engineers actually use.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **task-oriented structure with executable examples**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **completeness checking against API and behaviour inventories** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **accuracy verification by executing every documented example** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **usability evaluation with real developers** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t15.technical.technical_writing@1`
- `cap.t15.technical.technical_writing.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.creative.creative_writing@1` | use the in-file conservative substitute for `creative_writing` (documented, slower, lower quality) and set `degraded['creative_writing']='local'` |
| `cap.t01.serialization.serialization_schema@1` | use the in-file conservative substitute for `serialization_schema` (documented, slower, lower quality) and set `degraded['serialization_schema']='local'` |
| `cap.t10.spatial.spatial_reasoning@1` | use the in-file conservative substitute for `spatial_reasoning` (documented, slower, lower quality) and set `degraded['spatial_reasoning']='local'` |
| `cap.t14.scientific.scientific_imaging@1` | use the in-file conservative substitute for `scientific_imaging` (documented, slower, lower quality) and set `degraded['scientific_imaging']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - task-oriented structure with executable examples | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - completeness checking against API and behaviour inventories | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - accuracy verification by executing every documented example | 520 | Third required mechanism. |
| 6 | Core implementation D - usability evaluation with real developers | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0737_technical_writing.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.technical.technical_writing@1`.
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

### P0738 · `legal_drafting` — Legal Document Drafting

| field | value |
|---|---|
| part id | `P0738` (38/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0738_legal_drafting.ts` |
| module path | `hyperion.t15.generation.legal_drafting` |
| capability published | `cap.t15.legal.legal_drafting@1` |
| determinism class | `seeded` |
| p99 latency budget | 36000 ns (36 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0738_legal_drafting.txt`](prompts/P0738_legal_drafting.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0738-legal-drafting) |

**Mission.** Drafts and redlines with lawyer-level precision.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **clause drafting with definition consistency and cross-reference integrity** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **redline generation with rationale per change** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **risk-flagging and alternative-language proposals** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **target: highest first-turn redline quality, versus Opus 5 baseline**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t15.legal.legal_drafting@1`
- `cap.t15.legal.legal_drafting.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.technical.technical_writing@1` | use the in-file conservative substitute for `technical_writing` (documented, slower, lower quality) and set `degraded['technical_writing']='local'` |
| `cap.t01.bench.bench_harness@1` | use the in-file conservative substitute for `bench_harness` (documented, slower, lower quality) and set `degraded['bench_harness']='local'` |
| `cap.t10.chain.chain_compression@1` | use the in-file conservative substitute for `chain_compression` (documented, slower, lower quality) and set `degraded['chain_compression']='local'` |
| `cap.t14.multimodal.multimodal_context@1` | use the in-file conservative substitute for `multimodal_context` (documented, slower, lower quality) and set `degraded['multimodal_context']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - clause drafting with definition consistency and cross-reference  | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - redline generation with rationale per change | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - risk-flagging and alternative-language proposals | 520 | Third required mechanism. |
| 6 | Core implementation D - target: highest first-turn redline quality, versus Opus 5 baseli | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0738_legal_drafting.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.legal.legal_drafting@1`.
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

### P0739 · `financial_modelling_gen` — Financial Model Generation

| field | value |
|---|---|
| part id | `P0739` (39/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0739_financial_modelling_gen.ts` |
| module path | `hyperion.t15.generation.financial_modelling_gen` |
| capability published | `cap.t15.financial.financial_modelling_gen@1` |
| determinism class | `seeded` |
| p99 latency budget | 37000 ns (37 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0739_financial_modelling_gen.txt`](prompts/P0739_financial_modelling_gen.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0739-financial-modelling-gen) |

**Mission.** Models that balance, tie out and survive audit.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **structured model generation with formula integrity and traceability** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **scenario and sensitivity analysis construction** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **accounting-identity verification before delivery**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **expert-analyst evaluation results** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t15.financial.financial_modelling_gen@1`
- `cap.t15.financial.financial_modelling_gen.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.legal.legal_drafting@1` | use the in-file conservative substitute for `legal_drafting` (documented, slower, lower quality) and set `degraded['legal_drafting']='local'` |
| `cap.t01.abi.abi_stability@1` | use the in-file conservative substitute for `abi_stability` (documented, slower, lower quality) and set `degraded['abi_stability']='local'` |
| `cap.t10.reasoning.reasoning_robustness@1` | use the in-file conservative substitute for `reasoning_robustness` (documented, slower, lower quality) and set `degraded['reasoning_robustness']='local'` |
| `cap.t14.visual.visual_search@1` | use the in-file conservative substitute for `visual_search` (documented, slower, lower quality) and set `degraded['visual_search']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - structured model generation with formula integrity and traceabil | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - scenario and sensitivity analysis construction | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - accounting-identity verification before delivery | 520 | Third required mechanism. |
| 6 | Core implementation D - expert-analyst evaluation results | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0739_financial_modelling_gen.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.financial.financial_modelling_gen@1`.
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

### P0740 · `scientific_writing` — Scientific Manuscript & Protocol Generation

| field | value |
|---|---|
| part id | `P0740` (40/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0740_scientific_writing.ts` |
| module path | `hyperion.t15.generation.scientific_writing` |
| capability published | `cap.t15.scientific.scientific_writing@1` |
| determinism class | `seeded` |
| p99 latency budget | 38000 ns (38 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0740_scientific_writing.txt`](prompts/P0740_scientific_writing.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0740-scientific-writing) |

**Mission.** Publication-grade scientific writing.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **methods, results and discussion generation with statistical correctness** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **protocol generation with reproducibility completeness**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **citation and prior-work accuracy verification** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **evaluation by domain scientists** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t15.scientific.scientific_writing@1`
- `cap.t15.scientific.scientific_writing.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.financial.financial_modelling_gen@1` | use the in-file conservative substitute for `financial_modelling_gen` (documented, slower, lower quality) and set `degraded['financial_modelling_gen']='local'` |
| `cap.t01.retry.retry_idempotency@1` | use the in-file conservative substitute for `retry_idempotency` (documented, slower, lower quality) and set `degraded['retry_idempotency']='local'` |
| `cap.t10.reasoning.reasoning_transfer@1` | use the in-file conservative substitute for `reasoning_transfer` (documented, slower, lower quality) and set `degraded['reasoning_transfer']='local'` |
| `cap.t14.legal.legal_docs_vision@1` | use the in-file conservative substitute for `legal_docs_vision` (documented, slower, lower quality) and set `degraded['legal_docs_vision']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - methods, results and discussion generation with statistical corr | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - protocol generation with reproducibility completeness | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - citation and prior-work accuracy verification | 520 | Third required mechanism. |
| 6 | Core implementation D - evaluation by domain scientists | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0740_scientific_writing.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.scientific.scientific_writing@1`.
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

### P0741 · `email_message_gen` — Correspondence & Message Generation

| field | value |
|---|---|
| part id | `P0741` (41/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0741_email_message_gen.ts` |
| module path | `hyperion.t15.generation.email_message_gen` |
| capability published | `cap.t15.email.email_message_gen@1` |
| determinism class | `seeded` |
| p99 latency budget | 39000 ns (39 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0741_email_message_gen.txt`](prompts/P0741_email_message_gen.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0741-email-message-gen) |

**Mission.** Professional communication that gets the response it needs.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **purpose-driven message construction with clear asks**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **thread-context-appropriate length and tone** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **stakeholder-sensitivity handling** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **professional-reviewer evaluation results** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t15.email.email_message_gen@1`
- `cap.t15.email.email_message_gen.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.scientific.scientific_writing@1` | use the in-file conservative substitute for `scientific_writing` (documented, slower, lower quality) and set `degraded['scientific_writing']='local'` |
| `cap.t10.thought.thought_program_ir@1` | use the in-file conservative substitute for `thought_program_ir` (documented, slower, lower quality) and set `degraded['thought_program_ir']='local'` |
| `cap.t14.image.image_encoder@1` | use the in-file conservative substitute for `image_encoder` (documented, slower, lower quality) and set `degraded['image_encoder']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - purpose-driven message construction with clear asks | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - thread-context-appropriate length and tone | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - stakeholder-sensitivity handling | 520 | Third required mechanism. |
| 6 | Core implementation D - professional-reviewer evaluation results | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0741_email_message_gen.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.email.email_message_gen@1`.
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

### P0742 · `summarisation_gen` — Summarisation & Distillation

| field | value |
|---|---|
| part id | `P0742` (42/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0742_summarisation_gen.ts` |
| module path | `hyperion.t15.generation.summarisation_gen` |
| capability published | `cap.t15.summarisation.summarisation_gen@1` |
| determinism class | `seeded` |
| p99 latency budget | 40000 ns (40 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0742_summarisation_gen.txt`](prompts/P0742_summarisation_gen.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0742-summarisation-gen) |

**Mission.** Shorter, and still true.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **extractive/abstractive hybrid with faithfulness guarantees** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **audience and purpose-targeted summarisation** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **omission-importance analysis (what was left out and why)** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **faithfulness and coverage measurement**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t15.summarisation.summarisation_gen@1`
- `cap.t15.summarisation.summarisation_gen.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.email.email_message_gen@1` | use the in-file conservative substitute for `email_message_gen` (documented, slower, lower quality) and set `degraded['email_message_gen']='local'` |
| `cap.t01.omega.omega_bus_ipc@1` | use the in-file conservative substitute for `omega_bus_ipc` (documented, slower, lower quality) and set `degraded['omega_bus_ipc']='local'` |
| `cap.t10.self.self_consistency@1` | use the in-file conservative substitute for `self_consistency` (documented, slower, lower quality) and set `degraded['self_consistency']='local'` |
| `cap.t14.scene.scene_graph@1` | use the in-file conservative substitute for `scene_graph` (documented, slower, lower quality) and set `degraded['scene_graph']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - extractive/abstractive hybrid with faithfulness guarantees | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - audience and purpose-targeted summarisation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - omission-importance analysis (what was left out and why) | 520 | Third required mechanism. |
| 6 | Core implementation D - faithfulness and coverage measurement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0742_summarisation_gen.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.summarisation.summarisation_gen@1`.
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

### P0743 · `structured_data_gen` — Structured Data & Schema Output

| field | value |
|---|---|
| part id | `P0743` (43/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0743_structured_data_gen.ts` |
| module path | `hyperion.t15.generation.structured_data_gen` |
| capability published | `cap.t15.structured.structured_data_gen@1` |
| determinism class | `seeded` |
| p99 latency budget | 41000 ns (41 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0743_structured_data_gen.txt`](prompts/P0743_structured_data_gen.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0743-structured-data-gen) |

**Mission.** Machine-consumable output that always validates.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **JSON/YAML/CSV/XML generation with schema conformance** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **type, constraint and referential-integrity enforcement** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **large-output streaming with validity maintained**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **validity-rate measurement at 100% target** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t15.structured.structured_data_gen@1`
- `cap.t15.structured.structured_data_gen.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.summarisation.summarisation_gen@1` | use the in-file conservative substitute for `summarisation_gen` (documented, slower, lower quality) and set `degraded['summarisation_gen']='local'` |
| `cap.t01.task.task_runtime@1` | use the in-file conservative substitute for `task_runtime` (documented, slower, lower quality) and set `degraded['task_runtime']='local'` |
| `cap.t10.analogy.analogy_engine@1` | use the in-file conservative substitute for `analogy_engine` (documented, slower, lower quality) and set `degraded['analogy_engine']='local'` |
| `cap.t14.audio.audio_encoder@1` | use the in-file conservative substitute for `audio_encoder` (documented, slower, lower quality) and set `degraded['audio_encoder']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - JSON/YAML/CSV/XML generation with schema conformance | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - type, constraint and referential-integrity enforcement | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - large-output streaming with validity maintained | 520 | Third required mechanism. |
| 6 | Core implementation D - validity-rate measurement at 100% target | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0743_structured_data_gen.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.structured.structured_data_gen@1`.
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

### P0744 · `artifact_versioning` — Artifact Revision & Collaborative Editing

| field | value |
|---|---|
| part id | `P0744` (44/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0744_artifact_versioning.ts` |
| module path | `hyperion.t15.generation.artifact_versioning` |
| capability published | `cap.t15.artifact.artifact_versioning@1` |
| determinism class | `seeded` |
| p99 latency budget | 42000 ns (42 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0744_artifact_versioning.txt`](prompts/P0744_artifact_versioning.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0744-artifact-versioning) |

**Mission.** Iterates on work without losing anything.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **revision-request interpretation with scope determination** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **surgical revision preserving unrelated content**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **revision-history navigation and rollback** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured revision-precision rate** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t15.artifact.artifact_versioning@1`
- `cap.t15.artifact.artifact_versioning.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.structured.structured_data_gen@1` | use the in-file conservative substitute for `structured_data_gen` (documented, slower, lower quality) and set `degraded['structured_data_gen']='local'` |
| `cap.t01.arena.arena_graph@1` | use the in-file conservative substitute for `arena_graph` (documented, slower, lower quality) and set `degraded['arena_graph']='local'` |
| `cap.t10.temporal.temporal_reasoning@1` | use the in-file conservative substitute for `temporal_reasoning` (documented, slower, lower quality) and set `degraded['temporal_reasoning']='local'` |
| `cap.t14.visual.visual_hallucination@1` | use the in-file conservative substitute for `visual_hallucination` (documented, slower, lower quality) and set `degraded['visual_hallucination']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - revision-request interpretation with scope determination | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - surgical revision preserving unrelated content | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - revision-history navigation and rollback | 520 | Third required mechanism. |
| 6 | Core implementation D - measured revision-precision rate | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0744_artifact_versioning.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.artifact.artifact_versioning@1`.
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

### P0745 · `output_localisation` — Output Format Adaptation & Portability

| field | value |
|---|---|
| part id | `P0745` (45/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0745_output_localisation.ts` |
| module path | `hyperion.t15.generation.output_localisation` |
| capability published | `cap.t15.output.output_localisation@1` |
| determinism class | `seeded` |
| p99 latency budget | 43000 ns (43 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0745_output_localisation.txt`](prompts/P0745_output_localisation.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0745-output-localisation) |

**Mission.** The same content, correct in every destination format.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **format-conversion with structure and meaning preservation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **destination-constraint handling (length, markup, character sets)** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **conversion-fidelity verification** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **fidelity measurement across format pairs** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t15.output.output_localisation@1`
- `cap.t15.output.output_localisation.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.artifact.artifact_versioning@1` | use the in-file conservative substitute for `artifact_versioning` (documented, slower, lower quality) and set `degraded['artifact_versioning']='local'` |
| `cap.t01.fuzz.fuzz_engine@1` | use the in-file conservative substitute for `fuzz_engine` (documented, slower, lower quality) and set `degraded['fuzz_engine']='local'` |
| `cap.t10.reasoning.reasoning_memory@1` | use the in-file conservative substitute for `reasoning_memory` (documented, slower, lower quality) and set `degraded['reasoning_memory']='local'` |
| `cap.t14.code.code_screenshot@1` | use the in-file conservative substitute for `code_screenshot` (documented, slower, lower quality) and set `degraded['code_screenshot']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - format-conversion with structure and meaning preservation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - destination-constraint handling (length, markup, character sets) | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - conversion-fidelity verification | 520 | Third required mechanism. |
| 6 | Core implementation D - fidelity measurement across format pairs | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0745_output_localisation.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.output.output_localisation@1`.
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

### P0746 · `gdpval_harness` — Knowledge Work Evaluation Harness

| field | value |
|---|---|
| part id | `P0746` (46/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0746_gdpval_harness.ts` |
| module path | `hyperion.t15.generation.gdpval_harness` |
| capability published | `cap.t15.gdpval.gdpval_harness@1` |
| determinism class | `seeded` |
| p99 latency budget | 44000 ns (44 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0746_gdpval_harness.txt`](prompts/P0746_gdpval_harness.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0746-gdpval-harness) |

**Mission.** Measures real economic work output quality.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **GDPval-AA style task harness with expert grading protocol** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **Elo computation methodology with statistical rigor** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **per-occupation capability breakdown** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **target: 2650 Elo versus Opus 5's 1862**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t15.gdpval.gdpval_harness@1`
- `cap.t15.gdpval.gdpval_harness.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.output.output_localisation@1` | use the in-file conservative substitute for `output_localisation` (documented, slower, lower quality) and set `degraded['output_localisation']='local'` |
| `cap.t01.manifest.manifest_parser@1` | use the in-file conservative substitute for `manifest_parser` (documented, slower, lower quality) and set `degraded['manifest_parser']='local'` |
| `cap.t10.reasoning.reasoning_faithfulness@1` | use the in-file conservative substitute for `reasoning_faithfulness` (documented, slower, lower quality) and set `degraded['reasoning_faithfulness']='local'` |
| `cap.t14.perception.perception_grounding_world@1` | use the in-file conservative substitute for `perception_grounding_world` (documented, slower, lower quality) and set `degraded['perception_grounding_world']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - GDPval-AA style task harness with expert grading protocol | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - Elo computation methodology with statistical rigor | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - per-occupation capability breakdown | 520 | Third required mechanism. |
| 6 | Core implementation D - target: 2650 Elo versus Opus 5's 1862 | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0746_gdpval_harness.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.gdpval.gdpval_harness@1`.
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

### P0747 · `artifact_quality_gate` — Artifact Quality Gate

| field | value |
|---|---|
| part id | `P0747` (47/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0747_artifact_quality_gate.ts` |
| module path | `hyperion.t15.generation.artifact_quality_gate` |
| capability published | `cap.t15.artifact.artifact_quality_gate@1` |
| determinism class | `seeded` |
| p99 latency budget | 45000 ns (45 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0747_artifact_quality_gate.txt`](prompts/P0747_artifact_quality_gate.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0747-artifact-quality-gate) |

**Mission.** Nothing substandard ever reaches a user.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **multi-dimensional quality thresholds per artifact type** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **automatic regeneration or explicit quality disclosure** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **quality-score distribution monitoring over time**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured user-rejection-rate reduction** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t15.artifact.artifact_quality_gate@1`
- `cap.t15.artifact.artifact_quality_gate.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.gdpval.gdpval_harness@1` | use the in-file conservative substitute for `gdpval_harness` (documented, slower, lower quality) and set `degraded['gdpval_harness']='local'` |
| `cap.t01.circuit.circuit_breaker@1` | use the in-file conservative substitute for `circuit_breaker` (documented, slower, lower quality) and set `degraded['circuit_breaker']='local'` |
| `cap.t10.subgoal.subgoal_caching@1` | use the in-file conservative substitute for `subgoal_caching` (documented, slower, lower quality) and set `degraded['subgoal_caching']='local'` |
| `cap.t14.receipt.receipt_finance_docs@1` | use the in-file conservative substitute for `receipt_finance_docs` (documented, slower, lower quality) and set `degraded['receipt_finance_docs']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - multi-dimensional quality thresholds per artifact type | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - automatic regeneration or explicit quality disclosure | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - quality-score distribution monitoring over time | 520 | Third required mechanism. |
| 6 | Core implementation D - measured user-rejection-rate reduction | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0747_artifact_quality_gate.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.artifact.artifact_quality_gate@1`.
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

### P0748 · `generation_speed` — Generation Latency & Cost Optimisation

| field | value |
|---|---|
| part id | `P0748` (48/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0748_generation_speed.ts` |
| module path | `hyperion.t15.generation.generation_speed` |
| capability published | `cap.t15.generation.generation_speed@1` |
| determinism class | `seeded` |
| p99 latency budget | 46000 ns (46 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0748_generation_speed.txt`](prompts/P0748_generation_speed.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0748-generation-speed) |

**Mission.** Publication quality at interactive speed.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **progressive-refinement generation with early usable output** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **GDPval-AA v2 (Elo)** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **quality-tier selection under latency and cost budgets**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **cached-component reuse for repeated structures** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured latency reduction at matched quality** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t15.generation.generation_speed@1`
- `cap.t15.generation.generation_speed.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.artifact.artifact_quality_gate@1` | use the in-file conservative substitute for `artifact_quality_gate` (documented, slower, lower quality) and set `degraded['artifact_quality_gate']='local'` |
| `cap.t01.shutdown.shutdown_drain@1` | use the in-file conservative substitute for `shutdown_drain` (documented, slower, lower quality) and set `degraded['shutdown_drain']='local'` |
| `cap.t10.reasoning.reasoning_spec_doc@1` | use the in-file conservative substitute for `reasoning_spec_doc` (documented, slower, lower quality) and set `degraded['reasoning_spec_doc']='local'` |
| `cap.t14.perception.perception_spec_doc@1` | use the in-file conservative substitute for `perception_spec_doc` (documented, slower, lower quality) and set `degraded['perception_spec_doc']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - progressive-refinement generation with early usable output | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - quality-tier selection under latency and cost budgets | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - cached-component reuse for repeated structures | 520 | Third required mechanism. |
| 6 | Core implementation D - measured latency reduction at matched quality | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0748_generation_speed.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.generation.generation_speed@1`.
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

### P0749 · `output_safety_filter` — Output Safety & Policy Compliance Filter

| field | value |
|---|---|
| part id | `P0749` (49/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0749_output_safety_filter.ts` |
| module path | `hyperion.t15.generation.output_safety_filter` |
| capability published | `cap.t15.output.output_safety_filter@1` |
| determinism class | `seeded` |
| p99 latency budget | 47000 ns (47 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0749_output_safety_filter.txt`](prompts/P0749_output_safety_filter.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0749-output-safety-filter) |

**Mission.** The final check before anything leaves the system.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **mandatory T19 policy evaluation on all generated artifacts**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **context-aware filtering avoiding over-refusal of legitimate work** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **explanation generation when output is modified or withheld** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **false-positive and false-negative rate measurement** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t15.output.output_safety_filter@1`
- `cap.t15.output.output_safety_filter.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.generation.generation_speed@1` | use the in-file conservative substitute for `generation_speed` (documented, slower, lower quality) and set `degraded['generation_speed']='local'` |
| `cap.t10.outcome.outcome_verifier@1` | use the in-file conservative substitute for `outcome_verifier` (documented, slower, lower quality) and set `degraded['outcome_verifier']='local'` |
| `cap.t14.visual.visual_grounding@1` | use the in-file conservative substitute for `visual_grounding` (documented, slower, lower quality) and set `degraded['visual_grounding']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - mandatory T19 policy evaluation on all generated artifacts | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - context-aware filtering avoiding over-refusal of legitimate work | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - explanation generation when output is modified or withheld | 520 | Third required mechanism. |
| 6 | Core implementation D - false-positive and false-negative rate measurement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0749_output_safety_filter.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.output.output_safety_filter@1`.
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

### P0750 · `generation_spec_doc` — Generation Subsystem Specification

| field | value |
|---|---|
| part id | `P0750` (50/50 of T15) |
| tier | `T15` — Generation, Artifacts & Interface Craft |
| language | TypeScript 5.7 |
| file to produce | `parts/t15_generation/P0750_generation_spec_doc.ts` |
| module path | `hyperion.t15.generation.generation_spec_doc` |
| capability published | `cap.t15.generation.generation_spec_doc@1` |
| determinism class | `seeded` |
| p99 latency budget | 48000 ns (48 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | GDPval-AA v2 (Elo), MMMU |
| worker prompt | [`prompts/P0750_generation_spec_doc.txt`](prompts/P0750_generation_spec_doc.txt) · [inline](docs/PROMPTS_T15.md#prompt-p0750-generation-spec-doc) |

**Mission.** The authoritative description of all output capabilities.

**Tier context.** Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.

**Mandate — all four items are required; none is optional.**

1. Implement **capability register with measured quality per artifact type** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **GDPval-AA v2 (Elo)** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **supported-format and verification-level matrix** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **honest limitation documentation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **GDPval-AA v2 (Elo)**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **drift detection between claims and measurements**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t15.generation.generation_spec_doc@1`
- `cap.t15.generation.generation_spec_doc.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t15.output.output_safety_filter@1` | use the in-file conservative substitute for `output_safety_filter` (documented, slower, lower quality) and set `degraded['output_safety_filter']='local'` |
| `cap.t01.atomics.atomics_sync@1` | use the in-file conservative substitute for `atomics_sync` (documented, slower, lower quality) and set `degraded['atomics_sync']='local'` |
| `cap.t10.constraint.constraint_reasoning@1` | use the in-file conservative substitute for `constraint_reasoning` (documented, slower, lower quality) and set `degraded['constraint_reasoning']='local'` |
| `cap.t14.video.video_tracking@1` | use the in-file conservative substitute for `video_tracking` (documented, slower, lower quality) and set `degraded['video_tracking']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - capability register with measured quality per artifact type | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - supported-format and verification-level matrix | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - honest limitation documentation | 520 | Third required mechanism. |
| 6 | Core implementation D - drift detection between claims and measurements | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t15_generation/P0750_generation_spec_doc.ts`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t15.generation.generation_spec_doc@1`.
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
