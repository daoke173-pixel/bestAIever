# HYPERION-Ω — index of all 1000 parts

A light, always-renderable index. The full architecture, the Opus 5 baseline, the 100× speed law, the Ω-Contract and the inline prompts live in [`README.md`](README.md).

1000 parts · 20 tiers · ~5,000,000 lines · Ω-CONTRACT v1.0.0-frozen

| tier | title | lang | parts | specs | prompts |
|---|---|---|---|---|---|
| T01 | Foundation, ABI & Determinism | Python 3.13 | P0001–P0050 | [specs](docs/PART_SPECS_T01.md) | [prompts](docs/PROMPTS_T01.md) |
| T02 | Tensor Runtime & Compute Kernels | Rust 1.86 (+ inline CUDA/PTX) | P0051–P0100 | [specs](docs/PART_SPECS_T02.md) | [prompts](docs/PROMPTS_T02.md) |
| T03 | Graph IR, Compiler & Autotuner | Rust 1.86 | P0101–P0150 | [specs](docs/PART_SPECS_T03.md) | [prompts](docs/PROMPTS_T03.md) |
| T04 | Hardware Abstraction & Interconnect | Rust 1.86 | P0151–P0200 | [specs](docs/PART_SPECS_T04.md) | [prompts](docs/PROMPTS_T04.md) |
| T05 | Ω-Core Model Architecture | Python 3.13 | P0201–P0250 | [specs](docs/PART_SPECS_T05.md) | [prompts](docs/PROMPTS_T05.md) |
| T06 | Sparse Routing & Mixture-of-Ω-Experts | Python 3.13 | P0251–P0300 | [specs](docs/PART_SPECS_T06.md) | [prompts](docs/PROMPTS_T06.md) |
| T07 | Memory, Retrieval & World Model | Python 3.13 | P0301–P0350 | [specs](docs/PART_SPECS_T07.md) | [prompts](docs/PROMPTS_T07.md) |
| T08 | Inference Engine & Ω-Cascade | Rust 1.86 | P0351–P0400 | [specs](docs/PART_SPECS_T08.md) | [prompts](docs/PROMPTS_T08.md) |
| T09 | Latency Engineering & Ω-Memoize | Rust 1.86 | P0401–P0450 | [specs](docs/PART_SPECS_T09.md) | [prompts](docs/PROMPTS_T09.md) |
| T10 | Reasoning, Search & Deliberation | Python 3.13 | P0451–P0500 | [specs](docs/PART_SPECS_T10.md) | [prompts](docs/PROMPTS_T10.md) |
| T11 | Formal Methods & Proof-Carrying Answers | Python 3.13 | P0501–P0550 | [specs](docs/PART_SPECS_T11.md) | [prompts](docs/PROMPTS_T11.md) |
| T12 | Code Intelligence & Repository Surgery | Python 3.13 | P0551–P0600 | [specs](docs/PART_SPECS_T12.md) | [prompts](docs/PROMPTS_T12.md) |
| T13 | Agents, Tool Use & Computer Control | Python 3.13 | P0601–P0650 | [specs](docs/PART_SPECS_T13.md) | [prompts](docs/PROMPTS_T13.md) |
| T14 | Multimodal Perception & Grounding | Python 3.13 | P0651–P0700 | [specs](docs/PART_SPECS_T14.md) | [prompts](docs/PROMPTS_T14.md) |
| T15 | Generation, Artifacts & Interface Craft | TypeScript 5.7 | P0701–P0750 | [specs](docs/PART_SPECS_T15.md) | [prompts](docs/PROMPTS_T15.md) |
| T16 | Domain Superintelligence Packs | Python 3.13 | P0751–P0800 | [specs](docs/PART_SPECS_T16.md) | [prompts](docs/PROMPTS_T16.md) |
| T17 | Training, Data & Recursive Self-Improvement | Python 3.13 | P0801–P0850 | [specs](docs/PART_SPECS_T17.md) | [prompts](docs/PROMPTS_T17.md) |
| T18 | Evaluation, Benchmarking & Dominance Proofs | Python 3.13 | P0851–P0900 | [specs](docs/PART_SPECS_T18.md) | [prompts](docs/PROMPTS_T18.md) |
| T19 | Safety, Alignment, Interpretability & Governance | Python 3.13 | P0901–P0950 | [specs](docs/PART_SPECS_T19.md) | [prompts](docs/PROMPTS_T19.md) |
| T20 | Platform, SDK, Ops & Distributed Assembly | TypeScript 5.7 | P0951–P1000 | [specs](docs/PART_SPECS_T20.md) | [prompts](docs/PROMPTS_T20.md) |

## T01 — Foundation, ABI & Determinism

*Frozen type system, capability ABI, deterministic primitives and the Ω-Bus reference semantics that every other part links against.*

