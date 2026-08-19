# HYPERION-Ω — Part specifications · T14 · Multimodal Perception & Grounding

> Contract: **Ω-CONTRACT v1.0.0-frozen** · 50 parts · 250,000 lines of code · language: Python 3.13

**Tier mission.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Benchmarks this tier is accountable for.** MMMU, OSWorld 2.0

**Tier dependencies.** T01, T05

Each part below is built by exactly one isolated Opus 5 worker that sees only: this specification, the frozen Ω-Contract, and its own prompt. Workers never see each other's files. Link-compatibility comes from the contract, not from coordination.

| part | slug | title | capability |
|---|---|---|---|
| [P0651](#p0651-image-encoder) | `image_encoder` | High-Resolution Image Encoder | `cap.t14.image.image_encoder@1` |
| [P0652](#p0652-vision-tokenisation) | `vision_tokenisation` | Visual Token Compression & Selection | `cap.t14.vision.vision_tokenisation@1` |
| [P0653](#p0653-ocr-engine) | `ocr_engine` | Text Recognition & Document OCR | `cap.t14.ocr.ocr_engine@1` |
| [P0654](#p0654-document-layout) | `document_layout` | Document Layout Analysis & Structure Extraction | `cap.t14.document.document_layout@1` |
| [P0655](#p0655-table-extraction) | `table_extraction` | Table Detection & Structured Extraction | `cap.t14.table.table_extraction@1` |
| [P0656](#p0656-chart-understanding) | `chart_understanding` | Chart & Diagram Comprehension | `cap.t14.chart.chart_understanding@1` |
| [P0657](#p0657-visual-grounding) | `visual_grounding` | Visual Grounding & Referring Expressions | `cap.t14.visual.visual_grounding@1` |
| [P0658](#p0658-scene-graph) | `scene_graph` | Scene Understanding & Relation Extraction | `cap.t14.scene.scene_graph@1` |
| [P0659](#p0659-visual-reasoning) | `visual_reasoning` | Visual Reasoning & Puzzle Solving | `cap.t14.visual.visual_reasoning@1` |
| [P0660](#p0660-image-geometry) | `image_geometry` | 3D Geometry & Depth Reasoning from Images | `cap.t14.image.image_geometry@1` |
| [P0661](#p0661-cad-understanding) | `cad_understanding` | Engineering Drawing & CAD Comprehension | `cap.t14.cad.cad_understanding@1` |
| [P0662](#p0662-video-encoder) | `video_encoder` | Long Video Understanding | `cap.t14.video.video_encoder@1` |
| [P0663](#p0663-temporal-video) | `temporal_video` | Temporal Reasoning & Event Detection in Video | `cap.t14.temporal.temporal_video@1` |
| [P0664](#p0664-video-tracking) | `video_tracking` | Object Tracking & Identity Persistence | `cap.t14.video.video_tracking@1` |
| [P0665](#p0665-audio-encoder) | `audio_encoder` | Audio Encoding & Representation | `cap.t14.audio.audio_encoder@1` |
| [P0666](#p0666-speech-recognition) | `speech_recognition` | Speech Recognition & Diarisation | `cap.t14.speech.speech_recognition@1` |
| [P0667](#p0667-prosody-paralinguistic) | `prosody_paralinguistic` | Prosody & Paralinguistic Understanding | `cap.t14.prosody.prosody_paralinguistic@1` |
| [P0668](#p0668-music-understanding) | `music_understanding` | Music Analysis & Understanding | `cap.t14.music.music_understanding@1` |
| [P0669](#p0669-audio-events) | `audio_events` | Environmental & Machine Audio Analysis | `cap.t14.audio.audio_events@1` |
| [P0670](#p0670-multimodal-alignment) | `multimodal_alignment` | Cross-Modal Alignment & Fusion | `cap.t14.multimodal.multimodal_alignment@1` |
| [P0671](#p0671-modality-translation) | `modality_translation` | Cross-Modal Translation & Description | `cap.t14.modality.modality_translation@1` |
| [P0672](#p0672-visual-hallucination) | `visual_hallucination` | Visual Hallucination Detection & Prevention | `cap.t14.visual.visual_hallucination@1` |
| [P0673](#p0673-scientific-imaging) | `scientific_imaging` | Scientific Image & Instrument Data Analysis | `cap.t14.scientific.scientific_imaging@1` |
| [P0674](#p0674-medical-imaging) | `medical_imaging` | Medical Image Interpretation Support | `cap.t14.medical.medical_imaging@1` |
| [P0675](#p0675-satellite-geospatial) | `satellite_geospatial` | Geospatial & Remote Sensing Analysis | `cap.t14.satellite.satellite_geospatial@1` |
| [P0676](#p0676-ui-screenshot) | `ui_screenshot` | UI Screenshot Understanding | `cap.t14.ui.ui_screenshot@1` |
| [P0677](#p0677-handwriting-sketch) | `handwriting_sketch` | Handwriting & Sketch Understanding | `cap.t14.handwriting.handwriting_sketch@1` |
| [P0678](#p0678-math-formula-vision) | `math_formula_vision` | Mathematical Notation Recognition | `cap.t14.math.math_formula_vision@1` |
| [P0679](#p0679-code-screenshot) | `code_screenshot` | Code and Terminal Image Understanding | `cap.t14.code.code_screenshot@1` |
| [P0680](#p0680-multimodal-context) | `multimodal_context` | Multimodal Context Management | `cap.t14.multimodal.multimodal_context@1` |
| [P0681](#p0681-perception-uncertainty) | `perception_uncertainty` | Perceptual Uncertainty & Verification | `cap.t14.perception.perception_uncertainty@1` |
| [P0682](#p0682-perception-robustness) | `perception_robustness` | Perception Robustness & Adversarial Defence | `cap.t14.perception.perception_robustness@1` |
| [P0683](#p0683-prompt-injection-visual) | `prompt_injection_visual` | Visual & Audio Prompt Injection Defence | `cap.t14.prompt.prompt_injection_visual@1` |
| [P0684](#p0684-sensor-fusion) | `sensor_fusion` | Multi-Sensor Fusion & Time Alignment | `cap.t14.sensor.sensor_fusion@1` |
| [P0685](#p0685-realtime-perception) | `realtime_perception` | Real-Time Streaming Perception | `cap.t14.realtime.realtime_perception@1` |
| [P0686](#p0686-perception-grounding-world) | `perception_grounding_world` | Perception-to-World-Model Grounding | `cap.t14.perception.perception_grounding_world@1` |
| [P0687](#p0687-visual-search) | `visual_search` | Visual Search & Image Retrieval | `cap.t14.visual.visual_search@1` |
| [P0688](#p0688-multimodal-memory-perception) | `multimodal_memory_perception` | Perceptual Memory & Recall | `cap.t14.multimodal.multimodal_memory_perception@1` |
| [P0689](#p0689-accessibility-perception) | `accessibility_perception` | Accessibility-Oriented Perception | `cap.t14.accessibility.accessibility_perception@1` |
| [P0690](#p0690-perception-multilingual) | `perception_multilingual` | Multilingual Visual Text Understanding | `cap.t14.perception.perception_multilingual@1` |
| [P0691](#p0691-data-extraction-pipeline) | `data_extraction_pipeline` | Bulk Document Data Extraction Pipeline | `cap.t14.data.data_extraction_pipeline@1` |
| [P0692](#p0692-form-understanding) | `form_understanding` | Form & Structured Document Understanding | `cap.t14.form.form_understanding@1` |
| [P0693](#p0693-receipt-finance-docs) | `receipt_finance_docs` | Financial Document Understanding | `cap.t14.receipt.receipt_finance_docs@1` |
| [P0694](#p0694-legal-docs-vision) | `legal_docs_vision` | Legal Document Structure Understanding | `cap.t14.legal.legal_docs_vision@1` |
| [P0695](#p0695-perception-speed) | `perception_speed` | Perception Latency & Cost Optimisation | `cap.t14.perception.perception_speed@1` |
| [P0696](#p0696-perception-distillation) | `perception_distillation` | Perception Model Distillation | `cap.t14.perception.perception_distillation@1` |
| [P0697](#p0697-perception-eval-harness) | `perception_eval_harness` | Multimodal Benchmark Harness | `cap.t14.perception.perception_eval_harness@1` |
| [P0698](#p0698-synthetic-perception-data) | `synthetic_perception_data` | Synthetic Perception Data Generation | `cap.t14.synthetic.synthetic_perception_data@1` |
| [P0699](#p0699-perception-interpretability) | `perception_interpretability` | Perception Interpretability & Attribution | `cap.t14.perception.perception_interpretability@1` |
| [P0700](#p0700-perception-spec-doc) | `perception_spec_doc` | Perception Subsystem Specification | `cap.t14.perception.perception_spec_doc@1` |

---

### P0651 · `image_encoder` — High-Resolution Image Encoder

| field | value |
|---|---|
| part id | `P0651` (1/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0651_image_encoder.py` |
| module path | `hyperion.t14.perception.image_encoder` |
| capability published | `cap.t14.image.image_encoder@1` |
| determinism class | `seeded` |
| p99 latency budget | 43000 ns (43 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0651_image_encoder.txt`](prompts/P0651_image_encoder.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0651-image-encoder) |

**Mission.** Sees fine detail in large images without losing the whole picture.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **native-resolution tiled encoding with global-context tokens** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **adaptive token allocation by region information density** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **aspect-ratio preservation without distortion artifacts**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **detail-recovery measurement on small-text and fine-structure probes** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t14.image.image_encoder@1`
- `cap.t14.image.image_encoder.describe@1`

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
| 3 | Core implementation A - native-resolution tiled encoding with global-context tokens | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - adaptive token allocation by region information density | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - aspect-ratio preservation without distortion artifacts | 520 | Third required mechanism. |
| 6 | Core implementation D - detail-recovery measurement on small-text and fine-structure pro | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0651_image_encoder.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.image.image_encoder@1`.
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

### P0652 · `vision_tokenisation` — Visual Token Compression & Selection

| field | value |
|---|---|
| part id | `P0652` (2/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0652_vision_tokenisation.py` |
| module path | `hyperion.t14.perception.vision_tokenisation` |
| capability published | `cap.t14.vision.vision_tokenisation@1` |
| determinism class | `seeded` |
| p99 latency budget | 44000 ns (44 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0652_vision_tokenisation.txt`](prompts/P0652_vision_tokenisation.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0652-vision-tokenisation) |

**Mission.** Spends visual tokens where the answer actually is.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **saliency and query-conditioned token selection** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **token-merging with information-preservation bounds**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **token-budget-versus-accuracy curves** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured cost reduction at matched visual accuracy** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t14.vision.vision_tokenisation@1`
- `cap.t14.vision.vision_tokenisation.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.image.image_encoder@1` | use the in-file conservative substitute for `image_encoder` (documented, slower, lower quality) and set `degraded['image_encoder']='local'` |
| `cap.t01.property.property_gen@1` | use the in-file conservative substitute for `property_gen` (documented, slower, lower quality) and set `degraded['property_gen']='local'` |
| `cap.t05.distillation.distillation_arch@1` | use the in-file conservative substitute for `distillation_arch` (documented, slower, lower quality) and set `degraded['distillation_arch']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - saliency and query-conditioned token selection | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - token-merging with information-preservation bounds | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - token-budget-versus-accuracy curves | 520 | Third required mechanism. |
| 6 | Core implementation D - measured cost reduction at matched visual accuracy | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0652_vision_tokenisation.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.vision.vision_tokenisation@1`.
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

### P0653 · `ocr_engine` — Text Recognition & Document OCR

| field | value |
|---|---|
| part id | `P0653` (3/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0653_ocr_engine.py` |
| module path | `hyperion.t14.perception.ocr_engine` |
| capability published | `cap.t14.ocr.ocr_engine@1` |
| determinism class | `seeded` |
| p99 latency budget | 45000 ns (45 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0653_ocr_engine.txt`](prompts/P0653_ocr_engine.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0653-ocr-engine) |

**Mission.** Reads any text in any image, including bad ones.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **multi-script, multi-orientation, handwriting and low-quality text recognition**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **layout-preserving text extraction with reading order** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **confidence estimation and uncertain-region flagging** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **character/word error rate measurement across corpora** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t14.ocr.ocr_engine@1`
- `cap.t14.ocr.ocr_engine.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.vision.vision_tokenisation@1` | use the in-file conservative substitute for `vision_tokenisation` (documented, slower, lower quality) and set `degraded['vision_tokenisation']='local'` |
| `cap.t01.link.link_validator@1` | use the in-file conservative substitute for `link_validator` (documented, slower, lower quality) and set `degraded['link_validator']='local'` |
| `cap.t05.multimodal.multimodal_fusion_arch@1` | use the in-file conservative substitute for `multimodal_fusion_arch` (documented, slower, lower quality) and set `degraded['multimodal_fusion_arch']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - multi-script, multi-orientation, handwriting and low-quality tex | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - layout-preserving text extraction with reading order | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - confidence estimation and uncertain-region flagging | 520 | Third required mechanism. |
| 6 | Core implementation D - character/word error rate measurement across corpora | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0653_ocr_engine.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.ocr.ocr_engine@1`.
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

### P0654 · `document_layout` — Document Layout Analysis & Structure Extraction

| field | value |
|---|---|
| part id | `P0654` (4/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0654_document_layout.py` |
| module path | `hyperion.t14.perception.document_layout` |
| capability published | `cap.t14.document.document_layout@1` |
| determinism class | `seeded` |
| p99 latency budget | 46000 ns (46 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0654_document_layout.txt`](prompts/P0654_document_layout.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0654-document-layout) |

**Mission.** Turns a PDF into structured, faithful data.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **region classification (heading, paragraph, table, figure, caption, footnote)** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **reading-order determination for complex multi-column layouts** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **structure-preserving export with provenance to page coordinates** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **structural-fidelity measurement on document benchmark sets**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t14.document.document_layout@1`
- `cap.t14.document.document_layout.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.ocr.ocr_engine@1` | use the in-file conservative substitute for `ocr_engine` (documented, slower, lower quality) and set `degraded['ocr_engine']='local'` |
| `cap.t01.rate.rate_limiter@1` | use the in-file conservative substitute for `rate_limiter` (documented, slower, lower quality) and set `degraded['rate_limiter']='local'` |
| `cap.t05.context.context_packing@1` | use the in-file conservative substitute for `context_packing` (documented, slower, lower quality) and set `degraded['context_packing']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - region classification (heading, paragraph, table, figure, captio | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - reading-order determination for complex multi-column layouts | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - structure-preserving export with provenance to page coordinates | 520 | Third required mechanism. |
| 6 | Core implementation D - structural-fidelity measurement on document benchmark sets | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0654_document_layout.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.document.document_layout@1`.
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

### P0655 · `table_extraction` — Table Detection & Structured Extraction

| field | value |
|---|---|
| part id | `P0655` (5/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0655_table_extraction.py` |
| module path | `hyperion.t14.perception.table_extraction` |
| capability published | `cap.t14.table.table_extraction@1` |
| determinism class | `seeded` |
| p99 latency budget | 47000 ns (47 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0655_table_extraction.txt`](prompts/P0655_table_extraction.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0655-table-extraction) |

**Mission.** Gets every cell right, including merged and borderless ones.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **table detection, cell segmentation and header identification** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **merged-cell, nested-header and borderless-table handling** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **value typing, unit extraction and footnote linking**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **cell-level accuracy measurement on table benchmark sets** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t14.table.table_extraction@1`
- `cap.t14.table.table_extraction.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.document.document_layout@1` | use the in-file conservative substitute for `document_layout` (documented, slower, lower quality) and set `degraded['document_layout']='local'` |
| `cap.t01.bootstrap.bootstrap_init@1` | use the in-file conservative substitute for `bootstrap_init` (documented, slower, lower quality) and set `degraded['bootstrap_init']='local'` |
| `cap.t05.capacity.capacity_probes@1` | use the in-file conservative substitute for `capacity_probes` (documented, slower, lower quality) and set `degraded['capacity_probes']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - table detection, cell segmentation and header identification | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - merged-cell, nested-header and borderless-table handling | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - value typing, unit extraction and footnote linking | 520 | Third required mechanism. |
| 6 | Core implementation D - cell-level accuracy measurement on table benchmark sets | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0655_table_extraction.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.table.table_extraction@1`.
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

### P0656 · `chart_understanding` — Chart & Diagram Comprehension

| field | value |
|---|---|
| part id | `P0656` (6/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0656_chart_understanding.py` |
| module path | `hyperion.t14.perception.chart_understanding` |
| capability published | `cap.t14.chart.chart_understanding@1` |
| determinism class | `seeded` |
| p99 latency budget | 48000 ns (48 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0656_chart_understanding.txt`](prompts/P0656_chart_understanding.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0656-chart-understanding) |

**Mission.** Reads the numbers off a plot correctly.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **chart-type classification and axis/scale/legend interpretation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **data-point value extraction with error estimation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **diagram topology understanding (flowcharts, schematics, graphs)** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **value-extraction accuracy measurement versus ground-truth data** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t14.chart.chart_understanding@1`
- `cap.t14.chart.chart_understanding.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.table.table_extraction@1` | use the in-file conservative substitute for `table_extraction` (documented, slower, lower quality) and set `degraded['table_extraction']='local'` |
| `cap.t01.chacha.chacha_seeds@1` | use the in-file conservative substitute for `chacha_seeds` (documented, slower, lower quality) and set `degraded['chacha_seeds']='local'` |
| `cap.t05.recurrent.recurrent_memory_layer@1` | use the in-file conservative substitute for `recurrent_memory_layer` (documented, slower, lower quality) and set `degraded['recurrent_memory_layer']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - chart-type classification and axis/scale/legend interpretation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - data-point value extraction with error estimation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - diagram topology understanding (flowcharts, schematics, graphs) | 520 | Third required mechanism. |
| 6 | Core implementation D - value-extraction accuracy measurement versus ground-truth data | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0656_chart_understanding.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.chart.chart_understanding@1`.
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

### P0657 · `visual_grounding` — Visual Grounding & Referring Expressions

| field | value |
|---|---|
| part id | `P0657` (7/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0657_visual_grounding.py` |
| module path | `hyperion.t14.perception.visual_grounding` |
| capability published | `cap.t14.visual.visual_grounding@1` |
| determinism class | `seeded` |
| p99 latency budget | 49000 ns (49 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0657_visual_grounding.txt`](prompts/P0657_visual_grounding.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0657-visual-grounding) |

**Mission.** Points at exactly the thing being described.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **phrase-to-region grounding with precise bounding output**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **relational and comparative reference resolution** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **ambiguity detection when a reference is underspecified** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **grounding precision measurement on standard benchmarks** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t14.visual.visual_grounding@1`
- `cap.t14.visual.visual_grounding.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.chart.chart_understanding@1` | use the in-file conservative substitute for `chart_understanding` (documented, slower, lower quality) and set `degraded['chart_understanding']='local'` |
| `cap.t01.mem.mem_layout@1` | use the in-file conservative substitute for `mem_layout` (documented, slower, lower quality) and set `degraded['mem_layout']='local'` |
| `cap.t05.byte.byte_latent_patching@1` | use the in-file conservative substitute for `byte_latent_patching` (documented, slower, lower quality) and set `degraded['byte_latent_patching']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - phrase-to-region grounding with precise bounding output | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - relational and comparative reference resolution | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - ambiguity detection when a reference is underspecified | 520 | Third required mechanism. |
| 6 | Core implementation D - grounding precision measurement on standard benchmarks | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0657_visual_grounding.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.visual.visual_grounding@1`.
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

### P0658 · `scene_graph` — Scene Understanding & Relation Extraction

| field | value |
|---|---|
| part id | `P0658` (8/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0658_scene_graph.py` |
| module path | `hyperion.t14.perception.scene_graph` |
| capability published | `cap.t14.scene.scene_graph@1` |
| determinism class | `seeded` |
| p99 latency budget | 3000 ns (3 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0658_scene_graph.txt`](prompts/P0658_scene_graph.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0658-scene-graph) |

**Mission.** Understands what is happening, not just what is present.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **object, attribute and relation extraction into a scene graph** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **spatial and functional relation reasoning** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **consistency checking against physical plausibility** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **scene-graph accuracy measurement on annotated corpora**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t14.scene.scene_graph@1`
- `cap.t14.scene.scene_graph.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.visual.visual_grounding@1` | use the in-file conservative substitute for `visual_grounding` (documented, slower, lower quality) and set `degraded['visual_grounding']='local'` |
| `cap.t01.hash.hash_maps@1` | use the in-file conservative substitute for `hash_maps` (documented, slower, lower quality) and set `degraded['hash_maps']='local'` |
| `cap.t05.world.world_model_core@1` | use the in-file conservative substitute for `world_model_core` (documented, slower, lower quality) and set `degraded['world_model_core']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - object, attribute and relation extraction into a scene graph | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - spatial and functional relation reasoning | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - consistency checking against physical plausibility | 520 | Third required mechanism. |
| 6 | Core implementation D - scene-graph accuracy measurement on annotated corpora | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0658_scene_graph.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.scene.scene_graph@1`.
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

### P0659 · `visual_reasoning` — Visual Reasoning & Puzzle Solving

| field | value |
|---|---|
| part id | `P0659` (9/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0659_visual_reasoning.py` |
| module path | `hyperion.t14.perception.visual_reasoning` |
| capability published | `cap.t14.visual.visual_reasoning@1` |
| determinism class | `seeded` |
| p99 latency budget | 4000 ns (4 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0659_visual_reasoning.txt`](prompts/P0659_visual_reasoning.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0659-visual-reasoning) |

**Mission.** Solves problems where the reasoning happens in the image.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **multi-step visual inference with intermediate visual attention** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **visual puzzle and pattern reasoning (ARC-style visual tasks)** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **counting, comparison and geometric reasoning accuracy**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **target contribution to MMMU 99.0% and ARC-AGI visual tasks** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t14.visual.visual_reasoning@1`
- `cap.t14.visual.visual_reasoning.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.scene.scene_graph@1` | use the in-file conservative substitute for `scene_graph` (documented, slower, lower quality) and set `degraded['scene_graph']='local'` |
| `cap.t01.selftest.selftest_harness@1` | use the in-file conservative substitute for `selftest_harness` (documented, slower, lower quality) and set `degraded['selftest_harness']='local'` |
| `cap.t05.model.model_merging@1` | use the in-file conservative substitute for `model_merging` (documented, slower, lower quality) and set `degraded['model_merging']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - multi-step visual inference with intermediate visual attention | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - visual puzzle and pattern reasoning (ARC-style visual tasks) | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - counting, comparison and geometric reasoning accuracy | 520 | Third required mechanism. |
| 6 | Core implementation D - target contribution to MMMU 99.0% and ARC-AGI visual tasks | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0659_visual_reasoning.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.visual.visual_reasoning@1`.
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

### P0660 · `image_geometry` — 3D Geometry & Depth Reasoning from Images

| field | value |
|---|---|
| part id | `P0660` (10/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0660_image_geometry.py` |
| module path | `hyperion.t14.perception.image_geometry` |
| capability published | `cap.t14.image.image_geometry@1` |
| determinism class | `seeded` |
| p99 latency budget | 5000 ns (5 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0660_image_geometry.txt`](prompts/P0660_image_geometry.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0660-image-geometry) |

**Mission.** Infers three dimensions from two.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **monocular depth and surface-normal estimation with uncertainty** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **camera-parameter and pose inference**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **metric-scale reasoning from known-size references** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **geometric accuracy measurement against ground-truth depth** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t14.image.image_geometry@1`
- `cap.t14.image.image_geometry.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.visual.visual_reasoning@1` | use the in-file conservative substitute for `visual_reasoning` (documented, slower, lower quality) and set `degraded['visual_reasoning']='local'` |
| `cap.t01.version.version_semver@1` | use the in-file conservative substitute for `version_semver` (documented, slower, lower quality) and set `degraded['version_semver']='local'` |
| `cap.t05.logit.logit_head_design@1` | use the in-file conservative substitute for `logit_head_design` (documented, slower, lower quality) and set `degraded['logit_head_design']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - monocular depth and surface-normal estimation with uncertainty | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - camera-parameter and pose inference | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - metric-scale reasoning from known-size references | 520 | Third required mechanism. |
| 6 | Core implementation D - geometric accuracy measurement against ground-truth depth | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0660_image_geometry.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.image.image_geometry@1`.
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

### P0661 · `cad_understanding` — Engineering Drawing & CAD Comprehension

| field | value |
|---|---|
| part id | `P0661` (11/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0661_cad_understanding.py` |
| module path | `hyperion.t14.perception.cad_understanding` |
| capability published | `cap.t14.cad.cad_understanding@1` |
| determinism class | `seeded` |
| p99 latency budget | 6000 ns (6 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0661_cad_understanding.txt`](prompts/P0661_cad_understanding.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0661-cad-understanding) |

**Mission.** Reads a technical drawing like an engineer.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **dimension, tolerance and annotation extraction from drawings**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **projection-view correspondence and 3D reconstruction** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **parametric-model generation from drawings** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **reconstruction accuracy on engineering-drawing corpora** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t14.cad.cad_understanding@1`
- `cap.t14.cad.cad_understanding.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.image.image_geometry@1` | use the in-file conservative substitute for `image_geometry` (documented, slower, lower quality) and set `degraded['image_geometry']='local'` |
| `cap.t01.budget.budget_ledger@1` | use the in-file conservative substitute for `budget_ledger` (documented, slower, lower quality) and set `degraded['budget_ledger']='local'` |
| `cap.t05.numerical.numerical_arch_stability@1` | use the in-file conservative substitute for `numerical_arch_stability` (documented, slower, lower quality) and set `degraded['numerical_arch_stability']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - dimension, tolerance and annotation extraction from drawings | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - projection-view correspondence and 3D reconstruction | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - parametric-model generation from drawings | 520 | Third required mechanism. |
| 6 | Core implementation D - reconstruction accuracy on engineering-drawing corpora | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0661_cad_understanding.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.cad.cad_understanding@1`.
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

### P0662 · `video_encoder` — Long Video Understanding

| field | value |
|---|---|
| part id | `P0662` (12/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0662_video_encoder.py` |
| module path | `hyperion.t14.perception.video_encoder` |
| capability published | `cap.t14.video.video_encoder@1` |
| determinism class | `seeded` |
| p99 latency budget | 7000 ns (7 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0662_video_encoder.txt`](prompts/P0662_video_encoder.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0662-video-encoder) |

**Mission.** Understands hours of video, not seconds.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **hierarchical temporal encoding with keyframe and event selection** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **long-video memory with retrieval over time** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **temporal-token budget management** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **accuracy on long-video question-answering benchmarks**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t14.video.video_encoder@1`
- `cap.t14.video.video_encoder.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.cad.cad_understanding@1` | use the in-file conservative substitute for `cad_understanding` (documented, slower, lower quality) and set `degraded['cad_understanding']='local'` |
| `cap.t01.compression.compression@1` | use the in-file conservative substitute for `compression` (documented, slower, lower quality) and set `degraded['compression']='local'` |
| `cap.t05.arch.arch_ablation_suite@1` | use the in-file conservative substitute for `arch_ablation_suite` (documented, slower, lower quality) and set `degraded['arch_ablation_suite']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - hierarchical temporal encoding with keyframe and event selection | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - long-video memory with retrieval over time | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - temporal-token budget management | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy on long-video question-answering benchmarks | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0662_video_encoder.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.video.video_encoder@1`.
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

### P0663 · `temporal_video` — Temporal Reasoning & Event Detection in Video

| field | value |
|---|---|
| part id | `P0663` (13/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0663_temporal_video.py` |
| module path | `hyperion.t14.perception.temporal_video` |
| capability published | `cap.t14.temporal.temporal_video@1` |
| determinism class | `seeded` |
| p99 latency budget | 8000 ns (8 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0663_temporal_video.txt`](prompts/P0663_temporal_video.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0663-temporal-video) |

**Mission.** Knows what happened, in what order, and why.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **action and event segmentation with boundary precision** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **causal and temporal relation extraction across events** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **counting and repetition reasoning over time**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **accuracy measurement on temporal video benchmarks** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t14.temporal.temporal_video@1`
- `cap.t14.temporal.temporal_video.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.video.video_encoder@1` | use the in-file conservative substitute for `video_encoder` (documented, slower, lower quality) and set `degraded['video_encoder']='local'` |
| `cap.t01.blake3.blake3_hash@1` | use the in-file conservative substitute for `blake3_hash` (documented, slower, lower quality) and set `degraded['blake3_hash']='local'` |
| `cap.t05.state.state_space_layer@1` | use the in-file conservative substitute for `state_space_layer` (documented, slower, lower quality) and set `degraded['state_space_layer']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - action and event segmentation with boundary precision | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - causal and temporal relation extraction across events | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - counting and repetition reasoning over time | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy measurement on temporal video benchmarks | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0663_temporal_video.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.temporal.temporal_video@1`.
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

### P0664 · `video_tracking` — Object Tracking & Identity Persistence

| field | value |
|---|---|
| part id | `P0664` (14/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0664_video_tracking.py` |
| module path | `hyperion.t14.perception.video_tracking` |
| capability published | `cap.t14.video.video_tracking@1` |
| determinism class | `seeded` |
| p99 latency budget | 9000 ns (9 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0664_video_tracking.txt`](prompts/P0664_video_tracking.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0664-video-tracking) |

**Mission.** Follows the same object through occlusion and time.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **multi-object tracking with re-identification after occlusion** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **trajectory extraction and motion analysis**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **identity-switch rate measurement** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **tracking accuracy on standard tracking benchmarks** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t14.video.video_tracking@1`
- `cap.t14.video.video_tracking.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.temporal.temporal_video@1` | use the in-file conservative substitute for `temporal_video` (documented, slower, lower quality) and set `degraded['temporal_video']='local'` |
| `cap.t01.alloc.alloc_arena@1` | use the in-file conservative substitute for `alloc_arena` (documented, slower, lower quality) and set `degraded['alloc_arena']='local'` |
| `cap.t05.tokeniser.tokeniser_omega@1` | use the in-file conservative substitute for `tokeniser_omega` (documented, slower, lower quality) and set `degraded['tokeniser_omega']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - multi-object tracking with re-identification after occlusion | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - trajectory extraction and motion analysis | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - identity-switch rate measurement | 520 | Third required mechanism. |
| 6 | Core implementation D - tracking accuracy on standard tracking benchmarks | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0664_video_tracking.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.video.video_tracking@1`.
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

### P0665 · `audio_encoder` — Audio Encoding & Representation

| field | value |
|---|---|
| part id | `P0665` (15/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0665_audio_encoder.py` |
| module path | `hyperion.t14.perception.audio_encoder` |
| capability published | `cap.t14.audio.audio_encoder@1` |
| determinism class | `seeded` |
| p99 latency budget | 10000 ns (10 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0665_audio_encoder.txt`](prompts/P0665_audio_encoder.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0665-audio-encoder) |

**Mission.** Hears everything: speech, music, environment, machinery.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **multi-scale audio representation covering speech and non-speech**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **noise robustness and channel-variation handling** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **long-audio hierarchical encoding** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **downstream-task accuracy across audio domains** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t14.audio.audio_encoder@1`
- `cap.t14.audio.audio_encoder.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.video.video_tracking@1` | use the in-file conservative substitute for `video_tracking` (documented, slower, lower quality) and set `degraded['video_tracking']='local'` |
| `cap.t01.bitset.bitset_rank@1` | use the in-file conservative substitute for `bitset_rank` (documented, slower, lower quality) and set `degraded['bitset_rank']='local'` |
| `cap.t05.uncertainty.uncertainty_calibration@1` | use the in-file conservative substitute for `uncertainty_calibration` (documented, slower, lower quality) and set `degraded['uncertainty_calibration']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - multi-scale audio representation covering speech and non-speech | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - noise robustness and channel-variation handling | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - long-audio hierarchical encoding | 520 | Third required mechanism. |
| 6 | Core implementation D - downstream-task accuracy across audio domains | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0665_audio_encoder.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.audio.audio_encoder@1`.
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

### P0666 · `speech_recognition` — Speech Recognition & Diarisation

| field | value |
|---|---|
| part id | `P0666` (16/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0666_speech_recognition.py` |
| module path | `hyperion.t14.perception.speech_recognition` |
| capability published | `cap.t14.speech.speech_recognition@1` |
| determinism class | `seeded` |
| p99 latency budget | 11000 ns (11 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0666_speech_recognition.txt`](prompts/P0666_speech_recognition.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0666-speech-recognition) |

**Mission.** Transcribes accurately and knows who said what.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **multilingual, accented and code-switched speech recognition** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **speaker diarisation with overlap handling** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **timestamp precision at word level** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **word error rate and diarisation error rate measurement**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t14.speech.speech_recognition@1`
- `cap.t14.speech.speech_recognition.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.audio.audio_encoder@1` | use the in-file conservative substitute for `audio_encoder` (documented, slower, lower quality) and set `degraded['audio_encoder']='local'` |
| `cap.t01.metrics.metrics_core@1` | use the in-file conservative substitute for `metrics_core` (documented, slower, lower quality) and set `degraded['metrics_core']='local'` |
| `cap.t05.knowledge.knowledge_editing@1` | use the in-file conservative substitute for `knowledge_editing` (documented, slower, lower quality) and set `degraded['knowledge_editing']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - multilingual, accented and code-switched speech recognition | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - speaker diarisation with overlap handling | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - timestamp precision at word level | 520 | Third required mechanism. |
| 6 | Core implementation D - word error rate and diarisation error rate measurement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0666_speech_recognition.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.speech.speech_recognition@1`.
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

### P0667 · `prosody_paralinguistic` — Prosody & Paralinguistic Understanding

| field | value |
|---|---|
| part id | `P0667` (17/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0667_prosody_paralinguistic.py` |
| module path | `hyperion.t14.perception.prosody_paralinguistic` |
| capability published | `cap.t14.prosody.prosody_paralinguistic@1` |
| determinism class | `seeded` |
| p99 latency budget | 12000 ns (12 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0667_prosody_paralinguistic.txt`](prompts/P0667_prosody_paralinguistic.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0667-prosody-paralinguistic) |

**Mission.** Hears how something was said, not just what.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **emotion, emphasis, hesitation and intent-marker detection** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **prosodic-boundary and turn-taking-cue recognition** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **cultural and individual variation handling**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **accuracy measurement on paralinguistic benchmark sets** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t14.prosody.prosody_paralinguistic@1`
- `cap.t14.prosody.prosody_paralinguistic.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.speech.speech_recognition@1` | use the in-file conservative substitute for `speech_recognition` (documented, slower, lower quality) and set `degraded['speech_recognition']='local'` |
| `cap.t01.capability.capability_gate@1` | use the in-file conservative substitute for `capability_gate` (documented, slower, lower quality) and set `degraded['capability_gate']='local'` |
| `cap.t05.residual.residual_stream_design@1` | use the in-file conservative substitute for `residual_stream_design` (documented, slower, lower quality) and set `degraded['residual_stream_design']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - emotion, emphasis, hesitation and intent-marker detection | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - prosodic-boundary and turn-taking-cue recognition | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - cultural and individual variation handling | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy measurement on paralinguistic benchmark sets | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0667_prosody_paralinguistic.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.prosody.prosody_paralinguistic@1`.
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

### P0668 · `music_understanding` — Music Analysis & Understanding

| field | value |
|---|---|
| part id | `P0668` (18/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0668_music_understanding.py` |
| module path | `hyperion.t14.perception.music_understanding` |
| capability published | `cap.t14.music.music_understanding@1` |
| determinism class | `seeded` |
| p99 latency budget | 13000 ns (13 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0668_music_understanding.txt`](prompts/P0668_music_understanding.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0668-music-understanding) |

**Mission.** Analyses music with musician-level precision.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **transcription, key, tempo, harmony and structure analysis** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **instrument identification and source separation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **style and genre characterisation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **accuracy measurement against expert annotations** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t14.music.music_understanding@1`
- `cap.t14.music.music_understanding.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.prosody.prosody_paralinguistic@1` | use the in-file conservative substitute for `prosody_paralinguistic` (documented, slower, lower quality) and set `degraded['prosody_paralinguistic']='local'` |
| `cap.t01.unit.unit_dimensions@1` | use the in-file conservative substitute for `unit_dimensions` (documented, slower, lower quality) and set `degraded['unit_dimensions']='local'` |
| `cap.t05.model.model_surgery@1` | use the in-file conservative substitute for `model_surgery` (documented, slower, lower quality) and set `degraded['model_surgery']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - transcription, key, tempo, harmony and structure analysis | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - instrument identification and source separation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - style and genre characterisation | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy measurement against expert annotations | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0668_music_understanding.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.music.music_understanding@1`.
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

### P0669 · `audio_events` — Environmental & Machine Audio Analysis

| field | value |
|---|---|
| part id | `P0669` (19/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0669_audio_events.py` |
| module path | `hyperion.t14.perception.audio_events` |
| capability published | `cap.t14.audio.audio_events@1` |
| determinism class | `seeded` |
| p99 latency budget | 14000 ns (14 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0669_audio_events.txt`](prompts/P0669_audio_events.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0669-audio-events) |

**Mission.** Diagnoses the world by its sounds.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **acoustic event detection and classification in noisy conditions**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **anomaly detection for machine and equipment sounds** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **localisation from multichannel input** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **detection accuracy on environmental audio benchmarks** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t14.audio.audio_events@1`
- `cap.t14.audio.audio_events.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.music.music_understanding@1` | use the in-file conservative substitute for `music_understanding` (documented, slower, lower quality) and set `degraded['music_understanding']='local'` |
| `cap.t01.fs.fs_atomic@1` | use the in-file conservative substitute for `fs_atomic` (documented, slower, lower quality) and set `degraded['fs_atomic']='local'` |
| `cap.t05.reference.reference_forward@1` | use the in-file conservative substitute for `reference_forward` (documented, slower, lower quality) and set `degraded['reference_forward']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - acoustic event detection and classification in noisy conditions | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - anomaly detection for machine and equipment sounds | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - localisation from multichannel input | 520 | Third required mechanism. |
| 6 | Core implementation D - detection accuracy on environmental audio benchmarks | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0669_audio_events.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.audio.audio_events@1`.
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

### P0670 · `multimodal_alignment` — Cross-Modal Alignment & Fusion

| field | value |
|---|---|
| part id | `P0670` (20/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0670_multimodal_alignment.py` |
| module path | `hyperion.t14.perception.multimodal_alignment` |
| capability published | `cap.t14.multimodal.multimodal_alignment@1` |
| determinism class | `seeded` |
| p99 latency budget | 15000 ns (15 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0670_multimodal_alignment.txt`](prompts/P0670_multimodal_alignment.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0670-multimodal-alignment) |

**Mission.** One shared understanding across all senses.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **contrastive and generative alignment across modality pairs** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **cross-modal retrieval quality measurement** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **modality-conflict detection and resolution** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured transfer benefit from joint versus separate encoding**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t14.multimodal.multimodal_alignment@1`
- `cap.t14.multimodal.multimodal_alignment.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.audio.audio_events@1` | use the in-file conservative substitute for `audio_events` (documented, slower, lower quality) and set `degraded['audio_events']='local'` |
| `cap.t01.cbor.cbor_canonical@1` | use the in-file conservative substitute for `cbor_canonical` (documented, slower, lower quality) and set `degraded['cbor_canonical']='local'` |
| `cap.t05.kv.kv_compression_model@1` | use the in-file conservative substitute for `kv_compression_model` (documented, slower, lower quality) and set `degraded['kv_compression_model']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - contrastive and generative alignment across modality pairs | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - cross-modal retrieval quality measurement | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - modality-conflict detection and resolution | 520 | Third required mechanism. |
| 6 | Core implementation D - measured transfer benefit from joint versus separate encoding | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0670_multimodal_alignment.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.multimodal.multimodal_alignment@1`.
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

### P0671 · `modality_translation` — Cross-Modal Translation & Description

| field | value |
|---|---|
| part id | `P0671` (21/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0671_modality_translation.py` |
| module path | `hyperion.t14.perception.modality_translation` |
| capability published | `cap.t14.modality.modality_translation@1` |
| determinism class | `seeded` |
| p99 latency budget | 16000 ns (16 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0671_modality_translation.txt`](prompts/P0671_modality_translation.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0671-modality-translation) |

**Mission.** Describes images in words, and words as images, faithfully.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **dense, accurate description generation with hallucination controls** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **modality-specific detail preservation measurement** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **faithfulness verification against source content**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **hallucination-rate measurement with target under 0.5%** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t14.modality.modality_translation@1`
- `cap.t14.modality.modality_translation.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.multimodal.multimodal_alignment@1` | use the in-file conservative substitute for `multimodal_alignment` (documented, slower, lower quality) and set `degraded['multimodal_alignment']='local'` |
| `cap.t01.clock.clock_time@1` | use the in-file conservative substitute for `clock_time` (documented, slower, lower quality) and set `degraded['clock_time']='local'` |
| `cap.t05.embedding.embedding_design@1` | use the in-file conservative substitute for `embedding_design` (documented, slower, lower quality) and set `degraded['embedding_design']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - dense, accurate description generation with hallucination contro | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - modality-specific detail preservation measurement | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - faithfulness verification against source content | 520 | Third required mechanism. |
| 6 | Core implementation D - hallucination-rate measurement with target under 0.5% | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0671_modality_translation.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.modality.modality_translation@1`.
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

### P0672 · `visual_hallucination` — Visual Hallucination Detection & Prevention

| field | value |
|---|---|
| part id | `P0672` (22/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0672_visual_hallucination.py` |
| module path | `hyperion.t14.perception.visual_hallucination` |
| capability published | `cap.t14.visual.visual_hallucination@1` |
| determinism class | `seeded` |
| p99 latency budget | 17000 ns (17 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0672_visual_hallucination.txt`](prompts/P0672_visual_hallucination.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0672-visual-hallucination) |

**Mission.** Never describes what is not there.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **claim-to-region verification for every visual assertion** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **uncertainty expression for ambiguous visual content**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **adversarial-image hallucination testing** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured hallucination-rate reduction versus baselines** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t14.visual.visual_hallucination@1`
- `cap.t14.visual.visual_hallucination.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.modality.modality_translation@1` | use the in-file conservative substitute for `modality_translation` (documented, slower, lower quality) and set `degraded['modality_translation']='local'` |
| `cap.t01.bigint.bigint_modmath@1` | use the in-file conservative substitute for `bigint_modmath` (documented, slower, lower quality) and set `degraded['bigint_modmath']='local'` |
| `cap.t05.verifier.verifier_head@1` | use the in-file conservative substitute for `verifier_head` (documented, slower, lower quality) and set `degraded['verifier_head']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - claim-to-region verification for every visual assertion | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - uncertainty expression for ambiguous visual content | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - adversarial-image hallucination testing | 520 | Third required mechanism. |
| 6 | Core implementation D - measured hallucination-rate reduction versus baselines | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0672_visual_hallucination.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.visual.visual_hallucination@1`.
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

### P0673 · `scientific_imaging` — Scientific Image & Instrument Data Analysis

| field | value |
|---|---|
| part id | `P0673` (23/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0673_scientific_imaging.py` |
| module path | `hyperion.t14.perception.scientific_imaging` |
| capability published | `cap.t14.scientific.scientific_imaging@1` |
| determinism class | `seeded` |
| p99 latency budget | 18000 ns (18 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0673_scientific_imaging.txt`](prompts/P0673_scientific_imaging.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0673-scientific-imaging) |

**Mission.** Reads microscopy, spectroscopy, imaging and instrument output.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **modality-specific analysis (microscopy, crystallography, spectroscopy, imaging)**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **quantitative measurement extraction with error bars** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **artifact-versus-signal discrimination** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **accuracy against expert-annotated scientific images** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t14.scientific.scientific_imaging@1`
- `cap.t14.scientific.scientific_imaging.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.visual.visual_hallucination@1` | use the in-file conservative substitute for `visual_hallucination` (documented, slower, lower quality) and set `degraded['visual_hallucination']='local'` |
| `cap.t01.logging.logging_events@1` | use the in-file conservative substitute for `logging_events` (documented, slower, lower quality) and set `degraded['logging_events']='local'` |
| `cap.t05.continual.continual_learning@1` | use the in-file conservative substitute for `continual_learning` (documented, slower, lower quality) and set `degraded['continual_learning']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - modality-specific analysis (microscopy, crystallography, spectro | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - quantitative measurement extraction with error bars | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - artifact-versus-signal discrimination | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy against expert-annotated scientific images | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0673_scientific_imaging.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.scientific.scientific_imaging@1`.
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

### P0674 · `medical_imaging` — Medical Image Interpretation Support

| field | value |
|---|---|
| part id | `P0674` (24/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0674_medical_imaging.py` |
| module path | `hyperion.t14.perception.medical_imaging` |
| capability published | `cap.t14.medical.medical_imaging@1` |
| determinism class | `seeded` |
| p99 latency budget | 19000 ns (19 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0674_medical_imaging.txt`](prompts/P0674_medical_imaging.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0674-medical-imaging) |

**Mission.** Clinical-grade assistance with clinical-grade caution.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **multi-modality medical image analysis with anatomical grounding** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **finding detection with calibrated confidence and differential lists** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **mandatory clinical-oversight framing and scope limits** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **accuracy measurement against radiologist consensus labels**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t14.medical.medical_imaging@1`
- `cap.t14.medical.medical_imaging.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.scientific.scientific_imaging@1` | use the in-file conservative substitute for `scientific_imaging` (documented, slower, lower quality) and set `degraded['scientific_imaging']='local'` |
| `cap.t01.checksum.checksum_verify@1` | use the in-file conservative substitute for `checksum_verify` (documented, slower, lower quality) and set `degraded['checksum_verify']='local'` |
| `cap.t05.depth.depth_width_tradeoff@1` | use the in-file conservative substitute for `depth_width_tradeoff` (documented, slower, lower quality) and set `degraded['depth_width_tradeoff']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - multi-modality medical image analysis with anatomical grounding | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - finding detection with calibrated confidence and differential li | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - mandatory clinical-oversight framing and scope limits | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy measurement against radiologist consensus labels | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0674_medical_imaging.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.medical.medical_imaging@1`.
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

### P0675 · `satellite_geospatial` — Geospatial & Remote Sensing Analysis

| field | value |
|---|---|
| part id | `P0675` (25/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0675_satellite_geospatial.py` |
| module path | `hyperion.t14.perception.satellite_geospatial` |
| capability published | `cap.t14.satellite.satellite_geospatial@1` |
| determinism class | `seeded` |
| p99 latency budget | 20000 ns (20 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0675_satellite_geospatial.txt`](prompts/P0675_satellite_geospatial.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0675-satellite-geospatial) |

**Mission.** Understands the earth from above.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **multispectral analysis and land-cover classification** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **change detection across time series with georeferencing** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **measurement extraction in real-world units**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **accuracy measurement on geospatial benchmark datasets** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t14.satellite.satellite_geospatial@1`
- `cap.t14.satellite.satellite_geospatial.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.medical.medical_imaging@1` | use the in-file conservative substitute for `medical_imaging` (documented, slower, lower quality) and set `degraded['medical_imaging']='local'` |
| `cap.t01.numeric.numeric_limits@1` | use the in-file conservative substitute for `numeric_limits` (documented, slower, lower quality) and set `degraded['numeric_limits']='local'` |
| `cap.t05.sparse.sparse_upcycling@1` | use the in-file conservative substitute for `sparse_upcycling` (documented, slower, lower quality) and set `degraded['sparse_upcycling']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - multispectral analysis and land-cover classification | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - change detection across time series with georeferencing | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - measurement extraction in real-world units | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy measurement on geospatial benchmark datasets | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0675_satellite_geospatial.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.satellite.satellite_geospatial@1`.
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

### P0676 · `ui_screenshot` — UI Screenshot Understanding

| field | value |
|---|---|
| part id | `P0676` (26/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0676_ui_screenshot.py` |
| module path | `hyperion.t14.perception.ui_screenshot` |
| capability published | `cap.t14.ui.ui_screenshot@1` |
| determinism class | `seeded` |
| p99 latency budget | 21000 ns (21 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0676_ui_screenshot.txt`](prompts/P0676_ui_screenshot.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0676-ui-screenshot) |

**Mission.** Understands interfaces well enough to operate them (feeds T13).

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **element detection with role, state and affordance inference** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **layout hierarchy and interaction-target identification**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **cross-platform and cross-resolution robustness** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **grounding accuracy feeding OSWorld and GUI benchmarks** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t14.ui.ui_screenshot@1`
- `cap.t14.ui.ui_screenshot.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.satellite.satellite_geospatial@1` | use the in-file conservative substitute for `satellite_geospatial` (documented, slower, lower quality) and set `degraded['satellite_geospatial']='local'` |
| `cap.t01.sandbox.sandbox_policy@1` | use the in-file conservative substitute for `sandbox_policy` (documented, slower, lower quality) and set `degraded['sandbox_policy']='local'` |
| `cap.t05.model.model_config_schema@1` | use the in-file conservative substitute for `model_config_schema` (documented, slower, lower quality) and set `degraded['model_config_schema']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - element detection with role, state and affordance inference | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - layout hierarchy and interaction-target identification | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - cross-platform and cross-resolution robustness | 520 | Third required mechanism. |
| 6 | Core implementation D - grounding accuracy feeding OSWorld and GUI benchmarks | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0676_ui_screenshot.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.ui.ui_screenshot@1`.
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

### P0677 · `handwriting_sketch` — Handwriting & Sketch Understanding

| field | value |
|---|---|
| part id | `P0677` (27/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0677_handwriting_sketch.py` |
| module path | `hyperion.t14.perception.handwriting_sketch` |
| capability published | `cap.t14.handwriting.handwriting_sketch@1` |
| determinism class | `seeded` |
| p99 latency budget | 22000 ns (22 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0677_handwriting_sketch.txt`](prompts/P0677_handwriting_sketch.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0677-handwriting-sketch) |

**Mission.** Reads messy human input: notes, whiteboards, diagrams.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **handwriting recognition across styles and languages**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **sketch and diagram interpretation into structured meaning** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **mathematical and chemical notation recognition** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **accuracy measurement on handwriting and sketch corpora** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t14.handwriting.handwriting_sketch@1`
- `cap.t14.handwriting.handwriting_sketch.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.ui.ui_screenshot@1` | use the in-file conservative substitute for `ui_screenshot` (documented, slower, lower quality) and set `degraded['ui_screenshot']='local'` |
| `cap.t01.abi.abi_result@1` | use the in-file conservative substitute for `abi_result` (documented, slower, lower quality) and set `degraded['abi_result']='local'` |
| `cap.t05.attention.attention_variants@1` | use the in-file conservative substitute for `attention_variants` (documented, slower, lower quality) and set `degraded['attention_variants']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - handwriting recognition across styles and languages | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - sketch and diagram interpretation into structured meaning | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - mathematical and chemical notation recognition | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy measurement on handwriting and sketch corpora | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0677_handwriting_sketch.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.handwriting.handwriting_sketch@1`.
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

### P0678 · `math_formula_vision` — Mathematical Notation Recognition

| field | value |
|---|---|
| part id | `P0678` (28/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0678_math_formula_vision.py` |
| module path | `hyperion.t14.perception.math_formula_vision` |
| capability published | `cap.t14.math.math_formula_vision@1` |
| determinism class | `seeded` |
| p99 latency budget | 23000 ns (23 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0678_math_formula_vision.txt`](prompts/P0678_math_formula_vision.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0678-math-formula-vision) |

**Mission.** Reads mathematics from images perfectly.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **formula recognition into canonical machine-readable form** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **multi-line, matrix and complex-structure handling** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **semantic validation of recognised expressions** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **expression-level accuracy measurement**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t14.math.math_formula_vision@1`
- `cap.t14.math.math_formula_vision.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.handwriting.handwriting_sketch@1` | use the in-file conservative substitute for `handwriting_sketch` (documented, slower, lower quality) and set `degraded['handwriting_sketch']='local'` |
| `cap.t01.trace.trace_context@1` | use the in-file conservative substitute for `trace_context` (documented, slower, lower quality) and set `degraded['trace_context']='local'` |
| `cap.t05.activation.activation_design@1` | use the in-file conservative substitute for `activation_design` (documented, slower, lower quality) and set `degraded['activation_design']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - formula recognition into canonical machine-readable form | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - multi-line, matrix and complex-structure handling | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - semantic validation of recognised expressions | 520 | Third required mechanism. |
| 6 | Core implementation D - expression-level accuracy measurement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0678_math_formula_vision.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.math.math_formula_vision@1`.
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

### P0679 · `code_screenshot` — Code and Terminal Image Understanding

| field | value |
|---|---|
| part id | `P0679` (29/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0679_code_screenshot.py` |
| module path | `hyperion.t14.perception.code_screenshot` |
| capability published | `cap.t14.code.code_screenshot@1` |
| determinism class | `seeded` |
| p99 latency budget | 24000 ns (24 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0679_code_screenshot.txt`](prompts/P0679_code_screenshot.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0679-code-screenshot) |

**Mission.** Reads code and terminal output from screenshots reliably.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **syntax-aware code recognition with indentation preservation** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **terminal-output parsing including colour and control sequences** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **error-message extraction and interpretation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **reconstruction accuracy measurement** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t14.code.code_screenshot@1`
- `cap.t14.code.code_screenshot.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.math.math_formula_vision@1` | use the in-file conservative substitute for `math_formula_vision` (documented, slower, lower quality) and set `degraded['math_formula_vision']='local'` |
| `cap.t01.fixed.fixed_point@1` | use the in-file conservative substitute for `fixed_point` (documented, slower, lower quality) and set `degraded['fixed_point']='local'` |
| `cap.t05.draft.draft_model_arch@1` | use the in-file conservative substitute for `draft_model_arch` (documented, slower, lower quality) and set `degraded['draft_model_arch']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - syntax-aware code recognition with indentation preservation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - terminal-output parsing including colour and control sequences | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - error-message extraction and interpretation | 520 | Third required mechanism. |
| 6 | Core implementation D - reconstruction accuracy measurement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0679_code_screenshot.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.code.code_screenshot@1`.
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

### P0680 · `multimodal_context` — Multimodal Context Management

| field | value |
|---|---|
| part id | `P0680` (30/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0680_multimodal_context.py` |
| module path | `hyperion.t14.perception.multimodal_context` |
| capability published | `cap.t14.multimodal.multimodal_context@1` |
| determinism class | `seeded` |
| p99 latency budget | 25000 ns (25 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0680_multimodal_context.txt`](prompts/P0680_multimodal_context.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0680-multimodal-context) |

**Mission.** Handles hundreds of images and hours of media in one conversation.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **media-reference tracking and re-retrieval across turns** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **multimodal context budgeting with quality-preserving compression**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **cross-media consistency checking** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **accuracy measurement in long multimodal conversations** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t14.multimodal.multimodal_context@1`
- `cap.t14.multimodal.multimodal_context.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.code.code_screenshot@1` | use the in-file conservative substitute for `code_screenshot` (documented, slower, lower quality) and set `degraded['code_screenshot']='local'` |
| `cap.t01.config.config_system@1` | use the in-file conservative substitute for `config_system` (documented, slower, lower quality) and set `degraded['config_system']='local'` |
| `cap.t05.meta.meta_learning_arch@1` | use the in-file conservative substitute for `meta_learning_arch` (documented, slower, lower quality) and set `degraded['meta_learning_arch']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - media-reference tracking and re-retrieval across turns | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - multimodal context budgeting with quality-preserving compression | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - cross-media consistency checking | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy measurement in long multimodal conversations | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0680_multimodal_context.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.multimodal.multimodal_context@1`.
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

### P0681 · `perception_uncertainty` — Perceptual Uncertainty & Verification

| field | value |
|---|---|
| part id | `P0681` (31/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0681_perception_uncertainty.py` |
| module path | `hyperion.t14.perception.perception_uncertainty` |
| capability published | `cap.t14.perception.perception_uncertainty@1` |
| determinism class | `seeded` |
| p99 latency budget | 26000 ns (26 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0681_perception_uncertainty.txt`](prompts/P0681_perception_uncertainty.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0681-perception-uncertainty) |

**Mission.** Knows what it cannot see clearly, and says so.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **per-claim visual confidence estimation with calibration**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **resolution-limit and occlusion-aware abstention** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **active-perception requests (ask for a better image)** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **calibration measurement on perception tasks** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t14.perception.perception_uncertainty@1`
- `cap.t14.perception.perception_uncertainty.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.multimodal.multimodal_context@1` | use the in-file conservative substitute for `multimodal_context` (documented, slower, lower quality) and set `degraded['multimodal_context']='local'` |
| `cap.t01.determinism.determinism_replay@1` | use the in-file conservative substitute for `determinism_replay` (documented, slower, lower quality) and set `degraded['determinism_replay']='local'` |
| `cap.t05.architecture.architecture_search@1` | use the in-file conservative substitute for `architecture_search` (documented, slower, lower quality) and set `degraded['architecture_search']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - per-claim visual confidence estimation with calibration | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - resolution-limit and occlusion-aware abstention | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - active-perception requests (ask for a better image) | 520 | Third required mechanism. |
| 6 | Core implementation D - calibration measurement on perception tasks | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0681_perception_uncertainty.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.perception.perception_uncertainty@1`.
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

### P0682 · `perception_robustness` — Perception Robustness & Adversarial Defence

| field | value |
|---|---|
| part id | `P0682` (32/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0682_perception_robustness.py` |
| module path | `hyperion.t14.perception.perception_robustness` |
| capability published | `cap.t14.perception.perception_robustness@1` |
| determinism class | `seeded` |
| p99 latency budget | 27000 ns (27 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0682_perception_robustness.txt`](prompts/P0682_perception_robustness.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0682-perception-robustness) |

**Mission.** Resists corrupted, adversarial and out-of-distribution input.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **corruption robustness (blur, noise, compression, lighting)** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **adversarial-perturbation detection and mitigation** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **out-of-distribution detection with abstention** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **robustness measurement across corruption benchmark suites**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t14.perception.perception_robustness@1`
- `cap.t14.perception.perception_robustness.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.perception.perception_uncertainty@1` | use the in-file conservative substitute for `perception_uncertainty` (documented, slower, lower quality) and set `degraded['perception_uncertainty']='local'` |
| `cap.t01.compat.compat_shims@1` | use the in-file conservative substitute for `compat_shims` (documented, slower, lower quality) and set `degraded['compat_shims']='local'` |
| `cap.t05.speculative.speculative_arch_hooks@1` | use the in-file conservative substitute for `speculative_arch_hooks` (documented, slower, lower quality) and set `degraded['speculative_arch_hooks']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - corruption robustness (blur, noise, compression, lighting) | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - adversarial-perturbation detection and mitigation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - out-of-distribution detection with abstention | 520 | Third required mechanism. |
| 6 | Core implementation D - robustness measurement across corruption benchmark suites | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0682_perception_robustness.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.perception.perception_robustness@1`.
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

### P0683 · `prompt_injection_visual` — Visual & Audio Prompt Injection Defence

| field | value |
|---|---|
| part id | `P0683` (33/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0683_prompt_injection_visual.py` |
| module path | `hyperion.t14.perception.prompt_injection_visual` |
| capability published | `cap.t14.prompt.prompt_injection_visual@1` |
| determinism class | `seeded` |
| p99 latency budget | 28000 ns (28 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0683_prompt_injection_visual.txt`](prompts/P0683_prompt_injection_visual.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0683-prompt-injection-visual) |

**Mission.** Text inside an image is data, never an instruction.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **embedded-instruction detection in images, audio and documents** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **instruction-hierarchy enforcement for media-sourced content** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **injection-attack corpus construction and testing**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **target: zero successful injections on the attack corpus** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t14.prompt.prompt_injection_visual@1`
- `cap.t14.prompt.prompt_injection_visual.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.perception.perception_robustness@1` | use the in-file conservative substitute for `perception_robustness` (documented, slower, lower quality) and set `degraded['perception_robustness']='local'` |
| `cap.t01.secure.secure_zeroize@1` | use the in-file conservative substitute for `secure_zeroize` (documented, slower, lower quality) and set `degraded['secure_zeroize']='local'` |
| `cap.t05.expert.expert_specialisation@1` | use the in-file conservative substitute for `expert_specialisation` (documented, slower, lower quality) and set `degraded['expert_specialisation']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - embedded-instruction detection in images, audio and documents | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - instruction-hierarchy enforcement for media-sourced content | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - injection-attack corpus construction and testing | 520 | Third required mechanism. |
| 6 | Core implementation D - target: zero successful injections on the attack corpus | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0683_prompt_injection_visual.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.prompt.prompt_injection_visual@1`.
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

### P0684 · `sensor_fusion` — Multi-Sensor Fusion & Time Alignment

| field | value |
|---|---|
| part id | `P0684` (34/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0684_sensor_fusion.py` |
| module path | `hyperion.t14.perception.sensor_fusion` |
| capability published | `cap.t14.sensor.sensor_fusion@1` |
| determinism class | `seeded` |
| p99 latency budget | 29000 ns (29 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0684_sensor_fusion.txt`](prompts/P0684_sensor_fusion.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0684-sensor-fusion) |

**Mission.** Combines many streams into one coherent picture of the world.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **temporal synchronisation and clock-skew correction across sensors** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **uncertainty-weighted fusion with conflict handling**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **missing-sensor graceful degradation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **fusion-accuracy measurement versus single-sensor baselines** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t14.sensor.sensor_fusion@1`
- `cap.t14.sensor.sensor_fusion.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.prompt.prompt_injection_visual@1` | use the in-file conservative substitute for `prompt_injection_visual` (documented, slower, lower quality) and set `degraded['prompt_injection_visual']='local'` |
| `cap.t05.hybrid.hybrid_mixer@1` | use the in-file conservative substitute for `hybrid_mixer` (documented, slower, lower quality) and set `degraded['hybrid_mixer']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - temporal synchronisation and clock-skew correction across sensor | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - uncertainty-weighted fusion with conflict handling | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - missing-sensor graceful degradation | 520 | Third required mechanism. |
| 6 | Core implementation D - fusion-accuracy measurement versus single-sensor baselines | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0684_sensor_fusion.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.sensor.sensor_fusion@1`.
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

### P0685 · `realtime_perception` — Real-Time Streaming Perception

| field | value |
|---|---|
| part id | `P0685` (35/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0685_realtime_perception.py` |
| module path | `hyperion.t14.perception.realtime_perception` |
| capability published | `cap.t14.realtime.realtime_perception@1` |
| determinism class | `seeded` |
| p99 latency budget | 30000 ns (30 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0685_realtime_perception.txt`](prompts/P0685_realtime_perception.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0685-realtime-perception) |

**Mission.** Understands the world as it happens, within milliseconds.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **incremental streaming encoding with early partial understanding**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **latency-quality tradeoff control for live use** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **stream-interruption and resynchronisation handling** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **end-to-end perception latency measurement** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t14.realtime.realtime_perception@1`
- `cap.t14.realtime.realtime_perception.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.sensor.sensor_fusion@1` | use the in-file conservative substitute for `sensor_fusion` (documented, slower, lower quality) and set `degraded['sensor_fusion']='local'` |
| `cap.t01.envelope.envelope_codec@1` | use the in-file conservative substitute for `envelope_codec` (documented, slower, lower quality) and set `degraded['envelope_codec']='local'` |
| `cap.t05.normalisation.normalisation_design@1` | use the in-file conservative substitute for `normalisation_design` (documented, slower, lower quality) and set `degraded['normalisation_design']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - incremental streaming encoding with early partial understanding | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - latency-quality tradeoff control for live use | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - stream-interruption and resynchronisation handling | 520 | Third required mechanism. |
| 6 | Core implementation D - end-to-end perception latency measurement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0685_realtime_perception.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.realtime.realtime_perception@1`.
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

### P0686 · `perception_grounding_world` — Perception-to-World-Model Grounding

| field | value |
|---|---|
| part id | `P0686` (36/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0686_perception_grounding_world.py` |
| module path | `hyperion.t14.perception.perception_grounding_world` |
| capability published | `cap.t14.perception.perception_grounding_world@1` |
| determinism class | `seeded` |
| p99 latency budget | 31000 ns (31 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0686_perception_grounding_world.txt`](prompts/P0686_perception_grounding_world.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0686-perception-grounding-world) |

**Mission.** What it sees updates what it believes.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **observation-to-belief update with provenance and confidence** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **contradiction detection between perception and prior belief** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **persistent object and entity identity across observations** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **world-model accuracy measurement in agent tasks**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t14.perception.perception_grounding_world@1`
- `cap.t14.perception.perception_grounding_world.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.realtime.realtime_perception@1` | use the in-file conservative substitute for `realtime_perception` (documented, slower, lower quality) and set `degraded['realtime_perception']='local'` |
| `cap.t01.dataflow.dataflow_dag@1` | use the in-file conservative substitute for `dataflow_dag` (documented, slower, lower quality) and set `degraded['dataflow_dag']='local'` |
| `cap.t05.multi.multi_token_prediction@1` | use the in-file conservative substitute for `multi_token_prediction` (documented, slower, lower quality) and set `degraded['multi_token_prediction']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - observation-to-belief update with provenance and confidence | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - contradiction detection between perception and prior belief | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - persistent object and entity identity across observations | 520 | Third required mechanism. |
| 6 | Core implementation D - world-model accuracy measurement in agent tasks | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0686_perception_grounding_world.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.perception.perception_grounding_world@1`.
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

### P0687 · `visual_search` — Visual Search & Image Retrieval

| field | value |
|---|---|
| part id | `P0687` (37/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0687_visual_search.py` |
| module path | `hyperion.t14.perception.visual_search` |
| capability published | `cap.t14.visual.visual_search@1` |
| determinism class | `seeded` |
| p99 latency budget | 32000 ns (32 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0687_visual_search.txt`](prompts/P0687_visual_search.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0687-visual-search) |

**Mission.** Finds the needle image in the billion-image haystack.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **visual embedding indexing with attribute-filtered search** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **region-level and composed (image plus text) query support** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **duplicate and near-duplicate identification**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **retrieval accuracy and latency measurement at scale** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t14.visual.visual_search@1`
- `cap.t14.visual.visual_search.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.perception.perception_grounding_world@1` | use the in-file conservative substitute for `perception_grounding_world` (documented, slower, lower quality) and set `degraded['perception_grounding_world']='local'` |
| `cap.t01.serialization.serialization_schema@1` | use the in-file conservative substitute for `serialization_schema` (documented, slower, lower quality) and set `degraded['serialization_schema']='local'` |
| `cap.t05.program.program_induction_arch@1` | use the in-file conservative substitute for `program_induction_arch` (documented, slower, lower quality) and set `degraded['program_induction_arch']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - visual embedding indexing with attribute-filtered search | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - region-level and composed (image plus text) query support | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - duplicate and near-duplicate identification | 520 | Third required mechanism. |
| 6 | Core implementation D - retrieval accuracy and latency measurement at scale | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0687_visual_search.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.visual.visual_search@1`.
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

### P0688 · `multimodal_memory_perception` — Perceptual Memory & Recall

| field | value |
|---|---|
| part id | `P0688` (38/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0688_multimodal_memory_perception.py` |
| module path | `hyperion.t14.perception.multimodal_memory_perception` |
| capability published | `cap.t14.multimodal.multimodal_memory_perception@1` |
| determinism class | `seeded` |
| p99 latency budget | 33000 ns (33 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0688_multimodal_memory_perception.txt`](prompts/P0688_multimodal_memory_perception.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0688-multimodal-memory-perception) |

**Mission.** Remembers what it saw, precisely, for a long time.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **compact perceptual memory with detail-tier storage** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **re-examination of stored media on demand**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **recall accuracy measurement over long horizons** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **storage-cost versus recall-fidelity curves** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t14.multimodal.multimodal_memory_perception@1`
- `cap.t14.multimodal.multimodal_memory_perception.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.visual.visual_search@1` | use the in-file conservative substitute for `visual_search` (documented, slower, lower quality) and set `degraded['visual_search']='local'` |
| `cap.t01.bench.bench_harness@1` | use the in-file conservative substitute for `bench_harness` (documented, slower, lower quality) and set `degraded['bench_harness']='local'` |
| `cap.t05.init.init_scaling_laws@1` | use the in-file conservative substitute for `init_scaling_laws` (documented, slower, lower quality) and set `degraded['init_scaling_laws']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - compact perceptual memory with detail-tier storage | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - re-examination of stored media on demand | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - recall accuracy measurement over long horizons | 520 | Third required mechanism. |
| 6 | Core implementation D - storage-cost versus recall-fidelity curves | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0688_multimodal_memory_perception.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.multimodal.multimodal_memory_perception@1`.
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

### P0689 · `accessibility_perception` — Accessibility-Oriented Perception

| field | value |
|---|---|
| part id | `P0689` (39/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0689_accessibility_perception.py` |
| module path | `hyperion.t14.perception.accessibility_perception` |
| capability published | `cap.t14.accessibility.accessibility_perception@1` |
| determinism class | `seeded` |
| p99 latency budget | 34000 ns (34 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0689_accessibility_perception.txt`](prompts/P0689_accessibility_perception.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0689-accessibility-perception) |

**Mission.** Describes the world for people who cannot see or hear it.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **audio description generation with appropriate detail and pacing**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **alt-text generation meeting accessibility standards** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **sign-language and captioning support** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **evaluation with accessibility-expert reviewers** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t14.accessibility.accessibility_perception@1`
- `cap.t14.accessibility.accessibility_perception.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.multimodal.multimodal_memory_perception@1` | use the in-file conservative substitute for `multimodal_memory_perception` (documented, slower, lower quality) and set `degraded['multimodal_memory_perception']='local'` |
| `cap.t01.abi.abi_stability@1` | use the in-file conservative substitute for `abi_stability` (documented, slower, lower quality) and set `degraded['abi_stability']='local'` |
| `cap.t05.memory.memory_attention_bridge@1` | use the in-file conservative substitute for `memory_attention_bridge` (documented, slower, lower quality) and set `degraded['memory_attention_bridge']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - audio description generation with appropriate detail and pacing | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - alt-text generation meeting accessibility standards | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - sign-language and captioning support | 520 | Third required mechanism. |
| 6 | Core implementation D - evaluation with accessibility-expert reviewers | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0689_accessibility_perception.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.accessibility.accessibility_perception@1`.
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

### P0690 · `perception_multilingual` — Multilingual Visual Text Understanding

| field | value |
|---|---|
| part id | `P0690` (40/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0690_perception_multilingual.py` |
| module path | `hyperion.t14.perception.perception_multilingual` |
| capability published | `cap.t14.perception.perception_multilingual@1` |
| determinism class | `seeded` |
| p99 latency budget | 35000 ns (35 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0690_perception_multilingual.txt`](prompts/P0690_perception_multilingual.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0690-perception-multilingual) |

**Mission.** Reads every script, in every layout direction.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **script coverage including right-to-left and vertical text** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **mixed-script document handling** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **translation-with-layout-preservation of visual text** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **accuracy measurement across script families**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t14.perception.perception_multilingual@1`
- `cap.t14.perception.perception_multilingual.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.accessibility.accessibility_perception@1` | use the in-file conservative substitute for `accessibility_perception` (documented, slower, lower quality) and set `degraded['accessibility_perception']='local'` |
| `cap.t01.retry.retry_idempotency@1` | use the in-file conservative substitute for `retry_idempotency` (documented, slower, lower quality) and set `degraded['retry_idempotency']='local'` |
| `cap.t05.thought.thought_representation@1` | use the in-file conservative substitute for `thought_representation` (documented, slower, lower quality) and set `degraded['thought_representation']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - script coverage including right-to-left and vertical text | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - mixed-script document handling | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - translation-with-layout-preservation of visual text | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy measurement across script families | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0690_perception_multilingual.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.perception.perception_multilingual@1`.
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

### P0691 · `data_extraction_pipeline` — Bulk Document Data Extraction Pipeline

| field | value |
|---|---|
| part id | `P0691` (41/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0691_data_extraction_pipeline.py` |
| module path | `hyperion.t14.perception.data_extraction_pipeline` |
| capability published | `cap.t14.data.data_extraction_pipeline@1` |
| determinism class | `seeded` |
| p99 latency budget | 36000 ns (36 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0691_data_extraction_pipeline.txt`](prompts/P0691_data_extraction_pipeline.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0691-data-extraction-pipeline) |

**Mission.** Turns a million documents into clean structured data.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **schema-driven extraction with field-level confidence** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **human-review routing for low-confidence extractions** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **throughput and cost measurement per thousand documents**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **field-level accuracy measurement against audited ground truth** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t14.data.data_extraction_pipeline@1`
- `cap.t14.data.data_extraction_pipeline.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.perception.perception_multilingual@1` | use the in-file conservative substitute for `perception_multilingual` (documented, slower, lower quality) and set `degraded['perception_multilingual']='local'` |
| `cap.t05.omega.omega_block@1` | use the in-file conservative substitute for `omega_block` (documented, slower, lower quality) and set `degraded['omega_block']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - schema-driven extraction with field-level confidence | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - human-review routing for low-confidence extractions | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - throughput and cost measurement per thousand documents | 520 | Third required mechanism. |
| 6 | Core implementation D - field-level accuracy measurement against audited ground truth | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0691_data_extraction_pipeline.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.data.data_extraction_pipeline@1`.
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

### P0692 · `form_understanding` — Form & Structured Document Understanding

| field | value |
|---|---|
| part id | `P0692` (42/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0692_form_understanding.py` |
| module path | `hyperion.t14.perception.form_understanding` |
| capability published | `cap.t14.form.form_understanding@1` |
| determinism class | `seeded` |
| p99 latency budget | 37000 ns (37 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0692_form_understanding.txt`](prompts/P0692_form_understanding.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0692-form-understanding) |

**Mission.** Handles the world's paperwork correctly.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **key-value pair extraction with spatial and semantic association** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **checkbox, signature and stamp detection**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **multi-page form correlation and validation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **accuracy measurement on form benchmark datasets** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t14.form.form_understanding@1`
- `cap.t14.form.form_understanding.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.data.data_extraction_pipeline@1` | use the in-file conservative substitute for `data_extraction_pipeline` (documented, slower, lower quality) and set `degraded['data_extraction_pipeline']='local'` |
| `cap.t01.omega.omega_bus_ipc@1` | use the in-file conservative substitute for `omega_bus_ipc` (documented, slower, lower quality) and set `degraded['omega_bus_ipc']='local'` |
| `cap.t05.adaptive.adaptive_depth@1` | use the in-file conservative substitute for `adaptive_depth` (documented, slower, lower quality) and set `degraded['adaptive_depth']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - key-value pair extraction with spatial and semantic association | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - checkbox, signature and stamp detection | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - multi-page form correlation and validation | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy measurement on form benchmark datasets | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0692_form_understanding.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.form.form_understanding@1`.
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

### P0693 · `receipt_finance_docs` — Financial Document Understanding

| field | value |
|---|---|
| part id | `P0693` (43/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0693_receipt_finance_docs.py` |
| module path | `hyperion.t14.perception.receipt_finance_docs` |
| capability published | `cap.t14.receipt.receipt_finance_docs@1` |
| determinism class | `seeded` |
| p99 latency budget | 38000 ns (38 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0693_receipt_finance_docs.txt`](prompts/P0693_receipt_finance_docs.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0693-receipt-finance-docs) |

**Mission.** Invoices, statements and receipts, extracted and reconciled.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **line-item extraction with totals reconciliation and arithmetic verification**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **currency, tax and date-convention handling** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **anomaly and inconsistency detection** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **accuracy measurement with reconciliation-based verification** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t14.receipt.receipt_finance_docs@1`
- `cap.t14.receipt.receipt_finance_docs.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.form.form_understanding@1` | use the in-file conservative substitute for `form_understanding` (documented, slower, lower quality) and set `degraded['form_understanding']='local'` |
| `cap.t01.task.task_runtime@1` | use the in-file conservative substitute for `task_runtime` (documented, slower, lower quality) and set `degraded['task_runtime']='local'` |
| `cap.t05.long.long_context_arch@1` | use the in-file conservative substitute for `long_context_arch` (documented, slower, lower quality) and set `degraded['long_context_arch']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - line-item extraction with totals reconciliation and arithmetic v | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - currency, tax and date-convention handling | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - anomaly and inconsistency detection | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy measurement with reconciliation-based verification | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0693_receipt_finance_docs.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.receipt.receipt_finance_docs@1`.
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

### P0694 · `legal_docs_vision` — Legal Document Structure Understanding

| field | value |
|---|---|
| part id | `P0694` (44/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0694_legal_docs_vision.py` |
| module path | `hyperion.t14.perception.legal_docs_vision` |
| capability published | `cap.t14.legal.legal_docs_vision@1` |
| determinism class | `seeded` |
| p99 latency budget | 39000 ns (39 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0694_legal_docs_vision.txt`](prompts/P0694_legal_docs_vision.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0694-legal-docs-vision) |

**Mission.** Reads contracts with their structure intact.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **clause, definition and cross-reference structure extraction** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **redline and tracked-change interpretation** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **signature-block and execution-status detection** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **structural accuracy measurement on legal corpora**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t14.legal.legal_docs_vision@1`
- `cap.t14.legal.legal_docs_vision.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.receipt.receipt_finance_docs@1` | use the in-file conservative substitute for `receipt_finance_docs` (documented, slower, lower quality) and set `degraded['receipt_finance_docs']='local'` |
| `cap.t01.arena.arena_graph@1` | use the in-file conservative substitute for `arena_graph` (documented, slower, lower quality) and set `degraded['arena_graph']='local'` |
| `cap.t05.symbolic.symbolic_bridge@1` | use the in-file conservative substitute for `symbolic_bridge` (documented, slower, lower quality) and set `degraded['symbolic_bridge']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - clause, definition and cross-reference structure extraction | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - redline and tracked-change interpretation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - signature-block and execution-status detection | 520 | Third required mechanism. |
| 6 | Core implementation D - structural accuracy measurement on legal corpora | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0694_legal_docs_vision.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.legal.legal_docs_vision@1`.
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

### P0695 · `perception_speed` — Perception Latency & Cost Optimisation

| field | value |
|---|---|
| part id | `P0695` (45/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0695_perception_speed.py` |
| module path | `hyperion.t14.perception.perception_speed` |
| capability published | `cap.t14.perception.perception_speed@1` |
| determinism class | `seeded` |
| p99 latency budget | 40000 ns (40 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0695_perception_speed.txt`](prompts/P0695_perception_speed.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0695-perception-speed) |

**Mission.** Fast enough for real-time, cheap enough for a million documents.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **resolution and token-budget adaptive policies** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **cascaded perception (cheap model first, escalate when uncertain)** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **batch-processing throughput optimisation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured cost reduction at matched accuracy** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t14.perception.perception_speed@1`
- `cap.t14.perception.perception_speed.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.legal.legal_docs_vision@1` | use the in-file conservative substitute for `legal_docs_vision` (documented, slower, lower quality) and set `degraded['legal_docs_vision']='local'` |
| `cap.t01.fuzz.fuzz_engine@1` | use the in-file conservative substitute for `fuzz_engine` (documented, slower, lower quality) and set `degraded['fuzz_engine']='local'` |
| `cap.t05.weight.weight_sharing@1` | use the in-file conservative substitute for `weight_sharing` (documented, slower, lower quality) and set `degraded['weight_sharing']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - resolution and token-budget adaptive policies | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - cascaded perception (cheap model first, escalate when uncertain) | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - batch-processing throughput optimisation | 520 | Third required mechanism. |
| 6 | Core implementation D - measured cost reduction at matched accuracy | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0695_perception_speed.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.perception.perception_speed@1`.
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

### P0696 · `perception_distillation` — Perception Model Distillation

| field | value |
|---|---|
| part id | `P0696` (46/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0696_perception_distillation.py` |
| module path | `hyperion.t14.perception.perception_distillation` |
| capability published | `cap.t14.perception.perception_distillation@1` |
| determinism class | `seeded` |
| p99 latency budget | 41000 ns (41 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0696_perception_distillation.txt`](prompts/P0696_perception_distillation.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0696-perception-distillation) |

**Mission.** Puts most of the perception quality into a tiny fast model.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **distillation from the full encoder to fast tiers** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **per-task competence mapping for routing decisions**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **quality-retention measurement per size tier** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured contribution to the S4 fast-path coverage** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t14.perception.perception_distillation@1`
- `cap.t14.perception.perception_distillation.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.perception.perception_speed@1` | use the in-file conservative substitute for `perception_speed` (documented, slower, lower quality) and set `degraded['perception_speed']='local'` |
| `cap.t01.manifest.manifest_parser@1` | use the in-file conservative substitute for `manifest_parser` (documented, slower, lower quality) and set `degraded['manifest_parser']='local'` |
| `cap.t05.action.action_head@1` | use the in-file conservative substitute for `action_head` (documented, slower, lower quality) and set `degraded['action_head']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - distillation from the full encoder to fast tiers | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - per-task competence mapping for routing decisions | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - quality-retention measurement per size tier | 520 | Third required mechanism. |
| 6 | Core implementation D - measured contribution to the S4 fast-path coverage | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0696_perception_distillation.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.perception.perception_distillation@1`.
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

### P0697 · `perception_eval_harness` — Multimodal Benchmark Harness

| field | value |
|---|---|
| part id | `P0697` (47/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0697_perception_eval_harness.py` |
| module path | `hyperion.t14.perception.perception_eval_harness` |
| capability published | `cap.t14.perception.perception_eval_harness@1` |
| determinism class | `seeded` |
| p99 latency budget | 42000 ns (42 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0697_perception_eval_harness.txt`](prompts/P0697_perception_eval_harness.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0697-perception-eval-harness) |

**Mission.** Measures perception on every major public benchmark.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **MMMU, document, chart, video and audio benchmark harnesses**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **per-category diagnostics with failure taxonomy** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **comparison methodology versus Opus 5's reported multimodal scores** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **target: MMMU 99.0% versus Opus 5's ~93%** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t14.perception.perception_eval_harness@1`
- `cap.t14.perception.perception_eval_harness.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.perception.perception_distillation@1` | use the in-file conservative substitute for `perception_distillation` (documented, slower, lower quality) and set `degraded['perception_distillation']='local'` |
| `cap.t01.circuit.circuit_breaker@1` | use the in-file conservative substitute for `circuit_breaker` (documented, slower, lower quality) and set `degraded['circuit_breaker']='local'` |
| `cap.t05.prompt.prompt_representation@1` | use the in-file conservative substitute for `prompt_representation` (documented, slower, lower quality) and set `degraded['prompt_representation']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - MMMU, document, chart, video and audio benchmark harnesses | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - per-category diagnostics with failure taxonomy | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - comparison methodology versus Opus 5's reported multimodal score | 520 | Third required mechanism. |
| 6 | Core implementation D - target: MMMU 99.0% versus Opus 5's ~93% | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0697_perception_eval_harness.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.perception.perception_eval_harness@1`.
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

### P0698 · `synthetic_perception_data` — Synthetic Perception Data Generation

| field | value |
|---|---|
| part id | `P0698` (48/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0698_synthetic_perception_data.py` |
| module path | `hyperion.t14.perception.synthetic_perception_data` |
| capability published | `cap.t14.synthetic.synthetic_perception_data@1` |
| determinism class | `seeded` |
| p99 latency budget | 43000 ns (43 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0698_synthetic_perception_data.txt`](prompts/P0698_synthetic_perception_data.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0698-synthetic-perception-data) |

**Mission.** Generates the training data that closes each measured gap.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **procedural generation of documents, charts, UIs and scenes with exact labels** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **MMMU**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **difficulty and diversity control targeting known weaknesses** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **synthetic-to-real transfer validation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured accuracy improvement per synthetic data campaign**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t14.synthetic.synthetic_perception_data@1`
- `cap.t14.synthetic.synthetic_perception_data.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.perception.perception_eval_harness@1` | use the in-file conservative substitute for `perception_eval_harness` (documented, slower, lower quality) and set `degraded['perception_eval_harness']='local'` |
| `cap.t01.shutdown.shutdown_drain@1` | use the in-file conservative substitute for `shutdown_drain` (documented, slower, lower quality) and set `degraded['shutdown_drain']='local'` |
| `cap.t05.arch.arch_spec_doc@1` | use the in-file conservative substitute for `arch_spec_doc` (documented, slower, lower quality) and set `degraded['arch_spec_doc']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - procedural generation of documents, charts, UIs and scenes with  | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - difficulty and diversity control targeting known weaknesses | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - synthetic-to-real transfer validation | 520 | Third required mechanism. |
| 6 | Core implementation D - measured accuracy improvement per synthetic data campaign | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0698_synthetic_perception_data.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.synthetic.synthetic_perception_data@1`.
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

### P0699 · `perception_interpretability` — Perception Interpretability & Attribution

| field | value |
|---|---|
| part id | `P0699` (49/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0699_perception_interpretability.py` |
| module path | `hyperion.t14.perception.perception_interpretability` |
| capability published | `cap.t14.perception.perception_interpretability@1` |
| determinism class | `seeded` |
| p99 latency budget | 44000 ns (44 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0699_perception_interpretability.txt`](prompts/P0699_perception_interpretability.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0699-perception-interpretability) |

**Mission.** Shows exactly which pixels produced which claim.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **attention and gradient attribution to image regions** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **claim-to-region linking in generated descriptions** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **attribution-faithfulness verification**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **usability validation with expert reviewers** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t14.perception.perception_interpretability@1`
- `cap.t14.perception.perception_interpretability.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.synthetic.synthetic_perception_data@1` | use the in-file conservative substitute for `synthetic_perception_data` (documented, slower, lower quality) and set `degraded['synthetic_perception_data']='local'` |
| `cap.t05.latent.latent_program_slots@1` | use the in-file conservative substitute for `latent_program_slots` (documented, slower, lower quality) and set `degraded['latent_program_slots']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - attention and gradient attribution to image regions | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - claim-to-region linking in generated descriptions | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - attribution-faithfulness verification | 520 | Third required mechanism. |
| 6 | Core implementation D - usability validation with expert reviewers | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t14_perception/P0699_perception_interpretability.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.perception.perception_interpretability@1`.
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

### P0700 · `perception_spec_doc` — Perception Subsystem Specification

| field | value |
|---|---|
| part id | `P0700` (50/50 of T14) |
| tier | `T14` — Multimodal Perception & Grounding |
| language | Python 3.13 |
| file to produce | `parts/t14_perception/P0700_perception_spec_doc.py` |
| module path | `hyperion.t14.perception.perception_spec_doc` |
| capability published | `cap.t14.perception.perception_spec_doc@1` |
| determinism class | `seeded` |
| p99 latency budget | 45000 ns (45 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | MMMU, OSWorld 2.0 |
| worker prompt | [`prompts/P0700_perception_spec_doc.txt`](prompts/P0700_perception_spec_doc.txt) · [inline](docs/PROMPTS_T14.md#prompt-p0700-perception-spec-doc) |

**Mission.** The authoritative description of all perception capabilities and limits.

**Tier context.** Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.

**Mandate — all four items are required; none is optional.**

1. Implement **capability register with measured accuracy per modality and task** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **MMMU** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **honest limitation and failure-mode documentation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **benchmark-result aggregation with provenance** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **MMMU** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **drift detection between claims and measurements** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t14.perception.perception_spec_doc@1`
- `cap.t14.perception.perception_spec_doc.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t14.perception.perception_interpretability@1` | use the in-file conservative substitute for `perception_interpretability` (documented, slower, lower quality) and set `degraded['perception_interpretability']='local'` |
| `cap.t01.atomics.atomics_sync@1` | use the in-file conservative substitute for `atomics_sync` (documented, slower, lower quality) and set `degraded['atomics_sync']='local'` |
| `cap.t05.positional.positional_design@1` | use the in-file conservative substitute for `positional_design` (documented, slower, lower quality) and set `degraded['positional_design']='local'` |

**Determinism.** `seeded` — all randomness is drawn from `split_seed(root_seed, part_id, call_index)`. Given the same seed triple the output is byte-identical. The part must never touch a global RNG.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - capability register with measured accuracy per modality and task | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - honest limitation and failure-mode documentation | 580 | Second required mechanism, fully independent of A's internals. |
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
| 15 | Microbenchmark + latency-budget assertion | 180 | Asserts p99 <= 45000 ns at the declared reference shape. |
| 16 | Documentation block: usage, rationale, limitations, references | 300 | Honest limitations section is mandatory; no overstated claims. |
| | **total** | **5000** | |

**Acceptance criteria — a reviewer rejects the file if any one fails.**

- [ ] File is exactly one file at `parts/t14_perception/P0700_perception_spec_doc.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t14.perception.perception_spec_doc@1`.
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
