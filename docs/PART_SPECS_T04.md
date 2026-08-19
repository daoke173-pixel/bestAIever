# HYPERION-Ω — Part specifications · T04 · Hardware Abstraction & Interconnect

> Contract: **Ω-CONTRACT v1.0.0-frozen** · 50 parts · 250,000 lines of code · language: Rust 1.86

**Tier mission.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Benchmarks this tier is accountable for.** SWE-bench Verified

**Tier dependencies.** T01, T02

Each part below is built by exactly one isolated Opus 5 worker that sees only: this specification, the frozen Ω-Contract, and its own prompt. Workers never see each other's files. Link-compatibility comes from the contract, not from coordination.

| part | slug | title | capability |
|---|---|---|---|
| [P0151](#p0151-device-abstraction) | `device_abstraction` | Device Abstraction Layer | `cap.t04.device.device_abstraction@1` |
| [P0152](#p0152-topology-discovery) | `topology_discovery` | Interconnect Topology Discovery | `cap.t04.topology.topology_discovery@1` |
| [P0153](#p0153-collective-global) | `collective_global` | Multi-Node Collective Library | `cap.t04.collective.collective_global@1` |
| [P0154](#p0154-rdma-transport) | `rdma_transport` | RDMA & Zero-Copy Network Transport | `cap.t04.rdma.rdma_transport@1` |
| [P0155](#p0155-tcp-fallback) | `tcp_fallback` | Reliable TCP/QUIC Transport Fallback | `cap.t04.tcp.tcp_fallback@1` |
| [P0156](#p0156-comm-scheduler) | `comm_scheduler` | Communication Scheduling & Prioritisation | `cap.t04.comm.comm_scheduler@1` |
| [P0157](#p0157-expert-parallel-fabric) | `expert_parallel_fabric` | Expert-Parallel Routing Fabric | `cap.t04.expert.expert_parallel_fabric@1` |
| [P0158](#p0158-sequence-parallel-fabric) | `sequence_parallel_fabric` | Sequence & Context Parallel Fabric | `cap.t04.sequence.sequence_parallel_fabric@1` |
| [P0159](#p0159-pipeline-fabric) | `pipeline_fabric` | Pipeline Stage Transport | `cap.t04.pipeline.pipeline_fabric@1` |
| [P0160](#p0160-param-server-shard) | `param_server_shard` | Sharded Parameter Store | `cap.t04.param.param_server_shard@1` |
| [P0161](#p0161-weight-streaming) | `weight_streaming` | Weight Streaming & Tiering | `cap.t04.weight.weight_streaming@1` |
| [P0162](#p0162-nvme-offload) | `nvme_offload` | NVMe / Storage Offload Engine | `cap.t04.nvme.nvme_offload@1` |
| [P0163](#p0163-host-pinned-pool) | `host_pinned_pool` | Host Pinned Memory Manager | `cap.t04.host.host_pinned_pool@1` |
| [P0164](#p0164-device-health) | `device_health` | Device Health Monitoring & Prediction | `cap.t04.device.device_health@1` |
| [P0165](#p0165-fault-domains) | `fault_domains` | Fault Domain Modelling & Placement | `cap.t04.fault.fault_domains@1` |
| [P0166](#p0166-elastic-scaling) | `elastic_scaling` | Elastic Membership & Rescaling | `cap.t04.elastic.elastic_scaling@1` |
| [P0167](#p0167-checkpoint-transport) | `checkpoint_transport` | Distributed Checkpoint IO | `cap.t04.checkpoint.checkpoint_transport@1` |
| [P0168](#p0168-failure-recovery) | `failure_recovery` | Failure Detection & Fast Restart | `cap.t04.failure.failure_recovery@1` |
| [P0169](#p0169-straggler-mitigation) | `straggler_mitigation` | Straggler Detection & Mitigation | `cap.t04.straggler.straggler_mitigation@1` |
| [P0170](#p0170-power-cluster) | `power_cluster` | Cluster Power & Energy Governance | `cap.t04.power.power_cluster@1` |
| [P0171](#p0171-network-congestion) | `network_congestion` | Congestion Control & Traffic Engineering | `cap.t04.network.network_congestion@1` |
| [P0172](#p0172-multi-tenancy) | `multi_tenancy` | Multi-Tenant Isolation & QoS | `cap.t04.multi.multi_tenancy@1` |
| [P0173](#p0173-device-virtualisation) | `device_virtualisation` | Device Partitioning & Virtualisation | `cap.t04.device.device_virtualisation@1` |
| [P0174](#p0174-heterogeneous-pool) | `heterogeneous_pool` | Heterogeneous Hardware Pooling | `cap.t04.heterogeneous.heterogeneous_pool@1` |
| [P0175](#p0175-edge-runtime) | `edge_runtime` | Edge & On-Device Runtime | `cap.t04.edge.edge_runtime@1` |
| [P0176](#p0176-cloud-provisioner) | `cloud_provisioner` | Capacity Provisioning & Placement Planner | `cap.t04.cloud.cloud_provisioner@1` |
| [P0177](#p0177-scheduler-cluster) | `scheduler_cluster` | Cluster Job Scheduler Integration | `cap.t04.scheduler.scheduler_cluster@1` |
| [P0178](#p0178-service-discovery) | `service_discovery` | Service Discovery & Membership Registry | `cap.t04.service.service_discovery@1` |
| [P0179](#p0179-consensus-core) | `consensus_core` | Lightweight Consensus & Leader Election | `cap.t04.consensus.consensus_core@1` |
| [P0180](#p0180-distributed-lock) | `distributed_lock` | Distributed Locking & Fencing | `cap.t04.distributed.distributed_lock@1` |
| [P0181](#p0181-clock-sync) | `clock_sync` | Cluster Clock Synchronisation | `cap.t04.clock.clock_sync@1` |
| [P0182](#p0182-data-locality) | `data_locality` | Data Locality & Cache Affinity Router | `cap.t04.data.data_locality@1` |
| [P0183](#p0183-bandwidth-accounting) | `bandwidth_accounting` | Bandwidth & Interconnect Accounting | `cap.t04.bandwidth.bandwidth_accounting@1` |
| [P0184](#p0184-secure-channel) | `secure_channel` | Encrypted Inter-Node Channels | `cap.t04.secure.secure_channel@1` |
| [P0185](#p0185-confidential-compute) | `confidential_compute` | Confidential Computing Integration | `cap.t04.confidential.confidential_compute@1` |
| [P0186](#p0186-firmware-compat) | `firmware_compat` | Driver & Firmware Compatibility Matrix | `cap.t04.firmware.firmware_compat@1` |
| [P0187](#p0187-nic-offload) | `nic_offload` | Network Offload & In-Network Compute | `cap.t04.nic.nic_offload@1` |
| [P0188](#p0188-device-reset) | `device_reset` | Device Reset & Isolation Recovery | `cap.t04.device.device_reset@1` |
| [P0189](#p0189-numa-topology-cluster) | `numa_topology_cluster` | Host-Level Resource Topology Binding | `cap.t04.numa.numa_topology_cluster@1` |
| [P0190](#p0190-telemetry-transport) | `telemetry_transport` | High-Volume Telemetry Pipeline | `cap.t04.telemetry.telemetry_transport@1` |
| [P0191](#p0191-simulation-cluster) | `simulation_cluster` | Cluster Simulator | `cap.t04.simulation.simulation_cluster@1` |
| [P0192](#p0192-capacity-benchmarks) | `capacity_benchmarks` | Distributed Benchmark Suite | `cap.t04.capacity.capacity_benchmarks@1` |
| [P0193](#p0193-cost-model-cluster) | `cost_model_cluster` | Total-Cost-of-Serving Model | `cap.t04.cost.cost_model_cluster@1` |
| [P0194](#p0194-request-router) | `request_router` | Global Request Router & Load Balancer | `cap.t04.request.request_router@1` |
| [P0195](#p0195-region-failover) | `region_failover` | Multi-Region Replication & Failover | `cap.t04.region.region_failover@1` |
| [P0196](#p0196-hw-sw-codesign) | `hw_sw_codesign` | Hardware/Software Co-Design Specification | `cap.t04.hw.hw_sw_codesign@1` |
| [P0197](#p0197-green-scheduling) | `green_scheduling` | Carbon-Aware Scheduling | `cap.t04.green.green_scheduling@1` |
| [P0198](#p0198-device-alloc-fair) | `device_alloc_fair` | Fair-Share Device Allocation | `cap.t04.device.device_alloc_fair@1` |
| [P0199](#p0199-hpc-interop) | `hpc_interop` | HPC & Scientific Stack Interoperability | `cap.t04.hpc.hpc_interop@1` |
| [P0200](#p0200-provision-verify) | `provision_verify` | Node Admission & Continuous Verification | `cap.t04.provision.provision_verify@1` |

---

### P0151 · `device_abstraction` — Device Abstraction Layer

| field | value |
|---|---|
| part id | `P0151` (1/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0151_device_abstraction.rs` |
| module path | `hyperion.t04.hardware.device_abstraction` |
| capability published | `cap.t04.device.device_abstraction@1` |
| determinism class | `io` |
| p99 latency budget | 13000 ns (13 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0151_device_abstraction.txt`](prompts/P0151_device_abstraction.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0151-device-abstraction) |

**Mission.** One uniform device interface over every accelerator vendor and generation.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **device enumeration, capability probing and feature-flag normalisation** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **context/queue/event lifecycle with RAII-style safety** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **vendor backend trait with two reference implementations**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **conformance suite every backend must pass** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t04.device.device_abstraction@1`
- `cap.t04.device.device_abstraction.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t01.string.string_interning@1` | use the in-file conservative substitute for `string_interning` (documented, slower, lower quality) and set `degraded['string_interning']='local'` |
| `cap.t02.fused.fused_moe_kernel@1` | use the in-file conservative substitute for `fused_moe_kernel` (documented, slower, lower quality) and set `degraded['fused_moe_kernel']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - device enumeration, capability probing and feature-flag normalis | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - context/queue/event lifecycle with RAII-style safety | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - vendor backend trait with two reference implementations | 520 | Third required mechanism. |
| 6 | Core implementation D - conformance suite every backend must pass | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0151_device_abstraction.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.device.device_abstraction@1`.
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

### P0152 · `topology_discovery` — Interconnect Topology Discovery

| field | value |
|---|---|
| part id | `P0152` (2/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0152_topology_discovery.rs` |
| module path | `hyperion.t04.hardware.topology_discovery` |
| capability published | `cap.t04.topology.topology_discovery@1` |
| determinism class | `io` |
| p99 latency budget | 14000 ns (14 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0152_topology_discovery.txt`](prompts/P0152_topology_discovery.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0152-topology-discovery) |

**Mission.** Builds an exact machine graph: links, bandwidths, latencies, failure domains.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **PCIe/NVLink/fabric enumeration with bandwidth probing** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **multi-node topology assembly from per-node views**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **distance and bisection-bandwidth computation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **topology-vs-measurement validation and anomaly flagging** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t04.topology.topology_discovery@1`
- `cap.t04.topology.topology_discovery.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.device.device_abstraction@1` | use the in-file conservative substitute for `device_abstraction` (documented, slower, lower quality) and set `degraded['device_abstraction']='local'` |
| `cap.t01.property.property_gen@1` | use the in-file conservative substitute for `property_gen` (documented, slower, lower quality) and set `degraded['property_gen']='local'` |
| `cap.t02.numa.numa_placement@1` | use the in-file conservative substitute for `numa_placement` (documented, slower, lower quality) and set `degraded['numa_placement']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - PCIe/NVLink/fabric enumeration with bandwidth probing | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - multi-node topology assembly from per-node views | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - distance and bisection-bandwidth computation | 520 | Third required mechanism. |
| 6 | Core implementation D - topology-vs-measurement validation and anomaly flagging | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0152_topology_discovery.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.topology.topology_discovery@1`.
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

### P0153 · `collective_global` — Multi-Node Collective Library

| field | value |
|---|---|
| part id | `P0153` (3/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0153_collective_global.rs` |
| module path | `hyperion.t04.hardware.collective_global` |
| capability published | `cap.t04.collective.collective_global@1` |
| determinism class | `io` |
| p99 latency budget | 15000 ns (15 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0153_collective_global.txt`](prompts/P0153_collective_global.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0153-collective-global) |

**Mission.** Cluster-scale all-reduce/all-gather/all-to-all with topology awareness.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **hierarchical algorithms (intra-node then inter-node) with size-based selection**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **all-to-all optimisation for expert parallelism** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **deterministic reduction ordering across thousands of ranks** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **scaling efficiency measurement to 100k ranks** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t04.collective.collective_global@1`
- `cap.t04.collective.collective_global.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.topology.topology_discovery@1` | use the in-file conservative substitute for `topology_discovery` (documented, slower, lower quality) and set `degraded['topology_discovery']='local'` |
| `cap.t01.link.link_validator@1` | use the in-file conservative substitute for `link_validator` (documented, slower, lower quality) and set `degraded['link_validator']='local'` |
| `cap.t02.kernel.kernel_fusion_rules@1` | use the in-file conservative substitute for `kernel_fusion_rules` (documented, slower, lower quality) and set `degraded['kernel_fusion_rules']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - hierarchical algorithms (intra-node then inter-node) with size-b | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - all-to-all optimisation for expert parallelism | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - deterministic reduction ordering across thousands of ranks | 520 | Third required mechanism. |
| 6 | Core implementation D - scaling efficiency measurement to 100k ranks | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0153_collective_global.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.collective.collective_global@1`.
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

### P0154 · `rdma_transport` — RDMA & Zero-Copy Network Transport

| field | value |
|---|---|
| part id | `P0154` (4/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0154_rdma_transport.rs` |
| module path | `hyperion.t04.hardware.rdma_transport` |
| capability published | `cap.t04.rdma.rdma_transport@1` |
| determinism class | `io` |
| p99 latency budget | 16000 ns (16 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0154_rdma_transport.txt`](prompts/P0154_rdma_transport.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0154-rdma-transport) |

**Mission.** The lowest-latency path for tensors between machines.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **queue-pair management, memory registration and completion handling** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **zero-copy send/recv with pre-registered buffer pools** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **congestion control interaction and loss recovery** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **latency/bandwidth benchmark versus hardware line rate**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t04.rdma.rdma_transport@1`
- `cap.t04.rdma.rdma_transport.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.collective.collective_global@1` | use the in-file conservative substitute for `collective_global` (documented, slower, lower quality) and set `degraded['collective_global']='local'` |
| `cap.t01.rate.rate_limiter@1` | use the in-file conservative substitute for `rate_limiter` (documented, slower, lower quality) and set `degraded['rate_limiter']='local'` |
| `cap.t02.sparse.sparse_attention_kernels@1` | use the in-file conservative substitute for `sparse_attention_kernels` (documented, slower, lower quality) and set `degraded['sparse_attention_kernels']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - queue-pair management, memory registration and completion handli | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - zero-copy send/recv with pre-registered buffer pools | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - congestion control interaction and loss recovery | 520 | Third required mechanism. |
| 6 | Core implementation D - latency/bandwidth benchmark versus hardware line rate | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0154_rdma_transport.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.rdma.rdma_transport@1`.
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

### P0155 · `tcp_fallback` — Reliable TCP/QUIC Transport Fallback

| field | value |
|---|---|
| part id | `P0155` (5/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0155_tcp_fallback.rs` |
| module path | `hyperion.t04.hardware.tcp_fallback` |
| capability published | `cap.t04.tcp.tcp_fallback@1` |
| determinism class | `io` |
| p99 latency budget | 17000 ns (17 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0155_tcp_fallback.txt`](prompts/P0155_tcp_fallback.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0155-tcp-fallback) |

**Mission.** Works everywhere, degrades predictably when RDMA is unavailable.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **framing, multiplexing and flow control over stream transports** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **QUIC path with 0-RTT reconnect and stream priorities** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **adaptive chunk sizing and pacing**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured gap versus RDMA with documented degradation ladder** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t04.tcp.tcp_fallback@1`
- `cap.t04.tcp.tcp_fallback.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.rdma.rdma_transport@1` | use the in-file conservative substitute for `rdma_transport` (documented, slower, lower quality) and set `degraded['rdma_transport']='local'` |
| `cap.t01.bootstrap.bootstrap_init@1` | use the in-file conservative substitute for `bootstrap_init` (documented, slower, lower quality) and set `degraded['bootstrap_init']='local'` |
| `cap.t02.tensor.tensor_core_util@1` | use the in-file conservative substitute for `tensor_core_util` (documented, slower, lower quality) and set `degraded['tensor_core_util']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - framing, multiplexing and flow control over stream transports | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - QUIC path with 0-RTT reconnect and stream priorities | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - adaptive chunk sizing and pacing | 520 | Third required mechanism. |
| 6 | Core implementation D - measured gap versus RDMA with documented degradation ladder | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0155_tcp_fallback.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.tcp.tcp_fallback@1`.
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

### P0156 · `comm_scheduler` — Communication Scheduling & Prioritisation

| field | value |
|---|---|
| part id | `P0156` (6/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0156_comm_scheduler.rs` |
| module path | `hyperion.t04.hardware.comm_scheduler` |
| capability published | `cap.t04.comm.comm_scheduler@1` |
| determinism class | `io` |
| p99 latency budget | 18000 ns (18 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0156_comm_scheduler.txt`](prompts/P0156_comm_scheduler.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0156-comm-scheduler) |

**Mission.** Prevents communication from ever becoming the critical path.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **priority classes for latency-critical versus bulk transfers** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **bandwidth allocation with work-conserving fairness**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **deadline-aware scheduling tied to the task DAG** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured critical-path improvement** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t04.comm.comm_scheduler@1`
- `cap.t04.comm.comm_scheduler.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.tcp.tcp_fallback@1` | use the in-file conservative substitute for `tcp_fallback` (documented, slower, lower quality) and set `degraded['tcp_fallback']='local'` |
| `cap.t01.chacha.chacha_seeds@1` | use the in-file conservative substitute for `chacha_seeds` (documented, slower, lower quality) and set `degraded['chacha_seeds']='local'` |
| `cap.t02.attn.attn_flash_bwd@1` | use the in-file conservative substitute for `attn_flash_bwd` (documented, slower, lower quality) and set `degraded['attn_flash_bwd']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - priority classes for latency-critical versus bulk transfers | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - bandwidth allocation with work-conserving fairness | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - deadline-aware scheduling tied to the task DAG | 520 | Third required mechanism. |
| 6 | Core implementation D - measured critical-path improvement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0156_comm_scheduler.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.comm.comm_scheduler@1`.
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

### P0157 · `expert_parallel_fabric` — Expert-Parallel Routing Fabric

| field | value |
|---|---|
| part id | `P0157` (7/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0157_expert_parallel_fabric.rs` |
| module path | `hyperion.t04.hardware.expert_parallel_fabric` |
| capability published | `cap.t04.expert.expert_parallel_fabric@1` |
| determinism class | `io` |
| p99 latency budget | 19000 ns (19 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0157_expert_parallel_fabric.txt`](prompts/P0157_expert_parallel_fabric.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0157-expert-parallel-fabric) |

**Mission.** Moves tokens to experts across the cluster at MoE speed.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **token dispatch/combine with all-to-all and capacity control**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **locality-aware expert placement to shorten hops** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **skew handling with overflow rerouting** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **throughput at 512 experts across many nodes** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t04.expert.expert_parallel_fabric@1`
- `cap.t04.expert.expert_parallel_fabric.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.comm.comm_scheduler@1` | use the in-file conservative substitute for `comm_scheduler` (documented, slower, lower quality) and set `degraded['comm_scheduler']='local'` |
| `cap.t01.mem.mem_layout@1` | use the in-file conservative substitute for `mem_layout` (documented, slower, lower quality) and set `degraded['mem_layout']='local'` |
| `cap.t02.reduction.reduction_kernels@1` | use the in-file conservative substitute for `reduction_kernels` (documented, slower, lower quality) and set `degraded['reduction_kernels']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - token dispatch/combine with all-to-all and capacity control | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - locality-aware expert placement to shorten hops | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - skew handling with overflow rerouting | 520 | Third required mechanism. |
| 6 | Core implementation D - throughput at 512 experts across many nodes | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0157_expert_parallel_fabric.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.expert.expert_parallel_fabric@1`.
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

### P0158 · `sequence_parallel_fabric` — Sequence & Context Parallel Fabric

| field | value |
|---|---|
| part id | `P0158` (8/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0158_sequence_parallel_fabric.rs` |
| module path | `hyperion.t04.hardware.sequence_parallel_fabric` |
| capability published | `cap.t04.sequence.sequence_parallel_fabric@1` |
| determinism class | `io` |
| p99 latency budget | 20000 ns (20 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0158_sequence_parallel_fabric.txt`](prompts/P0158_sequence_parallel_fabric.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0158-sequence-parallel-fabric) |

**Mission.** Splits a single 1M-token context across machines.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **ring/striped context parallelism with overlapped attention communication** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **KV shard placement and migration policy** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **load balance under causal masking** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **scaling efficiency for very long contexts**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t04.sequence.sequence_parallel_fabric@1`
- `cap.t04.sequence.sequence_parallel_fabric.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.expert.expert_parallel_fabric@1` | use the in-file conservative substitute for `expert_parallel_fabric` (documented, slower, lower quality) and set `degraded['expert_parallel_fabric']='local'` |
| `cap.t01.hash.hash_maps@1` | use the in-file conservative substitute for `hash_maps` (documented, slower, lower quality) and set `degraded['hash_maps']='local'` |
| `cap.t02.rng.rng_kernels@1` | use the in-file conservative substitute for `rng_kernels` (documented, slower, lower quality) and set `degraded['rng_kernels']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - ring/striped context parallelism with overlapped attention commu | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - KV shard placement and migration policy | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - load balance under causal masking | 520 | Third required mechanism. |
| 6 | Core implementation D - scaling efficiency for very long contexts | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0158_sequence_parallel_fabric.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.sequence.sequence_parallel_fabric@1`.
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

### P0159 · `pipeline_fabric` — Pipeline Stage Transport

| field | value |
|---|---|
| part id | `P0159` (9/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0159_pipeline_fabric.rs` |
| module path | `hyperion.t04.hardware.pipeline_fabric` |
| capability published | `cap.t04.pipeline.pipeline_fabric@1` |
| determinism class | `io` |
| p99 latency budget | 21000 ns (21 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0159_pipeline_fabric.txt`](prompts/P0159_pipeline_fabric.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0159-pipeline-fabric) |

**Mission.** Activation and gradient movement between pipeline stages with no bubbles.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **point-to-point transfer with double buffering and prefetch** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **stage-boundary compression for activation traffic** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **backpressure integration with the pipeline schedule**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **bubble-fraction measurement** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t04.pipeline.pipeline_fabric@1`
- `cap.t04.pipeline.pipeline_fabric.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.sequence.sequence_parallel_fabric@1` | use the in-file conservative substitute for `sequence_parallel_fabric` (documented, slower, lower quality) and set `degraded['sequence_parallel_fabric']='local'` |
| `cap.t01.selftest.selftest_harness@1` | use the in-file conservative substitute for `selftest_harness` (documented, slower, lower quality) and set `degraded['selftest_harness']='local'` |
| `cap.t02.simd.simd_cpu@1` | use the in-file conservative substitute for `simd_cpu` (documented, slower, lower quality) and set `degraded['simd_cpu']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - point-to-point transfer with double buffering and prefetch | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - stage-boundary compression for activation traffic | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - backpressure integration with the pipeline schedule | 520 | Third required mechanism. |
| 6 | Core implementation D - bubble-fraction measurement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0159_pipeline_fabric.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.pipeline.pipeline_fabric@1`.
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

### P0160 · `param_server_shard` — Sharded Parameter Store

| field | value |
|---|---|
| part id | `P0160` (10/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0160_param_server_shard.rs` |
| module path | `hyperion.t04.hardware.param_server_shard` |
| capability published | `cap.t04.param.param_server_shard@1` |
| determinism class | `io` |
| p99 latency budget | 22000 ns (22 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0160_param_server_shard.txt`](prompts/P0160_param_server_shard.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0160-param-server-shard) |

**Mission.** Where the weights live, and how they get to compute fast.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **shard mapping with replication factor and placement policy** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **fast broadcast/gather of shards with topology awareness**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **hot-shard replication for skewed access** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **load time for a full model at cluster scale** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t04.param.param_server_shard@1`
- `cap.t04.param.param_server_shard.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.pipeline.pipeline_fabric@1` | use the in-file conservative substitute for `pipeline_fabric` (documented, slower, lower quality) and set `degraded['pipeline_fabric']='local'` |
| `cap.t01.version.version_semver@1` | use the in-file conservative substitute for `version_semver` (documented, slower, lower quality) and set `degraded['version_semver']='local'` |
| `cap.t02.emulation.emulation_reference@1` | use the in-file conservative substitute for `emulation_reference` (documented, slower, lower quality) and set `degraded['emulation_reference']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - shard mapping with replication factor and placement policy | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - fast broadcast/gather of shards with topology awareness | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - hot-shard replication for skewed access | 520 | Third required mechanism. |
| 6 | Core implementation D - load time for a full model at cluster scale | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0160_param_server_shard.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.param.param_server_shard@1`.
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

### P0161 · `weight_streaming` — Weight Streaming & Tiering

| field | value |
|---|---|
| part id | `P0161` (11/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0161_weight_streaming.rs` |
| module path | `hyperion.t04.hardware.weight_streaming` |
| capability published | `cap.t04.weight.weight_streaming@1` |
| determinism class | `io` |
| p99 latency budget | 23000 ns (23 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0161_weight_streaming.txt`](prompts/P0161_weight_streaming.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0161-weight-streaming) |

**Mission.** Runs models larger than device memory without stalling.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **prefetch schedule derived from the execution plan**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **multi-tier residency (device/host/NVMe) with cost-aware placement** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **double-buffered layer streaming overlapped with compute** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **stall-time measurement at multiple memory ratios** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t04.weight.weight_streaming@1`
- `cap.t04.weight.weight_streaming.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.param.param_server_shard@1` | use the in-file conservative substitute for `param_server_shard` (documented, slower, lower quality) and set `degraded['param_server_shard']='local'` |
| `cap.t01.budget.budget_ledger@1` | use the in-file conservative substitute for `budget_ledger` (documented, slower, lower quality) and set `degraded['budget_ledger']='local'` |
| `cap.t02.kernel.kernel_codegen_rt@1` | use the in-file conservative substitute for `kernel_codegen_rt` (documented, slower, lower quality) and set `degraded['kernel_codegen_rt']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - prefetch schedule derived from the execution plan | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - multi-tier residency (device/host/NVMe) with cost-aware placemen | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - double-buffered layer streaming overlapped with compute | 520 | Third required mechanism. |
| 6 | Core implementation D - stall-time measurement at multiple memory ratios | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0161_weight_streaming.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.weight.weight_streaming@1`.
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

### P0162 · `nvme_offload` — NVMe / Storage Offload Engine

| field | value |
|---|---|
| part id | `P0162` (12/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0162_nvme_offload.rs` |
| module path | `hyperion.t04.hardware.nvme_offload` |
| capability published | `cap.t04.nvme.nvme_offload@1` |
| determinism class | `io` |
| p99 latency budget | 24000 ns (24 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0162_nvme_offload.txt`](prompts/P0162_nvme_offload.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0162-nvme-offload) |

**Mission.** High-throughput spill for KV caches, activations and cold weights.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **direct-IO with queue depth tuning and alignment handling** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **GPU-direct storage paths where available** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **wear-aware write policy and lifetime accounting** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **achieved throughput versus device specification**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t04.nvme.nvme_offload@1`
- `cap.t04.nvme.nvme_offload.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.weight.weight_streaming@1` | use the in-file conservative substitute for `weight_streaming` (documented, slower, lower quality) and set `degraded['weight_streaming']='local'` |
| `cap.t01.compression.compression@1` | use the in-file conservative substitute for `compression` (documented, slower, lower quality) and set `degraded['compression']='local'` |
| `cap.t02.micro.micro_opt_catalog@1` | use the in-file conservative substitute for `micro_opt_catalog` (documented, slower, lower quality) and set `degraded['micro_opt_catalog']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - direct-IO with queue depth tuning and alignment handling | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - GPU-direct storage paths where available | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - wear-aware write policy and lifetime accounting | 520 | Third required mechanism. |
| 6 | Core implementation D - achieved throughput versus device specification | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0162_nvme_offload.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.nvme.nvme_offload@1`.
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

### P0163 · `host_pinned_pool` — Host Pinned Memory Manager

| field | value |
|---|---|
| part id | `P0163` (13/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0163_host_pinned_pool.rs` |
| module path | `hyperion.t04.hardware.host_pinned_pool` |
| capability published | `cap.t04.host.host_pinned_pool@1` |
| determinism class | `io` |
| p99 latency budget | 25000 ns (25 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0163_host_pinned_pool.txt`](prompts/P0163_host_pinned_pool.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0163-host-pinned-pool) |

**Mission.** Staging memory that never becomes a bottleneck or a leak.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **pinned pool with size classes and NUMA affinity** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **registration caching across transfers** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **leak/exhaustion detection with actionable diagnostics**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **transfer-rate measurement versus unpinned baseline** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t04.host.host_pinned_pool@1`
- `cap.t04.host.host_pinned_pool.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.nvme.nvme_offload@1` | use the in-file conservative substitute for `nvme_offload` (documented, slower, lower quality) and set `degraded['nvme_offload']='local'` |
| `cap.t01.blake3.blake3_hash@1` | use the in-file conservative substitute for `blake3_hash` (documented, slower, lower quality) and set `degraded['blake3_hash']='local'` |
| `cap.t02.attn.attn_flash_fwd@1` | use the in-file conservative substitute for `attn_flash_fwd` (documented, slower, lower quality) and set `degraded['attn_flash_fwd']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - pinned pool with size classes and NUMA affinity | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - registration caching across transfers | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - leak/exhaustion detection with actionable diagnostics | 520 | Third required mechanism. |
| 6 | Core implementation D - transfer-rate measurement versus unpinned baseline | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0163_host_pinned_pool.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.host.host_pinned_pool@1`.
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

### P0164 · `device_health` — Device Health Monitoring & Prediction

| field | value |
|---|---|
| part id | `P0164` (14/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0164_device_health.rs` |
| module path | `hyperion.t04.hardware.device_health` |
| capability published | `cap.t04.device.device_health@1` |
| determinism class | `io` |
| p99 latency budget | 26000 ns (26 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0164_device_health.txt`](prompts/P0164_device_health.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0164-device-health) |

**Mission.** Detects a degrading accelerator before it corrupts a run.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **telemetry ingestion: ECC, throttling, clocks, link errors, temperature** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **anomaly detection and remaining-useful-life estimation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **pre-emptive drain recommendation with cost/benefit** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **detection-rate evaluation on injected degradation** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t04.device.device_health@1`
- `cap.t04.device.device_health.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.host.host_pinned_pool@1` | use the in-file conservative substitute for `host_pinned_pool` (documented, slower, lower quality) and set `degraded['host_pinned_pool']='local'` |
| `cap.t01.alloc.alloc_arena@1` | use the in-file conservative substitute for `alloc_arena` (documented, slower, lower quality) and set `degraded['alloc_arena']='local'` |
| `cap.t02.elementwise.elementwise_fusion@1` | use the in-file conservative substitute for `elementwise_fusion` (documented, slower, lower quality) and set `degraded['elementwise_fusion']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - telemetry ingestion: ECC, throttling, clocks, link errors, tempe | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - anomaly detection and remaining-useful-life estimation | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - pre-emptive drain recommendation with cost/benefit | 520 | Third required mechanism. |
| 6 | Core implementation D - detection-rate evaluation on injected degradation | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0164_device_health.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.device.device_health@1`.
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

### P0165 · `fault_domains` — Fault Domain Modelling & Placement

| field | value |
|---|---|
| part id | `P0165` (15/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0165_fault_domains.rs` |
| module path | `hyperion.t04.hardware.fault_domains` |
| capability published | `cap.t04.fault.fault_domains@1` |
| determinism class | `io` |
| p99 latency budget | 27000 ns (27 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0165_fault_domains.txt`](prompts/P0165_fault_domains.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0165-fault-domains) |

**Mission.** Places replicas and shards so no single failure stops the assembly.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **failure-domain hierarchy (device, host, rack, zone) modelling**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **correlated-failure-aware placement solver** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **blast-radius computation for any single failure** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **simulated-failure survival testing** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t04.fault.fault_domains@1`
- `cap.t04.fault.fault_domains.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.device.device_health@1` | use the in-file conservative substitute for `device_health` (documented, slower, lower quality) and set `degraded['device_health']='local'` |
| `cap.t01.bitset.bitset_rank@1` | use the in-file conservative substitute for `bitset_rank` (documented, slower, lower quality) and set `degraded['bitset_rank']='local'` |
| `cap.t02.transpose.transpose_layout@1` | use the in-file conservative substitute for `transpose_layout` (documented, slower, lower quality) and set `degraded['transpose_layout']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - failure-domain hierarchy (device, host, rack, zone) modelling | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - correlated-failure-aware placement solver | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - blast-radius computation for any single failure | 520 | Third required mechanism. |
| 6 | Core implementation D - simulated-failure survival testing | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0165_fault_domains.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.fault.fault_domains@1`.
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

### P0166 · `elastic_scaling` — Elastic Membership & Rescaling

| field | value |
|---|---|
| part id | `P0166` (16/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0166_elastic_scaling.rs` |
| module path | `hyperion.t04.hardware.elastic_scaling` |
| capability published | `cap.t04.elastic.elastic_scaling@1` |
| determinism class | `io` |
| p99 latency budget | 28000 ns (28 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0166_elastic_scaling.txt`](prompts/P0166_elastic_scaling.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0166-elastic-scaling) |

**Mission.** Adds or removes machines mid-run without restarting.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **membership protocol with epochs and consistent views** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **state redistribution with minimal data movement** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **in-flight request preservation during rescale** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **rescale latency and throughput-dip measurement**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t04.elastic.elastic_scaling@1`
- `cap.t04.elastic.elastic_scaling.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.fault.fault_domains@1` | use the in-file conservative substitute for `fault_domains` (documented, slower, lower quality) and set `degraded['fault_domains']='local'` |
| `cap.t01.metrics.metrics_core@1` | use the in-file conservative substitute for `metrics_core` (documented, slower, lower quality) and set `degraded['metrics_core']='local'` |
| `cap.t02.cache.cache_blocking@1` | use the in-file conservative substitute for `cache_blocking` (documented, slower, lower quality) and set `degraded['cache_blocking']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - membership protocol with epochs and consistent views | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - state redistribution with minimal data movement | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - in-flight request preservation during rescale | 520 | Third required mechanism. |
| 6 | Core implementation D - rescale latency and throughput-dip measurement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0166_elastic_scaling.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.elastic.elastic_scaling@1`.
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

### P0167 · `checkpoint_transport` — Distributed Checkpoint IO

| field | value |
|---|---|
| part id | `P0167` (17/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0167_checkpoint_transport.rs` |
| module path | `hyperion.t04.hardware.checkpoint_transport` |
| capability published | `cap.t04.checkpoint.checkpoint_transport@1` |
| determinism class | `io` |
| p99 latency budget | 29000 ns (29 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0167_checkpoint_transport.txt`](prompts/P0167_checkpoint_transport.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0167-checkpoint-transport) |

**Mission.** Saves and restores petabyte-scale state fast and safely.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **sharded parallel write with aggregation to avoid small-file storms** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **async checkpointing overlapped with compute** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **integrity verification and partial-corruption recovery**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **checkpoint/restore wall-clock measurement at scale** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t04.checkpoint.checkpoint_transport@1`
- `cap.t04.checkpoint.checkpoint_transport.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.elastic.elastic_scaling@1` | use the in-file conservative substitute for `elastic_scaling` (documented, slower, lower quality) and set `degraded['elastic_scaling']='local'` |
| `cap.t01.capability.capability_gate@1` | use the in-file conservative substitute for `capability_gate` (documented, slower, lower quality) and set `degraded['capability_gate']='local'` |
| `cap.t02.profiler.profiler_hooks@1` | use the in-file conservative substitute for `profiler_hooks` (documented, slower, lower quality) and set `degraded['profiler_hooks']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - sharded parallel write with aggregation to avoid small-file stor | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - async checkpointing overlapped with compute | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - integrity verification and partial-corruption recovery | 520 | Third required mechanism. |
| 6 | Core implementation D - checkpoint/restore wall-clock measurement at scale | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0167_checkpoint_transport.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.checkpoint.checkpoint_transport@1`.
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

### P0168 · `failure_recovery` — Failure Detection & Fast Restart

| field | value |
|---|---|
| part id | `P0168` (18/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0168_failure_recovery.rs` |
| module path | `hyperion.t04.hardware.failure_recovery` |
| capability published | `cap.t04.failure.failure_recovery@1` |
| determinism class | `io` |
| p99 latency budget | 30000 ns (30 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0168_failure_recovery.txt`](prompts/P0168_failure_recovery.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0168-failure-recovery) |

**Mission.** Turns a machine loss into a small hiccup rather than a lost run.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **fast failure detection with false-positive suppression** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **in-memory redundant state for immediate recovery**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **partial restart limited to affected pipeline stages** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **mean-time-to-recovery measurement under injected faults** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t04.failure.failure_recovery@1`
- `cap.t04.failure.failure_recovery.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.checkpoint.checkpoint_transport@1` | use the in-file conservative substitute for `checkpoint_transport` (documented, slower, lower quality) and set `degraded['checkpoint_transport']='local'` |
| `cap.t01.unit.unit_dimensions@1` | use the in-file conservative substitute for `unit_dimensions` (documented, slower, lower quality) and set `degraded['unit_dimensions']='local'` |
| `cap.t02.error.error_correction@1` | use the in-file conservative substitute for `error_correction` (documented, slower, lower quality) and set `degraded['error_correction']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - fast failure detection with false-positive suppression | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - in-memory redundant state for immediate recovery | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - partial restart limited to affected pipeline stages | 520 | Third required mechanism. |
| 6 | Core implementation D - mean-time-to-recovery measurement under injected faults | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0168_failure_recovery.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.failure.failure_recovery@1`.
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

### P0169 · `straggler_mitigation` — Straggler Detection & Mitigation

| field | value |
|---|---|
| part id | `P0169` (19/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0169_straggler_mitigation.rs` |
| module path | `hyperion.t04.hardware.straggler_mitigation` |
| capability published | `cap.t04.straggler.straggler_mitigation@1` |
| determinism class | `io` |
| p99 latency budget | 31000 ns (31 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0169_straggler_mitigation.txt`](prompts/P0169_straggler_mitigation.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0169-straggler-mitigation) |

**Mission.** One slow machine must not slow 100k others.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **per-rank latency distribution tracking with robust statistics**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **speculative duplicate execution with first-wins semantics** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **work stealing/rebalancing across ranks** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **tail-latency improvement measurement** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t04.straggler.straggler_mitigation@1`
- `cap.t04.straggler.straggler_mitigation.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.failure.failure_recovery@1` | use the in-file conservative substitute for `failure_recovery` (documented, slower, lower quality) and set `degraded['failure_recovery']='local'` |
| `cap.t01.fs.fs_atomic@1` | use the in-file conservative substitute for `fs_atomic` (documented, slower, lower quality) and set `degraded['fs_atomic']='local'` |
| `cap.t02.kernel.kernel_bench_suite@1` | use the in-file conservative substitute for `kernel_bench_suite` (documented, slower, lower quality) and set `degraded['kernel_bench_suite']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - per-rank latency distribution tracking with robust statistics | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - speculative duplicate execution with first-wins semantics | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - work stealing/rebalancing across ranks | 520 | Third required mechanism. |
| 6 | Core implementation D - tail-latency improvement measurement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0169_straggler_mitigation.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.straggler.straggler_mitigation@1`.
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

### P0170 · `power_cluster` — Cluster Power & Energy Governance

| field | value |
|---|---|
| part id | `P0170` (20/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0170_power_cluster.rs` |
| module path | `hyperion.t04.hardware.power_cluster` |
| capability published | `cap.t04.power.power_cluster@1` |
| determinism class | `io` |
| p99 latency budget | 32000 ns (32 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0170_power_cluster.txt`](prompts/P0170_power_cluster.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0170-power-cluster) |

**Mission.** Maximises throughput per watt within facility limits.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **power-cap-aware scheduling and frequency policy** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **energy accounting per request and per part** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **thermal-headroom-aware placement** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured throughput-per-joule improvement**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t04.power.power_cluster@1`
- `cap.t04.power.power_cluster.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.straggler.straggler_mitigation@1` | use the in-file conservative substitute for `straggler_mitigation` (documented, slower, lower quality) and set `degraded['straggler_mitigation']='local'` |
| `cap.t01.cbor.cbor_canonical@1` | use the in-file conservative substitute for `cbor_canonical` (documented, slower, lower quality) and set `degraded['cbor_canonical']='local'` |
| `cap.t02.gemm.gemm_sparse@1` | use the in-file conservative substitute for `gemm_sparse` (documented, slower, lower quality) and set `degraded['gemm_sparse']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - power-cap-aware scheduling and frequency policy | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - energy accounting per request and per part | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - thermal-headroom-aware placement | 520 | Third required mechanism. |
| 6 | Core implementation D - measured throughput-per-joule improvement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0170_power_cluster.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.power.power_cluster@1`.
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

### P0171 · `network_congestion` — Congestion Control & Traffic Engineering

| field | value |
|---|---|
| part id | `P0171` (21/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0171_network_congestion.rs` |
| module path | `hyperion.t04.hardware.network_congestion` |
| capability published | `cap.t04.network.network_congestion@1` |
| determinism class | `io` |
| p99 latency budget | 33000 ns (33 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0171_network_congestion.txt`](prompts/P0171_network_congestion.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0171-network-congestion) |

**Mission.** Keeps the fabric out of collapse under all-to-all storms.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **adaptive routing and multipath spraying with reordering handling** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **incast avoidance via pacing and receiver-driven scheduling** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **congestion telemetry and hot-link detection**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **goodput measurement under adversarial traffic patterns** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t04.network.network_congestion@1`
- `cap.t04.network.network_congestion.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.power.power_cluster@1` | use the in-file conservative substitute for `power_cluster` (documented, slower, lower quality) and set `degraded['power_cluster']='local'` |
| `cap.t01.clock.clock_time@1` | use the in-file conservative substitute for `clock_time` (documented, slower, lower quality) and set `degraded['clock_time']='local'` |
| `cap.t02.softmax.softmax_norm@1` | use the in-file conservative substitute for `softmax_norm` (documented, slower, lower quality) and set `degraded['softmax_norm']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - adaptive routing and multipath spraying with reordering handling | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - incast avoidance via pacing and receiver-driven scheduling | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - congestion telemetry and hot-link detection | 520 | Third required mechanism. |
| 6 | Core implementation D - goodput measurement under adversarial traffic patterns | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0171_network_congestion.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.network.network_congestion@1`.
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

### P0172 · `multi_tenancy` — Multi-Tenant Isolation & QoS

| field | value |
|---|---|
| part id | `P0172` (22/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0172_multi_tenancy.rs` |
| module path | `hyperion.t04.hardware.multi_tenancy` |
| capability published | `cap.t04.multi.multi_tenancy@1` |
| determinism class | `io` |
| p99 latency budget | 34000 ns (34 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0172_multi_tenancy.txt`](prompts/P0172_multi_tenancy.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0172-multi-tenancy) |

**Mission.** Many workloads on one cluster with hard performance isolation.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **resource partitioning with enforcement at device and fabric level** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **QoS classes with latency SLOs and admission control**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **noisy-neighbour detection and mitigation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **SLO-attainment measurement under contention** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t04.multi.multi_tenancy@1`
- `cap.t04.multi.multi_tenancy.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.network.network_congestion@1` | use the in-file conservative substitute for `network_congestion` (documented, slower, lower quality) and set `degraded['network_congestion']='local'` |
| `cap.t01.bigint.bigint_modmath@1` | use the in-file conservative substitute for `bigint_modmath` (documented, slower, lower quality) and set `degraded['bigint_modmath']='local'` |
| `cap.t02.gather.gather_scatter@1` | use the in-file conservative substitute for `gather_scatter` (documented, slower, lower quality) and set `degraded['gather_scatter']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - resource partitioning with enforcement at device and fabric leve | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - QoS classes with latency SLOs and admission control | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - noisy-neighbour detection and mitigation | 520 | Third required mechanism. |
| 6 | Core implementation D - SLO-attainment measurement under contention | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0172_multi_tenancy.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.multi.multi_tenancy@1`.
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

### P0173 · `device_virtualisation` — Device Partitioning & Virtualisation

| field | value |
|---|---|
| part id | `P0173` (23/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0173_device_virtualisation.rs` |
| module path | `hyperion.t04.hardware.device_virtualisation` |
| capability published | `cap.t04.device.device_virtualisation@1` |
| determinism class | `io` |
| p99 latency budget | 35000 ns (35 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0173_device_virtualisation.txt`](prompts/P0173_device_virtualisation.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0173-device-virtualisation) |

**Mission.** Slices accelerators for small requests without waste.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **partition creation, sizing policy and lifecycle**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **performance-isolation verification between partitions** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **packing solver maximising utilisation under SLOs** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **utilisation improvement measurement** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t04.device.device_virtualisation@1`
- `cap.t04.device.device_virtualisation.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.multi.multi_tenancy@1` | use the in-file conservative substitute for `multi_tenancy` (documented, slower, lower quality) and set `degraded['multi_tenancy']='local'` |
| `cap.t01.logging.logging_events@1` | use the in-file conservative substitute for `logging_events` (documented, slower, lower quality) and set `degraded['logging_events']='local'` |
| `cap.t02.async.async_copy@1` | use the in-file conservative substitute for `async_copy` (documented, slower, lower quality) and set `degraded['async_copy']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - partition creation, sizing policy and lifecycle | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - performance-isolation verification between partitions | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - packing solver maximising utilisation under SLOs | 520 | Third required mechanism. |
| 6 | Core implementation D - utilisation improvement measurement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0173_device_virtualisation.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.device.device_virtualisation@1`.
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

### P0174 · `heterogeneous_pool` — Heterogeneous Hardware Pooling

| field | value |
|---|---|
| part id | `P0174` (24/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0174_heterogeneous_pool.rs` |
| module path | `hyperion.t04.hardware.heterogeneous_pool` |
| capability published | `cap.t04.heterogeneous.heterogeneous_pool@1` |
| determinism class | `io` |
| p99 latency budget | 36000 ns (36 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0174_heterogeneous_pool.txt`](prompts/P0174_heterogeneous_pool.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0174-heterogeneous-pool) |

**Mission.** Uses every generation and vendor of accelerator effectively together.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **capability-aware work routing with per-device cost models** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **mixed-generation collective handling with slowest-link awareness** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **graceful capability degradation for older devices** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **aggregate-throughput measurement across mixed pools**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t04.heterogeneous.heterogeneous_pool@1`
- `cap.t04.heterogeneous.heterogeneous_pool.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.device.device_virtualisation@1` | use the in-file conservative substitute for `device_virtualisation` (documented, slower, lower quality) and set `degraded['device_virtualisation']='local'` |
| `cap.t01.checksum.checksum_verify@1` | use the in-file conservative substitute for `checksum_verify` (documented, slower, lower quality) and set `degraded['checksum_verify']='local'` |
| `cap.t02.roofline.roofline_model@1` | use the in-file conservative substitute for `roofline_model` (documented, slower, lower quality) and set `degraded['roofline_model']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - capability-aware work routing with per-device cost models | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - mixed-generation collective handling with slowest-link awareness | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - graceful capability degradation for older devices | 520 | Third required mechanism. |
| 6 | Core implementation D - aggregate-throughput measurement across mixed pools | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0174_heterogeneous_pool.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.heterogeneous.heterogeneous_pool@1`.
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

### P0175 · `edge_runtime` — Edge & On-Device Runtime

| field | value |
|---|---|
| part id | `P0175` (25/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0175_edge_runtime.rs` |
| module path | `hyperion.t04.hardware.edge_runtime` |
| capability published | `cap.t04.edge.edge_runtime@1` |
| determinism class | `io` |
| p99 latency budget | 37000 ns (37 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0175_edge_runtime.txt`](prompts/P0175_edge_runtime.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0175-edge-runtime) |

**Mission.** Runs the distilled fast paths on laptops, phones and embedded targets.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **tight memory-budget execution with streaming weights** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **battery/thermal-aware scheduling** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **capability subset declaration and cloud handoff protocol**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **latency/quality measurements on constrained targets** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t04.edge.edge_runtime@1`
- `cap.t04.edge.edge_runtime.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.heterogeneous.heterogeneous_pool@1` | use the in-file conservative substitute for `heterogeneous_pool` (documented, slower, lower quality) and set `degraded['heterogeneous_pool']='local'` |
| `cap.t01.numeric.numeric_limits@1` | use the in-file conservative substitute for `numeric_limits` (documented, slower, lower quality) and set `degraded['numeric_limits']='local'` |
| `cap.t02.power.power_thermal@1` | use the in-file conservative substitute for `power_thermal` (documented, slower, lower quality) and set `degraded['power_thermal']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - tight memory-budget execution with streaming weights | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - battery/thermal-aware scheduling | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - capability subset declaration and cloud handoff protocol | 520 | Third required mechanism. |
| 6 | Core implementation D - latency/quality measurements on constrained targets | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0175_edge_runtime.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.edge.edge_runtime@1`.
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

### P0176 · `cloud_provisioner` — Capacity Provisioning & Placement Planner

| field | value |
|---|---|
| part id | `P0176` (26/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0176_cloud_provisioner.rs` |
| module path | `hyperion.t04.hardware.cloud_provisioner` |
| capability published | `cap.t04.cloud.cloud_provisioner@1` |
| determinism class | `io` |
| p99 latency budget | 38000 ns (38 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0176_cloud_provisioner.txt`](prompts/P0176_cloud_provisioner.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0176-cloud-provisioner) |

**Mission.** Decides what hardware to acquire and where to run each workload.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **demand forecasting from request traces** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **cost/latency/carbon multi-objective placement**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **spot/preemptible capacity strategy with checkpoint coupling** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **cost-per-request reduction measurement** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t04.cloud.cloud_provisioner@1`
- `cap.t04.cloud.cloud_provisioner.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.edge.edge_runtime@1` | use the in-file conservative substitute for `edge_runtime` (documented, slower, lower quality) and set `degraded['edge_runtime']='local'` |
| `cap.t01.sandbox.sandbox_policy@1` | use the in-file conservative substitute for `sandbox_policy` (documented, slower, lower quality) and set `degraded['sandbox_policy']='local'` |
| `cap.t02.ragged.ragged_batch@1` | use the in-file conservative substitute for `ragged_batch` (documented, slower, lower quality) and set `degraded['ragged_batch']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - demand forecasting from request traces | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - cost/latency/carbon multi-objective placement | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - spot/preemptible capacity strategy with checkpoint coupling | 520 | Third required mechanism. |
| 6 | Core implementation D - cost-per-request reduction measurement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0176_cloud_provisioner.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.cloud.cloud_provisioner@1`.
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

### P0177 · `scheduler_cluster` — Cluster Job Scheduler Integration

| field | value |
|---|---|
| part id | `P0177` (27/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0177_scheduler_cluster.rs` |
| module path | `hyperion.t04.hardware.scheduler_cluster` |
| capability published | `cap.t04.scheduler.scheduler_cluster@1` |
| determinism class | `io` |
| p99 latency budget | 39000 ns (39 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0177_scheduler_cluster.txt`](prompts/P0177_scheduler_cluster.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0177-scheduler-cluster) |

**Mission.** Plays well with Slurm/Kubernetes-class schedulers without losing control.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **gang scheduling and topology-aware allocation requests**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **preemption handling with fast drain and resume** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **queue-time prediction and backfill exploitation** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **allocation-quality measurement (topology compactness)** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t04.scheduler.scheduler_cluster@1`
- `cap.t04.scheduler.scheduler_cluster.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.cloud.cloud_provisioner@1` | use the in-file conservative substitute for `cloud_provisioner` (documented, slower, lower quality) and set `degraded['cloud_provisioner']='local'` |
| `cap.t01.abi.abi_result@1` | use the in-file conservative substitute for `abi_result` (documented, slower, lower quality) and set `degraded['abi_result']='local'` |
| `cap.t02.gemm.gemm_grouped@1` | use the in-file conservative substitute for `gemm_grouped` (documented, slower, lower quality) and set `degraded['gemm_grouped']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - gang scheduling and topology-aware allocation requests | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - preemption handling with fast drain and resume | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - queue-time prediction and backfill exploitation | 520 | Third required mechanism. |
| 6 | Core implementation D - allocation-quality measurement (topology compactness) | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0177_scheduler_cluster.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.scheduler.scheduler_cluster@1`.
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

### P0178 · `service_discovery` — Service Discovery & Membership Registry

| field | value |
|---|---|
| part id | `P0178` (28/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0178_service_discovery.rs` |
| module path | `hyperion.t04.hardware.service_discovery` |
| capability published | `cap.t04.service.service_discovery@1` |
| determinism class | `io` |
| p99 latency budget | 40000 ns (40 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0178_service_discovery.txt`](prompts/P0178_service_discovery.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0178-service-discovery) |

**Mission.** How 1000 parts across many machines find each other.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **gossip/consensus-backed registry with fast convergence** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **capability-indexed lookup with locality preference** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **partition tolerance behaviour and split-brain avoidance** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **convergence-time measurement at 100k nodes**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t04.service.service_discovery@1`
- `cap.t04.service.service_discovery.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.scheduler.scheduler_cluster@1` | use the in-file conservative substitute for `scheduler_cluster` (documented, slower, lower quality) and set `degraded['scheduler_cluster']='local'` |
| `cap.t01.trace.trace_context@1` | use the in-file conservative substitute for `trace_context` (documented, slower, lower quality) and set `degraded['trace_context']='local'` |
| `cap.t02.conv.conv_depthwise@1` | use the in-file conservative substitute for `conv_depthwise` (documented, slower, lower quality) and set `degraded['conv_depthwise']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - gossip/consensus-backed registry with fast convergence | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - capability-indexed lookup with locality preference | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - partition tolerance behaviour and split-brain avoidance | 520 | Third required mechanism. |
| 6 | Core implementation D - convergence-time measurement at 100k nodes | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0178_service_discovery.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.service.service_discovery@1`.
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

### P0179 · `consensus_core` — Lightweight Consensus & Leader Election

| field | value |
|---|---|
| part id | `P0179` (29/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0179_consensus_core.rs` |
| module path | `hyperion.t04.hardware.consensus_core` |
| capability published | `cap.t04.consensus.consensus_core@1` |
| determinism class | `io` |
| p99 latency budget | 41000 ns (41 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0179_consensus_core.txt`](prompts/P0179_consensus_core.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0179-consensus-core) |

**Mission.** Consistency for control-plane decisions only, never in the hot path.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **Raft-style log replication with pre-vote and joint consensus** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **lease-based leadership with clock-skew safety** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **linearisability testing under partitions**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **control-plane latency budget enforcement** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t04.consensus.consensus_core@1`
- `cap.t04.consensus.consensus_core.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.service.service_discovery@1` | use the in-file conservative substitute for `service_discovery` (documented, slower, lower quality) and set `degraded['service_discovery']='local'` |
| `cap.t01.fixed.fixed_point@1` | use the in-file conservative substitute for `fixed_point` (documented, slower, lower quality) and set `degraded['fixed_point']='local'` |
| `cap.t02.rope.rope_embed@1` | use the in-file conservative substitute for `rope_embed` (documented, slower, lower quality) and set `degraded['rope_embed']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - Raft-style log replication with pre-vote and joint consensus | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - lease-based leadership with clock-skew safety | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - linearisability testing under partitions | 520 | Third required mechanism. |
| 6 | Core implementation D - control-plane latency budget enforcement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0179_consensus_core.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.consensus.consensus_core@1`.
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

### P0180 · `distributed_lock` — Distributed Locking & Fencing

| field | value |
|---|---|
| part id | `P0180` (30/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0180_distributed_lock.rs` |
| module path | `hyperion.t04.hardware.distributed_lock` |
| capability published | `cap.t04.distributed.distributed_lock@1` |
| determinism class | `io` |
| p99 latency budget | 42000 ns (42 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0180_distributed_lock.txt`](prompts/P0180_distributed_lock.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0180-distributed-lock) |

**Mission.** Prevents two workers from ever doing the same irreversible thing.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **lease locks with monotonic fencing tokens** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **lock-holder failure detection and safe takeover**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **deadlock avoidance with ordered acquisition** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **safety verification under process pauses and clock jumps** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t04.distributed.distributed_lock@1`
- `cap.t04.distributed.distributed_lock.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.consensus.consensus_core@1` | use the in-file conservative substitute for `consensus_core` (documented, slower, lower quality) and set `degraded['consensus_core']='local'` |
| `cap.t01.config.config_system@1` | use the in-file conservative substitute for `config_system` (documented, slower, lower quality) and set `degraded['config_system']='local'` |
| `cap.t02.mem.mem_pool_device@1` | use the in-file conservative substitute for `mem_pool_device` (documented, slower, lower quality) and set `degraded['mem_pool_device']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - lease locks with monotonic fencing tokens | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - lock-holder failure detection and safe takeover | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - deadlock avoidance with ordered acquisition | 520 | Third required mechanism. |
| 6 | Core implementation D - safety verification under process pauses and clock jumps | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0180_distributed_lock.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.distributed.distributed_lock@1`.
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

### P0181 · `clock_sync` — Cluster Clock Synchronisation

| field | value |
|---|---|
| part id | `P0181` (31/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0181_clock_sync.rs` |
| module path | `hyperion.t04.hardware.clock_sync` |
| capability published | `cap.t04.clock.clock_sync@1` |
| determinism class | `io` |
| p99 latency budget | 43000 ns (43 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0181_clock_sync.txt`](prompts/P0181_clock_sync.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0181-clock-sync) |

**Mission.** Enough time agreement to reason about causality and deadlines.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **PTP/NTP ingestion with uncertainty intervals**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **hybrid logical clocks for causal ordering** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **skew-bound enforcement in deadline arithmetic** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured uncertainty and its effect on SLOs** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t04.clock.clock_sync@1`
- `cap.t04.clock.clock_sync.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.distributed.distributed_lock@1` | use the in-file conservative substitute for `distributed_lock` (documented, slower, lower quality) and set `degraded['distributed_lock']='local'` |
| `cap.t01.determinism.determinism_replay@1` | use the in-file conservative substitute for `determinism_replay` (documented, slower, lower quality) and set `degraded['determinism_replay']='local'` |
| `cap.t02.kernel.kernel_verify@1` | use the in-file conservative substitute for `kernel_verify` (documented, slower, lower quality) and set `degraded['kernel_verify']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - PTP/NTP ingestion with uncertainty intervals | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - hybrid logical clocks for causal ordering | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - skew-bound enforcement in deadline arithmetic | 520 | Third required mechanism. |
| 6 | Core implementation D - measured uncertainty and its effect on SLOs | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0181_clock_sync.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.clock.clock_sync@1`.
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

### P0182 · `data_locality` — Data Locality & Cache Affinity Router

| field | value |
|---|---|
| part id | `P0182` (32/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0182_data_locality.rs` |
| module path | `hyperion.t04.hardware.data_locality` |
| capability published | `cap.t04.data.data_locality@1` |
| determinism class | `io` |
| p99 latency budget | 44000 ns (44 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0182_data_locality.txt`](prompts/P0182_data_locality.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0182-data-locality) |

**Mission.** Routes work to where the bytes already are.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **consistent hashing with bounded loads and affinity keys** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **KV-cache-aware routing for multi-turn sessions** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **migration cost estimation versus remote-access cost** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **cache-hit-rate improvement measurement**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t04.data.data_locality@1`
- `cap.t04.data.data_locality.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.clock.clock_sync@1` | use the in-file conservative substitute for `clock_sync` (documented, slower, lower quality) and set `degraded['clock_sync']='local'` |
| `cap.t01.compat.compat_shims@1` | use the in-file conservative substitute for `compat_shims` (documented, slower, lower quality) and set `degraded['compat_shims']='local'` |
| `cap.t02.stream.stream_scheduler@1` | use the in-file conservative substitute for `stream_scheduler` (documented, slower, lower quality) and set `degraded['stream_scheduler']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - consistent hashing with bounded loads and affinity keys | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - KV-cache-aware routing for multi-turn sessions | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - migration cost estimation versus remote-access cost | 520 | Third required mechanism. |
| 6 | Core implementation D - cache-hit-rate improvement measurement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0182_data_locality.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.data.data_locality@1`.
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

### P0183 · `bandwidth_accounting` — Bandwidth & Interconnect Accounting

| field | value |
|---|---|
| part id | `P0183` (33/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0183_bandwidth_accounting.rs` |
| module path | `hyperion.t04.hardware.bandwidth_accounting` |
| capability published | `cap.t04.bandwidth.bandwidth_accounting@1` |
| determinism class | `io` |
| p99 latency budget | 45000 ns (45 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0183_bandwidth_accounting.txt`](prompts/P0183_bandwidth_accounting.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0183-bandwidth-accounting) |

**Mission.** Makes every byte moved visible and attributable.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **per-link, per-tier, per-request byte accounting** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **attribution to parts and phases with negligible overhead** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **budget enforcement on communication volume**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **report used by the compiler to reduce traffic** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t04.bandwidth.bandwidth_accounting@1`
- `cap.t04.bandwidth.bandwidth_accounting.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.data.data_locality@1` | use the in-file conservative substitute for `data_locality` (documented, slower, lower quality) and set `degraded['data_locality']='local'` |
| `cap.t01.secure.secure_zeroize@1` | use the in-file conservative substitute for `secure_zeroize` (documented, slower, lower quality) and set `degraded['secure_zeroize']='local'` |
| `cap.t02.tensor.tensor_view@1` | use the in-file conservative substitute for `tensor_view` (documented, slower, lower quality) and set `degraded['tensor_view']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - per-link, per-tier, per-request byte accounting | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - attribution to parts and phases with negligible overhead | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - budget enforcement on communication volume | 520 | Third required mechanism. |
| 6 | Core implementation D - report used by the compiler to reduce traffic | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0183_bandwidth_accounting.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.bandwidth.bandwidth_accounting@1`.
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

### P0184 · `secure_channel` — Encrypted Inter-Node Channels

| field | value |
|---|---|
| part id | `P0184` (34/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0184_secure_channel.rs` |
| module path | `hyperion.t04.hardware.secure_channel` |
| capability published | `cap.t04.secure.secure_channel@1` |
| determinism class | `io` |
| p99 latency budget | 46000 ns (46 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0184_secure_channel.txt`](prompts/P0184_secure_channel.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0184-secure-channel) |

**Mission.** Confidentiality and integrity without losing throughput.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **mutual authentication with short-lived certificates** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **AEAD framing with hardware offload where available**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **key rotation without connection drops** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **throughput cost measurement of encryption** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t04.secure.secure_channel@1`
- `cap.t04.secure.secure_channel.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.bandwidth.bandwidth_accounting@1` | use the in-file conservative substitute for `bandwidth_accounting` (documented, slower, lower quality) and set `degraded['bandwidth_accounting']='local'` |
| `cap.t02.gemm.gemm_int4@1` | use the in-file conservative substitute for `gemm_int4` (documented, slower, lower quality) and set `degraded['gemm_int4']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - mutual authentication with short-lived certificates | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - AEAD framing with hardware offload where available | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - key rotation without connection drops | 520 | Third required mechanism. |
| 6 | Core implementation D - throughput cost measurement of encryption | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0184_secure_channel.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.secure.secure_channel@1`.
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

### P0185 · `confidential_compute` — Confidential Computing Integration

| field | value |
|---|---|
| part id | `P0185` (35/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0185_confidential_compute.rs` |
| module path | `hyperion.t04.hardware.confidential_compute` |
| capability published | `cap.t04.confidential.confidential_compute@1` |
| determinism class | `io` |
| p99 latency budget | 47000 ns (47 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0185_confidential_compute.txt`](prompts/P0185_confidential_compute.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0185-confidential-compute) |

**Mission.** Runs sensitive workloads inside attested enclaves.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **attestation verification and policy binding**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **encrypted memory handling and IO shim overhead management** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **key release conditioned on measurement** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **performance overhead measurement and mitigation** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t04.confidential.confidential_compute@1`
- `cap.t04.confidential.confidential_compute.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.secure.secure_channel@1` | use the in-file conservative substitute for `secure_channel` (documented, slower, lower quality) and set `degraded['secure_channel']='local'` |
| `cap.t01.envelope.envelope_codec@1` | use the in-file conservative substitute for `envelope_codec` (documented, slower, lower quality) and set `degraded['envelope_codec']='local'` |
| `cap.t02.ssm.ssm_scan@1` | use the in-file conservative substitute for `ssm_scan` (documented, slower, lower quality) and set `degraded['ssm_scan']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - attestation verification and policy binding | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - encrypted memory handling and IO shim overhead management | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - key release conditioned on measurement | 520 | Third required mechanism. |
| 6 | Core implementation D - performance overhead measurement and mitigation | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0185_confidential_compute.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.confidential.confidential_compute@1`.
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

### P0186 · `firmware_compat` — Driver & Firmware Compatibility Matrix

| field | value |
|---|---|
| part id | `P0186` (36/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0186_firmware_compat.rs` |
| module path | `hyperion.t04.hardware.firmware_compat` |
| capability published | `cap.t04.firmware.firmware_compat@1` |
| determinism class | `io` |
| p99 latency budget | 48000 ns (48 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0186_firmware_compat.txt`](prompts/P0186_firmware_compat.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0186-firmware-compat) |

**Mission.** Prevents the classic 'works on that node' failure class.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **version detection, known-issue database and hard gating** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **capability differences normalised into the target description** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **pre-flight validation suite run at node admission** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **matrix coverage report**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t04.firmware.firmware_compat@1`
- `cap.t04.firmware.firmware_compat.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.confidential.confidential_compute@1` | use the in-file conservative substitute for `confidential_compute` (documented, slower, lower quality) and set `degraded['confidential_compute']='local'` |
| `cap.t01.dataflow.dataflow_dag@1` | use the in-file conservative substitute for `dataflow_dag` (documented, slower, lower quality) and set `degraded['dataflow_dag']='local'` |
| `cap.t02.kv.kv_cache_kernels@1` | use the in-file conservative substitute for `kv_cache_kernels` (documented, slower, lower quality) and set `degraded['kv_cache_kernels']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - version detection, known-issue database and hard gating | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - capability differences normalised into the target description | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - pre-flight validation suite run at node admission | 520 | Third required mechanism. |
| 6 | Core implementation D - matrix coverage report | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0186_firmware_compat.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.firmware.firmware_compat@1`.
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

### P0187 · `nic_offload` — Network Offload & In-Network Compute

| field | value |
|---|---|
| part id | `P0187` (37/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0187_nic_offload.rs` |
| module path | `hyperion.t04.hardware.nic_offload` |
| capability published | `cap.t04.nic.nic_offload@1` |
| determinism class | `io` |
| p99 latency budget | 49000 ns (49 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0187_nic_offload.txt`](prompts/P0187_nic_offload.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0187-nic-offload) |

**Mission.** Pushes reductions and packet work into NICs and switches.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **in-network all-reduce integration with fallback** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **kernel-bypass datapath with poll-mode threads** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **offload correctness verification versus host computation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured host-CPU and latency savings** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t04.nic.nic_offload@1`
- `cap.t04.nic.nic_offload.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.firmware.firmware_compat@1` | use the in-file conservative substitute for `firmware_compat` (documented, slower, lower quality) and set `degraded['firmware_compat']='local'` |
| `cap.t01.serialization.serialization_schema@1` | use the in-file conservative substitute for `serialization_schema` (documented, slower, lower quality) and set `degraded['serialization_schema']='local'` |
| `cap.t02.graph.graph_capture@1` | use the in-file conservative substitute for `graph_capture` (documented, slower, lower quality) and set `degraded['graph_capture']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - in-network all-reduce integration with fallback | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - kernel-bypass datapath with poll-mode threads | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - offload correctness verification versus host computation | 520 | Third required mechanism. |
| 6 | Core implementation D - measured host-CPU and latency savings | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0187_nic_offload.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.nic.nic_offload@1`.
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

### P0188 · `device_reset` — Device Reset & Isolation Recovery

| field | value |
|---|---|
| part id | `P0188` (38/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0188_device_reset.rs` |
| module path | `hyperion.t04.hardware.device_reset` |
| capability published | `cap.t04.device.device_reset@1` |
| determinism class | `io` |
| p99 latency budget | 3000 ns (3 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0188_device_reset.txt`](prompts/P0188_device_reset.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0188-device-reset) |

**Mission.** Recovers a wedged accelerator without rebooting the host.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **hang detection with watchdogs and progress counters** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **safe reset sequencing and state reconstruction**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **poison propagation prevention to healthy devices** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **recovery-success-rate measurement under injected hangs** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t04.device.device_reset@1`
- `cap.t04.device.device_reset.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.nic.nic_offload@1` | use the in-file conservative substitute for `nic_offload` (documented, slower, lower quality) and set `degraded['nic_offload']='local'` |
| `cap.t01.bench.bench_harness@1` | use the in-file conservative substitute for `bench_harness` (documented, slower, lower quality) and set `degraded['bench_harness']='local'` |
| `cap.t02.kernel.kernel_registry@1` | use the in-file conservative substitute for `kernel_registry` (documented, slower, lower quality) and set `degraded['kernel_registry']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - hang detection with watchdogs and progress counters | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - safe reset sequencing and state reconstruction | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - poison propagation prevention to healthy devices | 520 | Third required mechanism. |
| 6 | Core implementation D - recovery-success-rate measurement under injected hangs | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0188_device_reset.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.device.device_reset@1`.
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

### P0189 · `numa_topology_cluster` — Host-Level Resource Topology Binding

| field | value |
|---|---|
| part id | `P0189` (39/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0189_numa_topology_cluster.rs` |
| module path | `hyperion.t04.hardware.numa_topology_cluster` |
| capability published | `cap.t04.numa.numa_topology_cluster@1` |
| determinism class | `io` |
| p99 latency budget | 4000 ns (4 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0189_numa_topology_cluster.txt`](prompts/P0189_numa_topology_cluster.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0189-numa-topology-cluster) |

**Mission.** Binds threads, memory, devices and NICs coherently.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **CPU/GPU/NIC affinity solver from the topology graph**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **IRQ and interrupt-affinity configuration guidance** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **hugepage and transparent-hugepage policy** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured latency improvement from correct binding** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t04.numa.numa_topology_cluster@1`
- `cap.t04.numa.numa_topology_cluster.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.device.device_reset@1` | use the in-file conservative substitute for `device_reset` (documented, slower, lower quality) and set `degraded['device_reset']='local'` |
| `cap.t01.abi.abi_stability@1` | use the in-file conservative substitute for `abi_stability` (documented, slower, lower quality) and set `degraded['abi_stability']='local'` |
| `cap.t02.p2p.p2p_transfer@1` | use the in-file conservative substitute for `p2p_transfer` (documented, slower, lower quality) and set `degraded['p2p_transfer']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - CPU/GPU/NIC affinity solver from the topology graph | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - IRQ and interrupt-affinity configuration guidance | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - hugepage and transparent-hugepage policy | 520 | Third required mechanism. |
| 6 | Core implementation D - measured latency improvement from correct binding | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0189_numa_topology_cluster.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.numa.numa_topology_cluster@1`.
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

### P0190 · `telemetry_transport` — High-Volume Telemetry Pipeline

| field | value |
|---|---|
| part id | `P0190` (40/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0190_telemetry_transport.rs` |
| module path | `hyperion.t04.hardware.telemetry_transport` |
| capability published | `cap.t04.telemetry.telemetry_transport@1` |
| determinism class | `io` |
| p99 latency budget | 5000 ns (5 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0190_telemetry_transport.txt`](prompts/P0190_telemetry_transport.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0190-telemetry-transport) |

**Mission.** Ships metrics, traces and events from 100k nodes without cost explosion.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **local aggregation and pre-summarisation before egress** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **adaptive sampling with error-bound guarantees** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **backpressure and loss accounting** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **telemetry cost per request measurement**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t04.telemetry.telemetry_transport@1`
- `cap.t04.telemetry.telemetry_transport.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.numa.numa_topology_cluster@1` | use the in-file conservative substitute for `numa_topology_cluster` (documented, slower, lower quality) and set `degraded['numa_topology_cluster']='local'` |
| `cap.t01.retry.retry_idempotency@1` | use the in-file conservative substitute for `retry_idempotency` (documented, slower, lower quality) and set `degraded['retry_idempotency']='local'` |
| `cap.t02.mask.mask_engine@1` | use the in-file conservative substitute for `mask_engine` (documented, slower, lower quality) and set `degraded['mask_engine']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - local aggregation and pre-summarisation before egress | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - adaptive sampling with error-bound guarantees | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - backpressure and loss accounting | 520 | Third required mechanism. |
| 6 | Core implementation D - telemetry cost per request measurement | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0190_telemetry_transport.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.telemetry.telemetry_transport@1`.
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

### P0191 · `simulation_cluster` — Cluster Simulator

| field | value |
|---|---|
| part id | `P0191` (41/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0191_simulation_cluster.rs` |
| module path | `hyperion.t04.hardware.simulation_cluster` |
| capability published | `cap.t04.simulation.simulation_cluster@1` |
| determinism class | `io` |
| p99 latency budget | 6000 ns (6 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0191_simulation_cluster.txt`](prompts/P0191_simulation_cluster.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0191-simulation-cluster) |

**Mission.** Tests distributed logic at 100k scale on one machine.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **discrete-event simulation of compute, memory and network** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **fault, straggler and partition injection scenarios** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **calibration against real measurements with error reporting**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **scenario library covering all failure modes** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t04.simulation.simulation_cluster@1`
- `cap.t04.simulation.simulation_cluster.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.telemetry.telemetry_transport@1` | use the in-file conservative substitute for `telemetry_transport` (documented, slower, lower quality) and set `degraded['telemetry_transport']='local'` |
| `cap.t02.gemm.gemm_fp8@1` | use the in-file conservative substitute for `gemm_fp8` (documented, slower, lower quality) and set `degraded['gemm_fp8']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - discrete-event simulation of compute, memory and network | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - fault, straggler and partition injection scenarios | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - calibration against real measurements with error reporting | 520 | Third required mechanism. |
| 6 | Core implementation D - scenario library covering all failure modes | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0191_simulation_cluster.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.simulation.simulation_cluster@1`.
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

### P0192 · `capacity_benchmarks` — Distributed Benchmark Suite

| field | value |
|---|---|
| part id | `P0192` (42/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0192_capacity_benchmarks.rs` |
| module path | `hyperion.t04.hardware.capacity_benchmarks` |
| capability published | `cap.t04.capacity.capacity_benchmarks@1` |
| determinism class | `io` |
| p99 latency budget | 7000 ns (7 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0192_capacity_benchmarks.txt`](prompts/P0192_capacity_benchmarks.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0192-capacity-benchmarks) |

**Mission.** The canonical scaling measurements for the whole platform.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **strong/weak scaling harnesses with statistical rigor** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **communication microbenchmarks per link type**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **end-to-end throughput and latency at multiple scales** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **baseline records with machine fingerprints** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t04.capacity.capacity_benchmarks@1`
- `cap.t04.capacity.capacity_benchmarks.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.simulation.simulation_cluster@1` | use the in-file conservative substitute for `simulation_cluster` (documented, slower, lower quality) and set `degraded['simulation_cluster']='local'` |
| `cap.t01.omega.omega_bus_ipc@1` | use the in-file conservative substitute for `omega_bus_ipc` (documented, slower, lower quality) and set `degraded['omega_bus_ipc']='local'` |
| `cap.t02.attn.attn_linear@1` | use the in-file conservative substitute for `attn_linear` (documented, slower, lower quality) and set `degraded['attn_linear']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - strong/weak scaling harnesses with statistical rigor | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - communication microbenchmarks per link type | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - end-to-end throughput and latency at multiple scales | 520 | Third required mechanism. |
| 6 | Core implementation D - baseline records with machine fingerprints | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0192_capacity_benchmarks.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.capacity.capacity_benchmarks@1`.
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

### P0193 · `cost_model_cluster` — Total-Cost-of-Serving Model

| field | value |
|---|---|
| part id | `P0193` (43/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0193_cost_model_cluster.rs` |
| module path | `hyperion.t04.hardware.cost_model_cluster` |
| capability published | `cap.t04.cost.cost_model_cluster@1` |
| determinism class | `io` |
| p99 latency budget | 8000 ns (8 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0193_cost_model_cluster.txt`](prompts/P0193_cost_model_cluster.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0193-cost-model-cluster) |

**Mission.** Turns hardware, power and time into dollars per request.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **cost decomposition per device-hour, byte moved and joule**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **amortisation of compilation, warmup and idle capacity** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **what-if analysis for hardware and plan changes** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **validation against measured billing data** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t04.cost.cost_model_cluster@1`
- `cap.t04.cost.cost_model_cluster.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.capacity.capacity_benchmarks@1` | use the in-file conservative substitute for `capacity_benchmarks` (documented, slower, lower quality) and set `degraded['capacity_benchmarks']='local'` |
| `cap.t01.task.task_runtime@1` | use the in-file conservative substitute for `task_runtime` (documented, slower, lower quality) and set `degraded['task_runtime']='local'` |
| `cap.t02.quantize.quantize_kernels@1` | use the in-file conservative substitute for `quantize_kernels` (documented, slower, lower quality) and set `degraded['quantize_kernels']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - cost decomposition per device-hour, byte moved and joule | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - amortisation of compilation, warmup and idle capacity | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - what-if analysis for hardware and plan changes | 520 | Third required mechanism. |
| 6 | Core implementation D - validation against measured billing data | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0193_cost_model_cluster.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.cost.cost_model_cluster@1`.
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

### P0194 · `request_router` — Global Request Router & Load Balancer

| field | value |
|---|---|
| part id | `P0194` (44/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0194_request_router.rs` |
| module path | `hyperion.t04.hardware.request_router` |
| capability published | `cap.t04.request.request_router@1` |
| determinism class | `io` |
| p99 latency budget | 9000 ns (9 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0194_request_router.txt`](prompts/P0194_request_router.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0194-request-router) |

**Mission.** Sends each request to the cheapest machine that meets its SLO.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **latency-aware, cache-affinity-aware, cost-aware routing** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **queue-length and power-of-two-choices balancing** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **SLO-class routing with overflow tiers** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **tail-latency and cost measurement under mixed load**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t04.request.request_router@1`
- `cap.t04.request.request_router.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.cost.cost_model_cluster@1` | use the in-file conservative substitute for `cost_model_cluster` (documented, slower, lower quality) and set `degraded['cost_model_cluster']='local'` |
| `cap.t01.arena.arena_graph@1` | use the in-file conservative substitute for `arena_graph` (documented, slower, lower quality) and set `degraded['arena_graph']='local'` |
| `cap.t02.fused.fused_decode_step@1` | use the in-file conservative substitute for `fused_decode_step` (documented, slower, lower quality) and set `degraded['fused_decode_step']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - latency-aware, cache-affinity-aware, cost-aware routing | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - queue-length and power-of-two-choices balancing | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - SLO-class routing with overflow tiers | 520 | Third required mechanism. |
| 6 | Core implementation D - tail-latency and cost measurement under mixed load | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0194_request_router.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.request.request_router@1`.
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

### P0195 · `region_failover` — Multi-Region Replication & Failover

| field | value |
|---|---|
| part id | `P0195` (45/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0195_region_failover.rs` |
| module path | `hyperion.t04.hardware.region_failover` |
| capability published | `cap.t04.region.region_failover@1` |
| determinism class | `io` |
| p99 latency budget | 10000 ns (10 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0195_region_failover.txt`](prompts/P0195_region_failover.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0195-region-failover) |

**Mission.** Survives losing an entire datacentre.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **state replication strategy with RPO/RTO targets** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **traffic shifting with connection draining** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **consistency model documentation and enforcement**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **failover drill results and measured RTO** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t04.region.region_failover@1`
- `cap.t04.region.region_failover.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.request.request_router@1` | use the in-file conservative substitute for `request_router` (documented, slower, lower quality) and set `degraded['request_router']='local'` |
| `cap.t01.fuzz.fuzz_engine@1` | use the in-file conservative substitute for `fuzz_engine` (documented, slower, lower quality) and set `degraded['fuzz_engine']='local'` |
| `cap.t02.bf16.bf16_stability@1` | use the in-file conservative substitute for `bf16_stability` (documented, slower, lower quality) and set `degraded['bf16_stability']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - state replication strategy with RPO/RTO targets | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - traffic shifting with connection draining | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - consistency model documentation and enforcement | 520 | Third required mechanism. |
| 6 | Core implementation D - failover drill results and measured RTO | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0195_region_failover.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.region.region_failover@1`.
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

### P0196 · `hw_sw_codesign` — Hardware/Software Co-Design Specification

| field | value |
|---|---|
| part id | `P0196` (46/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0196_hw_sw_codesign.rs` |
| module path | `hyperion.t04.hardware.hw_sw_codesign` |
| capability published | `cap.t04.hw.hw_sw_codesign@1` |
| determinism class | `io` |
| p99 latency budget | 11000 ns (11 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0196_hw_sw_codesign.txt`](prompts/P0196_hw_sw_codesign.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0196-hw-sw-codesign) |

**Mission.** The precise ask to hardware vendors, derived from measured bottlenecks.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **bottleneck attribution from roofline and profiling data** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **quantified feature requests with projected speedups**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **custom-accelerator ISA proposal for the hottest kernels** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **projection methodology and validation plan** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t04.hw.hw_sw_codesign@1`
- `cap.t04.hw.hw_sw_codesign.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.region.region_failover@1` | use the in-file conservative substitute for `region_failover` (documented, slower, lower quality) and set `degraded['region_failover']='local'` |
| `cap.t01.manifest.manifest_parser@1` | use the in-file conservative substitute for `manifest_parser` (documented, slower, lower quality) and set `degraded['manifest_parser']='local'` |
| `cap.t02.collective.collective_local@1` | use the in-file conservative substitute for `collective_local` (documented, slower, lower quality) and set `degraded['collective_local']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - bottleneck attribution from roofline and profiling data | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - quantified feature requests with projected speedups | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - custom-accelerator ISA proposal for the hottest kernels | 520 | Third required mechanism. |
| 6 | Core implementation D - projection methodology and validation plan | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0196_hw_sw_codesign.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.hw.hw_sw_codesign@1`.
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

### P0197 · `green_scheduling` — Carbon-Aware Scheduling

| field | value |
|---|---|
| part id | `P0197` (47/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0197_green_scheduling.rs` |
| module path | `hyperion.t04.hardware.green_scheduling` |
| capability published | `cap.t04.green.green_scheduling@1` |
| determinism class | `io` |
| p99 latency budget | 12000 ns (12 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0197_green_scheduling.txt`](prompts/P0197_green_scheduling.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0197-green-scheduling) |

**Mission.** Same work, less carbon, no SLO loss.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **carbon-intensity signal ingestion and forecasting**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **deferrable-workload shifting under SLO constraints** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **carbon accounting per request** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured emissions reduction at constant SLO attainment** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t04.green.green_scheduling@1`
- `cap.t04.green.green_scheduling.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.hw.hw_sw_codesign@1` | use the in-file conservative substitute for `hw_sw_codesign` (documented, slower, lower quality) and set `degraded['hw_sw_codesign']='local'` |
| `cap.t01.circuit.circuit_breaker@1` | use the in-file conservative substitute for `circuit_breaker` (documented, slower, lower quality) and set `degraded['circuit_breaker']='local'` |
| `cap.t02.embedding.embedding_kernels@1` | use the in-file conservative substitute for `embedding_kernels` (documented, slower, lower quality) and set `degraded['embedding_kernels']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - carbon-intensity signal ingestion and forecasting | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - deferrable-workload shifting under SLO constraints | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - carbon accounting per request | 520 | Third required mechanism. |
| 6 | Core implementation D - measured emissions reduction at constant SLO attainment | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0197_green_scheduling.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.green.green_scheduling@1`.
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

### P0198 · `device_alloc_fair` — Fair-Share Device Allocation

| field | value |
|---|---|
| part id | `P0198` (48/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0198_device_alloc_fair.rs` |
| module path | `hyperion.t04.hardware.device_alloc_fair` |
| capability published | `cap.t04.device.device_alloc_fair@1` |
| determinism class | `io` |
| p99 latency budget | 13000 ns (13 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0198_device_alloc_fair.txt`](prompts/P0198_device_alloc_fair.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0198-device-alloc-fair) |

**Mission.** Long-term fairness across teams and workloads.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **dominant-resource fairness across heterogeneous devices** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **borrowing/lending with reclaim guarantees** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **starvation-freedom proof and monitoring** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **fairness metric measurement over long horizons**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t04.device.device_alloc_fair@1`
- `cap.t04.device.device_alloc_fair.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.green.green_scheduling@1` | use the in-file conservative substitute for `green_scheduling` (documented, slower, lower quality) and set `degraded['green_scheduling']='local'` |
| `cap.t01.shutdown.shutdown_drain@1` | use the in-file conservative substitute for `shutdown_drain` (documented, slower, lower quality) and set `degraded['shutdown_drain']='local'` |
| `cap.t02.kernel.kernel_docs_spec@1` | use the in-file conservative substitute for `kernel_docs_spec` (documented, slower, lower quality) and set `degraded['kernel_docs_spec']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - dominant-resource fairness across heterogeneous devices | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - borrowing/lending with reclaim guarantees | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - starvation-freedom proof and monitoring | 520 | Third required mechanism. |
| 6 | Core implementation D - fairness metric measurement over long horizons | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0198_device_alloc_fair.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.device.device_alloc_fair@1`.
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

### P0199 · `hpc_interop` — HPC & Scientific Stack Interoperability

| field | value |
|---|---|
| part id | `P0199` (49/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0199_hpc_interop.rs` |
| module path | `hyperion.t04.hardware.hpc_interop` |
| capability published | `cap.t04.hpc.hpc_interop@1` |
| determinism class | `io` |
| p99 latency budget | 14000 ns (14 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0199_hpc_interop.txt`](prompts/P0199_hpc_interop.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0199-hpc-interop) |

**Mission.** Works inside existing supercomputing environments.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **MPI-compatible bootstrap and communicator mapping** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **shared-filesystem-friendly IO patterns** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **job-script generation for major HPC sites**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **validated runs on multiple site configurations** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t04.hpc.hpc_interop@1`
- `cap.t04.hpc.hpc_interop.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.device.device_alloc_fair@1` | use the in-file conservative substitute for `device_alloc_fair` (documented, slower, lower quality) and set `degraded['device_alloc_fair']='local'` |
| `cap.t02.attn.attn_paged_decode@1` | use the in-file conservative substitute for `attn_paged_decode` (documented, slower, lower quality) and set `degraded['attn_paged_decode']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - MPI-compatible bootstrap and communicator mapping | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - shared-filesystem-friendly IO patterns | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - job-script generation for major HPC sites | 520 | Third required mechanism. |
| 6 | Core implementation D - validated runs on multiple site configurations | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0199_hpc_interop.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.hpc.hpc_interop@1`.
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

### P0200 · `provision_verify` — Node Admission & Continuous Verification

| field | value |
|---|---|
| part id | `P0200` (50/50 of T04) |
| tier | `T04` — Hardware Abstraction & Interconnect |
| language | Rust 1.86 |
| file to produce | `parts/t04_hardware/P0200_provision_verify.rs` |
| module path | `hyperion.t04.hardware.provision_verify` |
| capability published | `cap.t04.provision.provision_verify@1` |
| determinism class | `io` |
| p99 latency budget | 15000 ns (15 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | SWE-bench Verified |
| worker prompt | [`prompts/P0200_provision_verify.txt`](prompts/P0200_provision_verify.txt) · [inline](docs/PROMPTS_T04.md#prompt-p0200-provision-verify) |

**Mission.** Every machine proves it is healthy and correct before and during service.

**Tier context.** Device fabric, topology-aware collectives, RDMA transport, fault domains and power/thermal governance across 100k accelerators.

**Mandate — all four items are required; none is optional.**

1. Implement **burn-in suite: numeric correctness, bandwidth, thermal, memory integrity** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **continuous lightweight verification during production**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **SWE-bench Verified** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **automatic quarantine on verification failure** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **SWE-bench Verified** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **escape-rate measurement of bad nodes reaching production** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **SWE-bench Verified**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t04.provision.provision_verify@1`
- `cap.t04.provision.provision_verify.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t04.hpc.hpc_interop@1` | use the in-file conservative substitute for `hpc_interop` (documented, slower, lower quality) and set `degraded['hpc_interop']='local'` |
| `cap.t01.atomics.atomics_sync@1` | use the in-file conservative substitute for `atomics_sync` (documented, slower, lower quality) and set `degraded['atomics_sync']='local'` |
| `cap.t02.topk.topk_sort@1` | use the in-file conservative substitute for `topk_sort` (documented, slower, lower quality) and set `degraded['topk_sort']='local'` |

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - burn-in suite: numeric correctness, bandwidth, thermal, memory i | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - continuous lightweight verification during production | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - automatic quarantine on verification failure | 520 | Third required mechanism. |
| 6 | Core implementation D - escape-rate measurement of bad nodes reaching production | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t04_hardware/P0200_provision_verify.rs`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t04.provision.provision_verify@1`.
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