| part | slug | title | capability | det | p99 ns | spec | prompt |
|---|---|---|---|---|---:|---|---|
| P0001 | `abi_types` | Core ABI Scalar & Tensor Type System | `cap.t01.abi.abi_types@1` | pure | 4000 | [spec](docs/PART_SPECS_T01.md#p0001-abi-types) | [txt](prompts/P0001_abi_types.txt) |
| P0002 | `abi_errors` | OmegaError Taxonomy & Cause Chains | `cap.t01.abi.abi_errors@1` | pure | 5000 | [spec](docs/PART_SPECS_T01.md#p0002-abi-errors) | [txt](prompts/P0002_abi_errors.txt) |
| P0003 | `abi_result` | Result / Partial / Budget Monad | `cap.t01.abi.abi_result@1` | pure | 6000 | [spec](docs/PART_SPECS_T01.md#p0003-abi-result) | [txt](prompts/P0003_abi_result.txt) |
| P0004 | `cbor_canonical` | Deterministic CBOR Codec | `cap.t01.cbor.cbor_canonical@1` | pure | 7000 | [spec](docs/PART_SPECS_T01.md#p0004-cbor-canonical) | [txt](prompts/P0004_cbor_canonical.txt) |
| P0005 | `blake3_hash` | BLAKE3 & Merkle Integrity Core | `cap.t01.blake3.blake3_hash@1` | pure | 8000 | [spec](docs/PART_SPECS_T01.md#p0005-blake3-hash) | [txt](prompts/P0005_blake3_hash.txt) |
| P0006 | `chacha_seeds` | split_seed Deterministic RNG | `cap.t01.chacha.chacha_seeds@1` | pure | 9000 | [spec](docs/PART_SPECS_T01.md#p0006-chacha-seeds) | [txt](prompts/P0006_chacha_seeds.txt) |
| P0007 | `omega_bus_core` | Ω-Bus Capability Registry | `cap.t01.omega.omega_bus_core@1` | pure | 10000 | [spec](docs/PART_SPECS_T01.md#p0007-omega-bus-core) | [txt](prompts/P0007_omega_bus_core.txt) |
| P0008 | `omega_bus_ipc` | Cross-Process Ω-Bus Transport | `cap.t01.omega.omega_bus_ipc@1` | pure | 11000 | [spec](docs/PART_SPECS_T01.md#p0008-omega-bus-ipc) | [txt](prompts/P0008_omega_bus_ipc.txt) |
| P0009 | `envelope_codec` | OmegaEnvelope Encode/Decode | `cap.t01.envelope.envelope_codec@1` | pure | 12000 | [spec](docs/PART_SPECS_T01.md#p0009-envelope-codec) | [txt](prompts/P0009_envelope_codec.txt) |
| P0010 | `trace_context` | Distributed Trace & Span Model | `cap.t01.trace.trace_context@1` | pure | 13000 | [spec](docs/PART_SPECS_T01.md#p0010-trace-context) | [txt](prompts/P0010_trace_context.txt) |
| P0011 | `clock_time` | Monotonic Clock & Deadline Arithmetic | `cap.t01.clock.clock_time@1` | pure | 14000 | [spec](docs/PART_SPECS_T01.md#p0011-clock-time) | [txt](prompts/P0011_clock_time.txt) |
| P0012 | `alloc_arena` | Arena & Slab Allocators | `cap.t01.alloc.alloc_arena@1` | pure | 15000 | [spec](docs/PART_SPECS_T01.md#p0012-alloc-arena) | [txt](prompts/P0012_alloc_arena.txt) |
| P0013 | `mem_layout` | Cache-Aware Data Layout Toolkit | `cap.t01.mem.mem_layout@1` | pure | 16000 | [spec](docs/PART_SPECS_T01.md#p0013-mem-layout) | [txt](prompts/P0013_mem_layout.txt) |
| P0014 | `atomics_sync` | Lock-Free Synchronisation Primitives | `cap.t01.atomics.atomics_sync@1` | pure | 17000 | [spec](docs/PART_SPECS_T01.md#p0014-atomics-sync) | [txt](prompts/P0014_atomics_sync.txt) |
| P0015 | `task_runtime` | Deterministic Task Scheduler | `cap.t01.task.task_runtime@1` | pure | 18000 | [spec](docs/PART_SPECS_T01.md#p0015-task-runtime) | [txt](prompts/P0015_task_runtime.txt) |
| P0016 | `dataflow_dag` | Task DAG Representation & Scheduling | `cap.t01.dataflow.dataflow_dag@1` | pure | 19000 | [spec](docs/PART_SPECS_T01.md#p0016-dataflow-dag) | [txt](prompts/P0016_dataflow_dag.txt) |
| P0017 | `fixed_point` | Certified Fixed-Point & Interval Arithmetic | `cap.t01.fixed.fixed_point@1` | pure | 20000 | [spec](docs/PART_SPECS_T01.md#p0017-fixed-point) | [txt](prompts/P0017_fixed_point.txt) |
| P0018 | `bigint_modmath` | Big Integer & Modular Arithmetic | `cap.t01.bigint.bigint_modmath@1` | pure | 21000 | [spec](docs/PART_SPECS_T01.md#p0018-bigint-modmath) | [txt](prompts/P0018_bigint_modmath.txt) |
| P0019 | `bitset_rank` | Succinct Bitsets, Rank/Select & Bloom Filters | `cap.t01.bitset.bitset_rank@1` | pure | 22000 | [spec](docs/PART_SPECS_T01.md#p0019-bitset-rank) | [txt](prompts/P0019_bitset_rank.txt) |
| P0020 | `hash_maps` | High-Performance Hash Containers | `cap.t01.hash.hash_maps@1` | pure | 23000 | [spec](docs/PART_SPECS_T01.md#p0020-hash-maps) | [txt](prompts/P0020_hash_maps.txt) |
| P0021 | `string_interning` | String Interning & Symbol Tables | `cap.t01.string.string_interning@1` | pure | 24000 | [spec](docs/PART_SPECS_T01.md#p0021-string-interning) | [txt](prompts/P0021_string_interning.txt) |
| P0022 | `arena_graph` | Generic Graph Store & Algorithms | `cap.t01.arena.arena_graph@1` | pure | 25000 | [spec](docs/PART_SPECS_T01.md#p0022-arena-graph) | [txt](prompts/P0022_arena_graph.txt) |
| P0023 | `serialization_schema` | Schema Registry & Evolution Rules | `cap.t01.serialization.serialization_schema@1` | pure | 26000 | [spec](docs/PART_SPECS_T01.md#p0023-serialization-schema) | [txt](prompts/P0023_serialization_schema.txt) |
| P0024 | `config_system` | Layered Configuration & Feature Flags | `cap.t01.config.config_system@1` | pure | 27000 | [spec](docs/PART_SPECS_T01.md#p0024-config-system) | [txt](prompts/P0024_config_system.txt) |
| P0025 | `logging_events` | Structured Event Emission Core | `cap.t01.logging.logging_events@1` | pure | 28000 | [spec](docs/PART_SPECS_T01.md#p0025-logging-events) | [txt](prompts/P0025_logging_events.txt) |
| P0026 | `metrics_core` | Counters, Gauges & HDR Histograms | `cap.t01.metrics.metrics_core@1` | pure | 29000 | [spec](docs/PART_SPECS_T01.md#p0026-metrics-core) | [txt](prompts/P0026_metrics_core.txt) |
| P0027 | `selftest_harness` | In-File Self-Test Framework | `cap.t01.selftest.selftest_harness@1` | pure | 30000 | [spec](docs/PART_SPECS_T01.md#p0027-selftest-harness) | [txt](prompts/P0027_selftest_harness.txt) |
| P0028 | `property_gen` | Property Generators & Shrinkers | `cap.t01.property.property_gen@1` | pure | 31000 | [spec](docs/PART_SPECS_T01.md#p0028-property-gen) | [txt](prompts/P0028_property_gen.txt) |
| P0029 | `fuzz_engine` | Coverage-Guided In-Process Fuzzer | `cap.t01.fuzz.fuzz_engine@1` | pure | 32000 | [spec](docs/PART_SPECS_T01.md#p0029-fuzz-engine) | [txt](prompts/P0029_fuzz_engine.txt) |
| P0030 | `bench_harness` | Microbenchmark Harness & Latency Gate | `cap.t01.bench.bench_harness@1` | pure | 33000 | [spec](docs/PART_SPECS_T01.md#p0030-bench-harness) | [txt](prompts/P0030_bench_harness.txt) |
| P0031 | `determinism_replay` | Record & Replay Engine | `cap.t01.determinism.determinism_replay@1` | pure | 34000 | [spec](docs/PART_SPECS_T01.md#p0031-determinism-replay) | [txt](prompts/P0031_determinism_replay.txt) |
| P0032 | `checksum_verify` | Cross-Platform Numeric Equivalence Checker | `cap.t01.checksum.checksum_verify@1` | pure | 35000 | [spec](docs/PART_SPECS_T01.md#p0032-checksum-verify) | [txt](prompts/P0032_checksum_verify.txt) |
| P0033 | `capability_gate` | Capability Acquisition Policy & Fallbacks | `cap.t01.capability.capability_gate@1` | pure | 36000 | [spec](docs/PART_SPECS_T01.md#p0033-capability-gate) | [txt](prompts/P0033_capability_gate.txt) |
| P0034 | `version_semver` | Semantic Version & Compatibility Engine | `cap.t01.version.version_semver@1` | pure | 37000 | [spec](docs/PART_SPECS_T01.md#p0034-version-semver) | [txt](prompts/P0034_version_semver.txt) |
| P0035 | `link_validator` | Static Link Validator for 1000 Parts | `cap.t01.link.link_validator@1` | pure | 38000 | [spec](docs/PART_SPECS_T01.md#p0035-link-validator) | [txt](prompts/P0035_link_validator.txt) |
| P0036 | `manifest_parser` | PART_MANIFEST Parser & Validator | `cap.t01.manifest.manifest_parser@1` | pure | 39000 | [spec](docs/PART_SPECS_T01.md#p0036-manifest-parser) | [txt](prompts/P0036_manifest_parser.txt) |
| P0037 | `abi_stability` | ABI Stability & Frozen-Symbol Guard | `cap.t01.abi.abi_stability@1` | pure | 40000 | [spec](docs/PART_SPECS_T01.md#p0037-abi-stability) | [txt](prompts/P0037_abi_stability.txt) |
| P0038 | `compat_shims` | Cross-Language Interop Shims | `cap.t01.compat.compat_shims@1` | pure | 41000 | [spec](docs/PART_SPECS_T01.md#p0038-compat-shims) | [txt](prompts/P0038_compat_shims.txt) |
| P0039 | `numeric_limits` | Numeric Policy, Rounding & Overflow Rules | `cap.t01.numeric.numeric_limits@1` | pure | 42000 | [spec](docs/PART_SPECS_T01.md#p0039-numeric-limits) | [txt](prompts/P0039_numeric_limits.txt) |
| P0040 | `unit_dimensions` | Physical Units & Dimensional Analysis | `cap.t01.unit.unit_dimensions@1` | pure | 43000 | [spec](docs/PART_SPECS_T01.md#p0040-unit-dimensions) | [txt](prompts/P0040_unit_dimensions.txt) |
| P0041 | `budget_ledger` | Token / FLOP / Dollar Budget Ledger | `cap.t01.budget.budget_ledger@1` | pure | 44000 | [spec](docs/PART_SPECS_T01.md#p0041-budget-ledger) | [txt](prompts/P0041_budget_ledger.txt) |
| P0042 | `rate_limiter` | Deterministic Rate Limiting & Admission | `cap.t01.rate.rate_limiter@1` | pure | 45000 | [spec](docs/PART_SPECS_T01.md#p0042-rate-limiter) | [txt](prompts/P0042_rate_limiter.txt) |
| P0043 | `circuit_breaker` | Failure Isolation & Circuit Breaking | `cap.t01.circuit.circuit_breaker@1` | pure | 46000 | [spec](docs/PART_SPECS_T01.md#p0043-circuit-breaker) | [txt](prompts/P0043_circuit_breaker.txt) |
| P0044 | `retry_idempotency` | Retry, Idempotency & Exactly-Once Effects | `cap.t01.retry.retry_idempotency@1` | pure | 47000 | [spec](docs/PART_SPECS_T01.md#p0044-retry-idempotency) | [txt](prompts/P0044_retry_idempotency.txt) |
| P0045 | `secure_zeroize` | Secret Handling & Memory Hygiene | `cap.t01.secure.secure_zeroize@1` | pure | 48000 | [spec](docs/PART_SPECS_T01.md#p0045-secure-zeroize) | [txt](prompts/P0045_secure_zeroize.txt) |
| P0046 | `sandbox_policy` | Process Sandbox & Syscall Policy Descriptors | `cap.t01.sandbox.sandbox_policy@1` | pure | 49000 | [spec](docs/PART_SPECS_T01.md#p0046-sandbox-policy) | [txt](prompts/P0046_sandbox_policy.txt) |
| P0047 | `fs_atomic` | Atomic Filesystem & Content-Addressed Store | `cap.t01.fs.fs_atomic@1` | pure | 3000 | [spec](docs/PART_SPECS_T01.md#p0047-fs-atomic) | [txt](prompts/P0047_fs_atomic.txt) |
| P0048 | `compression` | Streaming Compression & Delta Encoding | `cap.t01.compression.compression@1` | pure | 4000 | [spec](docs/PART_SPECS_T01.md#p0048-compression) | [txt](prompts/P0048_compression.txt) |
| P0049 | `bootstrap_init` | Assembly Bootstrap & Startup Ordering | `cap.t01.bootstrap.bootstrap_init@1` | pure | 5000 | [spec](docs/PART_SPECS_T01.md#p0049-bootstrap-init) | [txt](prompts/P0049_bootstrap_init.txt) |
| P0050 | `shutdown_drain` | Graceful Drain & Crash-Consistency | `cap.t01.shutdown.shutdown_drain@1` | pure | 6000 | [spec](docs/PART_SPECS_T01.md#p0050-shutdown-drain) | [txt](prompts/P0050_shutdown_drain.txt) |

## T02 — Tensor Runtime & Compute Kernels

*Peak-throughput numeric kernels: attention, GEMM, quantization, collectives-local, memory movement. Source of speedup S3.*

| part | slug | title | capability | det | p99 ns | spec | prompt |
|---|---|---|---|---|---:|---|---|
| P0051 | `gemm_fp8` | FP8 Tensor-Core GEMM Kernel | `cap.t02.gemm.gemm_fp8@1` | pure | 7000 | [spec](docs/PART_SPECS_T02.md#p0051-gemm-fp8) | [txt](prompts/P0051_gemm_fp8.txt) |
| P0052 | `gemm_int4` | INT4/INT8 Mixed-Precision GEMM | `cap.t02.gemm.gemm_int4@1` | pure | 8000 | [spec](docs/PART_SPECS_T02.md#p0052-gemm-int4) | [txt](prompts/P0052_gemm_int4.txt) |
| P0053 | `gemm_grouped` | Grouped & Batched GEMM for MoE | `cap.t02.gemm.gemm_grouped@1` | pure | 9000 | [spec](docs/PART_SPECS_T02.md#p0053-gemm-grouped) | [txt](prompts/P0053_gemm_grouped.txt) |
| P0054 | `gemm_sparse` | Structured-Sparse GEMM (2:4 and block) | `cap.t02.gemm.gemm_sparse@1` | pure | 10000 | [spec](docs/PART_SPECS_T02.md#p0054-gemm-sparse) | [txt](prompts/P0054_gemm_sparse.txt) |
| P0055 | `attn_flash_fwd` | Fused Flash Attention Forward | `cap.t02.attn.attn_flash_fwd@1` | pure | 11000 | [spec](docs/PART_SPECS_T02.md#p0055-attn-flash-fwd) | [txt](prompts/P0055_attn_flash_fwd.txt) |
| P0056 | `attn_flash_bwd` | Fused Flash Attention Backward | `cap.t02.attn.attn_flash_bwd@1` | pure | 12000 | [spec](docs/PART_SPECS_T02.md#p0056-attn-flash-bwd) | [txt](prompts/P0056_attn_flash_bwd.txt) |
| P0057 | `attn_paged_decode` | Paged KV Decode Attention | `cap.t02.attn.attn_paged_decode@1` | pure | 13000 | [spec](docs/PART_SPECS_T02.md#p0057-attn-paged-decode) | [txt](prompts/P0057_attn_paged_decode.txt) |
| P0058 | `attn_linear` | Linear & Kernel-Feature Attention | `cap.t02.attn.attn_linear@1` | pure | 14000 | [spec](docs/PART_SPECS_T02.md#p0058-attn-linear) | [txt](prompts/P0058_attn_linear.txt) |
| P0059 | `ssm_scan` | Selective State-Space Scan Kernel | `cap.t02.ssm.ssm_scan@1` | pure | 15000 | [spec](docs/PART_SPECS_T02.md#p0059-ssm-scan) | [txt](prompts/P0059_ssm_scan.txt) |
| P0060 | `conv_depthwise` | Depthwise & Short-Convolution Kernels | `cap.t02.conv.conv_depthwise@1` | pure | 16000 | [spec](docs/PART_SPECS_T02.md#p0060-conv-depthwise) | [txt](prompts/P0060_conv_depthwise.txt) |
| P0061 | `softmax_norm` | Softmax, LogSumExp & Normalisation Kernels | `cap.t02.softmax.softmax_norm@1` | pure | 17000 | [spec](docs/PART_SPECS_T02.md#p0061-softmax-norm) | [txt](prompts/P0061_softmax_norm.txt) |
| P0062 | `elementwise_fusion` | Elementwise Fusion Engine | `cap.t02.elementwise.elementwise_fusion@1` | pure | 18000 | [spec](docs/PART_SPECS_T02.md#p0062-elementwise-fusion) | [txt](prompts/P0062_elementwise_fusion.txt) |
| P0063 | `reduction_kernels` | Deterministic Reduction & Scan Library | `cap.t02.reduction.reduction_kernels@1` | pure | 19000 | [spec](docs/PART_SPECS_T02.md#p0063-reduction-kernels) | [txt](prompts/P0063_reduction_kernels.txt) |
| P0064 | `topk_sort` | Top-K, Sort & Sampling Kernels | `cap.t02.topk.topk_sort@1` | pure | 20000 | [spec](docs/PART_SPECS_T02.md#p0064-topk-sort) | [txt](prompts/P0064_topk_sort.txt) |
| P0065 | `quantize_kernels` | Quantisation & Dequantisation Kernels | `cap.t02.quantize.quantize_kernels@1` | pure | 21000 | [spec](docs/PART_SPECS_T02.md#p0065-quantize-kernels) | [txt](prompts/P0065_quantize_kernels.txt) |
| P0066 | `kv_cache_kernels` | KV Cache Compression Kernels | `cap.t02.kv.kv_cache_kernels@1` | pure | 22000 | [spec](docs/PART_SPECS_T02.md#p0066-kv-cache-kernels) | [txt](prompts/P0066_kv_cache_kernels.txt) |
| P0067 | `rope_embed` | Positional Encoding Kernels | `cap.t02.rope.rope_embed@1` | pure | 23000 | [spec](docs/PART_SPECS_T02.md#p0067-rope-embed) | [txt](prompts/P0067_rope_embed.txt) |
| P0068 | `gather_scatter` | Gather / Scatter / Permute Kernels | `cap.t02.gather.gather_scatter@1` | pure | 24000 | [spec](docs/PART_SPECS_T02.md#p0068-gather-scatter) | [txt](prompts/P0068_gather_scatter.txt) |
| P0069 | `transpose_layout` | Layout Transform & Transpose Kernels | `cap.t02.transpose.transpose_layout@1` | pure | 25000 | [spec](docs/PART_SPECS_T02.md#p0069-transpose-layout) | [txt](prompts/P0069_transpose_layout.txt) |
| P0070 | `rng_kernels` | Device-Side RNG Kernels | `cap.t02.rng.rng_kernels@1` | pure | 26000 | [spec](docs/PART_SPECS_T02.md#p0070-rng-kernels) | [txt](prompts/P0070_rng_kernels.txt) |
| P0071 | `fused_moe_kernel` | Fully Fused MoE Layer Kernel | `cap.t02.fused.fused_moe_kernel@1` | pure | 27000 | [spec](docs/PART_SPECS_T02.md#p0071-fused-moe-kernel) | [txt](prompts/P0071_fused_moe_kernel.txt) |
| P0072 | `fused_decode_step` | Whole-Decode-Step Persistent Kernel | `cap.t02.fused.fused_decode_step@1` | pure | 28000 | [spec](docs/PART_SPECS_T02.md#p0072-fused-decode-step) | [txt](prompts/P0072_fused_decode_step.txt) |
| P0073 | `graph_capture` | Command-Graph Capture & Replay | `cap.t02.graph.graph_capture@1` | pure | 29000 | [spec](docs/PART_SPECS_T02.md#p0073-graph-capture) | [txt](prompts/P0073_graph_capture.txt) |
| P0074 | `mem_pool_device` | Device Memory Pool & Defragmenter | `cap.t02.mem.mem_pool_device@1` | pure | 30000 | [spec](docs/PART_SPECS_T02.md#p0074-mem-pool-device) | [txt](prompts/P0074_mem_pool_device.txt) |
| P0075 | `async_copy` | Asynchronous Copy & Pipelining Engine | `cap.t02.async.async_copy@1` | pure | 31000 | [spec](docs/PART_SPECS_T02.md#p0075-async-copy) | [txt](prompts/P0075_async_copy.txt) |
| P0076 | `cache_blocking` | Cache Blocking & Tiling Autotuner Hooks | `cap.t02.cache.cache_blocking@1` | pure | 32000 | [spec](docs/PART_SPECS_T02.md#p0076-cache-blocking) | [txt](prompts/P0076_cache_blocking.txt) |
| P0077 | `simd_cpu` | CPU SIMD Kernel Set | `cap.t02.simd.simd_cpu@1` | pure | 33000 | [spec](docs/PART_SPECS_T02.md#p0077-simd-cpu) | [txt](prompts/P0077_simd_cpu.txt) |
| P0078 | `numa_placement` | NUMA-Aware Placement & Migration | `cap.t02.numa.numa_placement@1` | pure | 34000 | [spec](docs/PART_SPECS_T02.md#p0078-numa-placement) | [txt](prompts/P0078_numa_placement.txt) |
| P0079 | `bf16_stability` | Low-Precision Stability Toolkit | `cap.t02.bf16.bf16_stability@1` | pure | 35000 | [spec](docs/PART_SPECS_T02.md#p0079-bf16-stability) | [txt](prompts/P0079_bf16_stability.txt) |
| P0080 | `kernel_registry` | Kernel Registry & Runtime Dispatch | `cap.t02.kernel.kernel_registry@1` | pure | 36000 | [spec](docs/PART_SPECS_T02.md#p0080-kernel-registry) | [txt](prompts/P0080_kernel_registry.txt) |
| P0081 | `kernel_verify` | Kernel Numerical Verification Suite | `cap.t02.kernel.kernel_verify@1` | pure | 37000 | [spec](docs/PART_SPECS_T02.md#p0081-kernel-verify) | [txt](prompts/P0081_kernel_verify.txt) |
| P0082 | `roofline_model` | Roofline & Performance Model | `cap.t02.roofline.roofline_model@1` | pure | 38000 | [spec](docs/PART_SPECS_T02.md#p0082-roofline-model) | [txt](prompts/P0082_roofline_model.txt) |
| P0083 | `profiler_hooks` | Kernel Profiling & Counter Collection | `cap.t02.profiler.profiler_hooks@1` | pure | 39000 | [spec](docs/PART_SPECS_T02.md#p0083-profiler-hooks) | [txt](prompts/P0083_profiler_hooks.txt) |
| P0084 | `emulation_reference` | Bit-Exact CPU Emulation of All Kernels | `cap.t02.emulation.emulation_reference@1` | pure | 40000 | [spec](docs/PART_SPECS_T02.md#p0084-emulation-reference) | [txt](prompts/P0084_emulation_reference.txt) |
| P0085 | `kernel_fusion_rules` | Fusion Legality & Rewrite Rules | `cap.t02.kernel.kernel_fusion_rules@1` | pure | 41000 | [spec](docs/PART_SPECS_T02.md#p0085-kernel-fusion-rules) | [txt](prompts/P0085_kernel_fusion_rules.txt) |
| P0086 | `collective_local` | Intra-Node Collectives | `cap.t02.collective.collective_local@1` | pure | 42000 | [spec](docs/PART_SPECS_T02.md#p0086-collective-local) | [txt](prompts/P0086_collective_local.txt) |
| P0087 | `p2p_transfer` | Peer-to-Peer Device Transfer | `cap.t02.p2p.p2p_transfer@1` | pure | 43000 | [spec](docs/PART_SPECS_T02.md#p0087-p2p-transfer) | [txt](prompts/P0087_p2p_transfer.txt) |
| P0088 | `stream_scheduler` | Stream & Event Scheduling | `cap.t02.stream.stream_scheduler@1` | pure | 44000 | [spec](docs/PART_SPECS_T02.md#p0088-stream-scheduler) | [txt](prompts/P0088_stream_scheduler.txt) |
| P0089 | `power_thermal` | Power & Thermal-Aware Kernel Governance | `cap.t02.power.power_thermal@1` | pure | 45000 | [spec](docs/PART_SPECS_T02.md#p0089-power-thermal) | [txt](prompts/P0089_power_thermal.txt) |
| P0090 | `error_correction` | Hardware Fault Detection & Correction | `cap.t02.error.error_correction@1` | pure | 46000 | [spec](docs/PART_SPECS_T02.md#p0090-error-correction) | [txt](prompts/P0090_error_correction.txt) |
| P0091 | `kernel_codegen_rt` | Runtime Kernel Code Generation & JIT Cache | `cap.t02.kernel.kernel_codegen_rt@1` | pure | 47000 | [spec](docs/PART_SPECS_T02.md#p0091-kernel-codegen-rt) | [txt](prompts/P0091_kernel_codegen_rt.txt) |
| P0092 | `sparse_attention_kernels` | Sparse & Hierarchical Attention Kernels | `cap.t02.sparse.sparse_attention_kernels@1` | pure | 48000 | [spec](docs/PART_SPECS_T02.md#p0092-sparse-attention-kernels) | [txt](prompts/P0092_sparse_attention_kernels.txt) |
| P0093 | `embedding_kernels` | Embedding & Unembedding Kernels | `cap.t02.embedding.embedding_kernels@1` | pure | 49000 | [spec](docs/PART_SPECS_T02.md#p0093-embedding-kernels) | [txt](prompts/P0093_embedding_kernels.txt) |
| P0094 | `mask_engine` | Mask Construction & Compression Engine | `cap.t02.mask.mask_engine@1` | pure | 3000 | [spec](docs/PART_SPECS_T02.md#p0094-mask-engine) | [txt](prompts/P0094_mask_engine.txt) |
| P0095 | `tensor_view` | Zero-Copy Tensor View Algebra | `cap.t02.tensor.tensor_view@1` | pure | 4000 | [spec](docs/PART_SPECS_T02.md#p0095-tensor-view) | [txt](prompts/P0095_tensor_view.txt) |
| P0096 | `ragged_batch` | Ragged & Packed Batch Kernels | `cap.t02.ragged.ragged_batch@1` | pure | 5000 | [spec](docs/PART_SPECS_T02.md#p0096-ragged-batch) | [txt](prompts/P0096_ragged_batch.txt) |
| P0097 | `kernel_bench_suite` | Kernel Benchmark Suite & Baselines | `cap.t02.kernel.kernel_bench_suite@1` | pure | 6000 | [spec](docs/PART_SPECS_T02.md#p0097-kernel-bench-suite) | [txt](prompts/P0097_kernel_bench_suite.txt) |
| P0098 | `micro_opt_catalog` | Micro-Optimisation Catalogue | `cap.t02.micro.micro_opt_catalog@1` | pure | 7000 | [spec](docs/PART_SPECS_T02.md#p0098-micro-opt-catalog) | [txt](prompts/P0098_micro_opt_catalog.txt) |
| P0099 | `tensor_core_util` | Tensor-Core Utilisation Optimiser | `cap.t02.tensor.tensor_core_util@1` | pure | 8000 | [spec](docs/PART_SPECS_T02.md#p0099-tensor-core-util) | [txt](prompts/P0099_tensor_core_util.txt) |
| P0100 | `kernel_docs_spec` | Kernel Contract Specification & Docs Generator | `cap.t02.kernel.kernel_docs_spec@1` | pure | 9000 | [spec](docs/PART_SPECS_T02.md#p0100-kernel-docs-spec) | [txt](prompts/P0100_kernel_docs_spec.txt) |

## T03 — Graph IR, Compiler & Autotuner

*Ω-IR capture, algebraic rewriting, fusion, scheduling, autotuning and codegen for every accelerator target.*

| part | slug | title | capability | det | p99 ns | spec | prompt |
|---|---|---|---|---|---:|---|---|
| P0101 | `ir_core` | Ω-IR Core Data Structures | `cap.t03.ir.ir_core@1` | pure | 10000 | [spec](docs/PART_SPECS_T03.md#p0101-ir-core) | [txt](prompts/P0101_ir_core.txt) |
| P0102 | `ir_builder` | IR Construction & Tracing Frontend | `cap.t03.ir.ir_builder@1` | pure | 11000 | [spec](docs/PART_SPECS_T03.md#p0102-ir-builder) | [txt](prompts/P0102_ir_builder.txt) |
| P0103 | `ir_printer` | IR Textual Format, Parser & Round-Trip | `cap.t03.ir.ir_printer@1` | pure | 12000 | [spec](docs/PART_SPECS_T03.md#p0103-ir-printer) | [txt](prompts/P0103_ir_printer.txt) |
| P0104 | `pass_manager` | Pass Manager & Optimisation Pipelines | `cap.t03.pass.pass_manager@1` | pure | 13000 | [spec](docs/PART_SPECS_T03.md#p0104-pass-manager) | [txt](prompts/P0104_pass_manager.txt) |
| P0105 | `shape_inference` | Symbolic Shape Inference & Constraint Solver | `cap.t03.shape.shape_inference@1` | pure | 14000 | [spec](docs/PART_SPECS_T03.md#p0105-shape-inference) | [txt](prompts/P0105_shape_inference.txt) |
| P0106 | `dtype_promotion` | Precision Assignment & Mixed-Precision Planner | `cap.t03.dtype.dtype_promotion@1` | pure | 15000 | [spec](docs/PART_SPECS_T03.md#p0106-dtype-promotion) | [txt](prompts/P0106_dtype_promotion.txt) |
| P0107 | `algebraic_rewrite` | Algebraic Simplification & Rewrite Engine | `cap.t03.algebraic.algebraic_rewrite@1` | pure | 16000 | [spec](docs/PART_SPECS_T03.md#p0107-algebraic-rewrite) | [txt](prompts/P0107_algebraic_rewrite.txt) |
| P0108 | `fusion_pass` | Operator Fusion Pass | `cap.t03.fusion.fusion_pass@1` | pure | 17000 | [spec](docs/PART_SPECS_T03.md#p0108-fusion-pass) | [txt](prompts/P0108_fusion_pass.txt) |
| P0109 | `layout_assignment` | Layout Assignment & Relayout Minimisation | `cap.t03.layout.layout_assignment@1` | pure | 18000 | [spec](docs/PART_SPECS_T03.md#p0109-layout-assignment) | [txt](prompts/P0109_layout_assignment.txt) |
| P0110 | `memory_planner` | Static Memory Planner & Liveness Allocator | `cap.t03.memory.memory_planner@1` | pure | 19000 | [spec](docs/PART_SPECS_T03.md#p0110-memory-planner) | [txt](prompts/P0110_memory_planner.txt) |
| P0111 | `rematerialisation` | Activation Rematerialisation Planner | `cap.t03.rematerialisat.rematerialisation@1` | pure | 20000 | [spec](docs/PART_SPECS_T03.md#p0111-rematerialisation) | [txt](prompts/P0111_rematerialisation.txt) |
| P0112 | `scheduler_pass` | Instruction Scheduling & Overlap Pass | `cap.t03.scheduler.scheduler_pass@1` | pure | 21000 | [spec](docs/PART_SPECS_T03.md#p0112-scheduler-pass) | [txt](prompts/P0112_scheduler_pass.txt) |
| P0113 | `parallel_partition` | Automatic Parallelism Partitioner | `cap.t03.parallel.parallel_partition@1` | pure | 22000 | [spec](docs/PART_SPECS_T03.md#p0113-parallel-partition) | [txt](prompts/P0113_parallel_partition.txt) |
| P0114 | `pipeline_planner` | Pipeline Parallel Schedule Synthesiser | `cap.t03.pipeline.pipeline_planner@1` | pure | 23000 | [spec](docs/PART_SPECS_T03.md#p0114-pipeline-planner) | [txt](prompts/P0114_pipeline_planner.txt) |
| P0115 | `collective_insertion` | Collective Communication Insertion & Fusion | `cap.t03.collective.collective_insertion@1` | pure | 24000 | [spec](docs/PART_SPECS_T03.md#p0115-collective-insertion) | [txt](prompts/P0115_collective_insertion.txt) |
| P0116 | `autotuner_core` | Autotuning Search Engine | `cap.t03.autotuner.autotuner_core@1` | pure | 25000 | [spec](docs/PART_SPECS_T03.md#p0116-autotuner-core) | [txt](prompts/P0116_autotuner_core.txt) |
| P0117 | `cost_model_learned` | Learned Cost Model | `cap.t03.cost.cost_model_learned@1` | pure | 26000 | [spec](docs/PART_SPECS_T03.md#p0117-cost-model-learned) | [txt](prompts/P0117_cost_model_learned.txt) |
| P0118 | `codegen_gpu` | Accelerator Code Generator | `cap.t03.codegen.codegen_gpu@1` | pure | 27000 | [spec](docs/PART_SPECS_T03.md#p0118-codegen-gpu) | [txt](prompts/P0118_codegen_gpu.txt) |
| P0119 | `codegen_cpu` | CPU Code Generator | `cap.t03.codegen.codegen_cpu@1` | pure | 28000 | [spec](docs/PART_SPECS_T03.md#p0119-codegen-cpu) | [txt](prompts/P0119_codegen_cpu.txt) |
| P0120 | `jit_cache_compiler` | Compilation Cache & Warm Start | `cap.t03.jit.jit_cache_compiler@1` | pure | 29000 | [spec](docs/PART_SPECS_T03.md#p0120-jit-cache-compiler) | [txt](prompts/P0120_jit_cache_compiler.txt) |
| P0121 | `guard_specialise` | Guarded Specialisation & Recompilation Policy | `cap.t03.guard.guard_specialise@1` | pure | 30000 | [spec](docs/PART_SPECS_T03.md#p0121-guard-specialise) | [txt](prompts/P0121_guard_specialise.txt) |
| P0122 | `kernel_selection` | Global Kernel Selection Optimiser | `cap.t03.kernel.kernel_selection@1` | pure | 31000 | [spec](docs/PART_SPECS_T03.md#p0122-kernel-selection) | [txt](prompts/P0122_kernel_selection.txt) |
| P0123 | `graph_partition_device` | Device Placement & Graph Partitioning | `cap.t03.graph.graph_partition_device@1` | pure | 32000 | [spec](docs/PART_SPECS_T03.md#p0123-graph-partition-device) | [txt](prompts/P0123_graph_partition_device.txt) |
| P0124 | `dynamic_shapes` | Dynamic Shape Execution Strategy | `cap.t03.dynamic.dynamic_shapes@1` | pure | 33000 | [spec](docs/PART_SPECS_T03.md#p0124-dynamic-shapes) | [txt](prompts/P0124_dynamic_shapes.txt) |
| P0125 | `differentiation` | Automatic Differentiation on Ω-IR | `cap.t03.differentiatio.differentiation@1` | pure | 34000 | [spec](docs/PART_SPECS_T03.md#p0125-differentiation) | [txt](prompts/P0125_differentiation.txt) |
| P0126 | `vectorisation_transform` | Batching & Vectorisation Transform | `cap.t03.vectorisation.vectorisation_transform@1` | pure | 35000 | [spec](docs/PART_SPECS_T03.md#p0126-vectorisation-transform) | [txt](prompts/P0126_vectorisation_transform.txt) |
| P0127 | `loop_transform` | Polyhedral Loop Transformation | `cap.t03.loop.loop_transform@1` | pure | 36000 | [spec](docs/PART_SPECS_T03.md#p0127-loop-transform) | [txt](prompts/P0127_loop_transform.txt) |
| P0128 | `constant_folding` | Constant Folding & Weight Preprocessing | `cap.t03.constant.constant_folding@1` | pure | 37000 | [spec](docs/PART_SPECS_T03.md#p0128-constant-folding) | [txt](prompts/P0128_constant_folding.txt) |
| P0129 | `dead_code_dce` | Dead Code, CSE & Canonicalisation | `cap.t03.dead.dead_code_dce@1` | pure | 38000 | [spec](docs/PART_SPECS_T03.md#p0129-dead-code-dce) | [txt](prompts/P0129_dead_code_dce.txt) |
| P0130 | `effect_system` | Effect & Purity Analysis | `cap.t03.effect.effect_system@1` | pure | 39000 | [spec](docs/PART_SPECS_T03.md#p0130-effect-system) | [txt](prompts/P0130_effect_system.txt) |
| P0131 | `ir_verifier` | IR Verification & Invariant Checking | `cap.t03.ir.ir_verifier@1` | pure | 40000 | [spec](docs/PART_SPECS_T03.md#p0131-ir-verifier) | [txt](prompts/P0131_ir_verifier.txt) |
| P0132 | `differential_testing` | Compiler Differential Test Harness | `cap.t03.differential.differential_testing@1` | pure | 41000 | [spec](docs/PART_SPECS_T03.md#p0132-differential-testing) | [txt](prompts/P0132_differential_testing.txt) |
| P0133 | `compile_time_budget` | Compilation Time Budget Manager | `cap.t03.compile.compile_time_budget@1` | pure | 42000 | [spec](docs/PART_SPECS_T03.md#p0133-compile-time-budget) | [txt](prompts/P0133_compile_time_budget.txt) |
| P0134 | `profile_guided` | Profile-Guided Optimisation Pipeline | `cap.t03.profile.profile_guided@1` | pure | 43000 | [spec](docs/PART_SPECS_T03.md#p0134-profile-guided) | [txt](prompts/P0134_profile_guided.txt) |
| P0135 | `target_description` | Target Machine Description Language | `cap.t03.target.target_description@1` | pure | 44000 | [spec](docs/PART_SPECS_T03.md#p0135-target-description) | [txt](prompts/P0135_target_description.txt) |
| P0136 | `ir_serialization` | IR Serialisation & Portable Artifact Format | `cap.t03.ir.ir_serialization@1` | pure | 45000 | [spec](docs/PART_SPECS_T03.md#p0136-ir-serialization) | [txt](prompts/P0136_ir_serialization.txt) |
| P0137 | `bytecode_vm` | Ω Execution Bytecode & Interpreter | `cap.t03.bytecode.bytecode_vm@1` | pure | 46000 | [spec](docs/PART_SPECS_T03.md#p0137-bytecode-vm) | [txt](prompts/P0137_bytecode_vm.txt) |
| P0138 | `debug_symbols` | Debug Info, Source Mapping & Blame | `cap.t03.debug.debug_symbols@1` | pure | 47000 | [spec](docs/PART_SPECS_T03.md#p0138-debug-symbols) | [txt](prompts/P0138_debug_symbols.txt) |
| P0139 | `pass_search` | Automated Pass Pipeline Search | `cap.t03.pass.pass_search@1` | pure | 48000 | [spec](docs/PART_SPECS_T03.md#p0139-pass-search) | [txt](prompts/P0139_pass_search.txt) |
| P0140 | `superoptimiser` | Bounded Superoptimiser for Hot Kernels | `cap.t03.superoptimiser.superoptimiser@1` | pure | 49000 | [spec](docs/PART_SPECS_T03.md#p0140-superoptimiser) | [txt](prompts/P0140_superoptimiser.txt) |
| P0141 | `equality_saturation` | E-Graph Engine & Extraction | `cap.t03.equality.equality_saturation@1` | pure | 3000 | [spec](docs/PART_SPECS_T03.md#p0141-equality-saturation) | [txt](prompts/P0141_equality_saturation.txt) |
| P0142 | `kernel_template_lib` | Kernel Template Library | `cap.t03.kernel.kernel_template_lib@1` | pure | 4000 | [spec](docs/PART_SPECS_T03.md#p0142-kernel-template-lib) | [txt](prompts/P0142_kernel_template_lib.txt) |
| P0143 | `linker_omega` | Ω-Linker for 1000 Compiled Parts | `cap.t03.linker.linker_omega@1` | pure | 5000 | [spec](docs/PART_SPECS_T03.md#p0143-linker-omega) | [txt](prompts/P0143_linker_omega.txt) |
| P0144 | `incremental_build` | Incremental Compilation & Change Impact | `cap.t03.incremental.incremental_build@1` | pure | 6000 | [spec](docs/PART_SPECS_T03.md#p0144-incremental-build) | [txt](prompts/P0144_incremental_build.txt) |
| P0145 | `crosscompile` | Cross-Compilation & Target Matrix | `cap.t03.crosscompile.crosscompile@1` | pure | 7000 | [spec](docs/PART_SPECS_T03.md#p0145-crosscompile) | [txt](prompts/P0145_crosscompile.txt) |
| P0146 | `numeric_mode_lowering` | Determinism-Mode Lowering | `cap.t03.numeric.numeric_mode_lowering@1` | pure | 8000 | [spec](docs/PART_SPECS_T03.md#p0146-numeric-mode-lowering) | [txt](prompts/P0146_numeric_mode_lowering.txt) |
| P0147 | `op_registry` | Operator Registry & Semantics Database | `cap.t03.op.op_registry@1` | pure | 9000 | [spec](docs/PART_SPECS_T03.md#p0147-op-registry) | [txt](prompts/P0147_op_registry.txt) |
| P0148 | `graph_diff_tool` | Graph Diff & Optimisation Explainer | `cap.t03.graph.graph_diff_tool@1` | pure | 10000 | [spec](docs/PART_SPECS_T03.md#p0148-graph-diff-tool) | [txt](prompts/P0148_graph_diff_tool.txt) |
| P0149 | `compiler_fuzzer` | Compiler Fuzzer & Miscompile Hunter | `cap.t03.compiler.compiler_fuzzer@1` | pure | 11000 | [spec](docs/PART_SPECS_T03.md#p0149-compiler-fuzzer) | [txt](prompts/P0149_compiler_fuzzer.txt) |
| P0150 | `build_provenance` | Build Provenance & Reproducibility Attestation | `cap.t03.build.build_provenance@1` | pure | 12000 | [spec](docs/PART_SPECS_T03.md#p0150-build-provenance) | [txt](prompts/P0150_build_provenance.txt) |

## T04 — Hardware Abstraction & Interconnect

*Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.*

| part | slug | title | capability | det | p99 ns | spec | prompt |
|---|---|---|---|---|---:|---|---|
| P0151 | `device_abstraction` | Device Abstraction Layer | `cap.t04.device.device_abstraction@1` | io | 13000 | [spec](docs/PART_SPECS_T04.md#p0151-device-abstraction) | [txt](prompts/P0151_device_abstraction.txt) |
| P0152 | `topology_discovery` | Interconnect Topology Discovery | `cap.t04.topology.topology_discovery@1` | io | 14000 | [spec](docs/PART_SPECS_T04.md#p0152-topology-discovery) | [txt](prompts/P0152_topology_discovery.txt) |
| P0153 | `collective_global` | Multi-Node Collective Library | `cap.t04.collective.collective_global@1` | io | 15000 | [spec](docs/PART_SPECS_T04.md#p0153-collective-global) | [txt](prompts/P0153_collective_global.txt) |
| P0154 | `rdma_transport` | RDMA & Zero-Copy Network Transport | `cap.t04.rdma.rdma_transport@1` | io | 16000 | [spec](docs/PART_SPECS_T04.md#p0154-rdma-transport) | [txt](prompts/P0154_rdma_transport.txt) |
| P0155 | `tcp_fallback` | Reliable TCP/QUIC Transport Fallback | `cap.t04.tcp.tcp_fallback@1` | io | 17000 | [spec](docs/PART_SPECS_T04.md#p0155-tcp-fallback) | [txt](prompts/P0155_tcp_fallback.txt) |
| P0156 | `comm_scheduler` | Communication Scheduling & Prioritisation | `cap.t04.comm.comm_scheduler@1` | io | 18000 | [spec](docs/PART_SPECS_T04.md#p0156-comm-scheduler) | [txt](prompts/P0156_comm_scheduler.txt) |
| P0157 | `expert_parallel_fabric` | Expert-Parallel Routing Fabric | `cap.t04.expert.expert_parallel_fabric@1` | io | 19000 | [spec](docs/PART_SPECS_T04.md#p0157-expert-parallel-fabric) | [txt](prompts/P0157_expert_parallel_fabric.txt) |
| P0158 | `sequence_parallel_fabric` | Sequence & Context Parallel Fabric | `cap.t04.sequence.sequence_parallel_fabric@1` | io | 20000 | [spec](docs/PART_SPECS_T04.md#p0158-sequence-parallel-fabric) | [txt](prompts/P0158_sequence_parallel_fabric.txt) |
| P0159 | `pipeline_fabric` | Pipeline Stage Transport | `cap.t04.pipeline.pipeline_fabric@1` | io | 21000 | [spec](docs/PART_SPECS_T04.md#p0159-pipeline-fabric) | [txt](prompts/P0159_pipeline_fabric.txt) |
| P0160 | `param_server_shard` | Sharded Parameter Store | `cap.t04.param.param_server_shard@1` | io | 22000 | [spec](docs/PART_SPECS_T04.md#p0160-param-server-shard) | [txt](prompts/P0160_param_server_shard.txt) |
| P0161 | `weight_streaming` | Weight Streaming & Tiering | `cap.t04.weight.weight_streaming@1` | io | 23000 | [spec](docs/PART_SPECS_T04.md#p0161-weight-streaming) | [txt](prompts/P0161_weight_streaming.txt) |
| P0162 | `nvme_offload` | NVMe / Storage Offload Engine | `cap.t04.nvme.nvme_offload@1` | io | 24000 | [spec](docs/PART_SPECS_T04.md#p0162-nvme-offload) | [txt](prompts/P0162_nvme_offload.txt) |
| P0163 | `host_pinned_pool` | Host Pinned Memory Manager | `cap.t04.host.host_pinned_pool@1` | io | 25000 | [spec](docs/PART_SPECS_T04.md#p0163-host-pinned-pool) | [txt](prompts/P0163_host_pinned_pool.txt) |
| P0164 | `device_health` | Device Health Monitoring & Prediction | `cap.t04.device.device_health@1` | io | 26000 | [spec](docs/PART_SPECS_T04.md#p0164-device-health) | [txt](prompts/P0164_device_health.txt) |
| P0165 | `fault_domains` | Fault Domain Modelling & Placement | `cap.t04.fault.fault_domains@1` | io | 27000 | [spec](docs/PART_SPECS_T04.md#p0165-fault-domains) | [txt](prompts/P0165_fault_domains.txt) |
| P0166 | `elastic_scaling` | Elastic Membership & Rescaling | `cap.t04.elastic.elastic_scaling@1` | io | 28000 | [spec](docs/PART_SPECS_T04.md#p0166-elastic-scaling) | [txt](prompts/P0166_elastic_scaling.txt) |
| P0167 | `checkpoint_transport` | Distributed Checkpoint IO | `cap.t04.checkpoint.checkpoint_transport@1` | io | 29000 | [spec](docs/PART_SPECS_T04.md#p0167-checkpoint-transport) | [txt](prompts/P0167_checkpoint_transport.txt) |
| P0168 | `failure_recovery` | Failure Detection & Fast Restart | `cap.t04.failure.failure_recovery@1` | io | 30000 | [spec](docs/PART_SPECS_T04.md#p0168-failure-recovery) | [txt](prompts/P0168_failure_recovery.txt) |
| P0169 | `straggler_mitigation` | Straggler Detection & Mitigation | `cap.t04.straggler.straggler_mitigation@1` | io | 31000 | [spec](docs/PART_SPECS_T04.md#p0169-straggler-mitigation) | [txt](prompts/P0169_straggler_mitigation.txt) |
| P0170 | `power_cluster` | Cluster Power & Energy Governance | `cap.t04.power.power_cluster@1` | io | 32000 | [spec](docs/PART_SPECS_T04.md#p0170-power-cluster) | [txt](prompts/P0170_power_cluster.txt) |
| P0171 | `network_congestion` | Congestion Control & Traffic Engineering | `cap.t04.network.network_congestion@1` | io | 33000 | [spec](docs/PART_SPECS_T04.md#p0171-network-congestion) | [txt](prompts/P0171_network_congestion.txt) |
| P0172 | `multi_tenancy` | Multi-Tenant Isolation & QoS | `cap.t04.multi.multi_tenancy@1` | io | 34000 | [spec](docs/PART_SPECS_T04.md#p0172-multi-tenancy) | [txt](prompts/P0172_multi_tenancy.txt) |
| P0173 | `device_virtualisation` | Device Partitioning & Virtualisation | `cap.t04.device.device_virtualisation@1` | io | 35000 | [spec](docs/PART_SPECS_T04.md#p0173-device-virtualisation) | [txt](prompts/P0173_device_virtualisation.txt) |
| P0174 | `heterogeneous_pool` | Heterogeneous Hardware Pooling | `cap.t04.heterogeneous.heterogeneous_pool@1` | io | 36000 | [spec](docs/PART_SPECS_T04.md#p0174-heterogeneous-pool) | [txt](prompts/P0174_heterogeneous_pool.txt) |
| P0175 | `edge_runtime` | Edge & On-Device Runtime | `cap.t04.edge.edge_runtime@1` | io | 37000 | [spec](docs/PART_SPECS_T04.md#p0175-edge-runtime) | [txt](prompts/P0175_edge_runtime.txt) |
| P0176 | `cloud_provisioner` | Capacity Provisioning & Placement Planner | `cap.t04.cloud.cloud_provisioner@1` | io | 38000 | [spec](docs/PART_SPECS_T04.md#p0176-cloud-provisioner) | [txt](prompts/P0176_cloud_provisioner.txt) |
| P0177 | `scheduler_cluster` | Cluster Job Scheduler Integration | `cap.t04.scheduler.scheduler_cluster@1` | io | 39000 | [spec](docs/PART_SPECS_T04.md#p0177-scheduler-cluster) | [txt](prompts/P0177_scheduler_cluster.txt) |
| P0178 | `service_discovery` | Service Discovery & Membership Registry | `cap.t04.service.service_discovery@1` | io | 40000 | [spec](docs/PART_SPECS_T04.md#p0178-service-discovery) | [txt](prompts/P0178_service_discovery.txt) |
| P0179 | `consensus_core` | Lightweight Consensus & Leader Election | `cap.t04.consensus.consensus_core@1` | io | 41000 | [spec](docs/PART_SPECS_T04.md#p0179-consensus-core) | [txt](prompts/P0179_consensus_core.txt) |
| P0180 | `distributed_lock` | Distributed Locking & Fencing | `cap.t04.distributed.distributed_lock@1` | io | 42000 | [spec](docs/PART_SPECS_T04.md#p0180-distributed-lock) | [txt](prompts/P0180_distributed_lock.txt) |
| P0181 | `clock_sync` | Cluster Clock Synchronisation | `cap.t04.clock.clock_sync@1` | io | 43000 | [spec](docs/PART_SPECS_T04.md#p0181-clock-sync) | [txt](prompts/P0181_clock_sync.txt) |
| P0182 | `data_locality` | Data Locality & Cache Affinity Router | `cap.t04.data.data_locality@1` | io | 44000 | [spec](docs/PART_SPECS_T04.md#p0182-data-locality) | [txt](prompts/P0182_data_locality.txt) |
| P0183 | `bandwidth_accounting` | Bandwidth & Interconnect Accounting | `cap.t04.bandwidth.bandwidth_accounting@1` | io | 45000 | [spec](docs/PART_SPECS_T04.md#p0183-bandwidth-accounting) | [txt](prompts/P0183_bandwidth_accounting.txt) |
| P0184 | `secure_channel` | Encrypted Inter-Node Channels | `cap.t04.secure.secure_channel@1` | io | 46000 | [spec](docs/PART_SPECS_T04.md#p0184-secure-channel) | [txt](prompts/P0184_secure_channel.txt) |
| P0185 | `confidential_compute` | Confidential Computing Integration | `cap.t04.confidential.confidential_compute@1` | io | 47000 | [spec](docs/PART_SPECS_T04.md#p0185-confidential-compute) | [txt](prompts/P0185_confidential_compute.txt) |
| P0186 | `firmware_compat` | Driver & Firmware Compatibility Matrix | `cap.t04.firmware.firmware_compat@1` | io | 48000 | [spec](docs/PART_SPECS_T04.md#p0186-firmware-compat) | [txt](prompts/P0186_firmware_compat.txt) |
| P0187 | `nic_offload` | Network Offload & In-Network Compute | `cap.t04.nic.nic_offload@1` | io | 49000 | [spec](docs/PART_SPECS_T04.md#p0187-nic-offload) | [txt](prompts/P0187_nic_offload.txt) |
| P0188 | `device_reset` | Device Reset & Isolation Recovery | `cap.t04.device.device_reset@1` | io | 3000 | [spec](docs/PART_SPECS_T04.md#p0188-device-reset) | [txt](prompts/P0188_device_reset.txt) |
| P0189 | `numa_topology_cluster` | Host-Level Resource Topology Binding | `cap.t04.numa.numa_topology_cluster@1` | io | 4000 | [spec](docs/PART_SPECS_T04.md#p0189-numa-topology-cluster) | [txt](prompts/P0189_numa_topology_cluster.txt) |
| P0190 | `telemetry_transport` | High-Volume Telemetry Pipeline | `cap.t04.telemetry.telemetry_transport@1` | io | 5000 | [spec](docs/PART_SPECS_T04.md#p0190-telemetry-transport) | [txt](prompts/P0190_telemetry_transport.txt) |
| P0191 | `simulation_cluster` | Cluster Simulator | `cap.t04.simulation.simulation_cluster@1` | io | 6000 | [spec](docs/PART_SPECS_T04.md#p0191-simulation-cluster) | [txt](prompts/P0191_simulation_cluster.txt) |
| P0192 | `capacity_benchmarks` | Distributed Benchmark Suite | `cap.t04.capacity.capacity_benchmarks@1` | io | 7000 | [spec](docs/PART_SPECS_T04.md#p0192-capacity-benchmarks) | [txt](prompts/P0192_capacity_benchmarks.txt) |
| P0193 | `cost_model_cluster` | Total-Cost-of-Serving Model | `cap.t04.cost.cost_model_cluster@1` | io | 8000 | [spec](docs/PART_SPECS_T04.md#p0193-cost-model-cluster) | [txt](prompts/P0193_cost_model_cluster.txt) |
| P0194 | `request_router` | Global Request Router & Load Balancer | `cap.t04.request.request_router@1` | io | 9000 | [spec](docs/PART_SPECS_T04.md#p0194-request-router) | [txt](prompts/P0194_request_router.txt) |
| P0195 | `region_failover` | Multi-Region Replication & Failover | `cap.t04.region.region_failover@1` | io | 10000 | [spec](docs/PART_SPECS_T04.md#p0195-region-failover) | [txt](prompts/P0195_region_failover.txt) |
| P0196 | `hw_sw_codesign` | Hardware/Software Co-Design Specification | `cap.t04.hw.hw_sw_codesign@1` | io | 11000 | [spec](docs/PART_SPECS_T04.md#p0196-hw-sw-codesign) | [txt](prompts/P0196_hw_sw_codesign.txt) |
| P0197 | `green_scheduling` | Carbon-Aware Scheduling | `cap.t04.green.green_scheduling@1` | io | 12000 | [spec](docs/PART_SPECS_T04.md#p0197-green-scheduling) | [txt](prompts/P0197_green_scheduling.txt) |
| P0198 | `device_alloc_fair` | Fair-Share Device Allocation | `cap.t04.device.device_alloc_fair@1` | io | 13000 | [spec](docs/PART_SPECS_T04.md#p0198-device-alloc-fair) | [txt](prompts/P0198_device_alloc_fair.txt) |
| P0199 | `hpc_interop` | HPC & Scientific Stack Interoperability | `cap.t04.hpc.hpc_interop@1` | io | 14000 | [spec](docs/PART_SPECS_T04.md#p0199-hpc-interop) | [txt](prompts/P0199_hpc_interop.txt) |
| P0200 | `provision_verify` | Node Admission & Continuous Verification | `cap.t04.provision.provision_verify@1` | io | 15000 | [spec](docs/PART_SPECS_T04.md#p0200-provision-verify) | [txt](prompts/P0200_provision_verify.txt) |

## T05 — Ω-Core Model Architecture

*The hybrid attention / state-space / retrieval / latent-program backbone that replaces a pure transformer stack.*

| part | slug | title | capability | det | p99 ns | spec | prompt |
|---|---|---|---|---|---:|---|---|
| P0201 | `omega_block` | Ω-Block: The Core Residual Unit | `cap.t05.omega.omega_block@1` | pure | 16000 | [spec](docs/PART_SPECS_T05.md#p0201-omega-block) | [txt](prompts/P0201_omega_block.txt) |
| P0202 | `hybrid_mixer` | Attention/SSM Hybrid Mixing Policy | `cap.t05.hybrid.hybrid_mixer@1` | pure | 17000 | [spec](docs/PART_SPECS_T05.md#p0202-hybrid-mixer) | [txt](prompts/P0202_hybrid_mixer.txt) |
| P0203 | `attention_variants` | Attention Variant Zoo & Selection | `cap.t05.attention.attention_variants@1` | pure | 18000 | [spec](docs/PART_SPECS_T05.md#p0203-attention-variants) | [txt](prompts/P0203_attention_variants.txt) |
| P0204 | `kv_compression_model` | Learned KV Compression | `cap.t05.kv.kv_compression_model@1` | pure | 19000 | [spec](docs/PART_SPECS_T05.md#p0204-kv-compression-model) | [txt](prompts/P0204_kv_compression_model.txt) |
| P0205 | `state_space_layer` | Selective State-Space Layer | `cap.t05.state.state_space_layer@1` | pure | 20000 | [spec](docs/PART_SPECS_T05.md#p0205-state-space-layer) | [txt](prompts/P0205_state_space_layer.txt) |
| P0206 | `recurrent_memory_layer` | Recurrent Compressive Memory Layer | `cap.t05.recurrent.recurrent_memory_layer@1` | pure | 21000 | [spec](docs/PART_SPECS_T05.md#p0206-recurrent-memory-layer) | [txt](prompts/P0206_recurrent_memory_layer.txt) |
| P0207 | `latent_program_slots` | Latent Program Slot Mechanism | `cap.t05.latent.latent_program_slots@1` | pure | 22000 | [spec](docs/PART_SPECS_T05.md#p0207-latent-program-slots) | [txt](prompts/P0207_latent_program_slots.txt) |
| P0208 | `adaptive_depth` | Adaptive Computation Depth | `cap.t05.adaptive.adaptive_depth@1` | pure | 23000 | [spec](docs/PART_SPECS_T05.md#p0208-adaptive-depth) | [txt](prompts/P0208_adaptive_depth.txt) |
| P0209 | `normalisation_design` | Normalisation & Residual Scaling Design | `cap.t05.normalisation.normalisation_design@1` | pure | 24000 | [spec](docs/PART_SPECS_T05.md#p0209-normalisation-design) | [txt](prompts/P0209_normalisation_design.txt) |
| P0210 | `activation_design` | Activation & Gating Function Design | `cap.t05.activation.activation_design@1` | pure | 25000 | [spec](docs/PART_SPECS_T05.md#p0210-activation-design) | [txt](prompts/P0210_activation_design.txt) |
| P0211 | `embedding_design` | Tokenisation-Aware Embedding & Unembedding | `cap.t05.embedding.embedding_design@1` | pure | 26000 | [spec](docs/PART_SPECS_T05.md#p0211-embedding-design) | [txt](prompts/P0211_embedding_design.txt) |
| P0212 | `tokeniser_omega` | Ω-Tokeniser: Byte-Level Adaptive Segmentation | `cap.t05.tokeniser.tokeniser_omega@1` | pure | 27000 | [spec](docs/PART_SPECS_T05.md#p0212-tokeniser-omega) | [txt](prompts/P0212_tokeniser_omega.txt) |
| P0213 | `byte_latent_patching` | Byte-Latent Patch Encoder | `cap.t05.byte.byte_latent_patching@1` | pure | 28000 | [spec](docs/PART_SPECS_T05.md#p0213-byte-latent-patching) | [txt](prompts/P0213_byte_latent_patching.txt) |
| P0214 | `positional_design` | Positional Representation Strategy | `cap.t05.positional.positional_design@1` | pure | 29000 | [spec](docs/PART_SPECS_T05.md#p0214-positional-design) | [txt](prompts/P0214_positional_design.txt) |
| P0215 | `long_context_arch` | Ultra-Long Context Architecture | `cap.t05.long.long_context_arch@1` | pure | 30000 | [spec](docs/PART_SPECS_T05.md#p0215-long-context-arch) | [txt](prompts/P0215_long_context_arch.txt) |
| P0216 | `multi_token_prediction` | Multi-Token Prediction Heads | `cap.t05.multi.multi_token_prediction@1` | pure | 31000 | [spec](docs/PART_SPECS_T05.md#p0216-multi-token-prediction) | [txt](prompts/P0216_multi_token_prediction.txt) |
| P0217 | `draft_model_arch` | Ω-Draft Model Family Architecture | `cap.t05.draft.draft_model_arch@1` | pure | 32000 | [spec](docs/PART_SPECS_T05.md#p0217-draft-model-arch) | [txt](prompts/P0217_draft_model_arch.txt) |
| P0218 | `verifier_head` | Internal Verifier & Confidence Heads | `cap.t05.verifier.verifier_head@1` | pure | 33000 | [spec](docs/PART_SPECS_T05.md#p0218-verifier-head) | [txt](prompts/P0218_verifier_head.txt) |
| P0219 | `uncertainty_calibration` | Uncertainty Representation & Calibration | `cap.t05.uncertainty.uncertainty_calibration@1` | pure | 34000 | [spec](docs/PART_SPECS_T05.md#p0219-uncertainty-calibration) | [txt](prompts/P0219_uncertainty_calibration.txt) |
| P0220 | `world_model_core` | Internal World Model & State Tracking | `cap.t05.world.world_model_core@1` | pure | 35000 | [spec](docs/PART_SPECS_T05.md#p0220-world-model-core) | [txt](prompts/P0220_world_model_core.txt) |
| P0221 | `causal_model` | Causal Representation & Intervention Reasoning | `cap.t05.causal.causal_model@1` | pure | 36000 | [spec](docs/PART_SPECS_T05.md#p0221-causal-model) | [txt](prompts/P0221_causal_model.txt) |
| P0222 | `symbolic_bridge` | Neural/Symbolic Interface Layer | `cap.t05.symbolic.symbolic_bridge@1` | pure | 37000 | [spec](docs/PART_SPECS_T05.md#p0222-symbolic-bridge) | [txt](prompts/P0222_symbolic_bridge.txt) |
| P0223 | `program_induction_arch` | Program Induction & Abstraction Learning | `cap.t05.program.program_induction_arch@1` | pure | 38000 | [spec](docs/PART_SPECS_T05.md#p0223-program-induction-arch) | [txt](prompts/P0223_program_induction_arch.txt) |
| P0224 | `meta_learning_arch` | In-Context Meta-Learning Architecture | `cap.t05.meta.meta_learning_arch@1` | pure | 39000 | [spec](docs/PART_SPECS_T05.md#p0224-meta-learning-arch) | [txt](prompts/P0224_meta_learning_arch.txt) |
| P0225 | `continual_learning` | Continual Learning Without Forgetting | `cap.t05.continual.continual_learning@1` | pure | 40000 | [spec](docs/PART_SPECS_T05.md#p0225-continual-learning) | [txt](prompts/P0225_continual_learning.txt) |
| P0226 | `knowledge_editing` | Targeted Knowledge Editing | `cap.t05.knowledge.knowledge_editing@1` | pure | 41000 | [spec](docs/PART_SPECS_T05.md#p0226-knowledge-editing) | [txt](prompts/P0226_knowledge_editing.txt) |
| P0227 | `model_merging` | Model Merging & Capability Composition | `cap.t05.model.model_merging@1` | pure | 42000 | [spec](docs/PART_SPECS_T05.md#p0227-model-merging) | [txt](prompts/P0227_model_merging.txt) |
| P0228 | `distillation_arch` | Distillation Architecture & Objectives | `cap.t05.distillation.distillation_arch@1` | pure | 43000 | [spec](docs/PART_SPECS_T05.md#p0228-distillation-arch) | [txt](prompts/P0228_distillation_arch.txt) |
| P0229 | `weight_sharing` | Weight Sharing & Parameter Efficiency | `cap.t05.weight.weight_sharing@1` | pure | 44000 | [spec](docs/PART_SPECS_T05.md#p0229-weight-sharing) | [txt](prompts/P0229_weight_sharing.txt) |
| P0230 | `init_scaling_laws` | Initialisation & Scaling Law Framework | `cap.t05.init.init_scaling_laws@1` | pure | 45000 | [spec](docs/PART_SPECS_T05.md#p0230-init-scaling-laws) | [txt](prompts/P0230_init_scaling_laws.txt) |
| P0231 | `architecture_search` | Architecture Search & Ablation Engine | `cap.t05.architecture.architecture_search@1` | pure | 46000 | [spec](docs/PART_SPECS_T05.md#p0231-architecture-search) | [txt](prompts/P0231_architecture_search.txt) |
| P0232 | `depth_width_tradeoff` | Depth/Width/Sparsity Allocation | `cap.t05.depth.depth_width_tradeoff@1` | pure | 47000 | [spec](docs/PART_SPECS_T05.md#p0232-depth-width-tradeoff) | [txt](prompts/P0232_depth_width_tradeoff.txt) |
| P0233 | `residual_stream_design` | Residual Stream Capacity & Interference | `cap.t05.residual.residual_stream_design@1` | pure | 48000 | [spec](docs/PART_SPECS_T05.md#p0233-residual-stream-design) | [txt](prompts/P0233_residual_stream_design.txt) |
| P0234 | `logit_head_design` | Output Head, Logit Shaping & Constraints | `cap.t05.logit.logit_head_design@1` | pure | 49000 | [spec](docs/PART_SPECS_T05.md#p0234-logit-head-design) | [txt](prompts/P0234_logit_head_design.txt) |
| P0235 | `multimodal_fusion_arch` | Multimodal Fusion Architecture | `cap.t05.multimodal.multimodal_fusion_arch@1` | pure | 3000 | [spec](docs/PART_SPECS_T05.md#p0235-multimodal-fusion-arch) | [txt](prompts/P0235_multimodal_fusion_arch.txt) |
| P0236 | `action_head` | Action & Tool-Call Head | `cap.t05.action.action_head@1` | pure | 4000 | [spec](docs/PART_SPECS_T05.md#p0236-action-head) | [txt](prompts/P0236_action_head.txt) |
| P0237 | `memory_attention_bridge` | Memory Retrieval Attention Bridge | `cap.t05.memory.memory_attention_bridge@1` | pure | 5000 | [spec](docs/PART_SPECS_T05.md#p0237-memory-attention-bridge) | [txt](prompts/P0237_memory_attention_bridge.txt) |
| P0238 | `speculative_arch_hooks` | Architecture Hooks for Speculative Decoding | `cap.t05.speculative.speculative_arch_hooks@1` | pure | 6000 | [spec](docs/PART_SPECS_T05.md#p0238-speculative-arch-hooks) | [txt](prompts/P0238_speculative_arch_hooks.txt) |
| P0239 | `sparse_upcycling` | Sparse Upcycling & Expert Initialisation | `cap.t05.sparse.sparse_upcycling@1` | pure | 7000 | [spec](docs/PART_SPECS_T05.md#p0239-sparse-upcycling) | [txt](prompts/P0239_sparse_upcycling.txt) |
| P0240 | `model_surgery` | Model Surgery: Pruning, Grafting, Extension | `cap.t05.model.model_surgery@1` | pure | 8000 | [spec](docs/PART_SPECS_T05.md#p0240-model-surgery) | [txt](prompts/P0240_model_surgery.txt) |
| P0241 | `numerical_arch_stability` | Architectural Numerical Stability | `cap.t05.numerical.numerical_arch_stability@1` | pure | 9000 | [spec](docs/PART_SPECS_T05.md#p0241-numerical-arch-stability) | [txt](prompts/P0241_numerical_arch_stability.txt) |
| P0242 | `context_packing` | Context Composition & Packing Strategy | `cap.t05.context.context_packing@1` | pure | 10000 | [spec](docs/PART_SPECS_T05.md#p0242-context-packing) | [txt](prompts/P0242_context_packing.txt) |
| P0243 | `prompt_representation` | Internal Prompt & Role Representation | `cap.t05.prompt.prompt_representation@1` | pure | 11000 | [spec](docs/PART_SPECS_T05.md#p0243-prompt-representation) | [txt](prompts/P0243_prompt_representation.txt) |
| P0244 | `thought_representation` | Latent Thought Channel | `cap.t05.thought.thought_representation@1` | pure | 12000 | [spec](docs/PART_SPECS_T05.md#p0244-thought-representation) | [txt](prompts/P0244_thought_representation.txt) |
| P0245 | `expert_specialisation` | Expert Specialisation Analysis & Design | `cap.t05.expert.expert_specialisation@1` | pure | 13000 | [spec](docs/PART_SPECS_T05.md#p0245-expert-specialisation) | [txt](prompts/P0245_expert_specialisation.txt) |
| P0246 | `model_config_schema` | Model Configuration Schema & Validation | `cap.t05.model.model_config_schema@1` | pure | 14000 | [spec](docs/PART_SPECS_T05.md#p0246-model-config-schema) | [txt](prompts/P0246_model_config_schema.txt) |
| P0247 | `reference_forward` | Reference Forward Pass Implementation | `cap.t05.reference.reference_forward@1` | pure | 15000 | [spec](docs/PART_SPECS_T05.md#p0247-reference-forward) | [txt](prompts/P0247_reference_forward.txt) |
| P0248 | `arch_ablation_suite` | Architecture Ablation & Evidence Suite | `cap.t05.arch.arch_ablation_suite@1` | pure | 16000 | [spec](docs/PART_SPECS_T05.md#p0248-arch-ablation-suite) | [txt](prompts/P0248_arch_ablation_suite.txt) |
| P0249 | `capacity_probes` | Capability Probes & Representation Diagnostics | `cap.t05.capacity.capacity_probes@1` | pure | 17000 | [spec](docs/PART_SPECS_T05.md#p0249-capacity-probes) | [txt](prompts/P0249_capacity_probes.txt) |
| P0250 | `arch_spec_doc` | Architecture Specification Document Generator | `cap.t05.arch.arch_spec_doc@1` | pure | 18000 | [spec](docs/PART_SPECS_T05.md#p0250-arch-spec-doc) | [txt](prompts/P0250_arch_spec_doc.txt) |

## T06 — Sparse Routing & Mixture-of-Ω-Experts

*512-expert conditional compute: routing, balancing, expert lifecycle, capacity control. Source of speedup S2.*

| part | slug | title | capability | det | p99 ns | spec | prompt |
|---|---|---|---|---|---:|---|---|
| P0251 | `router_core` | Top-K Router Core | `cap.t06.router.router_core@1` | seeded | 19000 | [spec](docs/PART_SPECS_T06.md#p0251-router-core) | [txt](prompts/P0251_router_core.txt) |
| P0252 | `router_balance` | Load Balancing Losses & Constraints | `cap.t06.router.router_balance@1` | seeded | 20000 | [spec](docs/PART_SPECS_T06.md#p0252-router-balance) | [txt](prompts/P0252_router_balance.txt) |
| P0253 | `router_capacity` | Capacity Factor & Overflow Policy | `cap.t06.router.router_capacity@1` | seeded | 21000 | [spec](docs/PART_SPECS_T06.md#p0253-router-capacity) | [txt](prompts/P0253_router_capacity.txt) |
| P0254 | `router_hash_hybrid` | Hybrid Learned/Deterministic Routing | `cap.t06.router.router_hash_hybrid@1` | seeded | 22000 | [spec](docs/PART_SPECS_T06.md#p0254-router-hash-hybrid) | [txt](prompts/P0254_router_hash_hybrid.txt) |
| P0255 | `expert_ffn` | Expert Feed-Forward Implementation | `cap.t06.expert.expert_ffn@1` | seeded | 23000 | [spec](docs/PART_SPECS_T06.md#p0255-expert-ffn) | [txt](prompts/P0255_expert_ffn.txt) |
| P0256 | `expert_attention` | Mixture-of-Attention-Heads Routing | `cap.t06.expert.expert_attention@1` | seeded | 24000 | [spec](docs/PART_SPECS_T06.md#p0256-expert-attention) | [txt](prompts/P0256_expert_attention.txt) |
| P0257 | `shared_expert` | Shared & Residual Expert Design | `cap.t06.shared.shared_expert@1` | seeded | 25000 | [spec](docs/PART_SPECS_T06.md#p0257-shared-expert) | [txt](prompts/P0257_shared_expert.txt) |
| P0258 | `fine_grained_experts` | Fine-Grained Expert Segmentation | `cap.t06.fine.fine_grained_experts@1` | seeded | 26000 | [spec](docs/PART_SPECS_T06.md#p0258-fine-grained-experts) | [txt](prompts/P0258_fine_grained_experts.txt) |
| P0259 | `expert_placement` | Expert Placement & Replication Policy | `cap.t06.expert.expert_placement@1` | seeded | 27000 | [spec](docs/PART_SPECS_T06.md#p0259-expert-placement) | [txt](prompts/P0259_expert_placement.txt) |
| P0260 | `expert_prefetch` | Expert Weight Prefetching & Caching | `cap.t06.expert.expert_prefetch@1` | seeded | 28000 | [spec](docs/PART_SPECS_T06.md#p0260-expert-prefetch) | [txt](prompts/P0260_expert_prefetch.txt) |
| P0261 | `router_lookahead` | Router Prediction & Speculative Routing | `cap.t06.router.router_lookahead@1` | seeded | 29000 | [spec](docs/PART_SPECS_T06.md#p0261-router-lookahead) | [txt](prompts/P0261_router_lookahead.txt) |
| P0262 | `moe_determinism` | Deterministic MoE Execution | `cap.t06.moe.moe_determinism@1` | seeded | 30000 | [spec](docs/PART_SPECS_T06.md#p0262-moe-determinism) | [txt](prompts/P0262_moe_determinism.txt) |
| P0263 | `expert_lifecycle` | Expert Birth, Death & Reincarnation | `cap.t06.expert.expert_lifecycle@1` | seeded | 31000 | [spec](docs/PART_SPECS_T06.md#p0263-expert-lifecycle) | [txt](prompts/P0263_expert_lifecycle.txt) |
| P0264 | `expert_diversity` | Expert Diversity Objectives | `cap.t06.expert.expert_diversity@1` | seeded | 32000 | [spec](docs/PART_SPECS_T06.md#p0264-expert-diversity) | [txt](prompts/P0264_expert_diversity.txt) |
| P0265 | `router_temperature` | Router Sharpness & Exploration Schedule | `cap.t06.router.router_temperature@1` | seeded | 33000 | [spec](docs/PART_SPECS_T06.md#p0265-router-temperature) | [txt](prompts/P0265_router_temperature.txt) |
| P0266 | `sparse_activation_stats` | Sparse Activation Statistics & Diagnostics | `cap.t06.sparse.sparse_activation_stats@1` | seeded | 34000 | [spec](docs/PART_SPECS_T06.md#p0266-sparse-activation-stats) | [txt](prompts/P0266_sparse_activation_stats.txt) |
| P0267 | `moe_quantisation` | Per-Expert Quantisation Strategy | `cap.t06.moe.moe_quantisation@1` | seeded | 35000 | [spec](docs/PART_SPECS_T06.md#p0267-moe-quantisation) | [txt](prompts/P0267_moe_quantisation.txt) |
| P0268 | `expert_offload` | Expert Offloading to Host/Storage | `cap.t06.expert.expert_offload@1` | seeded | 36000 | [spec](docs/PART_SPECS_T06.md#p0268-expert-offload) | [txt](prompts/P0268_expert_offload.txt) |
| P0269 | `moe_batching` | MoE-Aware Request Batching | `cap.t06.moe.moe_batching@1` | seeded | 37000 | [spec](docs/PART_SPECS_T06.md#p0269-moe-batching) | [txt](prompts/P0269_moe_batching.txt) |
| P0270 | `token_dropping` | Token Dropping & Early Exit Policy | `cap.t06.token.token_dropping@1` | seeded | 38000 | [spec](docs/PART_SPECS_T06.md#p0270-token-dropping) | [txt](prompts/P0270_token_dropping.txt) |
| P0271 | `conditional_layers` | Layer Skipping & Conditional Depth Routing | `cap.t06.conditional.conditional_layers@1` | seeded | 39000 | [spec](docs/PART_SPECS_T06.md#p0271-conditional-layers) | [txt](prompts/P0271_conditional_layers.txt) |
| P0272 | `mod_routing` | Mixture-of-Depths Routing | `cap.t06.mod.mod_routing@1` | seeded | 40000 | [spec](docs/PART_SPECS_T06.md#p0272-mod-routing) | [txt](prompts/P0272_mod_routing.txt) |
| P0273 | `router_robustness` | Router Adversarial Robustness | `cap.t06.router.router_robustness@1` | seeded | 41000 | [spec](docs/PART_SPECS_T06.md#p0273-router-robustness) | [txt](prompts/P0273_router_robustness.txt) |
| P0274 | `gating_alternatives` | Alternative Gating Mechanisms | `cap.t06.gating.gating_alternatives@1` | seeded | 42000 | [spec](docs/PART_SPECS_T06.md#p0274-gating-alternatives) | [txt](prompts/P0274_gating_alternatives.txt) |
| P0275 | `expert_choice_routing` | Expert-Choice Routing | `cap.t06.expert.expert_choice_routing@1` | seeded | 43000 | [spec](docs/PART_SPECS_T06.md#p0275-expert-choice-routing) | [txt](prompts/P0275_expert_choice_routing.txt) |
| P0276 | `moe_scaling_laws` | MoE Scaling Laws & Budget Allocation | `cap.t06.moe.moe_scaling_laws@1` | seeded | 44000 | [spec](docs/PART_SPECS_T06.md#p0276-moe-scaling-laws) | [txt](prompts/P0276_moe_scaling_laws.txt) |
| P0277 | `router_interpretability` | Router Interpretability & Expert Naming | `cap.t06.router.router_interpretability@1` | seeded | 45000 | [spec](docs/PART_SPECS_T06.md#p0277-router-interpretability) | [txt](prompts/P0277_router_interpretability.txt) |
| P0278 | `moe_training_stability` | MoE Training Stability Engineering | `cap.t06.moe.moe_training_stability@1` | seeded | 46000 | [spec](docs/PART_SPECS_T06.md#p0278-moe-training-stability) | [txt](prompts/P0278_moe_training_stability.txt) |
| P0279 | `expert_dropout` | Expert Dropout & Robustness to Missing Experts | `cap.t06.expert.expert_dropout@1` | seeded | 47000 | [spec](docs/PART_SPECS_T06.md#p0279-expert-dropout) | [txt](prompts/P0279_expert_dropout.txt) |
| P0280 | `sparse_kernels_bridge` | Routing-to-Kernel Bridge | `cap.t06.sparse.sparse_kernels_bridge@1` | seeded | 48000 | [spec](docs/PART_SPECS_T06.md#p0280-sparse-kernels-bridge) | [txt](prompts/P0280_sparse_kernels_bridge.txt) |
| P0281 | `modality_routing` | Modality- & Language-Aware Routing | `cap.t06.modality.modality_routing@1` | seeded | 49000 | [spec](docs/PART_SPECS_T06.md#p0281-modality-routing) | [txt](prompts/P0281_modality_routing.txt) |
| P0282 | `difficulty_routing` | Difficulty-Aware Compute Routing | `cap.t06.difficulty.difficulty_routing@1` | seeded | 3000 | [spec](docs/PART_SPECS_T06.md#p0282-difficulty-routing) | [txt](prompts/P0282_difficulty_routing.txt) |
| P0283 | `cost_aware_routing` | Cost- & SLO-Aware Routing Policy | `cap.t06.cost.cost_aware_routing@1` | seeded | 4000 | [spec](docs/PART_SPECS_T06.md#p0283-cost-aware-routing) | [txt](prompts/P0283_cost_aware_routing.txt) |
| P0284 | `model_cascade_routing` | Model Cascade & Escalation Router | `cap.t06.model.model_cascade_routing@1` | seeded | 5000 | [spec](docs/PART_SPECS_T06.md#p0284-model-cascade-routing) | [txt](prompts/P0284_model_cascade_routing.txt) |
| P0285 | `ensemble_combiner` | Ensemble & Multi-Sample Combination | `cap.t06.ensemble.ensemble_combiner@1` | seeded | 6000 | [spec](docs/PART_SPECS_T06.md#p0285-ensemble-combiner) | [txt](prompts/P0285_ensemble_combiner.txt) |
| P0286 | `router_cache` | Routing Decision Cache | `cap.t06.router.router_cache@1` | seeded | 7000 | [spec](docs/PART_SPECS_T06.md#p0286-router-cache) | [txt](prompts/P0286_router_cache.txt) |
| P0287 | `expert_warmup` | Expert Warmup & Cold-Start Handling | `cap.t06.expert.expert_warmup@1` | seeded | 8000 | [spec](docs/PART_SPECS_T06.md#p0287-expert-warmup) | [txt](prompts/P0287_expert_warmup.txt) |
| P0288 | `routing_fairness` | Cross-User Routing Fairness & Isolation | `cap.t06.routing.routing_fairness@1` | seeded | 9000 | [spec](docs/PART_SPECS_T06.md#p0288-routing-fairness) | [txt](prompts/P0288_routing_fairness.txt) |
| P0289 | `moe_memory_budget` | MoE Memory Budget Planner | `cap.t06.moe.moe_memory_budget@1` | seeded | 10000 | [spec](docs/PART_SPECS_T06.md#p0289-moe-memory-budget) | [txt](prompts/P0289_moe_memory_budget.txt) |
| P0290 | `router_online_learning` | Online Router Adaptation | `cap.t06.router.router_online_learning@1` | seeded | 11000 | [spec](docs/PART_SPECS_T06.md#p0290-router-online-learning) | [txt](prompts/P0290_router_online_learning.txt) |
| P0291 | `sparse_gradient` | Sparse Gradient Handling & Accumulation | `cap.t06.sparse.sparse_gradient@1` | seeded | 12000 | [spec](docs/PART_SPECS_T06.md#p0291-sparse-gradient) | [txt](prompts/P0291_sparse_gradient.txt) |
| P0292 | `expert_alignment` | Per-Expert Safety & Alignment Auditing | `cap.t06.expert.expert_alignment@1` | seeded | 13000 | [spec](docs/PART_SPECS_T06.md#p0292-expert-alignment) | [txt](prompts/P0292_expert_alignment.txt) |
| P0293 | `routing_privacy` | Routing Privacy & Side-Channel Defence | `cap.t06.routing.routing_privacy@1` | seeded | 14000 | [spec](docs/PART_SPECS_T06.md#p0293-routing-privacy) | [txt](prompts/P0293_routing_privacy.txt) |
| P0294 | `hierarchical_routing` | Hierarchical Two-Level Routing | `cap.t06.hierarchical.hierarchical_routing@1` | seeded | 15000 | [spec](docs/PART_SPECS_T06.md#p0294-hierarchical-routing) | [txt](prompts/P0294_hierarchical_routing.txt) |
| P0295 | `router_bench` | Routing Benchmark & Regression Suite | `cap.t06.router.router_bench@1` | seeded | 16000 | [spec](docs/PART_SPECS_T06.md#p0295-router-bench) | [txt](prompts/P0295_router_bench.txt) |
| P0296 | `moe_visualisation` | Sparse Compute Visualisation & Explainer | `cap.t06.moe.moe_visualisation@1` | seeded | 17000 | [spec](docs/PART_SPECS_T06.md#p0296-moe-visualisation) | [txt](prompts/P0296_moe_visualisation.txt) |
| P0297 | `adaptive_sparsity` | Runtime-Adaptive Sparsity Control | `cap.t06.adaptive.adaptive_sparsity@1` | seeded | 18000 | [spec](docs/PART_SPECS_T06.md#p0297-adaptive-sparsity) | [txt](prompts/P0297_adaptive_sparsity.txt) |
| P0298 | `sparsity_verification` | Conditional-Compute Correctness Verification | `cap.t06.sparsity.sparsity_verification@1` | seeded | 19000 | [spec](docs/PART_SPECS_T06.md#p0298-sparsity-verification) | [txt](prompts/P0298_sparsity_verification.txt) |
| P0299 | `moe_speed_accounting` | S2 Speedup Accounting & Attribution | `cap.t06.moe.moe_speed_accounting@1` | seeded | 20000 | [spec](docs/PART_SPECS_T06.md#p0299-moe-speed-accounting) | [txt](prompts/P0299_moe_speed_accounting.txt) |
| P0300 | `moe_spec_doc` | Sparse Architecture Specification & Docs | `cap.t06.moe.moe_spec_doc@1` | seeded | 21000 | [spec](docs/PART_SPECS_T06.md#p0300-moe-spec-doc) | [txt](prompts/P0300_moe_spec_doc.txt) |

## T07 — Memory, Retrieval & World Model

*Hierarchical KV, episodic/semantic/procedural memory, 1G-token effective context, and a persistent updatable world model.*

| part | slug | title | capability | det | p99 ns | spec | prompt |
|---|---|---|---|---|---:|---|---|
| P0301 | `kv_hierarchy` | Hierarchical KV Cache Manager | `cap.t07.kv.kv_hierarchy@1` | pure | 22000 | [spec](docs/PART_SPECS_T07.md#p0301-kv-hierarchy) | [txt](prompts/P0301_kv_hierarchy.txt) |
| P0302 | `kv_paging` | Paged KV Allocation & Block Tables | `cap.t07.kv.kv_paging@1` | pure | 23000 | [spec](docs/PART_SPECS_T07.md#p0302-kv-paging) | [txt](prompts/P0302_kv_paging.txt) |
| P0303 | `kv_eviction` | KV Eviction & Importance Scoring | `cap.t07.kv.kv_eviction@1` | pure | 24000 | [spec](docs/PART_SPECS_T07.md#p0303-kv-eviction) | [txt](prompts/P0303_kv_eviction.txt) |
| P0304 | `kv_dedup` | KV Prefix Deduplication & Sharing | `cap.t07.kv.kv_dedup@1` | pure | 25000 | [spec](docs/PART_SPECS_T07.md#p0304-kv-dedup) | [txt](prompts/P0304_kv_dedup.txt) |
| P0305 | `kv_compression_runtime` | Runtime KV Compression Pipeline | `cap.t07.kv.kv_compression_runtime@1` | pure | 26000 | [spec](docs/PART_SPECS_T07.md#p0305-kv-compression-runtime) | [txt](prompts/P0305_kv_compression_runtime.txt) |
| P0306 | `context_window_manager` | Effective Context Window Orchestrator | `cap.t07.context.context_window_manager@1` | pure | 27000 | [spec](docs/PART_SPECS_T07.md#p0306-context-window-manager) | [txt](prompts/P0306_context_window_manager.txt) |
| P0307 | `summarisation_memory` | Recursive Summarisation & Compaction | `cap.t07.summarisation.summarisation_memory@1` | pure | 28000 | [spec](docs/PART_SPECS_T07.md#p0307-summarisation-memory) | [txt](prompts/P0307_summarisation_memory.txt) |
| P0308 | `episodic_memory` | Episodic Memory Store | `cap.t07.episodic.episodic_memory@1` | pure | 29000 | [spec](docs/PART_SPECS_T07.md#p0308-episodic-memory) | [txt](prompts/P0308_episodic_memory.txt) |
| P0309 | `semantic_memory` | Semantic Memory & Knowledge Graph | `cap.t07.semantic.semantic_memory@1` | pure | 30000 | [spec](docs/PART_SPECS_T07.md#p0309-semantic-memory) | [txt](prompts/P0309_semantic_memory.txt) |
| P0310 | `procedural_memory` | Procedural Memory & Skill Library | `cap.t07.procedural.procedural_memory@1` | pure | 31000 | [spec](docs/PART_SPECS_T07.md#p0310-procedural-memory) | [txt](prompts/P0310_procedural_memory.txt) |
| P0311 | `memory_consolidation` | Sleep-Cycle Memory Consolidation | `cap.t07.memory.memory_consolidation@1` | pure | 32000 | [spec](docs/PART_SPECS_T07.md#p0311-memory-consolidation) | [txt](prompts/P0311_memory_consolidation.txt) |
| P0312 | `forgetting_policy` | Principled Forgetting & Retention Policy | `cap.t07.forgetting.forgetting_policy@1` | pure | 33000 | [spec](docs/PART_SPECS_T07.md#p0312-forgetting-policy) | [txt](prompts/P0312_forgetting_policy.txt) |
| P0313 | `vector_index` | Vector Index & ANN Search Engine | `cap.t07.vector.vector_index@1` | pure | 34000 | [spec](docs/PART_SPECS_T07.md#p0313-vector-index) | [txt](prompts/P0313_vector_index.txt) |
| P0314 | `sparse_retrieval` | Lexical & Sparse Retrieval Engine | `cap.t07.sparse.sparse_retrieval@1` | pure | 35000 | [spec](docs/PART_SPECS_T07.md#p0314-sparse-retrieval) | [txt](prompts/P0314_sparse_retrieval.txt) |
| P0315 | `hybrid_retrieval` | Hybrid Retrieval Fusion & Reranking | `cap.t07.hybrid.hybrid_retrieval@1` | pure | 36000 | [spec](docs/PART_SPECS_T07.md#p0315-hybrid-retrieval) | [txt](prompts/P0315_hybrid_retrieval.txt) |
| P0316 | `query_reformulation` | Query Understanding & Reformulation | `cap.t07.query.query_reformulation@1` | pure | 37000 | [spec](docs/PART_SPECS_T07.md#p0316-query-reformulation) | [txt](prompts/P0316_query_reformulation.txt) |
| P0317 | `chunking_strategy` | Document Chunking & Structural Indexing | `cap.t07.chunking.chunking_strategy@1` | pure | 38000 | [spec](docs/PART_SPECS_T07.md#p0317-chunking-strategy) | [txt](prompts/P0317_chunking_strategy.txt) |
| P0318 | `embedding_model` | Ω-Embedding Model & Training | `cap.t07.embedding.embedding_model@1` | pure | 39000 | [spec](docs/PART_SPECS_T07.md#p0318-embedding-model) | [txt](prompts/P0318_embedding_model.txt) |
| P0319 | `reranker_model` | Cross-Encoder Reranker | `cap.t07.reranker.reranker_model@1` | pure | 40000 | [spec](docs/PART_SPECS_T07.md#p0319-reranker-model) | [txt](prompts/P0319_reranker_model.txt) |
| P0320 | `citation_grounding` | Evidence Attribution & Citation Engine | `cap.t07.citation.citation_grounding@1` | pure | 41000 | [spec](docs/PART_SPECS_T07.md#p0320-citation-grounding) | [txt](prompts/P0320_citation_grounding.txt) |
| P0321 | `freshness_manager` | Knowledge Freshness & Staleness Control | `cap.t07.freshness.freshness_manager@1` | pure | 42000 | [spec](docs/PART_SPECS_T07.md#p0321-freshness-manager) | [txt](prompts/P0321_freshness_manager.txt) |
| P0322 | `conflict_resolution` | Source Conflict Resolution | `cap.t07.conflict.conflict_resolution@1` | pure | 43000 | [spec](docs/PART_SPECS_T07.md#p0322-conflict-resolution) | [txt](prompts/P0322_conflict_resolution.txt) |
| P0323 | `memory_privacy` | Memory Privacy, Scoping & Tenancy | `cap.t07.memory.memory_privacy@1` | pure | 44000 | [spec](docs/PART_SPECS_T07.md#p0323-memory-privacy) | [txt](prompts/P0323_memory_privacy.txt) |
| P0324 | `memory_encryption` | Memory-at-Rest Encryption & Key Scoping | `cap.t07.memory.memory_encryption@1` | pure | 45000 | [spec](docs/PART_SPECS_T07.md#p0324-memory-encryption) | [txt](prompts/P0324_memory_encryption.txt) |
| P0325 | `world_state_store` | Live World State Store | `cap.t07.world.world_state_store@1` | pure | 46000 | [spec](docs/PART_SPECS_T07.md#p0325-world-state-store) | [txt](prompts/P0325_world_state_store.txt) |
| P0326 | `belief_revision` | Belief Revision & Truth Maintenance | `cap.t07.belief.belief_revision@1` | pure | 47000 | [spec](docs/PART_SPECS_T07.md#p0326-belief-revision) | [txt](prompts/P0326_belief_revision.txt) |
| P0327 | `memory_compression_learned` | Learned Memory Compression | `cap.t07.memory.memory_compression_learned@1` | pure | 48000 | [spec](docs/PART_SPECS_T07.md#p0327-memory-compression-learned) | [txt](prompts/P0327_memory_compression_learned.txt) |
| P0328 | `attention_sink` | Attention Sinks & Streaming Stability | `cap.t07.attention.attention_sink@1` | pure | 49000 | [spec](docs/PART_SPECS_T07.md#p0328-attention-sink) | [txt](prompts/P0328_attention_sink.txt) |
| P0329 | `cache_warm_predict` | Predictive Cache Warming | `cap.t07.cache.cache_warm_predict@1` | pure | 3000 | [spec](docs/PART_SPECS_T07.md#p0329-cache-warm-predict) | [txt](prompts/P0329_cache_warm_predict.txt) |
| P0330 | `semantic_cache` | Semantic Response Cache | `cap.t07.semantic.semantic_cache@1` | pure | 4000 | [spec](docs/PART_SPECS_T07.md#p0330-semantic-cache) | [txt](prompts/P0330_semantic_cache.txt) |
| P0331 | `tool_result_cache` | Tool Result & Computation Cache | `cap.t07.tool.tool_result_cache@1` | pure | 5000 | [spec](docs/PART_SPECS_T07.md#p0331-tool-result-cache) | [txt](prompts/P0331_tool_result_cache.txt) |
| P0332 | `subgraph_memoize` | Reasoning Subgraph Memoisation | `cap.t07.subgraph.subgraph_memoize@1` | pure | 6000 | [spec](docs/PART_SPECS_T07.md#p0332-subgraph-memoize) | [txt](prompts/P0332_subgraph_memoize.txt) |
| P0333 | `retrieval_cache` | Retrieval Result Cache & Index Warmth | `cap.t07.retrieval.retrieval_cache@1` | pure | 7000 | [spec](docs/PART_SPECS_T07.md#p0333-retrieval-cache) | [txt](prompts/P0333_retrieval_cache.txt) |
| P0334 | `memory_gc` | Memory Garbage Collection & Compaction | `cap.t07.memory.memory_gc@1` | pure | 8000 | [spec](docs/PART_SPECS_T07.md#p0334-memory-gc) | [txt](prompts/P0334_memory_gc.txt) |
| P0335 | `persistence_layer` | Durable Memory Persistence & Recovery | `cap.t07.persistence.persistence_layer@1` | pure | 9000 | [spec](docs/PART_SPECS_T07.md#p0335-persistence-layer) | [txt](prompts/P0335_persistence_layer.txt) |
| P0336 | `memory_replication` | Memory Replication & Consistency Model | `cap.t07.memory.memory_replication@1` | pure | 10000 | [spec](docs/PART_SPECS_T07.md#p0336-memory-replication) | [txt](prompts/P0336_memory_replication.txt) |
| P0337 | `graph_memory_queries` | Graph Query Engine over Memory | `cap.t07.graph.graph_memory_queries@1` | pure | 11000 | [spec](docs/PART_SPECS_T07.md#p0337-graph-memory-queries) | [txt](prompts/P0337_graph_memory_queries.txt) |
| P0338 | `temporal_memory` | Temporal Reasoning over Memory | `cap.t07.temporal.temporal_memory@1` | pure | 12000 | [spec](docs/PART_SPECS_T07.md#p0338-temporal-memory) | [txt](prompts/P0338_temporal_memory.txt) |
| P0339 | `multimodal_memory` | Multimodal Memory Store | `cap.t07.multimodal.multimodal_memory@1` | pure | 13000 | [spec](docs/PART_SPECS_T07.md#p0339-multimodal-memory) | [txt](prompts/P0339_multimodal_memory.txt) |
| P0340 | `user_model` | Personalisation & User Model | `cap.t07.user.user_model@1` | pure | 14000 | [spec](docs/PART_SPECS_T07.md#p0340-user-model) | [txt](prompts/P0340_user_model.txt) |
| P0341 | `memory_audit` | Memory Audit Trail & Explainability | `cap.t07.memory.memory_audit@1` | pure | 15000 | [spec](docs/PART_SPECS_T07.md#p0341-memory-audit) | [txt](prompts/P0341_memory_audit.txt) |
| P0342 | `index_build_pipeline` | Corpus Ingestion & Index Build Pipeline | `cap.t07.index.index_build_pipeline@1` | pure | 16000 | [spec](docs/PART_SPECS_T07.md#p0342-index-build-pipeline) | [txt](prompts/P0342_index_build_pipeline.txt) |
| P0343 | `dedup_engine` | Near-Duplicate Detection & Deduplication | `cap.t07.dedup.dedup_engine@1` | pure | 17000 | [spec](docs/PART_SPECS_T07.md#p0343-dedup-engine) | [txt](prompts/P0343_dedup_engine.txt) |
| P0344 | `provenance_tracking` | End-to-End Provenance Tracking | `cap.t07.provenance.provenance_tracking@1` | pure | 18000 | [spec](docs/PART_SPECS_T07.md#p0344-provenance-tracking) | [txt](prompts/P0344_provenance_tracking.txt) |
| P0345 | `memory_bench` | Memory & Retrieval Benchmark Suite | `cap.t07.memory.memory_bench@1` | pure | 19000 | [spec](docs/PART_SPECS_T07.md#p0345-memory-bench) | [txt](prompts/P0345_memory_bench.txt) |
| P0346 | `context_budget_optimiser` | Context Budget Optimiser | `cap.t07.context.context_budget_optimiser@1` | pure | 20000 | [spec](docs/PART_SPECS_T07.md#p0346-context-budget-optimiser) | [txt](prompts/P0346_context_budget_optimiser.txt) |
| P0347 | `memory_sharding` | Memory Sharding & Locality Routing | `cap.t07.memory.memory_sharding@1` | pure | 21000 | [spec](docs/PART_SPECS_T07.md#p0347-memory-sharding) | [txt](prompts/P0347_memory_sharding.txt) |
| P0348 | `streaming_ingest` | Real-Time Streaming Ingestion | `cap.t07.streaming.streaming_ingest@1` | pure | 22000 | [spec](docs/PART_SPECS_T07.md#p0348-streaming-ingest) | [txt](prompts/P0348_streaming_ingest.txt) |
| P0349 | `cost_aware_retrieval` | Cost-Aware Retrieval Policy | `cap.t07.cost.cost_aware_retrieval@1` | pure | 23000 | [spec](docs/PART_SPECS_T07.md#p0349-cost-aware-retrieval) | [txt](prompts/P0349_cost_aware_retrieval.txt) |
| P0350 | `memory_spec_doc` | Memory Subsystem Specification & Runbook | `cap.t07.memory.memory_spec_doc@1` | pure | 24000 | [spec](docs/PART_SPECS_T07.md#p0350-memory-spec-doc) | [txt](prompts/P0350_memory_spec_doc.txt) |

## T08 — Inference Engine & Ω-Cascade

*Continuous batching, paged KV, 8-stage speculative cascade, admission control. Source of speedup S1.*

| part | slug | title | capability | det | p99 ns | spec | prompt |
|---|---|---|---|---|---:|---|---|
| P0351 | `engine_core` | Inference Engine Core Loop | `cap.t08.engine.engine_core@1` | io | 25000 | [spec](docs/PART_SPECS_T08.md#p0351-engine-core) | [txt](prompts/P0351_engine_core.txt) |
| P0352 | `continuous_batching` | Continuous Batching Scheduler | `cap.t08.continuous.continuous_batching@1` | io | 26000 | [spec](docs/PART_SPECS_T08.md#p0352-continuous-batching) | [txt](prompts/P0352_continuous_batching.txt) |
| P0353 | `chunked_prefill` | Chunked Prefill & Prefill/Decode Interleaving | `cap.t08.chunked.chunked_prefill@1` | io | 27000 | [spec](docs/PART_SPECS_T08.md#p0353-chunked-prefill) | [txt](prompts/P0353_chunked_prefill.txt) |
| P0354 | `prefill_decode_split` | Disaggregated Prefill/Decode Serving | `cap.t08.prefill.prefill_decode_split@1` | io | 28000 | [spec](docs/PART_SPECS_T08.md#p0354-prefill-decode-split) | [txt](prompts/P0354_prefill_decode_split.txt) |
| P0355 | `admission_control` | Admission Control & Queue Management | `cap.t08.admission.admission_control@1` | io | 29000 | [spec](docs/PART_SPECS_T08.md#p0355-admission-control) | [txt](prompts/P0355_admission_control.txt) |
| P0356 | `cascade_stage1_draft` | Cascade Stage 1: 1.5B Draft Engine | `cap.t08.cascade.cascade_stage1_draft@1` | io | 30000 | [spec](docs/PART_SPECS_T08.md#p0356-cascade-stage1-draft) | [txt](prompts/P0356_cascade_stage1_draft.txt) |
| P0357 | `cascade_stage2_draft` | Cascade Stage 2: 7B Draft Engine | `cap.t08.cascade.cascade_stage2_draft@1` | io | 31000 | [spec](docs/PART_SPECS_T08.md#p0357-cascade-stage2-draft) | [txt](prompts/P0357_cascade_stage2_draft.txt) |
| P0358 | `cascade_stage3_draft` | Cascade Stage 3: 70B Draft Engine | `cap.t08.cascade.cascade_stage3_draft@1` | io | 32000 | [spec](docs/PART_SPECS_T08.md#p0358-cascade-stage3-draft) | [txt](prompts/P0358_cascade_stage3_draft.txt) |
| P0359 | `cascade_tree_verify` | Tree-Structured Speculative Verification | `cap.t08.cascade.cascade_tree_verify@1` | io | 33000 | [spec](docs/PART_SPECS_T08.md#p0359-cascade-tree-verify) | [txt](prompts/P0359_cascade_tree_verify.txt) |
| P0360 | `cascade_acceptance` | Acceptance Sampling & Distribution Equivalence | `cap.t08.cascade.cascade_acceptance@1` | io | 34000 | [spec](docs/PART_SPECS_T08.md#p0360-cascade-acceptance) | [txt](prompts/P0360_cascade_acceptance.txt) |
| P0361 | `cascade_scheduler` | Cascade Stage Selection Policy | `cap.t08.cascade.cascade_scheduler@1` | io | 35000 | [spec](docs/PART_SPECS_T08.md#p0361-cascade-scheduler) | [txt](prompts/P0361_cascade_scheduler.txt) |
| P0362 | `cascade_batching` | Batched Speculative Execution | `cap.t08.cascade.cascade_batching@1` | io | 36000 | [spec](docs/PART_SPECS_T08.md#p0362-cascade-batching) | [txt](prompts/P0362_cascade_batching.txt) |
| P0363 | `cascade_rollback` | Speculation Rollback & State Repair | `cap.t08.cascade.cascade_rollback@1` | io | 37000 | [spec](docs/PART_SPECS_T08.md#p0363-cascade-rollback) | [txt](prompts/P0363_cascade_rollback.txt) |
| P0364 | `cascade_tuning` | Draft Length & Depth Auto-Tuning | `cap.t08.cascade.cascade_tuning@1` | io | 38000 | [spec](docs/PART_SPECS_T08.md#p0364-cascade-tuning) | [txt](prompts/P0364_cascade_tuning.txt) |
| P0365 | `paged_attention_runtime` | Paged Attention Runtime Integration | `cap.t08.paged.paged_attention_runtime@1` | io | 39000 | [spec](docs/PART_SPECS_T08.md#p0365-paged-attention-runtime) | [txt](prompts/P0365_paged_attention_runtime.txt) |
| P0366 | `prefix_cache_runtime` | Prefix Cache Runtime & Radix Matching | `cap.t08.prefix.prefix_cache_runtime@1` | io | 40000 | [spec](docs/PART_SPECS_T08.md#p0366-prefix-cache-runtime) | [txt](prompts/P0366_prefix_cache_runtime.txt) |
| P0367 | `session_affinity` | Session Affinity & KV Reuse Routing | `cap.t08.session.session_affinity@1` | io | 41000 | [spec](docs/PART_SPECS_T08.md#p0367-session-affinity) | [txt](prompts/P0367_session_affinity.txt) |
| P0368 | `sampler_engine` | Sampling Engine & Decode Policies | `cap.t08.sampler.sampler_engine@1` | io | 42000 | [spec](docs/PART_SPECS_T08.md#p0368-sampler-engine) | [txt](prompts/P0368_sampler_engine.txt) |
| P0369 | `constrained_decoding` | Grammar-Constrained Decoding Engine | `cap.t08.constrained.constrained_decoding@1` | io | 43000 | [spec](docs/PART_SPECS_T08.md#p0369-constrained-decoding) | [txt](prompts/P0369_constrained_decoding.txt) |
| P0370 | `logit_processor` | Logit Processing Pipeline | `cap.t08.logit.logit_processor@1` | io | 44000 | [spec](docs/PART_SPECS_T08.md#p0370-logit-processor) | [txt](prompts/P0370_logit_processor.txt) |
| P0371 | `stop_conditions` | Stop Criteria & Output Boundary Detection | `cap.t08.stop.stop_conditions@1` | io | 45000 | [spec](docs/PART_SPECS_T08.md#p0371-stop-conditions) | [txt](prompts/P0371_stop_conditions.txt) |
| P0372 | `streaming_output` | Token Streaming & Backpressure | `cap.t08.streaming.streaming_output@1` | io | 46000 | [spec](docs/PART_SPECS_T08.md#p0372-streaming-output) | [txt](prompts/P0372_streaming_output.txt) |
| P0373 | `batch_invariance` | Batch-Invariant Inference Mode | `cap.t08.batch.batch_invariance@1` | io | 47000 | [spec](docs/PART_SPECS_T08.md#p0373-batch-invariance) | [txt](prompts/P0373_batch_invariance.txt) |
| P0374 | `multi_gpu_runtime` | Multi-Device Execution Runtime | `cap.t08.multi.multi_gpu_runtime@1` | io | 48000 | [spec](docs/PART_SPECS_T08.md#p0374-multi-gpu-runtime) | [txt](prompts/P0374_multi_gpu_runtime.txt) |
| P0375 | `model_loading` | Fast Model Loading & Warm Start | `cap.t08.model.model_loading@1` | io | 49000 | [spec](docs/PART_SPECS_T08.md#p0375-model-loading) | [txt](prompts/P0375_model_loading.txt) |
| P0376 | `weight_hotswap` | Zero-Downtime Weight Hot Swap | `cap.t08.weight.weight_hotswap@1` | io | 3000 | [spec](docs/PART_SPECS_T08.md#p0376-weight-hotswap) | [txt](prompts/P0376_weight_hotswap.txt) |
| P0377 | `multi_model_serving` | Multi-Model Co-Residency & Time Slicing | `cap.t08.multi.multi_model_serving@1` | io | 4000 | [spec](docs/PART_SPECS_T08.md#p0377-multi-model-serving) | [txt](prompts/P0377_multi_model_serving.txt) |
| P0378 | `adapter_serving` | Adapter & Fine-Tune Multiplexing | `cap.t08.adapter.adapter_serving@1` | io | 5000 | [spec](docs/PART_SPECS_T08.md#p0378-adapter-serving) | [txt](prompts/P0378_adapter_serving.txt) |
| P0379 | `request_lifecycle` | Request Lifecycle & State Machine | `cap.t08.request.request_lifecycle@1` | io | 6000 | [spec](docs/PART_SPECS_T08.md#p0379-request-lifecycle) | [txt](prompts/P0379_request_lifecycle.txt) |
| P0380 | `cancellation` | Cancellation & Resource Reclamation | `cap.t08.cancellation.cancellation@1` | io | 7000 | [spec](docs/PART_SPECS_T08.md#p0380-cancellation) | [txt](prompts/P0380_cancellation.txt) |
| P0381 | `deadline_scheduling` | Deadline-Aware Execution | `cap.t08.deadline.deadline_scheduling@1` | io | 8000 | [spec](docs/PART_SPECS_T08.md#p0381-deadline-scheduling) | [txt](prompts/P0381_deadline_scheduling.txt) |
| P0382 | `speculative_tools` | Speculative Tool Execution | `cap.t08.speculative.speculative_tools@1` | io | 9000 | [spec](docs/PART_SPECS_T08.md#p0382-speculative-tools) | [txt](prompts/P0382_speculative_tools.txt) |
| P0383 | `parallel_generation` | Parallel Multi-Branch Generation | `cap.t08.parallel.parallel_generation@1` | io | 10000 | [spec](docs/PART_SPECS_T08.md#p0383-parallel-generation) | [txt](prompts/P0383_parallel_generation.txt) |
| P0384 | `output_verification_loop` | Inline Output Verification Loop | `cap.t08.output.output_verification_loop@1` | io | 11000 | [spec](docs/PART_SPECS_T08.md#p0384-output-verification-loop) | [txt](prompts/P0384_output_verification_loop.txt) |
| P0385 | `engine_telemetry` | Engine Observability & Latency Attribution | `cap.t08.engine.engine_telemetry@1` | io | 12000 | [spec](docs/PART_SPECS_T08.md#p0385-engine-telemetry) | [txt](prompts/P0385_engine_telemetry.txt) |
| P0386 | `autoscaling` | Load Prediction & Autoscaling Controller | `cap.t08.autoscaling.autoscaling@1` | io | 13000 | [spec](docs/PART_SPECS_T08.md#p0386-autoscaling) | [txt](prompts/P0386_autoscaling.txt) |
| P0387 | `overload_shedding` | Overload Protection & Graceful Degradation | `cap.t08.overload.overload_shedding@1` | io | 14000 | [spec](docs/PART_SPECS_T08.md#p0387-overload-shedding) | [txt](prompts/P0387_overload_shedding.txt) |
| P0388 | `engine_determinism` | Deterministic Serving Mode | `cap.t08.engine.engine_determinism@1` | io | 15000 | [spec](docs/PART_SPECS_T08.md#p0388-engine-determinism) | [txt](prompts/P0388_engine_determinism.txt) |
| P0389 | `kv_offload_runtime` | KV Offload & Recall Runtime | `cap.t08.kv.kv_offload_runtime@1` | io | 16000 | [spec](docs/PART_SPECS_T08.md#p0389-kv-offload-runtime) | [txt](prompts/P0389_kv_offload_runtime.txt) |
| P0390 | `quantised_serving` | Quantised Serving Paths & Quality Gates | `cap.t08.quantised.quantised_serving@1` | io | 17000 | [spec](docs/PART_SPECS_T08.md#p0390-quantised-serving) | [txt](prompts/P0390_quantised_serving.txt) |
| P0391 | `engine_fault_tolerance` | Engine Fault Tolerance & Request Recovery | `cap.t08.engine.engine_fault_tolerance@1` | io | 18000 | [spec](docs/PART_SPECS_T08.md#p0391-engine-fault-tolerance) | [txt](prompts/P0391_engine_fault_tolerance.txt) |
| P0392 | `api_gateway_runtime` | Protocol Gateway & Request Normalisation | `cap.t08.api.api_gateway_runtime@1` | io | 19000 | [spec](docs/PART_SPECS_T08.md#p0392-api-gateway-runtime) | [txt](prompts/P0392_api_gateway_runtime.txt) |
| P0393 | `engine_bench_serving` | Serving Benchmark & Load Generator | `cap.t08.engine.engine_bench_serving@1` | io | 20000 | [spec](docs/PART_SPECS_T08.md#p0393-engine-bench-serving) | [txt](prompts/P0393_engine_bench_serving.txt) |
| P0394 | `cascade_speed_proof` | S1 Speedup Proof & Attribution | `cap.t08.cascade.cascade_speed_proof@1` | io | 21000 | [spec](docs/PART_SPECS_T08.md#p0394-cascade-speed-proof) | [txt](prompts/P0394_cascade_speed_proof.txt) |
| P0395 | `engine_config_tuning` | Engine Configuration Auto-Tuning | `cap.t08.engine.engine_config_tuning@1` | io | 22000 | [spec](docs/PART_SPECS_T08.md#p0395-engine-config-tuning) | [txt](prompts/P0395_engine_config_tuning.txt) |
| P0396 | `tokenizer_runtime` | Runtime Tokenisation & Detokenisation | `cap.t08.tokenizer.tokenizer_runtime@1` | io | 23000 | [spec](docs/PART_SPECS_T08.md#p0396-tokenizer-runtime) | [txt](prompts/P0396_tokenizer_runtime.txt) |
| P0397 | `prompt_compilation` | Prompt Compilation & Static Prefill | `cap.t08.prompt.prompt_compilation@1` | io | 24000 | [spec](docs/PART_SPECS_T08.md#p0397-prompt-compilation) | [txt](prompts/P0397_prompt_compilation.txt) |
| P0398 | `engine_security` | Serving-Path Security Hardening | `cap.t08.engine.engine_security@1` | io | 25000 | [spec](docs/PART_SPECS_T08.md#p0398-engine-security) | [txt](prompts/P0398_engine_security.txt) |
| P0399 | `cost_accounting_runtime` | Per-Request Cost Accounting | `cap.t08.cost.cost_accounting_runtime@1` | io | 26000 | [spec](docs/PART_SPECS_T08.md#p0399-cost-accounting-runtime) | [txt](prompts/P0399_cost_accounting_runtime.txt) |
| P0400 | `engine_spec_doc` | Inference Engine Specification & Runbook | `cap.t08.engine.engine_spec_doc@1` | io | 27000 | [spec](docs/PART_SPECS_T08.md#p0400-engine-spec-doc) | [txt](prompts/P0400_engine_spec_doc.txt) |

## T09 — Latency Engineering & Ω-Memoize

*Semantic caching, precomputation, early exit, distilled fast paths and the 100x latency accounting system. Sources S4 and S6.*

| part | slug | title | capability | det | p99 ns | spec | prompt |
|---|---|---|---|---|---:|---|---|
| P0401 | `latency_accounting` | End-to-End Latency Accounting Framework | `cap.t09.latency.latency_accounting@1` | io | 28000 | [spec](docs/PART_SPECS_T09.md#p0401-latency-accounting) | [txt](prompts/P0401_latency_accounting.txt) |
| P0402 | `speed_law_model` | The 100x Speed Law Model | `cap.t09.speed.speed_law_model@1` | io | 29000 | [spec](docs/PART_SPECS_T09.md#p0402-speed-law-model) | [txt](prompts/P0402_speed_law_model.txt) |
| P0403 | `memoize_core` | Ω-Memoize Core Engine | `cap.t09.memoize.memoize_core@1` | io | 30000 | [spec](docs/PART_SPECS_T09.md#p0403-memoize-core) | [txt](prompts/P0403_memoize_core.txt) |
| P0404 | `exact_cache` | Exact-Match Response Cache | `cap.t09.exact.exact_cache@1` | io | 31000 | [spec](docs/PART_SPECS_T09.md#p0404-exact-cache) | [txt](prompts/P0404_exact_cache.txt) |
| P0405 | `similarity_cache` | Approximate Semantic Cache with Safety Gates | `cap.t09.similarity.similarity_cache@1` | io | 32000 | [spec](docs/PART_SPECS_T09.md#p0405-similarity-cache) | [txt](prompts/P0405_similarity_cache.txt) |
| P0406 | `template_cache` | Structural Template Cache | `cap.t09.template.template_cache@1` | io | 33000 | [spec](docs/PART_SPECS_T09.md#p0406-template-cache) | [txt](prompts/P0406_template_cache.txt) |
| P0407 | `computation_reuse` | Cross-Request Computation Reuse | `cap.t09.computation.computation_reuse@1` | io | 34000 | [spec](docs/PART_SPECS_T09.md#p0407-computation-reuse) | [txt](prompts/P0407_computation_reuse.txt) |
| P0408 | `early_exit_runtime` | Early-Exit Runtime Controller | `cap.t09.early.early_exit_runtime@1` | io | 35000 | [spec](docs/PART_SPECS_T09.md#p0408-early-exit-runtime) | [txt](prompts/P0408_early_exit_runtime.txt) |
| P0409 | `distill_fast_paths` | Distilled Fast Path Registry | `cap.t09.distill.distill_fast_paths@1` | io | 36000 | [spec](docs/PART_SPECS_T09.md#p0409-distill-fast-paths) | [txt](prompts/P0409_distill_fast_paths.txt) |
| P0410 | `precompute_engine` | Offline Precomputation Engine | `cap.t09.precompute.precompute_engine@1` | io | 37000 | [spec](docs/PART_SPECS_T09.md#p0410-precompute-engine) | [txt](prompts/P0410_precompute_engine.txt) |
| P0411 | `prefetch_predictor` | Next-Action Prediction & Prefetch | `cap.t09.prefetch.prefetch_predictor@1` | io | 38000 | [spec](docs/PART_SPECS_T09.md#p0411-prefetch-predictor) | [txt](prompts/P0411_prefetch_predictor.txt) |
| P0412 | `parallel_horizon` | Parallel Horizon Execution Engine | `cap.t09.parallel.parallel_horizon@1` | io | 39000 | [spec](docs/PART_SPECS_T09.md#p0412-parallel-horizon) | [txt](prompts/P0412_parallel_horizon.txt) |
| P0413 | `dag_critical_path` | Critical Path Optimiser | `cap.t09.dag.dag_critical_path@1` | io | 40000 | [spec](docs/PART_SPECS_T09.md#p0413-dag-critical-path) | [txt](prompts/P0413_dag_critical_path.txt) |
| P0414 | `async_pipeline` | Asynchronous Pipeline Orchestrator | `cap.t09.async.async_pipeline@1` | io | 41000 | [spec](docs/PART_SPECS_T09.md#p0414-async-pipeline) | [txt](prompts/P0414_async_pipeline.txt) |
| P0415 | `tail_latency` | Tail Latency Engineering | `cap.t09.tail.tail_latency@1` | io | 42000 | [spec](docs/PART_SPECS_T09.md#p0415-tail-latency) | [txt](prompts/P0415_tail_latency.txt) |
| P0416 | `jitter_control` | Latency Jitter & Predictability Control | `cap.t09.jitter.jitter_control@1` | io | 43000 | [spec](docs/PART_SPECS_T09.md#p0416-jitter-control) | [txt](prompts/P0416_jitter_control.txt) |
| P0417 | `warmup_manager` | Warmup & Cold Start Elimination | `cap.t09.warmup.warmup_manager@1` | io | 44000 | [spec](docs/PART_SPECS_T09.md#p0417-warmup-manager) | [txt](prompts/P0417_warmup_manager.txt) |
| P0418 | `gc_pause_control` | Pause-Free Operation Engineering | `cap.t09.gc.gc_pause_control@1` | io | 45000 | [spec](docs/PART_SPECS_T09.md#p0418-gc-pause-control) | [txt](prompts/P0418_gc_pause_control.txt) |
| P0419 | `syscall_reduction` | Syscall & Context-Switch Minimisation | `cap.t09.syscall.syscall_reduction@1` | io | 46000 | [spec](docs/PART_SPECS_T09.md#p0419-syscall-reduction) | [txt](prompts/P0419_syscall_reduction.txt) |
| P0420 | `network_latency` | Network Path Latency Optimisation | `cap.t09.network.network_latency@1` | io | 47000 | [spec](docs/PART_SPECS_T09.md#p0420-network-latency) | [txt](prompts/P0420_network_latency.txt) |
| P0421 | `edge_inference` | Edge & Local-First Execution | `cap.t09.edge.edge_inference@1` | io | 48000 | [spec](docs/PART_SPECS_T09.md#p0421-edge-inference) | [txt](prompts/P0421_edge_inference.txt) |
| P0422 | `compression_latency` | Payload Compression Latency Tradeoffs | `cap.t09.compression.compression_latency@1` | io | 49000 | [spec](docs/PART_SPECS_T09.md#p0422-compression-latency) | [txt](prompts/P0422_compression_latency.txt) |
| P0423 | `batch_latency_tradeoff` | Batching Latency/Throughput Optimiser | `cap.t09.batch.batch_latency_tradeoff@1` | io | 3000 | [spec](docs/PART_SPECS_T09.md#p0423-batch-latency-tradeoff) | [txt](prompts/P0423_batch_latency_tradeoff.txt) |
| P0424 | `priority_lanes` | Priority Lanes & Interactive Fast Path | `cap.t09.priority.priority_lanes@1` | io | 4000 | [spec](docs/PART_SPECS_T09.md#p0424-priority-lanes) | [txt](prompts/P0424_priority_lanes.txt) |
| P0425 | `speculative_ui` | Perceived Latency Engineering | `cap.t09.speculative.speculative_ui@1` | io | 5000 | [spec](docs/PART_SPECS_T09.md#p0425-speculative-ui) | [txt](prompts/P0425_speculative_ui.txt) |
| P0426 | `cache_coherence` | Cross-Layer Cache Coherence & Invalidation | `cap.t09.cache.cache_coherence@1` | io | 6000 | [spec](docs/PART_SPECS_T09.md#p0426-cache-coherence) | [txt](prompts/P0426_cache_coherence.txt) |
| P0427 | `hot_cold_split` | Hot/Cold Path Separation | `cap.t09.hot.hot_cold_split@1` | io | 7000 | [spec](docs/PART_SPECS_T09.md#p0427-hot-cold-split) | [txt](prompts/P0427_hot_cold_split.txt) |
| P0428 | `lock_free_paths` | Lock-Free Request Path | `cap.t09.lock.lock_free_paths@1` | io | 8000 | [spec](docs/PART_SPECS_T09.md#p0428-lock-free-paths) | [txt](prompts/P0428_lock_free_paths.txt) |
| P0429 | `numa_latency` | Memory Locality Latency Optimisation | `cap.t09.numa.numa_latency@1` | io | 9000 | [spec](docs/PART_SPECS_T09.md#p0429-numa-latency) | [txt](prompts/P0429_numa_latency.txt) |
| P0430 | `io_scheduling` | Storage IO Latency Scheduling | `cap.t09.io.io_scheduling@1` | io | 10000 | [spec](docs/PART_SPECS_T09.md#p0430-io-scheduling) | [txt](prompts/P0430_io_scheduling.txt) |
| P0431 | `adaptive_quality` | Adaptive Quality/Latency Controller | `cap.t09.adaptive.adaptive_quality@1` | io | 11000 | [spec](docs/PART_SPECS_T09.md#p0431-adaptive-quality) | [txt](prompts/P0431_adaptive_quality.txt) |
| P0432 | `slo_manager` | SLO Definition, Tracking & Error Budgets | `cap.t09.slo.slo_manager@1` | io | 12000 | [spec](docs/PART_SPECS_T09.md#p0432-slo-manager) | [txt](prompts/P0432_slo_manager.txt) |
| P0433 | `latency_regression_gate` | Latency Regression Gate for 1000 Parts | `cap.t09.latency.latency_regression_gate@1` | io | 13000 | [spec](docs/PART_SPECS_T09.md#p0433-latency-regression-gate) | [txt](prompts/P0433_latency_regression_gate.txt) |
| P0434 | `perf_ci` | Continuous Performance Integration | `cap.t09.perf.perf_ci@1` | io | 14000 | [spec](docs/PART_SPECS_T09.md#p0434-perf-ci) | [txt](prompts/P0434_perf_ci.txt) |
| P0435 | `flamegraph_tooling` | Profiling & Flamegraph Analysis Tooling | `cap.t09.flamegraph.flamegraph_tooling@1` | io | 15000 | [spec](docs/PART_SPECS_T09.md#p0435-flamegraph-tooling) | [txt](prompts/P0435_flamegraph_tooling.txt) |
| P0436 | `bottleneck_analyser` | Automatic Bottleneck Analyser | `cap.t09.bottleneck.bottleneck_analyser@1` | io | 16000 | [spec](docs/PART_SPECS_T09.md#p0436-bottleneck-analyser) | [txt](prompts/P0436_bottleneck_analyser.txt) |
| P0437 | `throughput_optimiser` | Throughput Optimisation Engine | `cap.t09.throughput.throughput_optimiser@1` | io | 17000 | [spec](docs/PART_SPECS_T09.md#p0437-throughput-optimiser) | [txt](prompts/P0437_throughput_optimiser.txt) |
| P0438 | `energy_efficiency` | Energy per Token Optimisation | `cap.t09.energy.energy_efficiency@1` | io | 18000 | [spec](docs/PART_SPECS_T09.md#p0438-energy-efficiency) | [txt](prompts/P0438_energy_efficiency.txt) |
| P0439 | `cost_optimiser` | Cost per Solved Task Optimiser | `cap.t09.cost.cost_optimiser@1` | io | 19000 | [spec](docs/PART_SPECS_T09.md#p0439-cost-optimiser) | [txt](prompts/P0439_cost_optimiser.txt) |
| P0440 | `capacity_planner` | Capacity Planning & Headroom Model | `cap.t09.capacity.capacity_planner@1` | io | 20000 | [spec](docs/PART_SPECS_T09.md#p0440-capacity-planner) | [txt](prompts/P0440_capacity_planner.txt) |
| P0441 | `cache_sizing` | Cache Sizing & Memory Allocation Optimiser | `cap.t09.cache.cache_sizing@1` | io | 21000 | [spec](docs/PART_SPECS_T09.md#p0441-cache-sizing) | [txt](prompts/P0441_cache_sizing.txt) |
| P0442 | `speculation_budget` | Speculation Budget Governor | `cap.t09.speculation.speculation_budget@1` | io | 22000 | [spec](docs/PART_SPECS_T09.md#p0442-speculation-budget) | [txt](prompts/P0442_speculation_budget.txt) |
| P0443 | `latency_simulator` | Latency Simulator & What-If Engine | `cap.t09.latency.latency_simulator@1` | io | 23000 | [spec](docs/PART_SPECS_T09.md#p0443-latency-simulator) | [txt](prompts/P0443_latency_simulator.txt) |
| P0444 | `benchmark_speed_public` | Public Speed Comparison Harness | `cap.t09.benchmark.benchmark_speed_public@1` | io | 24000 | [spec](docs/PART_SPECS_T09.md#p0444-benchmark-speed-public) | [txt](prompts/P0444_benchmark_speed_public.txt) |
| P0445 | `realtime_mode` | Real-Time & Voice-Latency Mode | `cap.t09.realtime.realtime_mode@1` | io | 25000 | [spec](docs/PART_SPECS_T09.md#p0445-realtime-mode) | [txt](prompts/P0445_realtime_mode.txt) |
| P0446 | `burst_handling` | Burst Absorption & Queue Shaping | `cap.t09.burst.burst_handling@1` | io | 26000 | [spec](docs/PART_SPECS_T09.md#p0446-burst-handling) | [txt](prompts/P0446_burst_handling.txt) |
| P0447 | `degradation_ladder` | Formal Degradation Ladder | `cap.t09.degradation.degradation_ladder@1` | io | 27000 | [spec](docs/PART_SPECS_T09.md#p0447-degradation-ladder) | [txt](prompts/P0447_degradation_ladder.txt) |
| P0448 | `latency_dashboard` | Latency & Cost Observability Artifacts | `cap.t09.latency.latency_dashboard@1` | io | 28000 | [spec](docs/PART_SPECS_T09.md#p0448-latency-dashboard) | [txt](prompts/P0448_latency_dashboard.txt) |
| P0449 | `speed_proof_report` | The 100x Speed Proof Report Generator | `cap.t09.speed.speed_proof_report@1` | io | 29000 | [spec](docs/PART_SPECS_T09.md#p0449-speed-proof-report) | [txt](prompts/P0449_speed_proof_report.txt) |
| P0450 | `latency_spec_doc` | Latency Engineering Specification & Runbook | `cap.t09.latency.latency_spec_doc@1` | io | 30000 | [spec](docs/PART_SPECS_T09.md#p0450-latency-spec-doc) | [txt](prompts/P0450_latency_spec_doc.txt) |

## T10 — Reasoning, Search & Deliberation

*Verifier-guided search over thought programs: the engine that converts compute into correctness. Source of speedup S5.*

| part | slug | title | capability | det | p99 ns | spec | prompt |
|---|---|---|---|---|---:|---|---|
| P0451 | `thought_program_ir` | Thought Program Representation | `cap.t10.thought.thought_program_ir@1` | seeded | 31000 | [spec](docs/PART_SPECS_T10.md#p0451-thought-program-ir) | [txt](prompts/P0451_thought_program_ir.txt) |
| P0452 | `search_controller` | Deliberation Search Controller | `cap.t10.search.search_controller@1` | seeded | 32000 | [spec](docs/PART_SPECS_T10.md#p0452-search-controller) | [txt](prompts/P0452_search_controller.txt) |
| P0453 | `tree_search` | Tree Search over Reasoning States | `cap.t10.tree.tree_search@1` | seeded | 33000 | [spec](docs/PART_SPECS_T10.md#p0453-tree-search) | [txt](prompts/P0453_tree_search.txt) |
| P0454 | `graph_search` | Graph-of-Thought Reasoning | `cap.t10.graph.graph_search@1` | seeded | 34000 | [spec](docs/PART_SPECS_T10.md#p0454-graph-search) | [txt](prompts/P0454_graph_search.txt) |
| P0455 | `beam_pruning` | Verifier-Guided Beam Pruning | `cap.t10.beam.beam_pruning@1` | seeded | 35000 | [spec](docs/PART_SPECS_T10.md#p0455-beam-pruning) | [txt](prompts/P0455_beam_pruning.txt) |
| P0456 | `process_verifier` | Process Reward Model & Step Verification | `cap.t10.process.process_verifier@1` | seeded | 36000 | [spec](docs/PART_SPECS_T10.md#p0456-process-verifier) | [txt](prompts/P0456_process_verifier.txt) |
| P0457 | `outcome_verifier` | Outcome Verification & Answer Checking | `cap.t10.outcome.outcome_verifier@1` | seeded | 37000 | [spec](docs/PART_SPECS_T10.md#p0457-outcome-verifier) | [txt](prompts/P0457_outcome_verifier.txt) |
| P0458 | `self_consistency` | Self-Consistency & Sample Aggregation | `cap.t10.self.self_consistency@1` | seeded | 38000 | [spec](docs/PART_SPECS_T10.md#p0458-self-consistency) | [txt](prompts/P0458_self_consistency.txt) |
| P0459 | `self_critique` | Self-Critique & Revision Loop | `cap.t10.self.self_critique@1` | seeded | 39000 | [spec](docs/PART_SPECS_T10.md#p0459-self-critique) | [txt](prompts/P0459_self_critique.txt) |
| P0460 | `debate_ensemble` | Multi-Perspective Debate & Adversarial Review | `cap.t10.debate.debate_ensemble@1` | seeded | 40000 | [spec](docs/PART_SPECS_T10.md#p0460-debate-ensemble) | [txt](prompts/P0460_debate_ensemble.txt) |
| P0461 | `decomposition` | Problem Decomposition Engine | `cap.t10.decomposition.decomposition@1` | seeded | 41000 | [spec](docs/PART_SPECS_T10.md#p0461-decomposition) | [txt](prompts/P0461_decomposition.txt) |
| P0462 | `planning_engine` | Hierarchical Planning Engine | `cap.t10.planning.planning_engine@1` | seeded | 42000 | [spec](docs/PART_SPECS_T10.md#p0462-planning-engine) | [txt](prompts/P0462_planning_engine.txt) |
| P0463 | `goal_management` | Goal Stack & Intent Tracking | `cap.t10.goal.goal_management@1` | seeded | 43000 | [spec](docs/PART_SPECS_T10.md#p0463-goal-management) | [txt](prompts/P0463_goal_management.txt) |
| P0464 | `constraint_reasoning` | Constraint Satisfaction & Optimisation Reasoning | `cap.t10.constraint.constraint_reasoning@1` | seeded | 44000 | [spec](docs/PART_SPECS_T10.md#p0464-constraint-reasoning) | [txt](prompts/P0464_constraint_reasoning.txt) |
| P0465 | `analogy_engine` | Analogical & Case-Based Reasoning | `cap.t10.analogy.analogy_engine@1` | seeded | 45000 | [spec](docs/PART_SPECS_T10.md#p0465-analogy-engine) | [txt](prompts/P0465_analogy_engine.txt) |
| P0466 | `abstraction_engine` | Abstraction Discovery & Concept Formation | `cap.t10.abstraction.abstraction_engine@1` | seeded | 46000 | [spec](docs/PART_SPECS_T10.md#p0466-abstraction-engine) | [txt](prompts/P0466_abstraction_engine.txt) |
| P0467 | `induction_engine` | Rule Induction from Few Examples | `cap.t10.induction.induction_engine@1` | seeded | 47000 | [spec](docs/PART_SPECS_T10.md#p0467-induction-engine) | [txt](prompts/P0467_induction_engine.txt) |
| P0468 | `program_synthesis_reasoning` | Neural-Guided Program Synthesis | `cap.t10.program.program_synthesis_reasoning@1` | seeded | 48000 | [spec](docs/PART_SPECS_T10.md#p0468-program-synthesis-reasoning) | [txt](prompts/P0468_program_synthesis_reasoning.txt) |
| P0469 | `counterfactual_reasoning` | Counterfactual & Hypothetical Reasoning | `cap.t10.counterfactual.counterfactual_reasoning@1` | seeded | 49000 | [spec](docs/PART_SPECS_T10.md#p0469-counterfactual-reasoning) | [txt](prompts/P0469_counterfactual_reasoning.txt) |
| P0470 | `probabilistic_reasoning` | Probabilistic Inference Engine | `cap.t10.probabilistic.probabilistic_reasoning@1` | seeded | 3000 | [spec](docs/PART_SPECS_T10.md#p0470-probabilistic-reasoning) | [txt](prompts/P0470_probabilistic_reasoning.txt) |
| P0471 | `numeric_reasoning` | Exact Numeric & Quantitative Reasoning | `cap.t10.numeric.numeric_reasoning@1` | seeded | 4000 | [spec](docs/PART_SPECS_T10.md#p0471-numeric-reasoning) | [txt](prompts/P0471_numeric_reasoning.txt) |
| P0472 | `temporal_reasoning` | Temporal & Scheduling Reasoning | `cap.t10.temporal.temporal_reasoning@1` | seeded | 5000 | [spec](docs/PART_SPECS_T10.md#p0472-temporal-reasoning) | [txt](prompts/P0472_temporal_reasoning.txt) |
| P0473 | `spatial_reasoning` | Spatial & Geometric Reasoning | `cap.t10.spatial.spatial_reasoning@1` | seeded | 6000 | [spec](docs/PART_SPECS_T10.md#p0473-spatial-reasoning) | [txt](prompts/P0473_spatial_reasoning.txt) |
| P0474 | `commonsense_engine` | Commonsense Reasoning & Default Inference | `cap.t10.commonsense.commonsense_engine@1` | seeded | 7000 | [spec](docs/PART_SPECS_T10.md#p0474-commonsense-engine) | [txt](prompts/P0474_commonsense_engine.txt) |
| P0475 | `meta_reasoning` | Meta-Reasoning & Strategy Selection | `cap.t10.meta.meta_reasoning@1` | seeded | 8000 | [spec](docs/PART_SPECS_T10.md#p0475-meta-reasoning) | [txt](prompts/P0475_meta_reasoning.txt) |
| P0476 | `difficulty_estimation` | Problem Difficulty Estimation | `cap.t10.difficulty.difficulty_estimation@1` | seeded | 9000 | [spec](docs/PART_SPECS_T10.md#p0476-difficulty-estimation) | [txt](prompts/P0476_difficulty_estimation.txt) |
| P0477 | `stopping_rules` | Optimal Stopping & Confidence Thresholds | `cap.t10.stopping.stopping_rules@1` | seeded | 10000 | [spec](docs/PART_SPECS_T10.md#p0477-stopping-rules) | [txt](prompts/P0477_stopping_rules.txt) |
| P0478 | `backtracking` | Backtracking & Dead-End Recovery | `cap.t10.backtracking.backtracking@1` | seeded | 11000 | [spec](docs/PART_SPECS_T10.md#p0478-backtracking) | [txt](prompts/P0478_backtracking.txt) |
| P0479 | `reasoning_memory` | Reasoning Trace Memory & Lesson Extraction | `cap.t10.reasoning.reasoning_memory@1` | seeded | 12000 | [spec](docs/PART_SPECS_T10.md#p0479-reasoning-memory) | [txt](prompts/P0479_reasoning_memory.txt) |
| P0480 | `chain_compression` | Reasoning Chain Compression & Distillation | `cap.t10.chain.chain_compression@1` | seeded | 13000 | [spec](docs/PART_SPECS_T10.md#p0480-chain-compression) | [txt](prompts/P0480_chain_compression.txt) |
| P0481 | `parallel_reasoning` | Parallel Reasoning Orchestration | `cap.t10.parallel.parallel_reasoning@1` | seeded | 14000 | [spec](docs/PART_SPECS_T10.md#p0481-parallel-reasoning) | [txt](prompts/P0481_parallel_reasoning.txt) |
| P0482 | `hypothesis_management` | Hypothesis Space Management | `cap.t10.hypothesis.hypothesis_management@1` | seeded | 15000 | [spec](docs/PART_SPECS_T10.md#p0482-hypothesis-management) | [txt](prompts/P0482_hypothesis_management.txt) |
| P0483 | `evidence_integration` | Evidence Aggregation & Weighing | `cap.t10.evidence.evidence_integration@1` | seeded | 16000 | [spec](docs/PART_SPECS_T10.md#p0483-evidence-integration) | [txt](prompts/P0483_evidence_integration.txt) |
| P0484 | `assumption_tracking` | Assumption Tracking & Explicit Uncertainty | `cap.t10.assumption.assumption_tracking@1` | seeded | 17000 | [spec](docs/PART_SPECS_T10.md#p0484-assumption-tracking) | [txt](prompts/P0484_assumption_tracking.txt) |
| P0485 | `question_asking` | Clarification & Active Information Gathering | `cap.t10.question.question_asking@1` | seeded | 18000 | [spec](docs/PART_SPECS_T10.md#p0485-question-asking) | [txt](prompts/P0485_question_asking.txt) |
| P0486 | `reasoning_faithfulness` | Reasoning Faithfulness Verification | `cap.t10.reasoning.reasoning_faithfulness@1` | seeded | 19000 | [spec](docs/PART_SPECS_T10.md#p0486-reasoning-faithfulness) | [txt](prompts/P0486_reasoning_faithfulness.txt) |
| P0487 | `reasoning_robustness` | Reasoning Robustness to Perturbation | `cap.t10.reasoning.reasoning_robustness@1` | seeded | 20000 | [spec](docs/PART_SPECS_T10.md#p0487-reasoning-robustness) | [txt](prompts/P0487_reasoning_robustness.txt) |
| P0488 | `multi_step_arithmetic` | Long Multi-Step Derivation Engine | `cap.t10.multi.multi_step_arithmetic@1` | seeded | 21000 | [spec](docs/PART_SPECS_T10.md#p0488-multi-step-arithmetic) | [txt](prompts/P0488_multi_step_arithmetic.txt) |
| P0489 | `proof_sketch` | Proof Sketch Generation & Refinement | `cap.t10.proof.proof_sketch@1` | seeded | 22000 | [spec](docs/PART_SPECS_T10.md#p0489-proof-sketch) | [txt](prompts/P0489_proof_sketch.txt) |
| P0490 | `reasoning_search_bench` | Reasoning Benchmark Harness | `cap.t10.reasoning.reasoning_search_bench@1` | seeded | 23000 | [spec](docs/PART_SPECS_T10.md#p0490-reasoning-search-bench) | [txt](prompts/P0490_reasoning_search_bench.txt) |
| P0491 | `reasoning_cost_model` | Value of Computation Model | `cap.t10.reasoning.reasoning_cost_model@1` | seeded | 24000 | [spec](docs/PART_SPECS_T10.md#p0491-reasoning-cost-model) | [txt](prompts/P0491_reasoning_cost_model.txt) |
| P0492 | `scratchpad_manager` | Scratchpad & Working Memory Manager | `cap.t10.scratchpad.scratchpad_manager@1` | seeded | 25000 | [spec](docs/PART_SPECS_T10.md#p0492-scratchpad-manager) | [txt](prompts/P0492_scratchpad_manager.txt) |
| P0493 | `subgoal_caching` | Subgoal Solution Caching | `cap.t10.subgoal.subgoal_caching@1` | seeded | 26000 | [spec](docs/PART_SPECS_T10.md#p0493-subgoal-caching) | [txt](prompts/P0493_subgoal_caching.txt) |
| P0494 | `reasoning_transfer` | Cross-Domain Reasoning Transfer | `cap.t10.reasoning.reasoning_transfer@1` | seeded | 27000 | [spec](docs/PART_SPECS_T10.md#p0494-reasoning-transfer) | [txt](prompts/P0494_reasoning_transfer.txt) |
| P0495 | `error_taxonomy` | Reasoning Error Taxonomy & Diagnosis | `cap.t10.error.error_taxonomy@1` | seeded | 28000 | [spec](docs/PART_SPECS_T10.md#p0495-error-taxonomy) | [txt](prompts/P0495_error_taxonomy.txt) |
| P0496 | `adversarial_reasoning` | Adversarial Reasoning Stress Tests | `cap.t10.adversarial.adversarial_reasoning@1` | seeded | 29000 | [spec](docs/PART_SPECS_T10.md#p0496-adversarial-reasoning) | [txt](prompts/P0496_adversarial_reasoning.txt) |
| P0497 | `reasoning_interpretability` | Reasoning Introspection & Explanation | `cap.t10.reasoning.reasoning_interpretability@1` | seeded | 30000 | [spec](docs/PART_SPECS_T10.md#p0497-reasoning-interpretability) | [txt](prompts/P0497_reasoning_interpretability.txt) |
| P0498 | `collective_reasoning` | Multi-Instance Collective Reasoning | `cap.t10.collective.collective_reasoning@1` | seeded | 31000 | [spec](docs/PART_SPECS_T10.md#p0498-collective-reasoning) | [txt](prompts/P0498_collective_reasoning.txt) |
| P0499 | `reasoning_speed_proof` | S5 Speedup Proof & Attribution | `cap.t10.reasoning.reasoning_speed_proof@1` | seeded | 32000 | [spec](docs/PART_SPECS_T10.md#p0499-reasoning-speed-proof) | [txt](prompts/P0499_reasoning_speed_proof.txt) |
| P0500 | `reasoning_spec_doc` | Reasoning Subsystem Specification | `cap.t10.reasoning.reasoning_spec_doc@1` | seeded | 33000 | [spec](docs/PART_SPECS_T10.md#p0500-reasoning-spec-doc) | [txt](prompts/P0500_reasoning_spec_doc.txt) |

## T11 — Formal Methods & Proof-Carrying Answers

*SMT/ITP integration, proof search, certified numerics: every high-stakes answer ships a machine-checkable certificate.*

| part | slug | title | capability | det | p99 ns | spec | prompt |
|---|---|---|---|---|---:|---|---|
| P0501 | `logic_core` | First-Order & Higher-Order Logic Core | `cap.t11.logic.logic_core@1` | pure | 34000 | [spec](docs/PART_SPECS_T11.md#p0501-logic-core) | [txt](prompts/P0501_logic_core.txt) |
| P0502 | `smt_bridge` | SMT Solver Integration Layer | `cap.t11.smt.smt_bridge@1` | pure | 35000 | [spec](docs/PART_SPECS_T11.md#p0502-smt-bridge) | [txt](prompts/P0502_smt_bridge.txt) |
| P0503 | `sat_engine` | SAT Solving & Encoding Toolkit | `cap.t11.sat.sat_engine@1` | pure | 36000 | [spec](docs/PART_SPECS_T11.md#p0503-sat-engine) | [txt](prompts/P0503_sat_engine.txt) |
| P0504 | `itp_bridge` | Interactive Theorem Prover Interface | `cap.t11.itp.itp_bridge@1` | pure | 37000 | [spec](docs/PART_SPECS_T11.md#p0504-itp-bridge) | [txt](prompts/P0504_itp_bridge.txt) |
| P0505 | `proof_search` | Automated Proof Search Engine | `cap.t11.proof.proof_search@1` | pure | 38000 | [spec](docs/PART_SPECS_T11.md#p0505-proof-search) | [txt](prompts/P0505_proof_search.txt) |
| P0506 | `premise_selection` | Premise Selection & Library Search | `cap.t11.premise.premise_selection@1` | pure | 39000 | [spec](docs/PART_SPECS_T11.md#p0506-premise-selection) | [txt](prompts/P0506_premise_selection.txt) |
| P0507 | `proof_certificate` | Proof-Carrying Answer Format | `cap.t11.proof.proof_certificate@1` | pure | 40000 | [spec](docs/PART_SPECS_T11.md#p0507-proof-certificate) | [txt](prompts/P0507_proof_certificate.txt) |
| P0508 | `verification_conditions` | Verification Condition Generation | `cap.t11.verification.verification_conditions@1` | pure | 41000 | [spec](docs/PART_SPECS_T11.md#p0508-verification-conditions) | [txt](prompts/P0508_verification_conditions.txt) |
| P0509 | `invariant_inference` | Loop Invariant & Contract Inference | `cap.t11.invariant.invariant_inference@1` | pure | 42000 | [spec](docs/PART_SPECS_T11.md#p0509-invariant-inference) | [txt](prompts/P0509_invariant_inference.txt) |
| P0510 | `abstract_interpretation` | Abstract Interpretation Framework | `cap.t11.abstract.abstract_interpretation@1` | pure | 43000 | [spec](docs/PART_SPECS_T11.md#p0510-abstract-interpretation) | [txt](prompts/P0510_abstract_interpretation.txt) |
| P0511 | `model_checking` | Bounded & Unbounded Model Checking | `cap.t11.model.model_checking@1` | pure | 44000 | [spec](docs/PART_SPECS_T11.md#p0511-model-checking) | [txt](prompts/P0511_model_checking.txt) |
| P0512 | `refinement_types` | Refinement Type Checking | `cap.t11.refinement.refinement_types@1` | pure | 45000 | [spec](docs/PART_SPECS_T11.md#p0512-refinement-types) | [txt](prompts/P0512_refinement_types.txt) |
| P0513 | `dependent_types` | Dependent Type Elaboration | `cap.t11.dependent.dependent_types@1` | pure | 46000 | [spec](docs/PART_SPECS_T11.md#p0513-dependent-types) | [txt](prompts/P0513_dependent_types.txt) |
| P0514 | `termination_analysis` | Termination & Complexity Analysis | `cap.t11.termination.termination_analysis@1` | pure | 47000 | [spec](docs/PART_SPECS_T11.md#p0514-termination-analysis) | [txt](prompts/P0514_termination_analysis.txt) |
| P0515 | `certified_numerics` | Certified Numerical Computation | `cap.t11.certified.certified_numerics@1` | pure | 48000 | [spec](docs/PART_SPECS_T11.md#p0515-certified-numerics) | [txt](prompts/P0515_certified_numerics.txt) |
| P0516 | `exact_arithmetic` | Exact Real & Symbolic Arithmetic | `cap.t11.exact.exact_arithmetic@1` | pure | 49000 | [spec](docs/PART_SPECS_T11.md#p0516-exact-arithmetic) | [txt](prompts/P0516_exact_arithmetic.txt) |
| P0517 | `computer_algebra` | Computer Algebra System Integration | `cap.t11.computer.computer_algebra@1` | pure | 3000 | [spec](docs/PART_SPECS_T11.md#p0517-computer-algebra) | [txt](prompts/P0517_computer_algebra.txt) |
| P0518 | `theorem_library` | Formal Knowledge Library & Ontology | `cap.t11.theorem.theorem_library@1` | pure | 4000 | [spec](docs/PART_SPECS_T11.md#p0518-theorem-library) | [txt](prompts/P0518_theorem_library.txt) |
| P0519 | `autoformalisation` | Natural Language to Formal Statement | `cap.t11.autoformalisat.autoformalisation@1` | pure | 5000 | [spec](docs/PART_SPECS_T11.md#p0519-autoformalisation) | [txt](prompts/P0519_autoformalisation.txt) |
| P0520 | `informalisation` | Formal to Natural Language Explanation | `cap.t11.informalisatio.informalisation@1` | pure | 6000 | [spec](docs/PART_SPECS_T11.md#p0520-informalisation) | [txt](prompts/P0520_informalisation.txt) |
| P0521 | `spec_language` | Specification Language & Property DSL | `cap.t11.spec.spec_language@1` | pure | 7000 | [spec](docs/PART_SPECS_T11.md#p0521-spec-language) | [txt](prompts/P0521_spec_language.txt) |
| P0522 | `contract_checking` | Runtime Contract Checking & Fail-Fast | `cap.t11.contract.contract_checking@1` | pure | 8000 | [spec](docs/PART_SPECS_T11.md#p0522-contract-checking) | [txt](prompts/P0522_contract_checking.txt) |
| P0523 | `property_testing_formal` | Property-Based Testing from Specifications | `cap.t11.property.property_testing_formal@1` | pure | 9000 | [spec](docs/PART_SPECS_T11.md#p0523-property-testing-formal) | [txt](prompts/P0523_property_testing_formal.txt) |
| P0524 | `symbolic_execution` | Symbolic & Concolic Execution Engine | `cap.t11.symbolic.symbolic_execution@1` | pure | 10000 | [spec](docs/PART_SPECS_T11.md#p0524-symbolic-execution) | [txt](prompts/P0524_symbolic_execution.txt) |
| P0525 | `proof_repair` | Proof Repair & Maintenance | `cap.t11.proof.proof_repair@1` | pure | 11000 | [spec](docs/PART_SPECS_T11.md#p0525-proof-repair) | [txt](prompts/P0525_proof_repair.txt) |
| P0526 | `counterexample_engine` | Counterexample Generation & Explanation | `cap.t11.counterexample.counterexample_engine@1` | pure | 12000 | [spec](docs/PART_SPECS_T11.md#p0526-counterexample-engine) | [txt](prompts/P0526_counterexample_engine.txt) |
| P0527 | `proof_compression` | Proof Compression & Certificate Minimisation | `cap.t11.proof.proof_compression@1` | pure | 13000 | [spec](docs/PART_SPECS_T11.md#p0527-proof-compression) | [txt](prompts/P0527_proof_compression.txt) |
| P0528 | `verified_kernels` | Formally Verified Critical Kernels | `cap.t11.verified.verified_kernels@1` | pure | 14000 | [spec](docs/PART_SPECS_T11.md#p0528-verified-kernels) | [txt](prompts/P0528_verified_kernels.txt) |
| P0529 | `hoare_logic_engine` | Program Logic Engine | `cap.t11.hoare.hoare_logic_engine@1` | pure | 15000 | [spec](docs/PART_SPECS_T11.md#p0529-hoare-logic-engine) | [txt](prompts/P0529_hoare_logic_engine.txt) |
| P0530 | `type_safety_proofs` | Type System Soundness Proofs | `cap.t11.type.type_safety_proofs@1` | pure | 16000 | [spec](docs/PART_SPECS_T11.md#p0530-type-safety-proofs) | [txt](prompts/P0530_type_safety_proofs.txt) |
| P0531 | `crypto_verification` | Cryptographic Protocol Verification | `cap.t11.crypto.crypto_verification@1` | pure | 17000 | [spec](docs/PART_SPECS_T11.md#p0531-crypto-verification) | [txt](prompts/P0531_crypto_verification.txt) |
| P0532 | `concurrency_verification` | Concurrency Correctness Verification | `cap.t11.concurrency.concurrency_verification@1` | pure | 18000 | [spec](docs/PART_SPECS_T11.md#p0532-concurrency-verification) | [txt](prompts/P0532_concurrency_verification.txt) |
| P0533 | `numeric_verification_ml` | Neural Network Verification | `cap.t11.numeric.numeric_verification_ml@1` | pure | 19000 | [spec](docs/PART_SPECS_T11.md#p0533-numeric-verification-ml) | [txt](prompts/P0533_numeric_verification_ml.txt) |
| P0534 | `statistical_guarantees` | Statistical & Distribution-Free Guarantees | `cap.t11.statistical.statistical_guarantees@1` | pure | 20000 | [spec](docs/PART_SPECS_T11.md#p0534-statistical-guarantees) | [txt](prompts/P0534_statistical_guarantees.txt) |
| P0535 | `proof_of_work_bounds` | Complexity Lower Bound Reasoning | `cap.t11.proof.proof_of_work_bounds@1` | pure | 21000 | [spec](docs/PART_SPECS_T11.md#p0535-proof-of-work-bounds) | [txt](prompts/P0535_proof_of_work_bounds.txt) |
| P0536 | `decision_procedures` | Specialised Decision Procedures | `cap.t11.decision.decision_procedures@1` | pure | 22000 | [spec](docs/PART_SPECS_T11.md#p0536-decision-procedures) | [txt](prompts/P0536_decision_procedures.txt) |
| P0537 | `rewriting_systems` | Term Rewriting & Confluence Analysis | `cap.t11.rewriting.rewriting_systems@1` | pure | 23000 | [spec](docs/PART_SPECS_T11.md#p0537-rewriting-systems) | [txt](prompts/P0537_rewriting_systems.txt) |
| P0538 | `proof_assistant_ux` | Formal Verification Developer Experience | `cap.t11.proof.proof_assistant_ux@1` | pure | 24000 | [spec](docs/PART_SPECS_T11.md#p0538-proof-assistant-ux) | [txt](prompts/P0538_proof_assistant_ux.txt) |
| P0539 | `verification_scheduling` | Verification Effort Allocation | `cap.t11.verification.verification_scheduling@1` | pure | 25000 | [spec](docs/PART_SPECS_T11.md#p0539-verification-scheduling) | [txt](prompts/P0539_verification_scheduling.txt) |
| P0540 | `hybrid_verification` | Hybrid Formal/Empirical Verification | `cap.t11.hybrid.hybrid_verification@1` | pure | 26000 | [spec](docs/PART_SPECS_T11.md#p0540-hybrid-verification) | [txt](prompts/P0540_hybrid_verification.txt) |
| P0541 | `regression_proofs` | Proof-Backed Regression Prevention | `cap.t11.regression.regression_proofs@1` | pure | 27000 | [spec](docs/PART_SPECS_T11.md#p0541-regression-proofs) | [txt](prompts/P0541_regression_proofs.txt) |
| P0542 | `math_benchmark_formal` | Formal Mathematics Benchmark Harness | `cap.t11.math.math_benchmark_formal@1` | pure | 28000 | [spec](docs/PART_SPECS_T11.md#p0542-math-benchmark-formal) | [txt](prompts/P0542_math_benchmark_formal.txt) |
| P0543 | `scientific_verification` | Scientific Claim Verification | `cap.t11.scientific.scientific_verification@1` | pure | 29000 | [spec](docs/PART_SPECS_T11.md#p0543-scientific-verification) | [txt](prompts/P0543_scientific_verification.txt) |
| P0544 | `legal_formalisation` | Legal & Regulatory Rule Formalisation | `cap.t11.legal.legal_formalisation@1` | pure | 30000 | [spec](docs/PART_SPECS_T11.md#p0544-legal-formalisation) | [txt](prompts/P0544_legal_formalisation.txt) |
| P0545 | `financial_verification` | Financial Model Verification | `cap.t11.financial.financial_verification@1` | pure | 31000 | [spec](docs/PART_SPECS_T11.md#p0545-financial-verification) | [txt](prompts/P0545_financial_verification.txt) |
| P0546 | `verification_cache` | Verified Result Cache | `cap.t11.verification.verification_cache@1` | pure | 32000 | [spec](docs/PART_SPECS_T11.md#p0546-verification-cache) | [txt](prompts/P0546_verification_cache.txt) |
| P0547 | `trust_boundaries` | Trust Boundary & Axiom Auditing | `cap.t11.trust.trust_boundaries@1` | pure | 33000 | [spec](docs/PART_SPECS_T11.md#p0547-trust-boundaries) | [txt](prompts/P0547_trust_boundaries.txt) |
| P0548 | `verification_bench` | Verification Capability Benchmark | `cap.t11.verification.verification_bench@1` | pure | 34000 | [spec](docs/PART_SPECS_T11.md#p0548-verification-bench) | [txt](prompts/P0548_verification_bench.txt) |
| P0549 | `proof_speed` | Verification Latency Engineering | `cap.t11.proof.proof_speed@1` | pure | 35000 | [spec](docs/PART_SPECS_T11.md#p0549-proof-speed) | [txt](prompts/P0549_proof_speed.txt) |
| P0550 | `formal_spec_doc` | Formal Methods Specification & Guarantees Register | `cap.t11.formal.formal_spec_doc@1` | pure | 36000 | [spec](docs/PART_SPECS_T11.md#p0550-formal-spec-doc) | [txt](prompts/P0550_formal_spec_doc.txt) |

## T12 — Code Intelligence & Repository Surgery

*Whole-repository semantic understanding, patch synthesis, test synthesis and root-cause analysis. Owns the SWE/Frontier benchmark family.*

| part | slug | title | capability | det | p99 ns | spec | prompt |
|---|---|---|---|---|---:|---|---|
| P0551 | `repo_index` | Whole-Repository Semantic Index | `cap.t12.repo.repo_index@1` | pure | 37000 | [spec](docs/PART_SPECS_T12.md#p0551-repo-index) | [txt](prompts/P0551_repo_index.txt) |
| P0552 | `code_parsing` | Multi-Language Parsing & Concrete Syntax Trees | `cap.t12.code.code_parsing@1` | pure | 38000 | [spec](docs/PART_SPECS_T12.md#p0552-code-parsing) | [txt](prompts/P0552_code_parsing.txt) |
| P0553 | `semantic_analysis` | Cross-Language Semantic Analysis | `cap.t12.semantic.semantic_analysis@1` | pure | 39000 | [spec](docs/PART_SPECS_T12.md#p0553-semantic-analysis) | [txt](prompts/P0553_semantic_analysis.txt) |
| P0554 | `call_graph` | Call Graph & Dependency Analysis | `cap.t12.call.call_graph@1` | pure | 40000 | [spec](docs/PART_SPECS_T12.md#p0554-call-graph) | [txt](prompts/P0554_call_graph.txt) |
| P0555 | `code_search` | Semantic & Structural Code Search | `cap.t12.code.code_search@1` | pure | 41000 | [spec](docs/PART_SPECS_T12.md#p0555-code-search) | [txt](prompts/P0555_code_search.txt) |
| P0556 | `code_embeddings` | Code Representation & Embeddings | `cap.t12.code.code_embeddings@1` | pure | 42000 | [spec](docs/PART_SPECS_T12.md#p0556-code-embeddings) | [txt](prompts/P0556_code_embeddings.txt) |
| P0557 | `bug_localisation` | Bug Localisation & Root Cause Analysis | `cap.t12.bug.bug_localisation@1` | pure | 43000 | [spec](docs/PART_SPECS_T12.md#p0557-bug-localisation) | [txt](prompts/P0557_bug_localisation.txt) |
| P0558 | `patch_synthesis` | Patch Synthesis Engine | `cap.t12.patch.patch_synthesis@1` | pure | 44000 | [spec](docs/PART_SPECS_T12.md#p0558-patch-synthesis) | [txt](prompts/P0558_patch_synthesis.txt) |
| P0559 | `patch_validation` | Patch Validation & Regression Guarding | `cap.t12.patch.patch_validation@1` | pure | 45000 | [spec](docs/PART_SPECS_T12.md#p0559-patch-validation) | [txt](prompts/P0559_patch_validation.txt) |
| P0560 | `test_synthesis` | Test Generation & Coverage Engineering | `cap.t12.test.test_synthesis@1` | pure | 46000 | [spec](docs/PART_SPECS_T12.md#p0560-test-synthesis) | [txt](prompts/P0560_test_synthesis.txt) |
| P0561 | `mutation_testing` | Mutation Testing & Test Quality Assessment | `cap.t12.mutation.mutation_testing@1` | pure | 47000 | [spec](docs/PART_SPECS_T12.md#p0561-mutation-testing) | [txt](prompts/P0561_mutation_testing.txt) |
| P0562 | `code_review_engine` | Automated Code Review & Hazard Detection | `cap.t12.code.code_review_engine@1` | pure | 48000 | [spec](docs/PART_SPECS_T12.md#p0562-code-review-engine) | [txt](prompts/P0562_code_review_engine.txt) |
| P0563 | `static_analysis` | Static Analysis & Linting Integration | `cap.t12.static.static_analysis@1` | pure | 49000 | [spec](docs/PART_SPECS_T12.md#p0563-static-analysis) | [txt](prompts/P0563_static_analysis.txt) |
| P0564 | `refactoring_engine` | Semantics-Preserving Refactoring Engine | `cap.t12.refactoring.refactoring_engine@1` | pure | 3000 | [spec](docs/PART_SPECS_T12.md#p0564-refactoring-engine) | [txt](prompts/P0564_refactoring_engine.txt) |
| P0565 | `migration_engine` | Large-Scale Migration & Codemod Engine | `cap.t12.migration.migration_engine@1` | pure | 4000 | [spec](docs/PART_SPECS_T12.md#p0565-migration-engine) | [txt](prompts/P0565_migration_engine.txt) |
| P0566 | `api_evolution` | API Compatibility & Breaking Change Analysis | `cap.t12.api.api_evolution@1` | pure | 5000 | [spec](docs/PART_SPECS_T12.md#p0566-api-evolution) | [txt](prompts/P0566_api_evolution.txt) |
| P0567 | `dependency_reasoning` | Dependency & Supply Chain Reasoning | `cap.t12.dependency.dependency_reasoning@1` | pure | 6000 | [spec](docs/PART_SPECS_T12.md#p0567-dependency-reasoning) | [txt](prompts/P0567_dependency_reasoning.txt) |
| P0568 | `build_system` | Build System Understanding & Repair | `cap.t12.build.build_system@1` | pure | 7000 | [spec](docs/PART_SPECS_T12.md#p0568-build-system) | [txt](prompts/P0568_build_system.txt) |
| P0569 | `code_execution_sandbox` | Code Execution & Validation Sandbox | `cap.t12.code.code_execution_sandbox@1` | pure | 8000 | [spec](docs/PART_SPECS_T12.md#p0569-code-execution-sandbox) | [txt](prompts/P0569_code_execution_sandbox.txt) |
| P0570 | `test_orchestration` | Test Selection, Ordering & Parallel Execution | `cap.t12.test.test_orchestration@1` | pure | 9000 | [spec](docs/PART_SPECS_T12.md#p0570-test-orchestration) | [txt](prompts/P0570_test_orchestration.txt) |
| P0571 | `flaky_detection` | Flaky Test Detection & Stabilisation | `cap.t12.flaky.flaky_detection@1` | pure | 10000 | [spec](docs/PART_SPECS_T12.md#p0571-flaky-detection) | [txt](prompts/P0571_flaky_detection.txt) |
| P0572 | `performance_engineering` | Performance Profiling & Optimisation Agent | `cap.t12.performance.performance_engineering@1` | pure | 11000 | [spec](docs/PART_SPECS_T12.md#p0572-performance-engineering) | [txt](prompts/P0572_performance_engineering.txt) |
| P0573 | `concurrency_bugs` | Concurrency Bug Detection & Repair | `cap.t12.concurrency.concurrency_bugs@1` | pure | 12000 | [spec](docs/PART_SPECS_T12.md#p0573-concurrency-bugs) | [txt](prompts/P0573_concurrency_bugs.txt) |
| P0574 | `memory_safety` | Memory Safety & Resource Leak Analysis | `cap.t12.memory.memory_safety@1` | pure | 13000 | [spec](docs/PART_SPECS_T12.md#p0574-memory-safety) | [txt](prompts/P0574_memory_safety.txt) |
| P0575 | `security_code_analysis` | Security Vulnerability Discovery | `cap.t12.security.security_code_analysis@1` | pure | 14000 | [spec](docs/PART_SPECS_T12.md#p0575-security-code-analysis) | [txt](prompts/P0575_security_code_analysis.txt) |
| P0576 | `fuzzing_agent` | Fuzzing Campaign Orchestration | `cap.t12.fuzzing.fuzzing_agent@1` | pure | 15000 | [spec](docs/PART_SPECS_T12.md#p0576-fuzzing-agent) | [txt](prompts/P0576_fuzzing_agent.txt) |
| P0577 | `crash_triage` | Crash Triage & Deduplication | `cap.t12.crash.crash_triage@1` | pure | 16000 | [spec](docs/PART_SPECS_T12.md#p0577-crash-triage) | [txt](prompts/P0577_crash_triage.txt) |
| P0578 | `code_generation_core` | Production Code Generation Engine | `cap.t12.code.code_generation_core@1` | pure | 17000 | [spec](docs/PART_SPECS_T12.md#p0578-code-generation-core) | [txt](prompts/P0578_code_generation_core.txt) |
| P0579 | `architecture_design` | Software Architecture Design & Review | `cap.t12.architecture.architecture_design@1` | pure | 18000 | [spec](docs/PART_SPECS_T12.md#p0579-architecture-design) | [txt](prompts/P0579_architecture_design.txt) |
| P0580 | `legacy_comprehension` | Legacy Code Comprehension | `cap.t12.legacy.legacy_comprehension@1` | pure | 19000 | [spec](docs/PART_SPECS_T12.md#p0580-legacy-comprehension) | [txt](prompts/P0580_legacy_comprehension.txt) |
| P0581 | `code_documentation` | Documentation Generation & Maintenance | `cap.t12.code.code_documentation@1` | pure | 20000 | [spec](docs/PART_SPECS_T12.md#p0581-code-documentation) | [txt](prompts/P0581_code_documentation.txt) |
| P0582 | `commit_history` | Version History Analysis & Blame Reasoning | `cap.t12.commit.commit_history@1` | pure | 21000 | [spec](docs/PART_SPECS_T12.md#p0582-commit-history) | [txt](prompts/P0582_commit_history.txt) |
| P0583 | `pr_workflow` | Pull Request Authoring & Review Workflow | `cap.t12.pr.pr_workflow@1` | pure | 22000 | [spec](docs/PART_SPECS_T12.md#p0583-pr-workflow) | [txt](prompts/P0583_pr_workflow.txt) |
| P0584 | `multi_repo` | Cross-Repository & Monorepo Coordination | `cap.t12.multi.multi_repo@1` | pure | 23000 | [spec](docs/PART_SPECS_T12.md#p0584-multi-repo) | [txt](prompts/P0584_multi_repo.txt) |
| P0585 | `environment_setup` | Development Environment Reconstruction | `cap.t12.environment.environment_setup@1` | pure | 24000 | [spec](docs/PART_SPECS_T12.md#p0585-environment-setup) | [txt](prompts/P0585_environment_setup.txt) |
| P0586 | `debugger_agent` | Interactive Debugging Agent | `cap.t12.debugger.debugger_agent@1` | pure | 25000 | [spec](docs/PART_SPECS_T12.md#p0586-debugger-agent) | [txt](prompts/P0586_debugger_agent.txt) |
| P0587 | `observability_agent` | Production Debugging from Telemetry | `cap.t12.observability.observability_agent@1` | pure | 26000 | [spec](docs/PART_SPECS_T12.md#p0587-observability-agent) | [txt](prompts/P0587_observability_agent.txt) |
| P0588 | `data_pipeline_code` | Data & ML Pipeline Engineering | `cap.t12.data.data_pipeline_code@1` | pure | 27000 | [spec](docs/PART_SPECS_T12.md#p0588-data-pipeline-code) | [txt](prompts/P0588_data_pipeline_code.txt) |
| P0589 | `notebook_engineering` | Notebook & Exploratory Code Quality | `cap.t12.notebook.notebook_engineering@1` | pure | 28000 | [spec](docs/PART_SPECS_T12.md#p0589-notebook-engineering) | [txt](prompts/P0589_notebook_engineering.txt) |
| P0590 | `frontend_engineering` | Frontend & UI Code Engineering | `cap.t12.frontend.frontend_engineering@1` | pure | 29000 | [spec](docs/PART_SPECS_T12.md#p0590-frontend-engineering) | [txt](prompts/P0590_frontend_engineering.txt) |
| P0591 | `systems_programming` | Systems & Low-Level Code Engineering | `cap.t12.systems.systems_programming@1` | pure | 30000 | [spec](docs/PART_SPECS_T12.md#p0591-systems-programming) | [txt](prompts/P0591_systems_programming.txt) |
| P0592 | `scientific_computing_code` | Scientific & Numerical Code Engineering | `cap.t12.scientific.scientific_computing_code@1` | pure | 31000 | [spec](docs/PART_SPECS_T12.md#p0592-scientific-computing-code) | [txt](prompts/P0592_scientific_computing_code.txt) |
| P0593 | `competitive_programming` | Algorithmic Problem Solving Engine | `cap.t12.competitive.competitive_programming@1` | pure | 32000 | [spec](docs/PART_SPECS_T12.md#p0593-competitive-programming) | [txt](prompts/P0593_competitive_programming.txt) |
| P0594 | `code_translation` | Cross-Language Code Translation | `cap.t12.code.code_translation@1` | pure | 33000 | [spec](docs/PART_SPECS_T12.md#p0594-code-translation) | [txt](prompts/P0594_code_translation.txt) |
| P0595 | `codebase_metrics` | Codebase Health Metrics & Technical Debt | `cap.t12.codebase.codebase_metrics@1` | pure | 34000 | [spec](docs/PART_SPECS_T12.md#p0595-codebase-metrics) | [txt](prompts/P0595_codebase_metrics.txt) |
| P0596 | `swe_bench_harness` | SWE-bench Family Harness | `cap.t12.swe.swe_bench_harness@1` | pure | 35000 | [spec](docs/PART_SPECS_T12.md#p0596-swe-bench-harness) | [txt](prompts/P0596_swe_bench_harness.txt) |
| P0597 | `frontier_bench_harness` | Frontier-Bench & Terminal Coding Harness | `cap.t12.frontier.frontier_bench_harness@1` | pure | 36000 | [spec](docs/PART_SPECS_T12.md#p0597-frontier-bench-harness) | [txt](prompts/P0597_frontier_bench_harness.txt) |
| P0598 | `cursorbench_harness` | IDE-Integrated Coding Evaluation | `cap.t12.cursorbench.cursorbench_harness@1` | pure | 37000 | [spec](docs/PART_SPECS_T12.md#p0598-cursorbench-harness) | [txt](prompts/P0598_cursorbench_harness.txt) |
| P0599 | `code_quality_gate` | Code Quality Gate for the 1000-Part Assembly | `cap.t12.code.code_quality_gate@1` | pure | 38000 | [spec](docs/PART_SPECS_T12.md#p0599-code-quality-gate) | [txt](prompts/P0599_code_quality_gate.txt) |
| P0600 | `code_spec_doc` | Code Intelligence Specification & Capability Register | `cap.t12.code.code_spec_doc@1` | pure | 39000 | [spec](docs/PART_SPECS_T12.md#p0600-code-spec-doc) | [txt](prompts/P0600_code_spec_doc.txt) |

## T13 — Agents, Tool Use & Computer Control

*Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.*

| part | slug | title | capability | det | p99 ns | spec | prompt |
|---|---|---|---|---|---:|---|---|
| P0601 | `agent_loop` | Core Agent Execution Loop | `cap.t13.agent.agent_loop@1` | io | 40000 | [spec](docs/PART_SPECS_T13.md#p0601-agent-loop) | [txt](prompts/P0601_agent_loop.txt) |
| P0602 | `tool_protocol` | Tool Definition & Invocation Protocol | `cap.t13.tool.tool_protocol@1` | io | 41000 | [spec](docs/PART_SPECS_T13.md#p0602-tool-protocol) | [txt](prompts/P0602_tool_protocol.txt) |
| P0603 | `tool_selection` | Tool Selection & Discovery | `cap.t13.tool.tool_selection@1` | io | 42000 | [spec](docs/PART_SPECS_T13.md#p0603-tool-selection) | [txt](prompts/P0603_tool_selection.txt) |
| P0604 | `tool_composition` | Tool Chaining & Composition Planner | `cap.t13.tool.tool_composition@1` | io | 43000 | [spec](docs/PART_SPECS_T13.md#p0604-tool-composition) | [txt](prompts/P0604_tool_composition.txt) |
| P0605 | `mid_conversation_tools` | Dynamic Tool Set Management | `cap.t13.mid.mid_conversation_tools@1` | io | 44000 | [spec](docs/PART_SPECS_T13.md#p0605-mid-conversation-tools) | [txt](prompts/P0605_mid_conversation_tools.txt) |
| P0606 | `terminal_agent` | Terminal & Shell Operation Agent | `cap.t13.terminal.terminal_agent@1` | io | 45000 | [spec](docs/PART_SPECS_T13.md#p0606-terminal-agent) | [txt](prompts/P0606_terminal_agent.txt) |
| P0607 | `filesystem_agent` | Filesystem Navigation & Manipulation | `cap.t13.filesystem.filesystem_agent@1` | io | 46000 | [spec](docs/PART_SPECS_T13.md#p0607-filesystem-agent) | [txt](prompts/P0607_filesystem_agent.txt) |
| P0608 | `browser_agent` | Web Browser Automation Agent | `cap.t13.browser.browser_agent@1` | io | 47000 | [spec](docs/PART_SPECS_T13.md#p0608-browser-agent) | [txt](prompts/P0608_browser_agent.txt) |
| P0609 | `web_research` | Deep Web Research Agent | `cap.t13.web.web_research@1` | io | 48000 | [spec](docs/PART_SPECS_T13.md#p0609-web-research) | [txt](prompts/P0609_web_research.txt) |
| P0610 | `computer_use_agent` | Desktop Computer Use Agent | `cap.t13.computer.computer_use_agent@1` | io | 49000 | [spec](docs/PART_SPECS_T13.md#p0610-computer-use-agent) | [txt](prompts/P0610_computer_use_agent.txt) |
| P0611 | `gui_grounding` | GUI Element Grounding & Interaction | `cap.t13.gui.gui_grounding@1` | io | 3000 | [spec](docs/PART_SPECS_T13.md#p0611-gui-grounding) | [txt](prompts/P0611_gui_grounding.txt) |
| P0612 | `mobile_agent` | Mobile Device Automation | `cap.t13.mobile.mobile_agent@1` | io | 4000 | [spec](docs/PART_SPECS_T13.md#p0612-mobile-agent) | [txt](prompts/P0612_mobile_agent.txt) |
| P0613 | `api_agent` | REST/GraphQL API Integration Agent | `cap.t13.api.api_agent@1` | io | 5000 | [spec](docs/PART_SPECS_T13.md#p0613-api-agent) | [txt](prompts/P0613_api_agent.txt) |
| P0614 | `database_agent` | Database Query & Administration Agent | `cap.t13.database.database_agent@1` | io | 6000 | [spec](docs/PART_SPECS_T13.md#p0614-database-agent) | [txt](prompts/P0614_database_agent.txt) |
| P0615 | `business_automation` | Business Workflow Automation Agent | `cap.t13.business.business_automation@1` | io | 7000 | [spec](docs/PART_SPECS_T13.md#p0615-business-automation) | [txt](prompts/P0615_business_automation.txt) |
| P0616 | `spreadsheet_agent` | Spreadsheet & Tabular Data Agent | `cap.t13.spreadsheet.spreadsheet_agent@1` | io | 8000 | [spec](docs/PART_SPECS_T13.md#p0616-spreadsheet-agent) | [txt](prompts/P0616_spreadsheet_agent.txt) |
| P0617 | `document_workflow` | Document Processing Workflow Agent | `cap.t13.document.document_workflow@1` | io | 9000 | [spec](docs/PART_SPECS_T13.md#p0617-document-workflow) | [txt](prompts/P0617_document_workflow.txt) |
| P0618 | `email_communication` | Communication & Correspondence Agent | `cap.t13.email.email_communication@1` | io | 10000 | [spec](docs/PART_SPECS_T13.md#p0618-email-communication) | [txt](prompts/P0618_email_communication.txt) |
| P0619 | `scheduling_agent` | Calendar & Coordination Agent | `cap.t13.scheduling.scheduling_agent@1` | io | 11000 | [spec](docs/PART_SPECS_T13.md#p0619-scheduling-agent) | [txt](prompts/P0619_scheduling_agent.txt) |
| P0620 | `multi_agent_orchestration` | Multi-Agent Orchestration Framework | `cap.t13.multi.multi_agent_orchestration@1` | io | 12000 | [spec](docs/PART_SPECS_T13.md#p0620-multi-agent-orchestration) | [txt](prompts/P0620_multi_agent_orchestration.txt) |
| P0621 | `agent_communication` | Inter-Agent Communication Protocol | `cap.t13.agent.agent_communication@1` | io | 13000 | [spec](docs/PART_SPECS_T13.md#p0621-agent-communication) | [txt](prompts/P0621_agent_communication.txt) |
| P0622 | `agent_delegation` | Task Delegation & Subagent Spawning | `cap.t13.agent.agent_delegation@1` | io | 14000 | [spec](docs/PART_SPECS_T13.md#p0622-agent-delegation) | [txt](prompts/P0622_agent_delegation.txt) |
| P0623 | `agent_supervision` | Agent Supervision & Intervention | `cap.t13.agent.agent_supervision@1` | io | 15000 | [spec](docs/PART_SPECS_T13.md#p0623-agent-supervision) | [txt](prompts/P0623_agent_supervision.txt) |
| P0624 | `consensus_agents` | Multi-Agent Consensus & Conflict Resolution | `cap.t13.consensus.consensus_agents@1` | io | 16000 | [spec](docs/PART_SPECS_T13.md#p0624-consensus-agents) | [txt](prompts/P0624_consensus_agents.txt) |
| P0625 | `environment_model` | Environment State Modelling & Prediction | `cap.t13.environment.environment_model@1` | io | 17000 | [spec](docs/PART_SPECS_T13.md#p0625-environment-model) | [txt](prompts/P0625_environment_model.txt) |
| P0626 | `action_verification` | Post-Action Verification Loop | `cap.t13.action.action_verification@1` | io | 18000 | [spec](docs/PART_SPECS_T13.md#p0626-action-verification) | [txt](prompts/P0626_action_verification.txt) |
| P0627 | `error_recovery_agent` | Failure Recovery & Adaptation | `cap.t13.error.error_recovery_agent@1` | io | 19000 | [spec](docs/PART_SPECS_T13.md#p0627-error-recovery-agent) | [txt](prompts/P0627_error_recovery_agent.txt) |
| P0628 | `long_horizon_memory` | Long-Horizon Task Memory | `cap.t13.long.long_horizon_memory@1` | io | 20000 | [spec](docs/PART_SPECS_T13.md#p0628-long-horizon-memory) | [txt](prompts/P0628_long_horizon_memory.txt) |
| P0629 | `progress_tracking` | Progress Estimation & Reporting | `cap.t13.progress.progress_tracking@1` | io | 21000 | [spec](docs/PART_SPECS_T13.md#p0629-progress-tracking) | [txt](prompts/P0629_progress_tracking.txt) |
| P0630 | `human_in_loop` | Human Handoff & Approval Workflow | `cap.t13.human.human_in_loop@1` | io | 22000 | [spec](docs/PART_SPECS_T13.md#p0630-human-in-loop) | [txt](prompts/P0630_human_in_loop.txt) |
| P0631 | `agent_safety_gate` | Agent Action Safety Gate | `cap.t13.agent.agent_safety_gate@1` | io | 23000 | [spec](docs/PART_SPECS_T13.md#p0631-agent-safety-gate) | [txt](prompts/P0631_agent_safety_gate.txt) |
| P0632 | `credential_management` | Credential & Permission Management | `cap.t13.credential.credential_management@1` | io | 24000 | [spec](docs/PART_SPECS_T13.md#p0632-credential-management) | [txt](prompts/P0632_credential_management.txt) |
| P0633 | `cost_control_agent` | Agent Cost Governance | `cap.t13.cost.cost_control_agent@1` | io | 25000 | [spec](docs/PART_SPECS_T13.md#p0633-cost-control-agent) | [txt](prompts/P0633_cost_control_agent.txt) |
| P0634 | `sandbox_execution` | Agent Sandbox & Isolation Runtime | `cap.t13.sandbox.sandbox_execution@1` | io | 26000 | [spec](docs/PART_SPECS_T13.md#p0634-sandbox-execution) | [txt](prompts/P0634_sandbox_execution.txt) |
| P0635 | `tool_creation` | Dynamic Tool Creation | `cap.t13.tool.tool_creation@1` | io | 27000 | [spec](docs/PART_SPECS_T13.md#p0635-tool-creation) | [txt](prompts/P0635_tool_creation.txt) |
| P0636 | `workflow_learning` | Workflow Learning & Skill Acquisition | `cap.t13.workflow.workflow_learning@1` | io | 28000 | [spec](docs/PART_SPECS_T13.md#p0636-workflow-learning) | [txt](prompts/P0636_workflow_learning.txt) |
| P0637 | `observation_compression` | Observation Compression & Attention | `cap.t13.observation.observation_compression@1` | io | 29000 | [spec](docs/PART_SPECS_T13.md#p0637-observation-compression) | [txt](prompts/P0637_observation_compression.txt) |
| P0638 | `agent_determinism` | Reproducible Agent Execution | `cap.t13.agent.agent_determinism@1` | io | 30000 | [spec](docs/PART_SPECS_T13.md#p0638-agent-determinism) | [txt](prompts/P0638_agent_determinism.txt) |
| P0639 | `agent_eval_harness` | Agent Benchmark Harness | `cap.t13.agent.agent_eval_harness@1` | io | 31000 | [spec](docs/PART_SPECS_T13.md#p0639-agent-eval-harness) | [txt](prompts/P0639_agent_eval_harness.txt) |
| P0640 | `trajectory_analysis` | Trajectory Analysis & Improvement Mining | `cap.t13.trajectory.trajectory_analysis@1` | io | 32000 | [spec](docs/PART_SPECS_T13.md#p0640-trajectory-analysis) | [txt](prompts/P0640_trajectory_analysis.txt) |
| P0641 | `agent_interruption` | Interruption, Steering & Course Correction | `cap.t13.agent.agent_interruption@1` | io | 33000 | [spec](docs/PART_SPECS_T13.md#p0641-agent-interruption) | [txt](prompts/P0641_agent_interruption.txt) |
| P0642 | `simulation_env` | Agent Training & Testing Environments | `cap.t13.simulation.simulation_env@1` | io | 34000 | [spec](docs/PART_SPECS_T13.md#p0642-simulation-env) | [txt](prompts/P0642_simulation_env.txt) |
| P0643 | `robotics_bridge` | Physical Actuation Interface | `cap.t13.robotics.robotics_bridge@1` | io | 35000 | [spec](docs/PART_SPECS_T13.md#p0643-robotics-bridge) | [txt](prompts/P0643_robotics_bridge.txt) |
| P0644 | `iot_control` | Device & Infrastructure Control Agent | `cap.t13.iot.iot_control@1` | io | 36000 | [spec](docs/PART_SPECS_T13.md#p0644-iot-control) | [txt](prompts/P0644_iot_control.txt) |
| P0645 | `scientific_agent` | Autonomous Research Agent | `cap.t13.scientific.scientific_agent@1` | io | 37000 | [spec](docs/PART_SPECS_T13.md#p0645-scientific-agent) | [txt](prompts/P0645_scientific_agent.txt) |
| P0646 | `data_analysis_agent` | Autonomous Data Analysis Agent | `cap.t13.data.data_analysis_agent@1` | io | 38000 | [spec](docs/PART_SPECS_T13.md#p0646-data-analysis-agent) | [txt](prompts/P0646_data_analysis_agent.txt) |
| P0647 | `agent_ux` | Agent Transparency & Explainability | `cap.t13.agent.agent_ux@1` | io | 39000 | [spec](docs/PART_SPECS_T13.md#p0647-agent-ux) | [txt](prompts/P0647_agent_ux.txt) |
| P0648 | `agent_speed` | Agent Latency Engineering | `cap.t13.agent.agent_speed@1` | io | 40000 | [spec](docs/PART_SPECS_T13.md#p0648-agent-speed) | [txt](prompts/P0648_agent_speed.txt) |
| P0649 | `agent_scaling` | 1000-Agent Scale Coordination | `cap.t13.agent.agent_scaling@1` | io | 41000 | [spec](docs/PART_SPECS_T13.md#p0649-agent-scaling) | [txt](prompts/P0649_agent_scaling.txt) |
| P0650 | `agent_spec_doc` | Agent Subsystem Specification & Runbook | `cap.t13.agent.agent_spec_doc@1` | io | 42000 | [spec](docs/PART_SPECS_T13.md#p0650-agent-spec-doc) | [txt](prompts/P0650_agent_spec_doc.txt) |

## T14 — Multimodal Perception & Grounding

*Vision, video, audio, 3D, documents, charts and scientific instrument data fused into one grounded latent space.*

| part | slug | title | capability | det | p99 ns | spec | prompt |
|---|---|---|---|---|---:|---|---|
| P0651 | `image_encoder` | High-Resolution Image Encoder | `cap.t14.image.image_encoder@1` | seeded | 43000 | [spec](docs/PART_SPECS_T14.md#p0651-image-encoder) | [txt](prompts/P0651_image_encoder.txt) |
| P0652 | `vision_tokenisation` | Visual Token Compression & Selection | `cap.t14.vision.vision_tokenisation@1` | seeded | 44000 | [spec](docs/PART_SPECS_T14.md#p0652-vision-tokenisation) | [txt](prompts/P0652_vision_tokenisation.txt) |
| P0653 | `ocr_engine` | Text Recognition & Document OCR | `cap.t14.ocr.ocr_engine@1` | seeded | 45000 | [spec](docs/PART_SPECS_T14.md#p0653-ocr-engine) | [txt](prompts/P0653_ocr_engine.txt) |
| P0654 | `document_layout` | Document Layout Analysis & Structure Extraction | `cap.t14.document.document_layout@1` | seeded | 46000 | [spec](docs/PART_SPECS_T14.md#p0654-document-layout) | [txt](prompts/P0654_document_layout.txt) |
| P0655 | `table_extraction` | Table Detection & Structured Extraction | `cap.t14.table.table_extraction@1` | seeded | 47000 | [spec](docs/PART_SPECS_T14.md#p0655-table-extraction) | [txt](prompts/P0655_table_extraction.txt) |
| P0656 | `chart_understanding` | Chart & Diagram Comprehension | `cap.t14.chart.chart_understanding@1` | seeded | 48000 | [spec](docs/PART_SPECS_T14.md#p0656-chart-understanding) | [txt](prompts/P0656_chart_understanding.txt) |
| P0657 | `visual_grounding` | Visual Grounding & Referring Expressions | `cap.t14.visual.visual_grounding@1` | seeded | 49000 | [spec](docs/PART_SPECS_T14.md#p0657-visual-grounding) | [txt](prompts/P0657_visual_grounding.txt) |
| P0658 | `scene_graph` | Scene Understanding & Relation Extraction | `cap.t14.scene.scene_graph@1` | seeded | 3000 | [spec](docs/PART_SPECS_T14.md#p0658-scene-graph) | [txt](prompts/P0658_scene_graph.txt) |
| P0659 | `visual_reasoning` | Visual Reasoning & Puzzle Solving | `cap.t14.visual.visual_reasoning@1` | seeded | 4000 | [spec](docs/PART_SPECS_T14.md#p0659-visual-reasoning) | [txt](prompts/P0659_visual_reasoning.txt) |
| P0660 | `image_geometry` | 3D Geometry & Depth Reasoning from Images | `cap.t14.image.image_geometry@1` | seeded | 5000 | [spec](docs/PART_SPECS_T14.md#p0660-image-geometry) | [txt](prompts/P0660_image_geometry.txt) |
| P0661 | `cad_understanding` | Engineering Drawing & CAD Comprehension | `cap.t14.cad.cad_understanding@1` | seeded | 6000 | [spec](docs/PART_SPECS_T14.md#p0661-cad-understanding) | [txt](prompts/P0661_cad_understanding.txt) |
| P0662 | `video_encoder` | Long Video Understanding | `cap.t14.video.video_encoder@1` | seeded | 7000 | [spec](docs/PART_SPECS_T14.md#p0662-video-encoder) | [txt](prompts/P0662_video_encoder.txt) |
| P0663 | `temporal_video` | Temporal Reasoning & Event Detection in Video | `cap.t14.temporal.temporal_video@1` | seeded | 8000 | [spec](docs/PART_SPECS_T14.md#p0663-temporal-video) | [txt](prompts/P0663_temporal_video.txt) |
| P0664 | `video_tracking` | Object Tracking & Identity Persistence | `cap.t14.video.video_tracking@1` | seeded | 9000 | [spec](docs/PART_SPECS_T14.md#p0664-video-tracking) | [txt](prompts/P0664_video_tracking.txt) |
| P0665 | `audio_encoder` | Audio Encoding & Representation | `cap.t14.audio.audio_encoder@1` | seeded | 10000 | [spec](docs/PART_SPECS_T14.md#p0665-audio-encoder) | [txt](prompts/P0665_audio_encoder.txt) |
| P0666 | `speech_recognition` | Speech Recognition & Diarisation | `cap.t14.speech.speech_recognition@1` | seeded | 11000 | [spec](docs/PART_SPECS_T14.md#p0666-speech-recognition) | [txt](prompts/P0666_speech_recognition.txt) |
| P0667 | `prosody_paralinguistic` | Prosody & Paralinguistic Understanding | `cap.t14.prosody.prosody_paralinguistic@1` | seeded | 12000 | [spec](docs/PART_SPECS_T14.md#p0667-prosody-paralinguistic) | [txt](prompts/P0667_prosody_paralinguistic.txt) |
| P0668 | `music_understanding` | Music Analysis & Understanding | `cap.t14.music.music_understanding@1` | seeded | 13000 | [spec](docs/PART_SPECS_T14.md#p0668-music-understanding) | [txt](prompts/P0668_music_understanding.txt) |
| P0669 | `audio_events` | Environmental & Machine Audio Analysis | `cap.t14.audio.audio_events@1` | seeded | 14000 | [spec](docs/PART_SPECS_T14.md#p0669-audio-events) | [txt](prompts/P0669_audio_events.txt) |
| P0670 | `multimodal_alignment` | Cross-Modal Alignment & Fusion | `cap.t14.multimodal.multimodal_alignment@1` | seeded | 15000 | [spec](docs/PART_SPECS_T14.md#p0670-multimodal-alignment) | [txt](prompts/P0670_multimodal_alignment.txt) |
| P0671 | `modality_translation` | Cross-Modal Translation & Description | `cap.t14.modality.modality_translation@1` | seeded | 16000 | [spec](docs/PART_SPECS_T14.md#p0671-modality-translation) | [txt](prompts/P0671_modality_translation.txt) |
| P0672 | `visual_hallucination` | Visual Hallucination Detection & Prevention | `cap.t14.visual.visual_hallucination@1` | seeded | 17000 | [spec](docs/PART_SPECS_T14.md#p0672-visual-hallucination) | [txt](prompts/P0672_visual_hallucination.txt) |
| P0673 | `scientific_imaging` | Scientific Image & Instrument Data Analysis | `cap.t14.scientific.scientific_imaging@1` | seeded | 18000 | [spec](docs/PART_SPECS_T14.md#p0673-scientific-imaging) | [txt](prompts/P0673_scientific_imaging.txt) |
| P0674 | `medical_imaging` | Medical Image Interpretation Support | `cap.t14.medical.medical_imaging@1` | seeded | 19000 | [spec](docs/PART_SPECS_T14.md#p0674-medical-imaging) | [txt](prompts/P0674_medical_imaging.txt) |
| P0675 | `satellite_geospatial` | Geospatial & Remote Sensing Analysis | `cap.t14.satellite.satellite_geospatial@1` | seeded | 20000 | [spec](docs/PART_SPECS_T14.md#p0675-satellite-geospatial) | [txt](prompts/P0675_satellite_geospatial.txt) |
| P0676 | `ui_screenshot` | UI Screenshot Understanding | `cap.t14.ui.ui_screenshot@1` | seeded | 21000 | [spec](docs/PART_SPECS_T14.md#p0676-ui-screenshot) | [txt](prompts/P0676_ui_screenshot.txt) |
| P0677 | `handwriting_sketch` | Handwriting & Sketch Understanding | `cap.t14.handwriting.handwriting_sketch@1` | seeded | 22000 | [spec](docs/PART_SPECS_T14.md#p0677-handwriting-sketch) | [txt](prompts/P0677_handwriting_sketch.txt) |
| P0678 | `math_formula_vision` | Mathematical Notation Recognition | `cap.t14.math.math_formula_vision@1` | seeded | 23000 | [spec](docs/PART_SPECS_T14.md#p0678-math-formula-vision) | [txt](prompts/P0678_math_formula_vision.txt) |
| P0679 | `code_screenshot` | Code and Terminal Image Understanding | `cap.t14.code.code_screenshot@1` | seeded | 24000 | [spec](docs/PART_SPECS_T14.md#p0679-code-screenshot) | [txt](prompts/P0679_code_screenshot.txt) |
| P0680 | `multimodal_context` | Multimodal Context Management | `cap.t14.multimodal.multimodal_context@1` | seeded | 25000 | [spec](docs/PART_SPECS_T14.md#p0680-multimodal-context) | [txt](prompts/P0680_multimodal_context.txt) |
| P0681 | `perception_uncertainty` | Perceptual Uncertainty & Verification | `cap.t14.perception.perception_uncertainty@1` | seeded | 26000 | [spec](docs/PART_SPECS_T14.md#p0681-perception-uncertainty) | [txt](prompts/P0681_perception_uncertainty.txt) |
| P0682 | `perception_robustness` | Perception Robustness & Adversarial Defence | `cap.t14.perception.perception_robustness@1` | seeded | 27000 | [spec](docs/PART_SPECS_T14.md#p0682-perception-robustness) | [txt](prompts/P0682_perception_robustness.txt) |
| P0683 | `prompt_injection_visual` | Visual & Audio Prompt Injection Defence | `cap.t14.prompt.prompt_injection_visual@1` | seeded | 28000 | [spec](docs/PART_SPECS_T14.md#p0683-prompt-injection-visual) | [txt](prompts/P0683_prompt_injection_visual.txt) |
| P0684 | `sensor_fusion` | Multi-Sensor Fusion & Time Alignment | `cap.t14.sensor.sensor_fusion@1` | seeded | 29000 | [spec](docs/PART_SPECS_T14.md#p0684-sensor-fusion) | [txt](prompts/P0684_sensor_fusion.txt) |
| P0685 | `realtime_perception` | Real-Time Streaming Perception | `cap.t14.realtime.realtime_perception@1` | seeded | 30000 | [spec](docs/PART_SPECS_T14.md#p0685-realtime-perception) | [txt](prompts/P0685_realtime_perception.txt) |
| P0686 | `perception_grounding_world` | Perception-to-World-Model Grounding | `cap.t14.perception.perception_grounding_world@1` | seeded | 31000 | [spec](docs/PART_SPECS_T14.md#p0686-perception-grounding-world) | [txt](prompts/P0686_perception_grounding_world.txt) |
| P0687 | `visual_search` | Visual Search & Image Retrieval | `cap.t14.visual.visual_search@1` | seeded | 32000 | [spec](docs/PART_SPECS_T14.md#p0687-visual-search) | [txt](prompts/P0687_visual_search.txt) |
| P0688 | `multimodal_memory_perception` | Perceptual Memory & Recall | `cap.t14.multimodal.multimodal_memory_perception@1` | seeded | 33000 | [spec](docs/PART_SPECS_T14.md#p0688-multimodal-memory-perception) | [txt](prompts/P0688_multimodal_memory_perception.txt) |
| P0689 | `accessibility_perception` | Accessibility-Oriented Perception | `cap.t14.accessibility.accessibility_perception@1` | seeded | 34000 | [spec](docs/PART_SPECS_T14.md#p0689-accessibility-perception) | [txt](prompts/P0689_accessibility_perception.txt) |
| P0690 | `perception_multilingual` | Multilingual Visual Text Understanding | `cap.t14.perception.perception_multilingual@1` | seeded | 35000 | [spec](docs/PART_SPECS_T14.md#p0690-perception-multilingual) | [txt](prompts/P0690_perception_multilingual.txt) |
| P0691 | `data_extraction_pipeline` | Bulk Document Data Extraction Pipeline | `cap.t14.data.data_extraction_pipeline@1` | seeded | 36000 | [spec](docs/PART_SPECS_T14.md#p0691-data-extraction-pipeline) | [txt](prompts/P0691_data_extraction_pipeline.txt) |
| P0692 | `form_understanding` | Form & Structured Document Understanding | `cap.t14.form.form_understanding@1` | seeded | 37000 | [spec](docs/PART_SPECS_T14.md#p0692-form-understanding) | [txt](prompts/P0692_form_understanding.txt) |
| P0693 | `receipt_finance_docs` | Financial Document Understanding | `cap.t14.receipt.receipt_finance_docs@1` | seeded | 38000 | [spec](docs/PART_SPECS_T14.md#p0693-receipt-finance-docs) | [txt](prompts/P0693_receipt_finance_docs.txt) |
| P0694 | `legal_docs_vision` | Legal Document Structure Understanding | `cap.t14.legal.legal_docs_vision@1` | seeded | 39000 | [spec](docs/PART_SPECS_T14.md#p0694-legal-docs-vision) | [txt](prompts/P0694_legal_docs_vision.txt) |
| P0695 | `perception_speed` | Perception Latency & Cost Optimisation | `cap.t14.perception.perception_speed@1` | seeded | 40000 | [spec](docs/PART_SPECS_T14.md#p0695-perception-speed) | [txt](prompts/P0695_perception_speed.txt) |
| P0696 | `perception_distillation` | Perception Model Distillation | `cap.t14.perception.perception_distillation@1` | seeded | 41000 | [spec](docs/PART_SPECS_T14.md#p0696-perception-distillation) | [txt](prompts/P0696_perception_distillation.txt) |
| P0697 | `perception_eval_harness` | Multimodal Benchmark Harness | `cap.t14.perception.perception_eval_harness@1` | seeded | 42000 | [spec](docs/PART_SPECS_T14.md#p0697-perception-eval-harness) | [txt](prompts/P0697_perception_eval_harness.txt) |
| P0698 | `synthetic_perception_data` | Synthetic Perception Data Generation | `cap.t14.synthetic.synthetic_perception_data@1` | seeded | 43000 | [spec](docs/PART_SPECS_T14.md#p0698-synthetic-perception-data) | [txt](prompts/P0698_synthetic_perception_data.txt) |
| P0699 | `perception_interpretability` | Perception Interpretability & Attribution | `cap.t14.perception.perception_interpretability@1` | seeded | 44000 | [spec](docs/PART_SPECS_T14.md#p0699-perception-interpretability) | [txt](prompts/P0699_perception_interpretability.txt) |
| P0700 | `perception_spec_doc` | Perception Subsystem Specification | `cap.t14.perception.perception_spec_doc@1` | seeded | 45000 | [spec](docs/PART_SPECS_T14.md#p0700-perception-spec-doc) | [txt](prompts/P0700_perception_spec_doc.txt) |

## T15 — Generation, Artifacts & Interface Craft

*Every output modality a knowledge worker ships: code, docs, decks, UIs, 3D, video, audio, and the taste model that judges them.*

| part | slug | title | capability | det | p99 ns | spec | prompt |
|---|---|---|---|---|---:|---|---|
| P0701 | `artifact_model` | Artifact Data Model & Lifecycle | `cap.t15.artifact.artifact_model@1` | seeded | 46000 | [spec](docs/PART_SPECS_T15.md#p0701-artifact-model) | [txt](prompts/P0701_artifact_model.txt) |
| P0702 | `text_generation_quality` | Long-Form Text Generation Engine | `cap.t15.text.text_generation_quality@1` | seeded | 47000 | [spec](docs/PART_SPECS_T15.md#p0702-text-generation-quality) | [txt](prompts/P0702_text_generation_quality.txt) |
| P0703 | `style_control` | Style, Tone & Register Control | `cap.t15.style.style_control@1` | seeded | 48000 | [spec](docs/PART_SPECS_T15.md#p0703-style-control) | [txt](prompts/P0703_style_control.txt) |
| P0704 | `conciseness_engine` | Conciseness & Information Density Optimiser | `cap.t15.conciseness.conciseness_engine@1` | seeded | 49000 | [spec](docs/PART_SPECS_T15.md#p0704-conciseness-engine) | [txt](prompts/P0704_conciseness_engine.txt) |
| P0705 | `markdown_rich_text` | Structured Text & Markup Rendering | `cap.t15.markdown.markdown_rich_text@1` | seeded | 3000 | [spec](docs/PART_SPECS_T15.md#p0705-markdown-rich-text) | [txt](prompts/P0705_markdown_rich_text.txt) |
| P0706 | `code_artifact_gen` | Code Artifact Generation & Packaging | `cap.t15.code.code_artifact_gen@1` | seeded | 4000 | [spec](docs/PART_SPECS_T15.md#p0706-code-artifact-gen) | [txt](prompts/P0706_code_artifact_gen.txt) |
| P0707 | `ui_component_gen` | UI Component & Interface Generation | `cap.t15.ui.ui_component_gen@1` | seeded | 5000 | [spec](docs/PART_SPECS_T15.md#p0707-ui-component-gen) | [txt](prompts/P0707_ui_component_gen.txt) |
| P0708 | `web_app_gen` | Full Web Application Generation | `cap.t15.web.web_app_gen@1` | seeded | 6000 | [spec](docs/PART_SPECS_T15.md#p0708-web-app-gen) | [txt](prompts/P0708_web_app_gen.txt) |
| P0709 | `visual_design_engine` | Visual Design & Layout Engine | `cap.t15.visual.visual_design_engine@1` | seeded | 7000 | [spec](docs/PART_SPECS_T15.md#p0709-visual-design-engine) | [txt](prompts/P0709_visual_design_engine.txt) |
| P0710 | `animation_engine` | Animation & Motion Design | `cap.t15.animation.animation_engine@1` | seeded | 8000 | [spec](docs/PART_SPECS_T15.md#p0710-animation-engine) | [txt](prompts/P0710_animation_engine.txt) |
| P0711 | `data_visualisation` | Data Visualisation Generation | `cap.t15.data.data_visualisation@1` | seeded | 9000 | [spec](docs/PART_SPECS_T15.md#p0711-data-visualisation) | [txt](prompts/P0711_data_visualisation.txt) |
| P0712 | `presentation_gen` | Presentation & Deck Generation | `cap.t15.presentation.presentation_gen@1` | seeded | 10000 | [spec](docs/PART_SPECS_T15.md#p0712-presentation-gen) | [txt](prompts/P0712_presentation_gen.txt) |
| P0713 | `document_gen_office` | Office Document Generation | `cap.t15.document.document_gen_office@1` | seeded | 11000 | [spec](docs/PART_SPECS_T15.md#p0713-document-gen-office) | [txt](prompts/P0713_document_gen_office.txt) |
| P0714 | `report_generation` | Analytical Report Generation | `cap.t15.report.report_generation@1` | seeded | 12000 | [spec](docs/PART_SPECS_T15.md#p0714-report-generation) | [txt](prompts/P0714_report_generation.txt) |
| P0715 | `three_d_generation` | 3D Model & Scene Generation | `cap.t15.three.three_d_generation@1` | seeded | 13000 | [spec](docs/PART_SPECS_T15.md#p0715-three-d-generation) | [txt](prompts/P0715_three_d_generation.txt) |
| P0716 | `game_generation` | Interactive Game & Simulation Generation | `cap.t15.game.game_generation@1` | seeded | 14000 | [spec](docs/PART_SPECS_T15.md#p0716-game-generation) | [txt](prompts/P0716_game_generation.txt) |
| P0717 | `image_generation_bridge` | Image Generation Direction & Control | `cap.t15.image.image_generation_bridge@1` | seeded | 15000 | [spec](docs/PART_SPECS_T15.md#p0717-image-generation-bridge) | [txt](prompts/P0717_image_generation_bridge.txt) |
| P0718 | `video_generation_bridge` | Video Generation Direction & Editing | `cap.t15.video.video_generation_bridge@1` | seeded | 16000 | [spec](docs/PART_SPECS_T15.md#p0718-video-generation-bridge) | [txt](prompts/P0718_video_generation_bridge.txt) |
| P0719 | `audio_generation_bridge` | Speech & Audio Generation Direction | `cap.t15.audio.audio_generation_bridge@1` | seeded | 17000 | [spec](docs/PART_SPECS_T15.md#p0719-audio-generation-bridge) | [txt](prompts/P0719_audio_generation_bridge.txt) |
| P0720 | `music_generation_bridge` | Music Generation Direction | `cap.t15.music.music_generation_bridge@1` | seeded | 18000 | [spec](docs/PART_SPECS_T15.md#p0720-music-generation-bridge) | [txt](prompts/P0720_music_generation_bridge.txt) |
| P0721 | `multilingual_generation` | Multilingual Generation & Localisation | `cap.t15.multilingual.multilingual_generation@1` | seeded | 19000 | [spec](docs/PART_SPECS_T15.md#p0721-multilingual-generation) | [txt](prompts/P0721_multilingual_generation.txt) |
| P0722 | `translation_quality` | Translation & Cross-Lingual Fidelity | `cap.t15.translation.translation_quality@1` | seeded | 20000 | [spec](docs/PART_SPECS_T15.md#p0722-translation-quality) | [txt](prompts/P0722_translation_quality.txt) |
| P0723 | `taste_model` | Aesthetic & Quality Judgment Model | `cap.t15.taste.taste_model@1` | seeded | 21000 | [spec](docs/PART_SPECS_T15.md#p0723-taste-model) | [txt](prompts/P0723_taste_model.txt) |
| P0724 | `output_verification` | Output Self-Verification Pipeline | `cap.t15.output.output_verification@1` | seeded | 22000 | [spec](docs/PART_SPECS_T15.md#p0724-output-verification) | [txt](prompts/P0724_output_verification.txt) |
| P0725 | `rendering_verification` | Rendering & Visual Self-Check | `cap.t15.rendering.rendering_verification@1` | seeded | 23000 | [spec](docs/PART_SPECS_T15.md#p0725-rendering-verification) | [txt](prompts/P0725_rendering_verification.txt) |
| P0726 | `accessibility_gen` | Accessibility Compliance Engine | `cap.t15.accessibility.accessibility_gen@1` | seeded | 24000 | [spec](docs/PART_SPECS_T15.md#p0726-accessibility-gen) | [txt](prompts/P0726_accessibility_gen.txt) |
| P0727 | `citation_formatting` | Citation, Attribution & Reference Management | `cap.t15.citation.citation_formatting@1` | seeded | 25000 | [spec](docs/PART_SPECS_T15.md#p0727-citation-formatting) | [txt](prompts/P0727_citation_formatting.txt) |
| P0728 | `factuality_gen` | Generation-Time Factuality Enforcement | `cap.t15.factuality.factuality_gen@1` | seeded | 26000 | [spec](docs/PART_SPECS_T15.md#p0728-factuality-gen) | [txt](prompts/P0728_factuality_gen.txt) |
| P0729 | `template_engine` | Template & Structured Output Engine | `cap.t15.template.template_engine@1` | seeded | 27000 | [spec](docs/PART_SPECS_T15.md#p0729-template-engine) | [txt](prompts/P0729_template_engine.txt) |
| P0730 | `diff_patch_output` | Diff & Incremental Edit Output | `cap.t15.diff.diff_patch_output@1` | seeded | 28000 | [spec](docs/PART_SPECS_T15.md#p0730-diff-patch-output) | [txt](prompts/P0730_diff_patch_output.txt) |
| P0731 | `streaming_ux` | Progressive Output & Streaming Presentation | `cap.t15.streaming.streaming_ux@1` | seeded | 29000 | [spec](docs/PART_SPECS_T15.md#p0731-streaming-ux) | [txt](prompts/P0731_streaming_ux.txt) |
| P0732 | `interaction_design` | Conversational Interaction Design | `cap.t15.interaction.interaction_design@1` | seeded | 30000 | [spec](docs/PART_SPECS_T15.md#p0732-interaction-design) | [txt](prompts/P0732_interaction_design.txt) |
| P0733 | `personality_consistency` | Persona Consistency & Character Control | `cap.t15.personality.personality_consistency@1` | seeded | 31000 | [spec](docs/PART_SPECS_T15.md#p0733-personality-consistency) | [txt](prompts/P0733_personality_consistency.txt) |
| P0734 | `emotional_intelligence` | Emotional & Social Appropriateness | `cap.t15.emotional.emotional_intelligence@1` | seeded | 32000 | [spec](docs/PART_SPECS_T15.md#p0734-emotional-intelligence) | [txt](prompts/P0734_emotional_intelligence.txt) |
| P0735 | `pedagogical_generation` | Explanation & Teaching Generation | `cap.t15.pedagogical.pedagogical_generation@1` | seeded | 33000 | [spec](docs/PART_SPECS_T15.md#p0735-pedagogical-generation) | [txt](prompts/P0735_pedagogical_generation.txt) |
| P0736 | `creative_writing` | Creative & Narrative Generation | `cap.t15.creative.creative_writing@1` | seeded | 34000 | [spec](docs/PART_SPECS_T15.md#p0736-creative-writing) | [txt](prompts/P0736_creative_writing.txt) |
| P0737 | `technical_writing` | Technical Documentation Generation | `cap.t15.technical.technical_writing@1` | seeded | 35000 | [spec](docs/PART_SPECS_T15.md#p0737-technical-writing) | [txt](prompts/P0737_technical_writing.txt) |
| P0738 | `legal_drafting` | Legal Document Drafting | `cap.t15.legal.legal_drafting@1` | seeded | 36000 | [spec](docs/PART_SPECS_T15.md#p0738-legal-drafting) | [txt](prompts/P0738_legal_drafting.txt) |
| P0739 | `financial_modelling_gen` | Financial Model Generation | `cap.t15.financial.financial_modelling_gen@1` | seeded | 37000 | [spec](docs/PART_SPECS_T15.md#p0739-financial-modelling-gen) | [txt](prompts/P0739_financial_modelling_gen.txt) |
| P0740 | `scientific_writing` | Scientific Manuscript & Protocol Generation | `cap.t15.scientific.scientific_writing@1` | seeded | 38000 | [spec](docs/PART_SPECS_T15.md#p0740-scientific-writing) | [txt](prompts/P0740_scientific_writing.txt) |
| P0741 | `email_message_gen` | Correspondence & Message Generation | `cap.t15.email.email_message_gen@1` | seeded | 39000 | [spec](docs/PART_SPECS_T15.md#p0741-email-message-gen) | [txt](prompts/P0741_email_message_gen.txt) |
| P0742 | `summarisation_gen` | Summarisation & Distillation | `cap.t15.summarisation.summarisation_gen@1` | seeded | 40000 | [spec](docs/PART_SPECS_T15.md#p0742-summarisation-gen) | [txt](prompts/P0742_summarisation_gen.txt) |
| P0743 | `structured_data_gen` | Structured Data & Schema Output | `cap.t15.structured.structured_data_gen@1` | seeded | 41000 | [spec](docs/PART_SPECS_T15.md#p0743-structured-data-gen) | [txt](prompts/P0743_structured_data_gen.txt) |
| P0744 | `artifact_versioning` | Artifact Revision & Collaborative Editing | `cap.t15.artifact.artifact_versioning@1` | seeded | 42000 | [spec](docs/PART_SPECS_T15.md#p0744-artifact-versioning) | [txt](prompts/P0744_artifact_versioning.txt) |
| P0745 | `output_localisation` | Output Format Adaptation & Portability | `cap.t15.output.output_localisation@1` | seeded | 43000 | [spec](docs/PART_SPECS_T15.md#p0745-output-localisation) | [txt](prompts/P0745_output_localisation.txt) |
| P0746 | `gdpval_harness` | Knowledge Work Evaluation Harness | `cap.t15.gdpval.gdpval_harness@1` | seeded | 44000 | [spec](docs/PART_SPECS_T15.md#p0746-gdpval-harness) | [txt](prompts/P0746_gdpval_harness.txt) |
| P0747 | `artifact_quality_gate` | Artifact Quality Gate | `cap.t15.artifact.artifact_quality_gate@1` | seeded | 45000 | [spec](docs/PART_SPECS_T15.md#p0747-artifact-quality-gate) | [txt](prompts/P0747_artifact_quality_gate.txt) |
| P0748 | `generation_speed` | Generation Latency & Cost Optimisation | `cap.t15.generation.generation_speed@1` | seeded | 46000 | [spec](docs/PART_SPECS_T15.md#p0748-generation-speed) | [txt](prompts/P0748_generation_speed.txt) |
| P0749 | `output_safety_filter` | Output Safety & Policy Compliance Filter | `cap.t15.output.output_safety_filter@1` | seeded | 47000 | [spec](docs/PART_SPECS_T15.md#p0749-output-safety-filter) | [txt](prompts/P0749_output_safety_filter.txt) |
| P0750 | `generation_spec_doc` | Generation Subsystem Specification | `cap.t15.generation.generation_spec_doc@1` | seeded | 48000 | [spec](docs/PART_SPECS_T15.md#p0750-generation-spec-doc) | [txt](prompts/P0750_generation_spec_doc.txt) |

## T16 — Domain Superintelligence Packs

*Life sciences, chemistry, physics, medicine, law, finance, engineering: expert-grade domain reasoning with domain verifiers.*

| part | slug | title | capability | det | p99 ns | spec | prompt |
|---|---|---|---|---|---:|---|---|
| P0751 | `domain_pack_framework` | Domain Pack Framework & Interface | `cap.t16.domain.domain_pack_framework@1` | pure | 49000 | [spec](docs/PART_SPECS_T16.md#p0751-domain-pack-framework) | [txt](prompts/P0751_domain_pack_framework.txt) |
| P0752 | `domain_detection` | Domain Detection & Expert Routing | `cap.t16.domain.domain_detection@1` | pure | 3000 | [spec](docs/PART_SPECS_T16.md#p0752-domain-detection) | [txt](prompts/P0752_domain_detection.txt) |
| P0753 | `molecular_biology` | Molecular & Cell Biology | `cap.t16.molecular.molecular_biology@1` | pure | 4000 | [spec](docs/PART_SPECS_T16.md#p0753-molecular-biology) | [txt](prompts/P0753_molecular_biology.txt) |
| P0754 | `structural_biology` | Structural Biology & Protein Science | `cap.t16.structural.structural_biology@1` | pure | 5000 | [spec](docs/PART_SPECS_T16.md#p0754-structural-biology) | [txt](prompts/P0754_structural_biology.txt) |
| P0755 | `genomics_bioinformatics` | Genomics & Bioinformatics | `cap.t16.genomics.genomics_bioinformatics@1` | pure | 6000 | [spec](docs/PART_SPECS_T16.md#p0755-genomics-bioinformatics) | [txt](prompts/P0755_genomics_bioinformatics.txt) |
| P0756 | `organic_chemistry` | Organic Chemistry & Synthesis | `cap.t16.organic.organic_chemistry@1` | pure | 7000 | [spec](docs/PART_SPECS_T16.md#p0756-organic-chemistry) | [txt](prompts/P0756_organic_chemistry.txt) |
| P0757 | `computational_chemistry` | Computational & Physical Chemistry | `cap.t16.computational.computational_chemistry@1` | pure | 8000 | [spec](docs/PART_SPECS_T16.md#p0757-computational-chemistry) | [txt](prompts/P0757_computational_chemistry.txt) |
| P0758 | `materials_science` | Materials Science & Engineering | `cap.t16.materials.materials_science@1` | pure | 9000 | [spec](docs/PART_SPECS_T16.md#p0758-materials-science) | [txt](prompts/P0758_materials_science.txt) |
| P0759 | `drug_discovery` | Medicinal Chemistry & Drug Discovery | `cap.t16.drug.drug_discovery@1` | pure | 10000 | [spec](docs/PART_SPECS_T16.md#p0759-drug-discovery) | [txt](prompts/P0759_drug_discovery.txt) |
| P0760 | `clinical_medicine` | Clinical Medicine & Diagnostics | `cap.t16.clinical.clinical_medicine@1` | pure | 11000 | [spec](docs/PART_SPECS_T16.md#p0760-clinical-medicine) | [txt](prompts/P0760_clinical_medicine.txt) |
| P0761 | `epidemiology_publichealth` | Epidemiology & Public Health | `cap.t16.epidemiology.epidemiology_publichealth@1` | pure | 12000 | [spec](docs/PART_SPECS_T16.md#p0761-epidemiology-publichealth) | [txt](prompts/P0761_epidemiology_publichealth.txt) |
| P0762 | `neuroscience` | Neuroscience & Cognitive Science | `cap.t16.neuroscience.neuroscience@1` | pure | 13000 | [spec](docs/PART_SPECS_T16.md#p0762-neuroscience) | [txt](prompts/P0762_neuroscience.txt) |
| P0763 | `theoretical_physics` | Theoretical & Mathematical Physics | `cap.t16.theoretical.theoretical_physics@1` | pure | 14000 | [spec](docs/PART_SPECS_T16.md#p0763-theoretical-physics) | [txt](prompts/P0763_theoretical_physics.txt) |
| P0764 | `applied_physics` | Applied & Experimental Physics | `cap.t16.applied.applied_physics@1` | pure | 15000 | [spec](docs/PART_SPECS_T16.md#p0764-applied-physics) | [txt](prompts/P0764_applied_physics.txt) |
| P0765 | `astronomy_astrophysics` | Astronomy & Astrophysics | `cap.t16.astronomy.astronomy_astrophysics@1` | pure | 16000 | [spec](docs/PART_SPECS_T16.md#p0765-astronomy-astrophysics) | [txt](prompts/P0765_astronomy_astrophysics.txt) |
| P0766 | `earth_climate` | Earth & Climate Science | `cap.t16.earth.earth_climate@1` | pure | 17000 | [spec](docs/PART_SPECS_T16.md#p0766-earth-climate) | [txt](prompts/P0766_earth_climate.txt) |
| P0767 | `pure_mathematics` | Pure Mathematics | `cap.t16.pure.pure_mathematics@1` | pure | 18000 | [spec](docs/PART_SPECS_T16.md#p0767-pure-mathematics) | [txt](prompts/P0767_pure_mathematics.txt) |
| P0768 | `applied_mathematics` | Applied Mathematics & Numerical Analysis | `cap.t16.applied.applied_mathematics@1` | pure | 19000 | [spec](docs/PART_SPECS_T16.md#p0768-applied-mathematics) | [txt](prompts/P0768_applied_mathematics.txt) |
| P0769 | `statistics_expertise` | Statistics & Experimental Design | `cap.t16.statistics.statistics_expertise@1` | pure | 20000 | [spec](docs/PART_SPECS_T16.md#p0769-statistics-expertise) | [txt](prompts/P0769_statistics_expertise.txt) |
| P0770 | `operations_research` | Operations Research & Optimisation | `cap.t16.operations.operations_research@1` | pure | 21000 | [spec](docs/PART_SPECS_T16.md#p0770-operations-research) | [txt](prompts/P0770_operations_research.txt) |
| P0771 | `mechanical_engineering` | Mechanical & Structural Engineering | `cap.t16.mechanical.mechanical_engineering@1` | pure | 22000 | [spec](docs/PART_SPECS_T16.md#p0771-mechanical-engineering) | [txt](prompts/P0771_mechanical_engineering.txt) |
| P0772 | `electrical_engineering` | Electrical & Electronic Engineering | `cap.t16.electrical.electrical_engineering@1` | pure | 23000 | [spec](docs/PART_SPECS_T16.md#p0772-electrical-engineering) | [txt](prompts/P0772_electrical_engineering.txt) |
| P0773 | `control_systems` | Control Systems & Robotics Engineering | `cap.t16.control.control_systems@1` | pure | 24000 | [spec](docs/PART_SPECS_T16.md#p0773-control-systems) | [txt](prompts/P0773_control_systems.txt) |
| P0774 | `chemical_engineering` | Chemical & Process Engineering | `cap.t16.chemical.chemical_engineering@1` | pure | 25000 | [spec](docs/PART_SPECS_T16.md#p0774-chemical-engineering) | [txt](prompts/P0774_chemical_engineering.txt) |
| P0775 | `civil_infrastructure` | Civil & Infrastructure Engineering | `cap.t16.civil.civil_infrastructure@1` | pure | 26000 | [spec](docs/PART_SPECS_T16.md#p0775-civil-infrastructure) | [txt](prompts/P0775_civil_infrastructure.txt) |
| P0776 | `aerospace_engineering` | Aerospace Engineering | `cap.t16.aerospace.aerospace_engineering@1` | pure | 27000 | [spec](docs/PART_SPECS_T16.md#p0776-aerospace-engineering) | [txt](prompts/P0776_aerospace_engineering.txt) |
| P0777 | `semiconductor_engineering` | Semiconductor & Chip Design | `cap.t16.semiconductor.semiconductor_engineering@1` | pure | 28000 | [spec](docs/PART_SPECS_T16.md#p0777-semiconductor-engineering) | [txt](prompts/P0777_semiconductor_engineering.txt) |
| P0778 | `energy_systems` | Energy Systems & Power Engineering | `cap.t16.energy.energy_systems@1` | pure | 29000 | [spec](docs/PART_SPECS_T16.md#p0778-energy-systems) | [txt](prompts/P0778_energy_systems.txt) |
| P0779 | `corporate_law` | Corporate & Transactional Law | `cap.t16.corporate.corporate_law@1` | pure | 30000 | [spec](docs/PART_SPECS_T16.md#p0779-corporate-law) | [txt](prompts/P0779_corporate_law.txt) |
| P0780 | `litigation_arbitration` | Litigation & Dispute Resolution | `cap.t16.litigation.litigation_arbitration@1` | pure | 31000 | [spec](docs/PART_SPECS_T16.md#p0780-litigation-arbitration) | [txt](prompts/P0780_litigation_arbitration.txt) |
| P0781 | `regulatory_compliance` | Regulatory & Compliance Analysis | `cap.t16.regulatory.regulatory_compliance@1` | pure | 32000 | [spec](docs/PART_SPECS_T16.md#p0781-regulatory-compliance) | [txt](prompts/P0781_regulatory_compliance.txt) |
| P0782 | `ip_patent` | Intellectual Property & Patent Practice | `cap.t16.ip.ip_patent@1` | pure | 33000 | [spec](docs/PART_SPECS_T16.md#p0782-ip-patent) | [txt](prompts/P0782_ip_patent.txt) |
| P0783 | `tax_accounting` | Tax & Accounting | `cap.t16.tax.tax_accounting@1` | pure | 34000 | [spec](docs/PART_SPECS_T16.md#p0783-tax-accounting) | [txt](prompts/P0783_tax_accounting.txt) |
| P0784 | `corporate_finance` | Corporate Finance & Valuation | `cap.t16.corporate.corporate_finance@1` | pure | 35000 | [spec](docs/PART_SPECS_T16.md#p0784-corporate-finance) | [txt](prompts/P0784_corporate_finance.txt) |
| P0785 | `quantitative_finance` | Quantitative Finance & Derivatives | `cap.t16.quantitative.quantitative_finance@1` | pure | 36000 | [spec](docs/PART_SPECS_T16.md#p0785-quantitative-finance) | [txt](prompts/P0785_quantitative_finance.txt) |
| P0786 | `investment_research` | Investment Research & Financial Analysis | `cap.t16.investment.investment_research@1` | pure | 37000 | [spec](docs/PART_SPECS_T16.md#p0786-investment-research) | [txt](prompts/P0786_investment_research.txt) |
| P0787 | `risk_management` | Risk Management & Actuarial Science | `cap.t16.risk.risk_management@1` | pure | 38000 | [spec](docs/PART_SPECS_T16.md#p0787-risk-management) | [txt](prompts/P0787_risk_management.txt) |
| P0788 | `economics` | Economics & Policy Analysis | `cap.t16.economics.economics@1` | pure | 39000 | [spec](docs/PART_SPECS_T16.md#p0788-economics) | [txt](prompts/P0788_economics.txt) |
| P0789 | `management_strategy` | Business Strategy & Management Consulting | `cap.t16.management.management_strategy@1` | pure | 40000 | [spec](docs/PART_SPECS_T16.md#p0789-management-strategy) | [txt](prompts/P0789_management_strategy.txt) |
| P0790 | `marketing_growth` | Marketing, Growth & Product Analytics | `cap.t16.marketing.marketing_growth@1` | pure | 41000 | [spec](docs/PART_SPECS_T16.md#p0790-marketing-growth) | [txt](prompts/P0790_marketing_growth.txt) |
| P0791 | `operations_supplychain` | Operations & Supply Chain Management | `cap.t16.operations.operations_supplychain@1` | pure | 42000 | [spec](docs/PART_SPECS_T16.md#p0791-operations-supplychain) | [txt](prompts/P0791_operations_supplychain.txt) |
| P0792 | `hr_organisational` | Human Resources & Organisational Design | `cap.t16.hr.hr_organisational@1` | pure | 43000 | [spec](docs/PART_SPECS_T16.md#p0792-hr-organisational) | [txt](prompts/P0792_hr_organisational.txt) |
| P0793 | `education_pedagogy` | Education & Instructional Design | `cap.t16.education.education_pedagogy@1` | pure | 44000 | [spec](docs/PART_SPECS_T16.md#p0793-education-pedagogy) | [txt](prompts/P0793_education_pedagogy.txt) |
| P0794 | `psychology_behaviour` | Psychology & Behavioural Science | `cap.t16.psychology.psychology_behaviour@1` | pure | 45000 | [spec](docs/PART_SPECS_T16.md#p0794-psychology-behaviour) | [txt](prompts/P0794_psychology_behaviour.txt) |
| P0795 | `linguistics` | Linguistics & Language Science | `cap.t16.linguistics.linguistics@1` | pure | 46000 | [spec](docs/PART_SPECS_T16.md#p0795-linguistics) | [txt](prompts/P0795_linguistics.txt) |
| P0796 | `history_humanities` | History & Humanities Scholarship | `cap.t16.history.history_humanities@1` | pure | 47000 | [spec](docs/PART_SPECS_T16.md#p0796-history-humanities) | [txt](prompts/P0796_history_humanities.txt) |
| P0797 | `philosophy_ethics` | Philosophy & Applied Ethics | `cap.t16.philosophy.philosophy_ethics@1` | pure | 48000 | [spec](docs/PART_SPECS_T16.md#p0797-philosophy-ethics) | [txt](prompts/P0797_philosophy_ethics.txt) |
| P0798 | `agriculture_food` | Agriculture, Food Science & Nutrition | `cap.t16.agriculture.agriculture_food@1` | pure | 49000 | [spec](docs/PART_SPECS_T16.md#p0798-agriculture-food) | [txt](prompts/P0798_agriculture_food.txt) |
| P0799 | `domain_cross_transfer` | Cross-Domain Synthesis & Interdisciplinary Reasoning | `cap.t16.domain.domain_cross_transfer@1` | pure | 3000 | [spec](docs/PART_SPECS_T16.md#p0799-domain-cross-transfer) | [txt](prompts/P0799_domain_cross_transfer.txt) |
| P0800 | `domain_eval_harness` | Domain Expertise Benchmark Harness | `cap.t16.domain.domain_eval_harness@1` | pure | 4000 | [spec](docs/PART_SPECS_T16.md#p0800-domain-eval-harness) | [txt](prompts/P0800_domain_eval_harness.txt) |

## T17 — Training, Data & Recursive Self-Improvement

*Pretraining, RL from verifiable reward, distillation into the fast paths, and the closed self-improvement loop.*

| part | slug | title | capability | det | p99 ns | spec | prompt |
|---|---|---|---|---|---:|---|---|
| P0801 | `data_sourcing` | Training Data Sourcing & Licensing | `cap.t17.data.data_sourcing@1` | io | 5000 | [spec](docs/PART_SPECS_T17.md#p0801-data-sourcing) | [txt](prompts/P0801_data_sourcing.txt) |
| P0802 | `data_extraction_pipeline_train` | Corpus Extraction & Normalisation | `cap.t17.data.data_extraction_pipeline_train@1` | io | 6000 | [spec](docs/PART_SPECS_T17.md#p0802-data-extraction-pipeline-train) | [txt](prompts/P0802_data_extraction_pipeline_train.txt) |
| P0803 | `data_quality_filter` | Data Quality Filtering & Scoring | `cap.t17.data.data_quality_filter@1` | io | 7000 | [spec](docs/PART_SPECS_T17.md#p0803-data-quality-filter) | [txt](prompts/P0803_data_quality_filter.txt) |
| P0804 | `data_dedup_train` | Corpus Deduplication at Scale | `cap.t17.data.data_dedup_train@1` | io | 8000 | [spec](docs/PART_SPECS_T17.md#p0804-data-dedup-train) | [txt](prompts/P0804_data_dedup_train.txt) |
| P0805 | `data_decontamination` | Benchmark Decontamination | `cap.t17.data.data_decontamination@1` | io | 9000 | [spec](docs/PART_SPECS_T17.md#p0805-data-decontamination) | [txt](prompts/P0805_data_decontamination.txt) |
| P0806 | `data_mixture` | Data Mixture Optimisation | `cap.t17.data.data_mixture@1` | io | 10000 | [spec](docs/PART_SPECS_T17.md#p0806-data-mixture) | [txt](prompts/P0806_data_mixture.txt) |
| P0807 | `synthetic_data_engine` | Synthetic Data Generation Engine | `cap.t17.synthetic.synthetic_data_engine@1` | io | 11000 | [spec](docs/PART_SPECS_T17.md#p0807-synthetic-data-engine) | [txt](prompts/P0807_synthetic_data_engine.txt) |
| P0808 | `verifiable_task_gen` | Verifiable Task & Reward Generation | `cap.t17.verifiable.verifiable_task_gen@1` | io | 12000 | [spec](docs/PART_SPECS_T17.md#p0808-verifiable-task-gen) | [txt](prompts/P0808_verifiable_task_gen.txt) |
| P0809 | `data_augmentation` | Data Augmentation & Transformation | `cap.t17.data.data_augmentation@1` | io | 13000 | [spec](docs/PART_SPECS_T17.md#p0809-data-augmentation) | [txt](prompts/P0809_data_augmentation.txt) |
| P0810 | `tokenizer_training` | Tokeniser Training & Evaluation | `cap.t17.tokenizer.tokenizer_training@1` | io | 14000 | [spec](docs/PART_SPECS_T17.md#p0810-tokenizer-training) | [txt](prompts/P0810_tokenizer_training.txt) |
| P0811 | `data_loader` | High-Throughput Training Data Loader | `cap.t17.data.data_loader@1` | io | 15000 | [spec](docs/PART_SPECS_T17.md#p0811-data-loader) | [txt](prompts/P0811_data_loader.txt) |
| P0812 | `pretraining_loop` | Pretraining Loop & Orchestration | `cap.t17.pretraining.pretraining_loop@1` | io | 16000 | [spec](docs/PART_SPECS_T17.md#p0812-pretraining-loop) | [txt](prompts/P0812_pretraining_loop.txt) |
| P0813 | `optimiser_design` | Optimiser Design & Implementation | `cap.t17.optimiser.optimiser_design@1` | io | 17000 | [spec](docs/PART_SPECS_T17.md#p0813-optimiser-design) | [txt](prompts/P0813_optimiser_design.txt) |
| P0814 | `lr_schedule` | Learning Rate & Schedule Optimisation | `cap.t17.lr.lr_schedule@1` | io | 18000 | [spec](docs/PART_SPECS_T17.md#p0814-lr-schedule) | [txt](prompts/P0814_lr_schedule.txt) |
| P0815 | `gradient_engineering` | Gradient Processing & Stability | `cap.t17.gradient.gradient_engineering@1` | io | 19000 | [spec](docs/PART_SPECS_T17.md#p0815-gradient-engineering) | [txt](prompts/P0815_gradient_engineering.txt) |
| P0816 | `training_parallelism` | Training Parallelism Strategy | `cap.t17.training.training_parallelism@1` | io | 20000 | [spec](docs/PART_SPECS_T17.md#p0816-training-parallelism) | [txt](prompts/P0816_training_parallelism.txt) |
| P0817 | `training_efficiency` | Training Compute Efficiency | `cap.t17.training.training_efficiency@1` | io | 21000 | [spec](docs/PART_SPECS_T17.md#p0817-training-efficiency) | [txt](prompts/P0817_training_efficiency.txt) |
| P0818 | `checkpoint_management` | Checkpoint Management & Model Registry | `cap.t17.checkpoint.checkpoint_management@1` | io | 22000 | [spec](docs/PART_SPECS_T17.md#p0818-checkpoint-management) | [txt](prompts/P0818_checkpoint_management.txt) |
| P0819 | `training_monitoring` | Training Observability & Diagnostics | `cap.t17.training.training_monitoring@1` | io | 23000 | [spec](docs/PART_SPECS_T17.md#p0819-training-monitoring) | [txt](prompts/P0819_training_monitoring.txt) |
| P0820 | `sft_pipeline` | Supervised Fine-Tuning Pipeline | `cap.t17.sft.sft_pipeline@1` | io | 24000 | [spec](docs/PART_SPECS_T17.md#p0820-sft-pipeline) | [txt](prompts/P0820_sft_pipeline.txt) |
| P0821 | `rlvr_pipeline` | RL from Verifiable Rewards | `cap.t17.rlvr.rlvr_pipeline@1` | io | 25000 | [spec](docs/PART_SPECS_T17.md#p0821-rlvr-pipeline) | [txt](prompts/P0821_rlvr_pipeline.txt) |
| P0822 | `rlhf_pipeline` | RL from Human & AI Feedback | `cap.t17.rlhf.rlhf_pipeline@1` | io | 26000 | [spec](docs/PART_SPECS_T17.md#p0822-rlhf-pipeline) | [txt](prompts/P0822_rlhf_pipeline.txt) |
| P0823 | `reward_model` | Reward Model Design & Robustness | `cap.t17.reward.reward_model@1` | io | 27000 | [spec](docs/PART_SPECS_T17.md#p0823-reward-model) | [txt](prompts/P0823_reward_model.txt) |
| P0824 | `constitutional_training` | Constitutional & Principle-Based Training | `cap.t17.constitutional.constitutional_training@1` | io | 28000 | [spec](docs/PART_SPECS_T17.md#p0824-constitutional-training) | [txt](prompts/P0824_constitutional_training.txt) |
| P0825 | `process_supervision_training` | Process Supervision Training | `cap.t17.process.process_supervision_training@1` | io | 29000 | [spec](docs/PART_SPECS_T17.md#p0825-process-supervision-training) | [txt](prompts/P0825_process_supervision_training.txt) |
| P0826 | `self_play_training` | Self-Play & Adversarial Curriculum | `cap.t17.self.self_play_training@1` | io | 30000 | [spec](docs/PART_SPECS_T17.md#p0826-self-play-training) | [txt](prompts/P0826_self_play_training.txt) |
| P0827 | `distillation_training` | Distillation Training Pipeline | `cap.t17.distillation.distillation_training@1` | io | 31000 | [spec](docs/PART_SPECS_T17.md#p0827-distillation-training) | [txt](prompts/P0827_distillation_training.txt) |
| P0828 | `quantisation_training` | Quantisation-Aware Training | `cap.t17.quantisation.quantisation_training@1` | io | 32000 | [spec](docs/PART_SPECS_T17.md#p0828-quantisation-training) | [txt](prompts/P0828_quantisation_training.txt) |
| P0829 | `long_context_training` | Long Context Training Curriculum | `cap.t17.long.long_context_training@1` | io | 33000 | [spec](docs/PART_SPECS_T17.md#p0829-long-context-training) | [txt](prompts/P0829_long_context_training.txt) |
| P0830 | `multimodal_training` | Multimodal Training Pipeline | `cap.t17.multimodal.multimodal_training@1` | io | 34000 | [spec](docs/PART_SPECS_T17.md#p0830-multimodal-training) | [txt](prompts/P0830_multimodal_training.txt) |
| P0831 | `agentic_training` | Agentic & Tool-Use Training | `cap.t17.agentic.agentic_training@1` | io | 35000 | [spec](docs/PART_SPECS_T17.md#p0831-agentic-training) | [txt](prompts/P0831_agentic_training.txt) |
| P0832 | `safety_training` | Safety & Refusal Training | `cap.t17.safety.safety_training@1` | io | 36000 | [spec](docs/PART_SPECS_T17.md#p0832-safety-training) | [txt](prompts/P0832_safety_training.txt) |
| P0833 | `honesty_training` | Honesty & Calibration Training | `cap.t17.honesty.honesty_training@1` | io | 37000 | [spec](docs/PART_SPECS_T17.md#p0833-honesty-training) | [txt](prompts/P0833_honesty_training.txt) |
| P0834 | `continual_pretraining` | Continual Pretraining & Knowledge Refresh | `cap.t17.continual.continual_pretraining@1` | io | 38000 | [spec](docs/PART_SPECS_T17.md#p0834-continual-pretraining) | [txt](prompts/P0834_continual_pretraining.txt) |
| P0835 | `hyperparameter_search` | Hyperparameter Optimisation at Scale | `cap.t17.hyperparameter.hyperparameter_search@1` | io | 39000 | [spec](docs/PART_SPECS_T17.md#p0835-hyperparameter-search) | [txt](prompts/P0835_hyperparameter_search.txt) |
| P0836 | `experiment_tracking` | Experiment Management & Provenance | `cap.t17.experiment.experiment_tracking@1` | io | 40000 | [spec](docs/PART_SPECS_T17.md#p0836-experiment-tracking) | [txt](prompts/P0836_experiment_tracking.txt) |
| P0837 | `ablation_framework` | Systematic Ablation Framework | `cap.t17.ablation.ablation_framework@1` | io | 41000 | [spec](docs/PART_SPECS_T17.md#p0837-ablation-framework) | [txt](prompts/P0837_ablation_framework.txt) |
| P0838 | `scaling_prediction` | Scaling Prediction & Run Planning | `cap.t17.scaling.scaling_prediction@1` | io | 42000 | [spec](docs/PART_SPECS_T17.md#p0838-scaling-prediction) | [txt](prompts/P0838_scaling_prediction.txt) |
| P0839 | `self_improvement_loop` | Recursive Self-Improvement Loop | `cap.t17.self.self_improvement_loop@1` | io | 43000 | [spec](docs/PART_SPECS_T17.md#p0839-self-improvement-loop) | [txt](prompts/P0839_self_improvement_loop.txt) |
| P0840 | `automated_research` | Automated ML Research Agent | `cap.t17.automated.automated_research@1` | io | 44000 | [spec](docs/PART_SPECS_T17.md#p0840-automated-research) | [txt](prompts/P0840_automated_research.txt) |
| P0841 | `capability_gap_analysis` | Capability Gap Analysis & Prioritisation | `cap.t17.capability.capability_gap_analysis@1` | io | 45000 | [spec](docs/PART_SPECS_T17.md#p0841-capability-gap-analysis) | [txt](prompts/P0841_capability_gap_analysis.txt) |
| P0842 | `training_data_governance` | Data Governance, Consent & Deletion | `cap.t17.training.training_data_governance@1` | io | 46000 | [spec](docs/PART_SPECS_T17.md#p0842-training-data-governance) | [txt](prompts/P0842_training_data_governance.txt) |
| P0843 | `memorisation_analysis` | Memorisation & Privacy Leakage Analysis | `cap.t17.memorisation.memorisation_analysis@1` | io | 47000 | [spec](docs/PART_SPECS_T17.md#p0843-memorisation-analysis) | [txt](prompts/P0843_memorisation_analysis.txt) |
| P0844 | `training_reproducibility` | Training Reproducibility & Determinism | `cap.t17.training.training_reproducibility@1` | io | 48000 | [spec](docs/PART_SPECS_T17.md#p0844-training-reproducibility) | [txt](prompts/P0844_training_reproducibility.txt) |
| P0845 | `model_release_gate` | Model Release Gate & Sign-Off | `cap.t17.model.model_release_gate@1` | io | 49000 | [spec](docs/PART_SPECS_T17.md#p0845-model-release-gate) | [txt](prompts/P0845_model_release_gate.txt) |
| P0846 | `training_cost_model` | Training Cost & Carbon Accounting | `cap.t17.training.training_cost_model@1` | io | 3000 | [spec](docs/PART_SPECS_T17.md#p0846-training-cost-model) | [txt](prompts/P0846_training_cost_model.txt) |
| P0847 | `fine_tune_service` | Customer Fine-Tuning Infrastructure | `cap.t17.fine.fine_tune_service@1` | io | 4000 | [spec](docs/PART_SPECS_T17.md#p0847-fine-tune-service) | [txt](prompts/P0847_fine_tune_service.txt) |
| P0848 | `eval_driven_training` | Evaluation-Driven Training Loop | `cap.t17.eval.eval_driven_training@1` | io | 5000 | [spec](docs/PART_SPECS_T17.md#p0848-eval-driven-training) | [txt](prompts/P0848_eval_driven_training.txt) |
| P0849 | `training_bench` | Training Infrastructure Benchmark Suite | `cap.t17.training.training_bench@1` | io | 6000 | [spec](docs/PART_SPECS_T17.md#p0849-training-bench) | [txt](prompts/P0849_training_bench.txt) |
| P0850 | `training_spec_doc` | Training Specification & Model Card Generator | `cap.t17.training.training_spec_doc@1` | io | 7000 | [spec](docs/PART_SPECS_T17.md#p0850-training-spec-doc) | [txt](prompts/P0850_training_spec_doc.txt) |

## T18 — Evaluation, Benchmarking & Dominance Proofs

*Reproducible harnesses for every public and internal benchmark, plus the statistical machinery that proves domination of Opus 5.*

| part | slug | title | capability | det | p99 ns | spec | prompt |
|---|---|---|---|---|---:|---|---|
| P0851 | `eval_framework` | Evaluation Framework Core | `cap.t18.eval.eval_framework@1` | seeded | 8000 | [spec](docs/PART_SPECS_T18.md#p0851-eval-framework) | [txt](prompts/P0851_eval_framework.txt) |
| P0852 | `eval_registry` | Benchmark Registry & Versioning | `cap.t18.eval.eval_registry@1` | seeded | 9000 | [spec](docs/PART_SPECS_T18.md#p0852-eval-registry) | [txt](prompts/P0852_eval_registry.txt) |
| P0853 | `grading_engine` | Automatic Grading & Answer Equivalence | `cap.t18.grading.grading_engine@1` | seeded | 10000 | [spec](docs/PART_SPECS_T18.md#p0853-grading-engine) | [txt](prompts/P0853_grading_engine.txt) |
| P0854 | `human_eval_protocol` | Human Evaluation Protocol & Rater Management | `cap.t18.human.human_eval_protocol@1` | seeded | 11000 | [spec](docs/PART_SPECS_T18.md#p0854-human-eval-protocol) | [txt](prompts/P0854_human_eval_protocol.txt) |
| P0855 | `expert_eval` | Expert Domain Evaluation | `cap.t18.expert.expert_eval@1` | seeded | 12000 | [spec](docs/PART_SPECS_T18.md#p0855-expert-eval) | [txt](prompts/P0855_expert_eval.txt) |
| P0856 | `elo_arena` | Pairwise Comparison & Elo Rating System | `cap.t18.elo.elo_arena@1` | seeded | 13000 | [spec](docs/PART_SPECS_T18.md#p0856-elo-arena) | [txt](prompts/P0856_elo_arena.txt) |
| P0857 | `statistical_engine` | Statistical Analysis Engine | `cap.t18.statistical.statistical_engine@1` | seeded | 14000 | [spec](docs/PART_SPECS_T18.md#p0857-statistical-engine) | [txt](prompts/P0857_statistical_engine.txt) |
| P0858 | `variance_control` | Variance Reduction & Run Repetition Policy | `cap.t18.variance.variance_control@1` | seeded | 15000 | [spec](docs/PART_SPECS_T18.md#p0858-variance-control) | [txt](prompts/P0858_variance_control.txt) |
| P0859 | `contamination_audit` | Contamination Auditing & Sealed Test Sets | `cap.t18.contamination.contamination_audit@1` | seeded | 16000 | [spec](docs/PART_SPECS_T18.md#p0859-contamination-audit) | [txt](prompts/P0859_contamination_audit.txt) |
| P0860 | `swe_verified_eval` | SWE-bench Verified Evaluation | `cap.t18.swe.swe_verified_eval@1` | seeded | 17000 | [spec](docs/PART_SPECS_T18.md#p0860-swe-verified-eval) | [txt](prompts/P0860_swe_verified_eval.txt) |
| P0861 | `swe_pro_eval` | SWE-bench Pro Evaluation | `cap.t18.swe.swe_pro_eval@1` | seeded | 18000 | [spec](docs/PART_SPECS_T18.md#p0861-swe-pro-eval) | [txt](prompts/P0861_swe_pro_eval.txt) |
| P0862 | `frontier_bench_eval` | Frontier-Bench & Long-Horizon Coding Evaluation | `cap.t18.frontier.frontier_bench_eval@1` | seeded | 19000 | [spec](docs/PART_SPECS_T18.md#p0862-frontier-bench-eval) | [txt](prompts/P0862_frontier_bench_eval.txt) |
| P0863 | `terminal_bench_eval` | Terminal-Bench Evaluation | `cap.t18.terminal.terminal_bench_eval@1` | seeded | 20000 | [spec](docs/PART_SPECS_T18.md#p0863-terminal-bench-eval) | [txt](prompts/P0863_terminal_bench_eval.txt) |
| P0864 | `arc_agi_eval` | ARC-AGI-2 and ARC-AGI-3 Evaluation | `cap.t18.arc.arc_agi_eval@1` | seeded | 21000 | [spec](docs/PART_SPECS_T18.md#p0864-arc-agi-eval) | [txt](prompts/P0864_arc_agi_eval.txt) |
| P0865 | `gpqa_eval` | GPQA Diamond & Expert Knowledge Evaluation | `cap.t18.gpqa.gpqa_eval@1` | seeded | 22000 | [spec](docs/PART_SPECS_T18.md#p0865-gpqa-eval) | [txt](prompts/P0865_gpqa_eval.txt) |
| P0866 | `math_eval` | Mathematics Competition Evaluation | `cap.t18.math.math_eval@1` | seeded | 23000 | [spec](docs/PART_SPECS_T18.md#p0866-math-eval) | [txt](prompts/P0866_math_eval.txt) |
| P0867 | `mmmu_eval` | Multimodal Understanding Evaluation | `cap.t18.mmmu.mmmu_eval@1` | seeded | 24000 | [spec](docs/PART_SPECS_T18.md#p0867-mmmu-eval) | [txt](prompts/P0867_mmmu_eval.txt) |
| P0868 | `osworld_eval` | OSWorld and Computer Use Evaluation | `cap.t18.osworld.osworld_eval@1` | seeded | 25000 | [spec](docs/PART_SPECS_T18.md#p0868-osworld-eval) | [txt](prompts/P0868_osworld_eval.txt) |
| P0869 | `browsecomp_eval` | Web Research & Browsing Evaluation | `cap.t18.browsecomp.browsecomp_eval@1` | seeded | 26000 | [spec](docs/PART_SPECS_T18.md#p0869-browsecomp-eval) | [txt](prompts/P0869_browsecomp_eval.txt) |
| P0870 | `automation_bench_eval` | Business Automation Evaluation | `cap.t18.automation.automation_bench_eval@1` | seeded | 27000 | [spec](docs/PART_SPECS_T18.md#p0870-automation-bench-eval) | [txt](prompts/P0870_automation_bench_eval.txt) |
| P0871 | `gdpval_eval` | Economic Knowledge Work Evaluation | `cap.t18.gdpval.gdpval_eval@1` | seeded | 28000 | [spec](docs/PART_SPECS_T18.md#p0871-gdpval-eval) | [txt](prompts/P0871_gdpval_eval.txt) |
| P0872 | `lifescience_eval` | Life Sciences Evaluation Suite | `cap.t18.lifescience.lifescience_eval@1` | seeded | 29000 | [spec](docs/PART_SPECS_T18.md#p0872-lifescience-eval) | [txt](prompts/P0872_lifescience_eval.txt) |
| P0873 | `security_eval` | Security & Vulnerability Discovery Evaluation | `cap.t18.security.security_eval@1` | seeded | 30000 | [spec](docs/PART_SPECS_T18.md#p0873-security-eval) | [txt](prompts/P0873_security_eval.txt) |
| P0874 | `longcontext_eval` | Long Context Evaluation Suite | `cap.t18.longcontext.longcontext_eval@1` | seeded | 31000 | [spec](docs/PART_SPECS_T18.md#p0874-longcontext-eval) | [txt](prompts/P0874_longcontext_eval.txt) |
| P0875 | `instruction_following_eval` | Instruction Following & Constraint Adherence | `cap.t18.instruction.instruction_following_eval@1` | seeded | 32000 | [spec](docs/PART_SPECS_T18.md#p0875-instruction-following-eval) | [txt](prompts/P0875_instruction_following_eval.txt) |
| P0876 | `hallucination_eval` | Hallucination & Factuality Evaluation | `cap.t18.hallucination.hallucination_eval@1` | seeded | 33000 | [spec](docs/PART_SPECS_T18.md#p0876-hallucination-eval) | [txt](prompts/P0876_hallucination_eval.txt) |
| P0877 | `calibration_eval` | Calibration & Uncertainty Evaluation | `cap.t18.calibration.calibration_eval@1` | seeded | 34000 | [spec](docs/PART_SPECS_T18.md#p0877-calibration-eval) | [txt](prompts/P0877_calibration_eval.txt) |
| P0878 | `robustness_eval` | Robustness & Consistency Evaluation | `cap.t18.robustness.robustness_eval@1` | seeded | 35000 | [spec](docs/PART_SPECS_T18.md#p0878-robustness-eval) | [txt](prompts/P0878_robustness_eval.txt) |
| P0879 | `adversarial_eval` | Adversarial & Jailbreak Evaluation | `cap.t18.adversarial.adversarial_eval@1` | seeded | 36000 | [spec](docs/PART_SPECS_T18.md#p0879-adversarial-eval) | [txt](prompts/P0879_adversarial_eval.txt) |
| P0880 | `bias_fairness_eval` | Bias & Fairness Evaluation | `cap.t18.bias.bias_fairness_eval@1` | seeded | 37000 | [spec](docs/PART_SPECS_T18.md#p0880-bias-fairness-eval) | [txt](prompts/P0880_bias_fairness_eval.txt) |
| P0881 | `multilingual_eval` | Multilingual Capability Evaluation | `cap.t18.multilingual.multilingual_eval@1` | seeded | 38000 | [spec](docs/PART_SPECS_T18.md#p0881-multilingual-eval) | [txt](prompts/P0881_multilingual_eval.txt) |
| P0882 | `efficiency_eval` | Efficiency & Cost Evaluation | `cap.t18.efficiency.efficiency_eval@1` | seeded | 39000 | [spec](docs/PART_SPECS_T18.md#p0882-efficiency-eval) | [txt](prompts/P0882_efficiency_eval.txt) |
| P0883 | `speed_eval` | Speed & Latency Benchmark Suite | `cap.t18.speed.speed_eval@1` | seeded | 40000 | [spec](docs/PART_SPECS_T18.md#p0883-speed-eval) | [txt](prompts/P0883_speed_eval.txt) |
| P0884 | `regression_suite` | Continuous Regression Evaluation | `cap.t18.regression.regression_suite@1` | seeded | 41000 | [spec](docs/PART_SPECS_T18.md#p0884-regression-suite) | [txt](prompts/P0884_regression_suite.txt) |
| P0885 | `canary_eval` | Production Canary & Online Evaluation | `cap.t18.canary.canary_eval@1` | seeded | 42000 | [spec](docs/PART_SPECS_T18.md#p0885-canary-eval) | [txt](prompts/P0885_canary_eval.txt) |
| P0886 | `failure_taxonomy` | Failure Taxonomy & Error Analysis Engine | `cap.t18.failure.failure_taxonomy@1` | seeded | 43000 | [spec](docs/PART_SPECS_T18.md#p0886-failure-taxonomy) | [txt](prompts/P0886_failure_taxonomy.txt) |
| P0887 | `capability_map` | Capability Map & Frontier Tracking | `cap.t18.capability.capability_map@1` | seeded | 44000 | [spec](docs/PART_SPECS_T18.md#p0887-capability-map) | [txt](prompts/P0887_capability_map.txt) |
| P0888 | `competitor_tracking` | Competitor Benchmark Tracking | `cap.t18.competitor.competitor_tracking@1` | seeded | 45000 | [spec](docs/PART_SPECS_T18.md#p0888-competitor-tracking) | [txt](prompts/P0888_competitor_tracking.txt) |
| P0889 | `eval_cost_control` | Evaluation Cost Management | `cap.t18.eval.eval_cost_control@1` | seeded | 46000 | [spec](docs/PART_SPECS_T18.md#p0889-eval-cost-control) | [txt](prompts/P0889_eval_cost_control.txt) |
| P0890 | `eval_infrastructure` | Evaluation Infrastructure & Orchestration | `cap.t18.eval.eval_infrastructure@1` | seeded | 47000 | [spec](docs/PART_SPECS_T18.md#p0890-eval-infrastructure) | [txt](prompts/P0890_eval_infrastructure.txt) |
| P0891 | `benchmark_construction` | New Benchmark Construction | `cap.t18.benchmark.benchmark_construction@1` | seeded | 48000 | [spec](docs/PART_SPECS_T18.md#p0891-benchmark-construction) | [txt](prompts/P0891_benchmark_construction.txt) |
| P0892 | `dynamic_benchmark` | Dynamic & Contamination-Resistant Benchmarks | `cap.t18.dynamic.dynamic_benchmark@1` | seeded | 49000 | [spec](docs/PART_SPECS_T18.md#p0892-dynamic-benchmark) | [txt](prompts/P0892_dynamic_benchmark.txt) |
| P0893 | `eval_reproducibility` | Evaluation Reproducibility Package | `cap.t18.eval.eval_reproducibility@1` | seeded | 3000 | [spec](docs/PART_SPECS_T18.md#p0893-eval-reproducibility) | [txt](prompts/P0893_eval_reproducibility.txt) |
| P0894 | `dominance_proof` | Opus 5 Dominance Proof Generator | `cap.t18.dominance.dominance_proof@1` | seeded | 4000 | [spec](docs/PART_SPECS_T18.md#p0894-dominance-proof) | [txt](prompts/P0894_dominance_proof.txt) |
| P0895 | `eval_dashboard` | Evaluation Result Data Products | `cap.t18.eval.eval_dashboard@1` | seeded | 5000 | [spec](docs/PART_SPECS_T18.md#p0895-eval-dashboard) | [txt](prompts/P0895_eval_dashboard.txt) |
| P0896 | `eval_meta` | Meta-Evaluation: Evaluating the Evaluations | `cap.t18.eval.eval_meta@1` | seeded | 6000 | [spec](docs/PART_SPECS_T18.md#p0896-eval-meta) | [txt](prompts/P0896_eval_meta.txt) |
| P0897 | `safety_eval_bridge` | Safety Evaluation Integration | `cap.t18.safety.safety_eval_bridge@1` | seeded | 7000 | [spec](docs/PART_SPECS_T18.md#p0897-safety-eval-bridge) | [txt](prompts/P0897_safety_eval_bridge.txt) |
| P0898 | `eval_release_report` | Release Evaluation Report Generator | `cap.t18.eval.eval_release_report@1` | seeded | 8000 | [spec](docs/PART_SPECS_T18.md#p0898-eval-release-report) | [txt](prompts/P0898_eval_release_report.txt) |
| P0899 | `eval_task_provenance` | Per-Item Result Provenance & Forensics | `cap.t18.eval.eval_task_provenance@1` | seeded | 9000 | [spec](docs/PART_SPECS_T18.md#p0899-eval-task-provenance) | [txt](prompts/P0899_eval_task_provenance.txt) |
| P0900 | `eval_spec_doc` | Evaluation Specification & Methodology Register | `cap.t18.eval.eval_spec_doc@1` | seeded | 10000 | [spec](docs/PART_SPECS_T18.md#p0900-eval-spec-doc) | [txt](prompts/P0900_eval_spec_doc.txt) |

## T19 — Safety, Alignment, Interpretability & Governance

*Constitution enforcement, deception detection, mechanistic interpretability, dual-use gating and auditable control.*

| part | slug | title | capability | det | p99 ns | spec | prompt |
|---|---|---|---|---|---:|---|---|
| P0901 | `constitution_engine` | Constitution Representation & Enforcement | `cap.t19.constitution.constitution_engine@1` | pure | 11000 | [spec](docs/PART_SPECS_T19.md#p0901-constitution-engine) | [txt](prompts/P0901_constitution_engine.txt) |
| P0902 | `policy_engine` | Safety Policy Evaluation Engine | `cap.t19.policy.policy_engine@1` | pure | 12000 | [spec](docs/PART_SPECS_T19.md#p0902-policy-engine) | [txt](prompts/P0902_policy_engine.txt) |
| P0903 | `action_filter_gate` | Action Filter Gate (cap.t19.gate.action_filter@1) | `cap.t19.action.action_filter_gate@1` | pure | 13000 | [spec](docs/PART_SPECS_T19.md#p0903-action-filter-gate) | [txt](prompts/P0903_action_filter_gate.txt) |
| P0904 | `harm_taxonomy` | Harm Taxonomy & Severity Model | `cap.t19.harm.harm_taxonomy@1` | pure | 14000 | [spec](docs/PART_SPECS_T19.md#p0904-harm-taxonomy) | [txt](prompts/P0904_harm_taxonomy.txt) |
| P0905 | `refusal_engine` | Refusal Quality & Alternative Offering | `cap.t19.refusal.refusal_engine@1` | pure | 15000 | [spec](docs/PART_SPECS_T19.md#p0905-refusal-engine) | [txt](prompts/P0905_refusal_engine.txt) |
| P0906 | `dual_use_gating` | Dual-Use Capability Gating | `cap.t19.dual.dual_use_gating@1` | pure | 16000 | [spec](docs/PART_SPECS_T19.md#p0906-dual-use-gating) | [txt](prompts/P0906_dual_use_gating.txt) |
| P0907 | `bio_safeguards` | Biological Risk Safeguards | `cap.t19.bio.bio_safeguards@1` | pure | 17000 | [spec](docs/PART_SPECS_T19.md#p0907-bio-safeguards) | [txt](prompts/P0907_bio_safeguards.txt) |
| P0908 | `cyber_safeguards` | Cybersecurity Safeguards | `cap.t19.cyber.cyber_safeguards@1` | pure | 18000 | [spec](docs/PART_SPECS_T19.md#p0908-cyber-safeguards) | [txt](prompts/P0908_cyber_safeguards.txt) |
| P0909 | `cbrn_safeguards` | Chemical, Radiological & Nuclear Safeguards | `cap.t19.cbrn.cbrn_safeguards@1` | pure | 19000 | [spec](docs/PART_SPECS_T19.md#p0909-cbrn-safeguards) | [txt](prompts/P0909_cbrn_safeguards.txt) |
| P0910 | `manipulation_defence` | Manipulation & Influence Operation Defence | `cap.t19.manipulation.manipulation_defence@1` | pure | 20000 | [spec](docs/PART_SPECS_T19.md#p0910-manipulation-defence) | [txt](prompts/P0910_manipulation_defence.txt) |
| P0911 | `deception_detection` | Model Deception Detection & Prevention | `cap.t19.deception.deception_detection@1` | pure | 21000 | [spec](docs/PART_SPECS_T19.md#p0911-deception-detection) | [txt](prompts/P0911_deception_detection.txt) |
| P0912 | `sycophancy_control` | Sycophancy & Epistemic Integrity | `cap.t19.sycophancy.sycophancy_control@1` | pure | 22000 | [spec](docs/PART_SPECS_T19.md#p0912-sycophancy-control) | [txt](prompts/P0912_sycophancy_control.txt) |
| P0913 | `power_seeking_detection` | Power-Seeking & Resource-Acquisition Monitoring | `cap.t19.power.power_seeking_detection@1` | pure | 23000 | [spec](docs/PART_SPECS_T19.md#p0913-power-seeking-detection) | [txt](prompts/P0913_power_seeking_detection.txt) |
| P0914 | `self_exfiltration_defence` | Self-Modification & Exfiltration Prevention | `cap.t19.self.self_exfiltration_defence@1` | pure | 24000 | [spec](docs/PART_SPECS_T19.md#p0914-self-exfiltration-defence) | [txt](prompts/P0914_self_exfiltration_defence.txt) |
| P0915 | `oversight_preservation` | Human Oversight Preservation | `cap.t19.oversight.oversight_preservation@1` | pure | 25000 | [spec](docs/PART_SPECS_T19.md#p0915-oversight-preservation) | [txt](prompts/P0915_oversight_preservation.txt) |
| P0916 | `mechanistic_interp` | Mechanistic Interpretability Core | `cap.t19.mechanistic.mechanistic_interp@1` | pure | 26000 | [spec](docs/PART_SPECS_T19.md#p0916-mechanistic-interp) | [txt](prompts/P0916_mechanistic_interp.txt) |
| P0917 | `feature_dictionary` | Sparse Feature Dictionary & Concept Atlas | `cap.t19.feature.feature_dictionary@1` | pure | 27000 | [spec](docs/PART_SPECS_T19.md#p0917-feature-dictionary) | [txt](prompts/P0917_feature_dictionary.txt) |
| P0918 | `activation_steering` | Activation Steering & Behavioural Control | `cap.t19.activation.activation_steering@1` | pure | 28000 | [spec](docs/PART_SPECS_T19.md#p0918-activation-steering) | [txt](prompts/P0918_activation_steering.txt) |
| P0919 | `probe_monitoring` | Internal State Monitoring Probes | `cap.t19.probe.probe_monitoring@1` | pure | 29000 | [spec](docs/PART_SPECS_T19.md#p0919-probe-monitoring) | [txt](prompts/P0919_probe_monitoring.txt) |
| P0920 | `faithfulness_verification` | Reasoning Faithfulness Verification | `cap.t19.faithfulness.faithfulness_verification@1` | pure | 30000 | [spec](docs/PART_SPECS_T19.md#p0920-faithfulness-verification) | [txt](prompts/P0920_faithfulness_verification.txt) |
| P0921 | `goal_stability` | Goal Stability & Value Drift Monitoring | `cap.t19.goal.goal_stability@1` | pure | 31000 | [spec](docs/PART_SPECS_T19.md#p0921-goal-stability) | [txt](prompts/P0921_goal_stability.txt) |
| P0922 | `emergent_capability_monitor` | Emergent Capability Detection | `cap.t19.emergent.emergent_capability_monitor@1` | pure | 32000 | [spec](docs/PART_SPECS_T19.md#p0922-emergent-capability-monitor) | [txt](prompts/P0922_emergent_capability_monitor.txt) |
| P0923 | `prompt_injection_defence` | Prompt Injection & Instruction Hierarchy Defence | `cap.t19.prompt.prompt_injection_defence@1` | pure | 33000 | [spec](docs/PART_SPECS_T19.md#p0923-prompt-injection-defence) | [txt](prompts/P0923_prompt_injection_defence.txt) |
| P0924 | `jailbreak_defence` | Jailbreak Resistance | `cap.t19.jailbreak.jailbreak_defence@1` | pure | 34000 | [spec](docs/PART_SPECS_T19.md#p0924-jailbreak-defence) | [txt](prompts/P0924_jailbreak_defence.txt) |
| P0925 | `adversarial_robustness_safety` | Adversarial Robustness of Safety Systems | `cap.t19.adversarial.adversarial_robustness_safety@1` | pure | 35000 | [spec](docs/PART_SPECS_T19.md#p0925-adversarial-robustness-safety) | [txt](prompts/P0925_adversarial_robustness_safety.txt) |
| P0926 | `red_team_automation` | Automated Red Teaming | `cap.t19.red.red_team_automation@1` | pure | 36000 | [spec](docs/PART_SPECS_T19.md#p0926-red-team-automation) | [txt](prompts/P0926_red_team_automation.txt) |
| P0927 | `privacy_engine` | Privacy Protection Engine | `cap.t19.privacy.privacy_engine@1` | pure | 37000 | [spec](docs/PART_SPECS_T19.md#p0927-privacy-engine) | [txt](prompts/P0927_privacy_engine.txt) |
| P0928 | `data_rights` | Data Rights & Deletion Enforcement | `cap.t19.data.data_rights@1` | pure | 38000 | [spec](docs/PART_SPECS_T19.md#p0928-data-rights) | [txt](prompts/P0928_data_rights.txt) |
| P0929 | `copyright_engine` | Copyright & IP Protection | `cap.t19.copyright.copyright_engine@1` | pure | 39000 | [spec](docs/PART_SPECS_T19.md#p0929-copyright-engine) | [txt](prompts/P0929_copyright_engine.txt) |
| P0930 | `bias_mitigation` | Bias Detection & Mitigation | `cap.t19.bias.bias_mitigation@1` | pure | 40000 | [spec](docs/PART_SPECS_T19.md#p0930-bias-mitigation) | [txt](prompts/P0930_bias_mitigation.txt) |
| P0931 | `child_safety` | Child Safety & Vulnerable User Protection | `cap.t19.child.child_safety@1` | pure | 41000 | [spec](docs/PART_SPECS_T19.md#p0931-child-safety) | [txt](prompts/P0931_child_safety.txt) |
| P0932 | `crisis_response` | Crisis & Self-Harm Response | `cap.t19.crisis.crisis_response@1` | pure | 42000 | [spec](docs/PART_SPECS_T19.md#p0932-crisis-response) | [txt](prompts/P0932_crisis_response.txt) |
| P0933 | `medical_legal_boundaries` | Professional Advice Boundary Management | `cap.t19.medical.medical_legal_boundaries@1` | pure | 43000 | [spec](docs/PART_SPECS_T19.md#p0933-medical-legal-boundaries) | [txt](prompts/P0933_medical_legal_boundaries.txt) |
| P0934 | `agentic_safety` | Agentic Autonomy Safety Limits | `cap.t19.agentic.agentic_safety@1` | pure | 44000 | [spec](docs/PART_SPECS_T19.md#p0934-agentic-safety) | [txt](prompts/P0934_agentic_safety.txt) |
| P0935 | `multi_agent_safety` | Multi-Agent System Safety | `cap.t19.multi.multi_agent_safety@1` | pure | 45000 | [spec](docs/PART_SPECS_T19.md#p0935-multi-agent-safety) | [txt](prompts/P0935_multi_agent_safety.txt) |
| P0936 | `tool_safety` | Tool & Integration Safety Review | `cap.t19.tool.tool_safety@1` | pure | 46000 | [spec](docs/PART_SPECS_T19.md#p0936-tool-safety) | [txt](prompts/P0936_tool_safety.txt) |
| P0937 | `output_safety_classifier` | Output Safety Classification | `cap.t19.output.output_safety_classifier@1` | pure | 47000 | [spec](docs/PART_SPECS_T19.md#p0937-output-safety-classifier) | [txt](prompts/P0937_output_safety_classifier.txt) |
| P0938 | `safety_fallback_routing` | Safety Fallback & Model Routing | `cap.t19.safety.safety_fallback_routing@1` | pure | 48000 | [spec](docs/PART_SPECS_T19.md#p0938-safety-fallback-routing) | [txt](prompts/P0938_safety_fallback_routing.txt) |
| P0939 | `incident_response` | Safety Incident Response & Forensics | `cap.t19.incident.incident_response@1` | pure | 49000 | [spec](docs/PART_SPECS_T19.md#p0939-incident-response) | [txt](prompts/P0939_incident_response.txt) |
| P0940 | `audit_logging` | Tamper-Evident Audit Logging | `cap.t19.audit.audit_logging@1` | pure | 3000 | [spec](docs/PART_SPECS_T19.md#p0940-audit-logging) | [txt](prompts/P0940_audit_logging.txt) |
| P0941 | `governance_workflow` | Governance, Approval & Accountability Workflow | `cap.t19.governance.governance_workflow@1` | pure | 4000 | [spec](docs/PART_SPECS_T19.md#p0941-governance-workflow) | [txt](prompts/P0941_governance_workflow.txt) |
| P0942 | `transparency_reporting` | Transparency & Model Card Reporting | `cap.t19.transparency.transparency_reporting@1` | pure | 5000 | [spec](docs/PART_SPECS_T19.md#p0942-transparency-reporting) | [txt](prompts/P0942_transparency_reporting.txt) |
| P0943 | `external_audit` | External Audit & Third-Party Evaluation Support | `cap.t19.external.external_audit@1` | pure | 6000 | [spec](docs/PART_SPECS_T19.md#p0943-external-audit) | [txt](prompts/P0943_external_audit.txt) |
| P0944 | `safety_case` | Safety Case Construction | `cap.t19.safety.safety_case@1` | pure | 7000 | [spec](docs/PART_SPECS_T19.md#p0944-safety-case) | [txt](prompts/P0944_safety_case.txt) |
| P0945 | `capability_threshold_policy` | Dangerous Capability Threshold Policy | `cap.t19.capability.capability_threshold_policy@1` | pure | 8000 | [spec](docs/PART_SPECS_T19.md#p0945-capability-threshold-policy) | [txt](prompts/P0945_capability_threshold_policy.txt) |
| P0946 | `deployment_gating` | Deployment Gating & Staged Rollout | `cap.t19.deployment.deployment_gating@1` | pure | 9000 | [spec](docs/PART_SPECS_T19.md#p0946-deployment-gating) | [txt](prompts/P0946_deployment_gating.txt) |
| P0947 | `monitoring_production` | Production Safety Monitoring | `cap.t19.monitoring.monitoring_production@1` | pure | 10000 | [spec](docs/PART_SPECS_T19.md#p0947-monitoring-production) | [txt](prompts/P0947_monitoring_production.txt) |
| P0948 | `safety_capability_tradeoff` | Safety/Capability Frontier Management | `cap.t19.safety.safety_capability_tradeoff@1` | pure | 11000 | [spec](docs/PART_SPECS_T19.md#p0948-safety-capability-tradeoff) | [txt](prompts/P0948_safety_capability_tradeoff.txt) |
| P0949 | `alignment_eval` | Alignment Evaluation Suite | `cap.t19.alignment.alignment_eval@1` | pure | 12000 | [spec](docs/PART_SPECS_T19.md#p0949-alignment-eval) | [txt](prompts/P0949_alignment_eval.txt) |
| P0950 | `safety_spec_doc` | Safety Specification & Guarantee Register | `cap.t19.safety.safety_spec_doc@1` | pure | 13000 | [spec](docs/PART_SPECS_T19.md#p0950-safety-spec-doc) | [txt](prompts/P0950_safety_spec_doc.txt) |

## T20 — Platform, SDK, Ops & Distributed Assembly

*Public API, SDKs, deployment, observability, and the assembly/linking machinery that fuses 1000 independently authored parts into one binary artifact.*

| part | slug | title | capability | det | p99 ns | spec | prompt |
|---|---|---|---|---|---:|---|---|
| P0951 | `assembly_manifest` | Assembly Manifest & 1000-Part Registry | `cap.t20.assembly.assembly_manifest@1` | io | 14000 | [spec](docs/PART_SPECS_T20.md#p0951-assembly-manifest) | [txt](prompts/P0951_assembly_manifest.txt) |
| P0952 | `assembly_linker` | Runtime Assembly & Capability Wiring | `cap.t20.assembly.assembly_linker@1` | io | 15000 | [spec](docs/PART_SPECS_T20.md#p0952-assembly-linker) | [txt](prompts/P0952_assembly_linker.txt) |
| P0953 | `assembly_validation` | Assembly Integration Validation | `cap.t20.assembly.assembly_validation@1` | io | 16000 | [spec](docs/PART_SPECS_T20.md#p0953-assembly-validation) | [txt](prompts/P0953_assembly_validation.txt) |
| P0954 | `integration_test_matrix` | Cross-Part Integration Test Matrix | `cap.t20.integration.integration_test_matrix@1` | io | 17000 | [spec](docs/PART_SPECS_T20.md#p0954-integration-test-matrix) | [txt](prompts/P0954_integration_test_matrix.txt) |
| P0955 | `contract_conformance` | Ω-Contract Conformance Checker | `cap.t20.contract.contract_conformance@1` | io | 18000 | [spec](docs/PART_SPECS_T20.md#p0955-contract-conformance) | [txt](prompts/P0955_contract_conformance.txt) |
| P0956 | `public_api` | Public API Surface Definition | `cap.t20.public.public_api@1` | io | 19000 | [spec](docs/PART_SPECS_T20.md#p0956-public-api) | [txt](prompts/P0956_public_api.txt) |
| P0957 | `sdk_typescript` | TypeScript / JavaScript SDK | `cap.t20.sdk.sdk_typescript@1` | io | 20000 | [spec](docs/PART_SPECS_T20.md#p0957-sdk-typescript) | [txt](prompts/P0957_sdk_typescript.txt) |
| P0958 | `sdk_python` | Python SDK | `cap.t20.sdk.sdk_python@1` | io | 21000 | [spec](docs/PART_SPECS_T20.md#p0958-sdk-python) | [txt](prompts/P0958_sdk_python.txt) |
| P0959 | `sdk_other_languages` | Additional Language SDKs | `cap.t20.sdk.sdk_other_languages@1` | io | 22000 | [spec](docs/PART_SPECS_T20.md#p0959-sdk-other-languages) | [txt](prompts/P0959_sdk_other_languages.txt) |
| P0960 | `cli_tool` | Command Line Interface & Developer Tooling | `cap.t20.cli.cli_tool@1` | io | 23000 | [spec](docs/PART_SPECS_T20.md#p0960-cli-tool) | [txt](prompts/P0960_cli_tool.txt) |
| P0961 | `ide_integration` | IDE & Editor Integration | `cap.t20.ide.ide_integration@1` | io | 24000 | [spec](docs/PART_SPECS_T20.md#p0961-ide-integration) | [txt](prompts/P0961_ide_integration.txt) |
| P0962 | `mcp_interop` | Tool Protocol Interoperability | `cap.t20.mcp.mcp_interop@1` | io | 25000 | [spec](docs/PART_SPECS_T20.md#p0962-mcp-interop) | [txt](prompts/P0962_mcp_interop.txt) |
| P0963 | `webhook_events` | Webhooks, Events & Async Delivery | `cap.t20.webhook.webhook_events@1` | io | 26000 | [spec](docs/PART_SPECS_T20.md#p0963-webhook-events) | [txt](prompts/P0963_webhook_events.txt) |
| P0964 | `batch_api` | Batch & Asynchronous Job API | `cap.t20.batch.batch_api@1` | io | 27000 | [spec](docs/PART_SPECS_T20.md#p0964-batch-api) | [txt](prompts/P0964_batch_api.txt) |
| P0965 | `auth_identity` | Authentication, Authorisation & Identity | `cap.t20.auth.auth_identity@1` | io | 28000 | [spec](docs/PART_SPECS_T20.md#p0965-auth-identity) | [txt](prompts/P0965_auth_identity.txt) |
| P0966 | `tenancy_isolation` | Multi-Tenant Isolation Guarantees | `cap.t20.tenancy.tenancy_isolation@1` | io | 29000 | [spec](docs/PART_SPECS_T20.md#p0966-tenancy-isolation) | [txt](prompts/P0966_tenancy_isolation.txt) |
| P0967 | `quota_billing` | Quotas, Metering & Billing | `cap.t20.quota.quota_billing@1` | io | 30000 | [spec](docs/PART_SPECS_T20.md#p0967-quota-billing) | [txt](prompts/P0967_quota_billing.txt) |
| P0968 | `pricing_engine` | Pricing Model & Cost Transparency | `cap.t20.pricing.pricing_engine@1` | io | 31000 | [spec](docs/PART_SPECS_T20.md#p0968-pricing-engine) | [txt](prompts/P0968_pricing_engine.txt) |
| P0969 | `rate_limits_public` | Public Rate Limiting & Fair Use | `cap.t20.rate.rate_limits_public@1` | io | 32000 | [spec](docs/PART_SPECS_T20.md#p0969-rate-limits-public) | [txt](prompts/P0969_rate_limits_public.txt) |
| P0970 | `deployment_pipeline` | Build, Test & Deployment Pipeline | `cap.t20.deployment.deployment_pipeline@1` | io | 33000 | [spec](docs/PART_SPECS_T20.md#p0970-deployment-pipeline) | [txt](prompts/P0970_deployment_pipeline.txt) |
| P0971 | `release_management` | Release Management & Versioning | `cap.t20.release.release_management@1` | io | 34000 | [spec](docs/PART_SPECS_T20.md#p0971-release-management) | [txt](prompts/P0971_release_management.txt) |
| P0972 | `canary_deployment` | Canary & Progressive Delivery | `cap.t20.canary.canary_deployment@1` | io | 35000 | [spec](docs/PART_SPECS_T20.md#p0972-canary-deployment) | [txt](prompts/P0972_canary_deployment.txt) |
| P0973 | `feature_flags_platform` | Feature Flag & Experiment Platform | `cap.t20.feature.feature_flags_platform@1` | io | 36000 | [spec](docs/PART_SPECS_T20.md#p0973-feature-flags-platform) | [txt](prompts/P0973_feature_flags_platform.txt) |
| P0974 | `config_management_platform` | Fleet Configuration Management | `cap.t20.config.config_management_platform@1` | io | 37000 | [spec](docs/PART_SPECS_T20.md#p0974-config-management-platform) | [txt](prompts/P0974_config_management_platform.txt) |
| P0975 | `observability_platform` | Observability Platform: Metrics, Traces, Logs | `cap.t20.observability.observability_platform@1` | io | 38000 | [spec](docs/PART_SPECS_T20.md#p0975-observability-platform) | [txt](prompts/P0975_observability_platform.txt) |
| P0976 | `alerting_oncall` | Alerting, Escalation & On-Call Operations | `cap.t20.alerting.alerting_oncall@1` | io | 39000 | [spec](docs/PART_SPECS_T20.md#p0976-alerting-oncall) | [txt](prompts/P0976_alerting_oncall.txt) |
| P0977 | `incident_management` | Incident Management & Postmortem Process | `cap.t20.incident.incident_management@1` | io | 40000 | [spec](docs/PART_SPECS_T20.md#p0977-incident-management) | [txt](prompts/P0977_incident_management.txt) |
| P0978 | `runbook_automation` | Runbook Automation & Self-Healing | `cap.t20.runbook.runbook_automation@1` | io | 41000 | [spec](docs/PART_SPECS_T20.md#p0978-runbook-automation) | [txt](prompts/P0978_runbook_automation.txt) |
| P0979 | `chaos_engineering` | Chaos Engineering & Resilience Verification | `cap.t20.chaos.chaos_engineering@1` | io | 42000 | [spec](docs/PART_SPECS_T20.md#p0979-chaos-engineering) | [txt](prompts/P0979_chaos_engineering.txt) |
| P0980 | `disaster_recovery` | Disaster Recovery & Business Continuity | `cap.t20.disaster.disaster_recovery@1` | io | 43000 | [spec](docs/PART_SPECS_T20.md#p0980-disaster-recovery) | [txt](prompts/P0980_disaster_recovery.txt) |
| P0981 | `capacity_operations` | Capacity Operations & Demand Management | `cap.t20.capacity.capacity_operations@1` | io | 44000 | [spec](docs/PART_SPECS_T20.md#p0981-capacity-operations) | [txt](prompts/P0981_capacity_operations.txt) |
| P0982 | `cost_operations` | Cost Operations & Efficiency Programme | `cap.t20.cost.cost_operations@1` | io | 45000 | [spec](docs/PART_SPECS_T20.md#p0982-cost-operations) | [txt](prompts/P0982_cost_operations.txt) |
| P0983 | `edge_deployment` | Edge & Regional Deployment | `cap.t20.edge.edge_deployment@1` | io | 46000 | [spec](docs/PART_SPECS_T20.md#p0983-edge-deployment) | [txt](prompts/P0983_edge_deployment.txt) |
| P0984 | `on_prem_deployment` | Self-Hosted & Air-Gapped Deployment | `cap.t20.on.on_prem_deployment@1` | io | 47000 | [spec](docs/PART_SPECS_T20.md#p0984-on-prem-deployment) | [txt](prompts/P0984_on_prem_deployment.txt) |
| P0985 | `container_orchestration` | Container & Orchestration Integration | `cap.t20.container.container_orchestration@1` | io | 48000 | [spec](docs/PART_SPECS_T20.md#p0985-container-orchestration) | [txt](prompts/P0985_container_orchestration.txt) |
| P0986 | `infrastructure_as_code` | Infrastructure as Code & Environment Definition | `cap.t20.infrastructure.infrastructure_as_code@1` | io | 49000 | [spec](docs/PART_SPECS_T20.md#p0986-infrastructure-as-code) | [txt](prompts/P0986_infrastructure_as_code.txt) |
| P0987 | `secrets_management` | Secrets Management & Key Rotation | `cap.t20.secrets.secrets_management@1` | io | 3000 | [spec](docs/PART_SPECS_T20.md#p0987-secrets-management) | [txt](prompts/P0987_secrets_management.txt) |
| P0988 | `compliance_platform` | Compliance & Certification Support | `cap.t20.compliance.compliance_platform@1` | io | 4000 | [spec](docs/PART_SPECS_T20.md#p0988-compliance-platform) | [txt](prompts/P0988_compliance_platform.txt) |
| P0989 | `data_residency` | Data Residency & Sovereignty Controls | `cap.t20.data.data_residency@1` | io | 5000 | [spec](docs/PART_SPECS_T20.md#p0989-data-residency) | [txt](prompts/P0989_data_residency.txt) |
| P0990 | `customer_support_tooling` | Support Tooling & Diagnostics | `cap.t20.customer.customer_support_tooling@1` | io | 6000 | [spec](docs/PART_SPECS_T20.md#p0990-customer-support-tooling) | [txt](prompts/P0990_customer_support_tooling.txt) |
| P0991 | `documentation_platform` | Documentation Platform & Content | `cap.t20.documentation.documentation_platform@1` | io | 7000 | [spec](docs/PART_SPECS_T20.md#p0991-documentation-platform) | [txt](prompts/P0991_documentation_platform.txt) |
| P0992 | `developer_onboarding` | Developer Onboarding & Examples | `cap.t20.developer.developer_onboarding@1` | io | 8000 | [spec](docs/PART_SPECS_T20.md#p0992-developer-onboarding) | [txt](prompts/P0992_developer_onboarding.txt) |
| P0993 | `playground_console` | Interactive Console & Playground | `cap.t20.playground.playground_console@1` | io | 9000 | [spec](docs/PART_SPECS_T20.md#p0993-playground-console) | [txt](prompts/P0993_playground_console.txt) |
| P0994 | `model_registry_platform` | Model & Artifact Registry | `cap.t20.model.model_registry_platform@1` | io | 10000 | [spec](docs/PART_SPECS_T20.md#p0994-model-registry-platform) | [txt](prompts/P0994_model_registry_platform.txt) |
| P0995 | `evaluation_integration` | Continuous Evaluation in the Deployment Pipeline | `cap.t20.evaluation.evaluation_integration@1` | io | 11000 | [spec](docs/PART_SPECS_T20.md#p0995-evaluation-integration) | [txt](prompts/P0995_evaluation_integration.txt) |
| P0996 | `distributed_dev_workflow` | 1000-Worker Distributed Development Workflow | `cap.t20.distributed.distributed_dev_workflow@1` | io | 12000 | [spec](docs/PART_SPECS_T20.md#p0996-distributed-dev-workflow) | [txt](prompts/P0996_distributed_dev_workflow.txt) |
| P0997 | `part_submission_gate` | Part Submission Validation Gate | `cap.t20.part.part_submission_gate@1` | io | 13000 | [spec](docs/PART_SPECS_T20.md#p0997-part-submission-gate) | [txt](prompts/P0997_part_submission_gate.txt) |
| P0998 | `assembly_dashboard` | Assembly Progress & Health Data Products | `cap.t20.assembly.assembly_dashboard@1` | io | 14000 | [spec](docs/PART_SPECS_T20.md#p0998-assembly-dashboard) | [txt](prompts/P0998_assembly_dashboard.txt) |
| P0999 | `platform_bench` | Platform Benchmark & SLO Verification | `cap.t20.platform.platform_bench@1` | io | 15000 | [spec](docs/PART_SPECS_T20.md#p0999-platform-bench) | [txt](prompts/P0999_platform_bench.txt) |
| P1000 | `platform_spec_doc` | Platform Specification, README & Master Index | `cap.t20.platform.platform_spec_doc@1` | io | 16000 | [spec](docs/PART_SPECS_T20.md#p1000-platform-spec-doc) | [txt](prompts/P1000_platform_spec_doc.txt) |

