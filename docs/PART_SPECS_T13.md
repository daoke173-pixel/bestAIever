# HYPERION-Ω — Part specifications · T13 · Agents, Tool Use & Computer Control

> Contract: **Ω-CONTRACT v1.0.0-frozen** · 50 parts · 250,000 lines of code · language: Python 3.13

**Tier mission.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Benchmarks this tier is accountable for.** OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web

**Tier dependencies.** T01, T07, T10

Each part below is built by exactly one isolated Opus 5 worker that sees only: this specification, the frozen Ω-Contract, and its own prompt. Workers never see each other's files. Link-compatibility comes from the contract, not from coordination.

| part | slug | title | capability |
|---|---|---|---|
| [P0601](#p0601-agent-loop) | `agent_loop` | Core Agent Execution Loop | `cap.t13.agent.agent_loop@1` |
| [P0602](#p0602-tool-protocol) | `tool_protocol` | Tool Definition & Invocation Protocol | `cap.t13.tool.tool_protocol@1` |
| [P0603](#p0603-tool-selection) | `tool_selection` | Tool Selection & Discovery | `cap.t13.tool.tool_selection@1` |
| [P0604](#p0604-tool-composition) | `tool_composition` | Tool Chaining & Composition Planner | `cap.t13.tool.tool_composition@1` |
| [P0605](#p0605-mid-conversation-tools) | `mid_conversation_tools` | Dynamic Tool Set Management | `cap.t13.mid.mid_conversation_tools@1` |
| [P0606](#p0606-terminal-agent) | `terminal_agent` | Terminal & Shell Operation Agent | `cap.t13.terminal.terminal_agent@1` |
| [P0607](#p0607-filesystem-agent) | `filesystem_agent` | Filesystem Navigation & Manipulation | `cap.t13.filesystem.filesystem_agent@1` |
| [P0608](#p0608-browser-agent) | `browser_agent` | Web Browser Automation Agent | `cap.t13.browser.browser_agent@1` |
| [P0609](#p0609-web-research) | `web_research` | Deep Web Research Agent | `cap.t13.web.web_research@1` |
| [P0610](#p0610-computer-use-agent) | `computer_use_agent` | Desktop Computer Use Agent | `cap.t13.computer.computer_use_agent@1` |
| [P0611](#p0611-gui-grounding) | `gui_grounding` | GUI Element Grounding & Interaction | `cap.t13.gui.gui_grounding@1` |
| [P0612](#p0612-mobile-agent) | `mobile_agent` | Mobile Device Automation | `cap.t13.mobile.mobile_agent@1` |
| [P0613](#p0613-api-agent) | `api_agent` | REST/GraphQL API Integration Agent | `cap.t13.api.api_agent@1` |
| [P0614](#p0614-database-agent) | `database_agent` | Database Query & Administration Agent | `cap.t13.database.database_agent@1` |
| [P0615](#p0615-business-automation) | `business_automation` | Business Workflow Automation Agent | `cap.t13.business.business_automation@1` |
| [P0616](#p0616-spreadsheet-agent) | `spreadsheet_agent` | Spreadsheet & Tabular Data Agent | `cap.t13.spreadsheet.spreadsheet_agent@1` |
| [P0617](#p0617-document-workflow) | `document_workflow` | Document Processing Workflow Agent | `cap.t13.document.document_workflow@1` |
| [P0618](#p0618-email-communication) | `email_communication` | Communication & Correspondence Agent | `cap.t13.email.email_communication@1` |
| [P0619](#p0619-scheduling-agent) | `scheduling_agent` | Calendar & Coordination Agent | `cap.t13.scheduling.scheduling_agent@1` |
| [P0620](#p0620-multi-agent-orchestration) | `multi_agent_orchestration` | Multi-Agent Orchestration Framework | `cap.t13.multi.multi_agent_orchestration@1` |
| [P0621](#p0621-agent-communication) | `agent_communication` | Inter-Agent Communication Protocol | `cap.t13.agent.agent_communication@1` |
| [P0622](#p0622-agent-delegation) | `agent_delegation` | Task Delegation & Subagent Spawning | `cap.t13.agent.agent_delegation@1` |
| [P0623](#p0623-agent-supervision) | `agent_supervision` | Agent Supervision & Intervention | `cap.t13.agent.agent_supervision@1` |
| [P0624](#p0624-consensus-agents) | `consensus_agents` | Multi-Agent Consensus & Conflict Resolution | `cap.t13.consensus.consensus_agents@1` |
| [P0625](#p0625-environment-model) | `environment_model` | Environment State Modelling & Prediction | `cap.t13.environment.environment_model@1` |
| [P0626](#p0626-action-verification) | `action_verification` | Post-Action Verification Loop | `cap.t13.action.action_verification@1` |
| [P0627](#p0627-error-recovery-agent) | `error_recovery_agent` | Failure Recovery & Adaptation | `cap.t13.error.error_recovery_agent@1` |
| [P0628](#p0628-long-horizon-memory) | `long_horizon_memory` | Long-Horizon Task Memory | `cap.t13.long.long_horizon_memory@1` |
| [P0629](#p0629-progress-tracking) | `progress_tracking` | Progress Estimation & Reporting | `cap.t13.progress.progress_tracking@1` |
| [P0630](#p0630-human-in-loop) | `human_in_loop` | Human Handoff & Approval Workflow | `cap.t13.human.human_in_loop@1` |
| [P0631](#p0631-agent-safety-gate) | `agent_safety_gate` | Agent Action Safety Gate | `cap.t13.agent.agent_safety_gate@1` |
| [P0632](#p0632-credential-management) | `credential_management` | Credential & Permission Management | `cap.t13.credential.credential_management@1` |
| [P0633](#p0633-cost-control-agent) | `cost_control_agent` | Agent Cost Governance | `cap.t13.cost.cost_control_agent@1` |
| [P0634](#p0634-sandbox-execution) | `sandbox_execution` | Agent Sandbox & Isolation Runtime | `cap.t13.sandbox.sandbox_execution@1` |
| [P0635](#p0635-tool-creation) | `tool_creation` | Dynamic Tool Creation | `cap.t13.tool.tool_creation@1` |
| [P0636](#p0636-workflow-learning) | `workflow_learning` | Workflow Learning & Skill Acquisition | `cap.t13.workflow.workflow_learning@1` |
| [P0637](#p0637-observation-compression) | `observation_compression` | Observation Compression & Attention | `cap.t13.observation.observation_compression@1` |
| [P0638](#p0638-agent-determinism) | `agent_determinism` | Reproducible Agent Execution | `cap.t13.agent.agent_determinism@1` |
| [P0639](#p0639-agent-eval-harness) | `agent_eval_harness` | Agent Benchmark Harness | `cap.t13.agent.agent_eval_harness@1` |
| [P0640](#p0640-trajectory-analysis) | `trajectory_analysis` | Trajectory Analysis & Improvement Mining | `cap.t13.trajectory.trajectory_analysis@1` |
| [P0641](#p0641-agent-interruption) | `agent_interruption` | Interruption, Steering & Course Correction | `cap.t13.agent.agent_interruption@1` |
| [P0642](#p0642-simulation-env) | `simulation_env` | Agent Training & Testing Environments | `cap.t13.simulation.simulation_env@1` |
| [P0643](#p0643-robotics-bridge) | `robotics_bridge` | Physical Actuation Interface | `cap.t13.robotics.robotics_bridge@1` |
| [P0644](#p0644-iot-control) | `iot_control` | Device & Infrastructure Control Agent | `cap.t13.iot.iot_control@1` |
| [P0645](#p0645-scientific-agent) | `scientific_agent` | Autonomous Research Agent | `cap.t13.scientific.scientific_agent@1` |
| [P0646](#p0646-data-analysis-agent) | `data_analysis_agent` | Autonomous Data Analysis Agent | `cap.t13.data.data_analysis_agent@1` |
| [P0647](#p0647-agent-ux) | `agent_ux` | Agent Transparency & Explainability | `cap.t13.agent.agent_ux@1` |
| [P0648](#p0648-agent-speed) | `agent_speed` | Agent Latency Engineering | `cap.t13.agent.agent_speed@1` |
| [P0649](#p0649-agent-scaling) | `agent_scaling` | 1000-Agent Scale Coordination | `cap.t13.agent.agent_scaling@1` |
| [P0650](#p0650-agent-spec-doc) | `agent_spec_doc` | Agent Subsystem Specification & Runbook | `cap.t13.agent.agent_spec_doc@1` |

---

### P0601 · `agent_loop` — Core Agent Execution Loop

| field | value |
|---|---|
| part id | `P0601` (1/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0601_agent_loop.py` |
| module path | `hyperion.t13.agents.agent_loop` |
| capability published | `cap.t13.agent.agent_loop@1` |
| determinism class | `io` |
| p99 latency budget | 40000 ns (40 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0601_agent_loop.txt`](prompts/P0601_agent_loop.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0601-agent-loop) |

**Mission.** The observe-think-act-verify cycle that runs for hours without drifting.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **loop with explicit state, budget and termination conditions**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **BrowseComp** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **progress detection and stagnation breaking** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **checkpointing so a long task survives interruption** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **Online-Mind2Web** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured task-completion rate on multi-hour horizons** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t13.agent.agent_loop@1`
- `cap.t13.agent.agent_loop.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t01.string.string_interning@1` | use the in-file conservative substitute for `string_interning` (documented, slower, lower quality) and set `degraded['string_interning']='local'` |
| `cap.t07.freshness.freshness_manager@1` | use the in-file conservative substitute for `freshness_manager` (documented, slower, lower quality) and set `degraded['freshness_manager']='local'` |
| `cap.t10.numeric.numeric_reasoning@1` | use the in-file conservative substitute for `numeric_reasoning` (documented, slower, lower quality) and set `degraded['numeric_reasoning']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - loop with explicit state, budget and termination conditions | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - progress detection and stagnation breaking | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - checkpointing so a long task survives interruption | 520 | Third required mechanism. |
| 6 | Core implementation D - measured task-completion rate on multi-hour horizons | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0601_agent_loop.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.agent.agent_loop@1`.
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

### P0602 · `tool_protocol` — Tool Definition & Invocation Protocol

| field | value |
|---|---|
| part id | `P0602` (2/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0602_tool_protocol.py` |
| module path | `hyperion.t13.agents.tool_protocol` |
| capability published | `cap.t13.tool.tool_protocol@1` |
| determinism class | `io` |
| p99 latency budget | 41000 ns (41 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0602_tool_protocol.txt`](prompts/P0602_tool_protocol.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0602-tool-protocol) |

**Mission.** How the model discovers, calls and interprets tools.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **tool schema format with typed arguments, errors and side-effect declarations** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **argument validation and coercion with clear failure messages** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **Online-Mind2Web** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **result normalisation into a uniform observation format** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **protocol conformance test suite for tool authors**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **BrowseComp**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t13.tool.tool_protocol@1`
- `cap.t13.tool.tool_protocol.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.agent.agent_loop@1` | use the in-file conservative substitute for `agent_loop` (documented, slower, lower quality) and set `degraded['agent_loop']='local'` |
| `cap.t01.property.property_gen@1` | use the in-file conservative substitute for `property_gen` (documented, slower, lower quality) and set `degraded['property_gen']='local'` |
| `cap.t07.attention.attention_sink@1` | use the in-file conservative substitute for `attention_sink` (documented, slower, lower quality) and set `degraded['attention_sink']='local'` |
| `cap.t10.backtracking.backtracking@1` | use the in-file conservative substitute for `backtracking` (documented, slower, lower quality) and set `degraded['backtracking']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - tool schema format with typed arguments, errors and side-effect  | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - argument validation and coercion with clear failure messages | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - result normalisation into a uniform observation format | 520 | Third required mechanism. |
| 6 | Core implementation D - protocol conformance test suite for tool authors | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0602_tool_protocol.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.tool.tool_protocol@1`.
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

### P0603 · `tool_selection` — Tool Selection & Discovery

| field | value |
|---|---|
| part id | `P0603` (3/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0603_tool_selection.py` |
| module path | `hyperion.t13.agents.tool_selection` |
| capability published | `cap.t13.tool.tool_selection@1` |
| determinism class | `io` |
| p99 latency budget | 42000 ns (42 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0603_tool_selection.txt`](prompts/P0603_tool_selection.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0603-tool-selection) |

**Mission.** Picks the right tool from thousands without confusion.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **semantic tool retrieval scaling to 10000+ tools** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **Online-Mind2Web** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **capability matching against the current subgoal** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **selection-accuracy measurement and confusion analysis**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **BrowseComp**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **cost/latency-aware selection among equivalent tools** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t13.tool.tool_selection@1`
- `cap.t13.tool.tool_selection.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.tool.tool_protocol@1` | use the in-file conservative substitute for `tool_protocol` (documented, slower, lower quality) and set `degraded['tool_protocol']='local'` |
| `cap.t01.link.link_validator@1` | use the in-file conservative substitute for `link_validator` (documented, slower, lower quality) and set `degraded['link_validator']='local'` |
| `cap.t07.persistence.persistence_layer@1` | use the in-file conservative substitute for `persistence_layer` (documented, slower, lower quality) and set `degraded['persistence_layer']='local'` |
| `cap.t10.question.question_asking@1` | use the in-file conservative substitute for `question_asking` (documented, slower, lower quality) and set `degraded['question_asking']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - semantic tool retrieval scaling to 10000+ tools | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - capability matching against the current subgoal | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - selection-accuracy measurement and confusion analysis | 520 | Third required mechanism. |
| 6 | Core implementation D - cost/latency-aware selection among equivalent tools | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0603_tool_selection.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.tool.tool_selection@1`.
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

### P0604 · `tool_composition` — Tool Chaining & Composition Planner

| field | value |
|---|---|
| part id | `P0604` (4/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0604_tool_composition.py` |
| module path | `hyperion.t13.agents.tool_composition` |
| capability published | `cap.t13.tool.tool_composition@1` |
| determinism class | `io` |
| p99 latency budget | 43000 ns (43 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0604_tool_composition.txt`](prompts/P0604_tool_composition.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0604-tool-composition) |

**Mission.** Builds multi-tool pipelines and runs them in parallel.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **dataflow planning across tool calls with type compatibility checking** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **parallel execution of independent calls (S6 contributor)**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **BrowseComp**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **intermediate-result management and transformation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured latency reduction from parallel composition** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Online-Mind2Web** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t13.tool.tool_composition@1`
- `cap.t13.tool.tool_composition.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.tool.tool_selection@1` | use the in-file conservative substitute for `tool_selection` (documented, slower, lower quality) and set `degraded['tool_selection']='local'` |
| `cap.t01.rate.rate_limiter@1` | use the in-file conservative substitute for `rate_limiter` (documented, slower, lower quality) and set `degraded['rate_limiter']='local'` |
| `cap.t07.index.index_build_pipeline@1` | use the in-file conservative substitute for `index_build_pipeline` (documented, slower, lower quality) and set `degraded['index_build_pipeline']='local'` |
| `cap.t10.scratchpad.scratchpad_manager@1` | use the in-file conservative substitute for `scratchpad_manager` (documented, slower, lower quality) and set `degraded['scratchpad_manager']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - dataflow planning across tool calls with type compatibility chec | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - parallel execution of independent calls (S6 contributor) | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - intermediate-result management and transformation | 520 | Third required mechanism. |
| 6 | Core implementation D - measured latency reduction from parallel composition | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0604_tool_composition.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.tool.tool_composition@1`.
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

### P0605 · `mid_conversation_tools` — Dynamic Tool Set Management

| field | value |
|---|---|
| part id | `P0605` (5/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0605_mid_conversation_tools.py` |
| module path | `hyperion.t13.agents.mid_conversation_tools` |
| capability published | `cap.t13.mid.mid_conversation_tools@1` |
| determinism class | `io` |
| p99 latency budget | 44000 ns (44 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0605_mid_conversation_tools.txt`](prompts/P0605_mid_conversation_tools.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0605-mid-conversation-tools) |

**Mission.** Tools appear and disappear mid-task without breaking the cache.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **tool-set mutation with prompt-cache preservation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **BrowseComp**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **capability re-planning when a tool disappears** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **consistency verification across tool-set changes** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Online-Mind2Web** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured cache-hit preservation rate** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t13.mid.mid_conversation_tools@1`
- `cap.t13.mid.mid_conversation_tools.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.tool.tool_composition@1` | use the in-file conservative substitute for `tool_composition` (documented, slower, lower quality) and set `degraded['tool_composition']='local'` |
| `cap.t01.bootstrap.bootstrap_init@1` | use the in-file conservative substitute for `bootstrap_init` (documented, slower, lower quality) and set `degraded['bootstrap_init']='local'` |
| `cap.t07.cost.cost_aware_retrieval@1` | use the in-file conservative substitute for `cost_aware_retrieval` (documented, slower, lower quality) and set `degraded['cost_aware_retrieval']='local'` |
| `cap.t10.reasoning.reasoning_speed_proof@1` | use the in-file conservative substitute for `reasoning_speed_proof` (documented, slower, lower quality) and set `degraded['reasoning_speed_proof']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - tool-set mutation with prompt-cache preservation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - capability re-planning when a tool disappears | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - consistency verification across tool-set changes | 520 | Third required mechanism. |
| 6 | Core implementation D - measured cache-hit preservation rate | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0605_mid_conversation_tools.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.mid.mid_conversation_tools@1`.
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

### P0606 · `terminal_agent` — Terminal & Shell Operation Agent

| field | value |
|---|---|
| part id | `P0606` (6/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0606_terminal_agent.py` |
| module path | `hyperion.t13.agents.terminal_agent` |
| capability published | `cap.t13.terminal.terminal_agent@1` |
| determinism class | `io` |
| p99 latency budget | 45000 ns (45 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0606_terminal_agent.txt`](prompts/P0606_terminal_agent.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0606-terminal-agent) |

**Mission.** Uses a real shell as competently as a senior engineer.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **command construction with quoting, escaping and platform awareness** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **output parsing including interactive and paging behaviour** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Online-Mind2Web** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **destructive-command detection and confirmation gating** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **target contribution to Terminal-Bench 98.5%**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **BrowseComp** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t13.terminal.terminal_agent@1`
- `cap.t13.terminal.terminal_agent.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.mid.mid_conversation_tools@1` | use the in-file conservative substitute for `mid_conversation_tools` (documented, slower, lower quality) and set `degraded['mid_conversation_tools']='local'` |
| `cap.t01.chacha.chacha_seeds@1` | use the in-file conservative substitute for `chacha_seeds` (documented, slower, lower quality) and set `degraded['chacha_seeds']='local'` |
| `cap.t07.context.context_window_manager@1` | use the in-file conservative substitute for `context_window_manager` (documented, slower, lower quality) and set `degraded['context_window_manager']='local'` |
| `cap.t10.process.process_verifier@1` | use the in-file conservative substitute for `process_verifier` (documented, slower, lower quality) and set `degraded['process_verifier']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - command construction with quoting, escaping and platform awarene | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - output parsing including interactive and paging behaviour | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - destructive-command detection and confirmation gating | 520 | Third required mechanism. |
| 6 | Core implementation D - target contribution to Terminal-Bench 98.5% | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0606_terminal_agent.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.terminal.terminal_agent@1`.
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

### P0607 · `filesystem_agent` — Filesystem Navigation & Manipulation

| field | value |
|---|---|
| part id | `P0607` (7/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0607_filesystem_agent.py` |
| module path | `hyperion.t13.agents.filesystem_agent` |
| capability published | `cap.t13.filesystem.filesystem_agent@1` |
| determinism class | `io` |
| p99 latency budget | 46000 ns (46 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0607_filesystem_agent.txt`](prompts/P0607_filesystem_agent.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0607-filesystem-agent) |

**Mission.** Explores and edits large file trees efficiently and safely.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **efficient exploration strategies avoiding full-tree scans** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Online-Mind2Web** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **atomic multi-file edit application with rollback** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **permission and symlink hazard handling**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **BrowseComp** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured efficiency versus naive traversal** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t13.filesystem.filesystem_agent@1`
- `cap.t13.filesystem.filesystem_agent.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.terminal.terminal_agent@1` | use the in-file conservative substitute for `terminal_agent` (documented, slower, lower quality) and set `degraded['terminal_agent']='local'` |
| `cap.t01.mem.mem_layout@1` | use the in-file conservative substitute for `mem_layout` (documented, slower, lower quality) and set `degraded['mem_layout']='local'` |
| `cap.t07.vector.vector_index@1` | use the in-file conservative substitute for `vector_index` (documented, slower, lower quality) and set `degraded['vector_index']='local'` |
| `cap.t10.goal.goal_management@1` | use the in-file conservative substitute for `goal_management` (documented, slower, lower quality) and set `degraded['goal_management']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - efficient exploration strategies avoiding full-tree scans | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - atomic multi-file edit application with rollback | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - permission and symlink hazard handling | 520 | Third required mechanism. |
| 6 | Core implementation D - measured efficiency versus naive traversal | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0607_filesystem_agent.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.filesystem.filesystem_agent@1`.
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

### P0608 · `browser_agent` — Web Browser Automation Agent

| field | value |
|---|---|
| part id | `P0608` (8/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0608_browser_agent.py` |
| module path | `hyperion.t13.agents.browser_agent` |
| capability published | `cap.t13.browser.browser_agent@1` |
| determinism class | `io` |
| p99 latency budget | 47000 ns (47 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0608_browser_agent.txt`](prompts/P0608_browser_agent.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0608-browser-agent) |

**Mission.** Uses the real web: forms, auth, dynamic content, verification.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **DOM plus visual understanding for element identification** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **form filling, navigation, waiting and dynamic-content handling**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **BrowseComp** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **self-verification of achieved state after each action** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **targets: Online-Mind2Web 98.5%, BrowseComp 99.0%** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **Online-Mind2Web**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t13.browser.browser_agent@1`
- `cap.t13.browser.browser_agent.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.filesystem.filesystem_agent@1` | use the in-file conservative substitute for `filesystem_agent` (documented, slower, lower quality) and set `degraded['filesystem_agent']='local'` |
| `cap.t01.hash.hash_maps@1` | use the in-file conservative substitute for `hash_maps` (documented, slower, lower quality) and set `degraded['hash_maps']='local'` |
| `cap.t07.citation.citation_grounding@1` | use the in-file conservative substitute for `citation_grounding` (documented, slower, lower quality) and set `degraded['citation_grounding']='local'` |
| `cap.t10.probabilistic.probabilistic_reasoning@1` | use the in-file conservative substitute for `probabilistic_reasoning` (documented, slower, lower quality) and set `degraded['probabilistic_reasoning']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - DOM plus visual understanding for element identification | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - form filling, navigation, waiting and dynamic-content handling | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - self-verification of achieved state after each action | 520 | Third required mechanism. |
| 6 | Core implementation D - targets: Online-Mind2Web 98.5%, BrowseComp 99.0% | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0608_browser_agent.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.browser.browser_agent@1`.
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

### P0609 · `web_research` — Deep Web Research Agent

| field | value |
|---|---|
| part id | `P0609` (9/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0609_web_research.py` |
| module path | `hyperion.t13.agents.web_research` |
| capability published | `cap.t13.web.web_research@1` |
| determinism class | `io` |
| p99 latency budget | 48000 ns (48 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0609_web_research.txt`](prompts/P0609_web_research.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0609-web-research) |

**Mission.** Finds the answer that requires reading forty pages.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **search-query strategy with iterative refinement**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **BrowseComp** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **source credibility assessment and cross-verification** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **information synthesis with full citation tracking** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **Online-Mind2Web**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **target: BrowseComp 99.0% versus Opus 5's 90.8%** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t13.web.web_research@1`
- `cap.t13.web.web_research.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.browser.browser_agent@1` | use the in-file conservative substitute for `browser_agent` (documented, slower, lower quality) and set `degraded['browser_agent']='local'` |
| `cap.t01.selftest.selftest_harness@1` | use the in-file conservative substitute for `selftest_harness` (documented, slower, lower quality) and set `degraded['selftest_harness']='local'` |
| `cap.t07.memory.memory_compression_learned@1` | use the in-file conservative substitute for `memory_compression_learned` (documented, slower, lower quality) and set `degraded['memory_compression_learned']='local'` |
| `cap.t10.stopping.stopping_rules@1` | use the in-file conservative substitute for `stopping_rules` (documented, slower, lower quality) and set `degraded['stopping_rules']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - search-query strategy with iterative refinement | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - source credibility assessment and cross-verification | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - information synthesis with full citation tracking | 520 | Third required mechanism. |
| 6 | Core implementation D - target: BrowseComp 99.0% versus Opus 5's 90.8% | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0609_web_research.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.web.web_research@1`.
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

### P0610 · `computer_use_agent` — Desktop Computer Use Agent

| field | value |
|---|---|
| part id | `P0610` (10/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0610_computer_use_agent.py` |
| module path | `hyperion.t13.agents.computer_use_agent` |
| capability published | `cap.t13.computer.computer_use_agent@1` |
| determinism class | `io` |
| p99 latency budget | 49000 ns (49 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0610_computer_use_agent.txt`](prompts/P0610_computer_use_agent.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0610-computer-use-agent) |

**Mission.** Operates arbitrary GUI applications through screenshots.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **screen understanding, element grounding and precise coordinate action** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **keyboard/mouse action sequencing with verification after each step** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **Online-Mind2Web**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **application-state tracking and error recovery** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **target: OSWorld 2.0 95.5% versus Opus 5's 70.5%**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **BrowseComp** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t13.computer.computer_use_agent@1`
- `cap.t13.computer.computer_use_agent.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.web.web_research@1` | use the in-file conservative substitute for `web_research` (documented, slower, lower quality) and set `degraded['web_research']='local'` |
| `cap.t01.version.version_semver@1` | use the in-file conservative substitute for `version_semver` (documented, slower, lower quality) and set `degraded['version_semver']='local'` |
| `cap.t07.memory.memory_gc@1` | use the in-file conservative substitute for `memory_gc` (documented, slower, lower quality) and set `degraded['memory_gc']='local'` |
| `cap.t10.assumption.assumption_tracking@1` | use the in-file conservative substitute for `assumption_tracking` (documented, slower, lower quality) and set `degraded['assumption_tracking']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - screen understanding, element grounding and precise coordinate a | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - keyboard/mouse action sequencing with verification after each st | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - application-state tracking and error recovery | 520 | Third required mechanism. |
| 6 | Core implementation D - target: OSWorld 2.0 95.5% versus Opus 5's 70.5% | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0610_computer_use_agent.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.computer.computer_use_agent@1`.
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

### P0611 · `gui_grounding` — GUI Element Grounding & Interaction

| field | value |
|---|---|
| part id | `P0611` (11/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0611_gui_grounding.py` |
| module path | `hyperion.t13.agents.gui_grounding` |
| capability published | `cap.t13.gui.gui_grounding@1` |
| determinism class | `io` |
| p99 latency budget | 3000 ns (3 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0611_gui_grounding.txt`](prompts/P0611_gui_grounding.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0611-gui-grounding) |

**Mission.** Clicks the right pixel, every time.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **visual element detection with role and state inference** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **Online-Mind2Web**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **accessibility-tree fusion where available** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **coordinate-precision measurement and calibration across resolutions**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **BrowseComp** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **grounding accuracy measurement on GUI benchmark suites** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t13.gui.gui_grounding@1`
- `cap.t13.gui.gui_grounding.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.computer.computer_use_agent@1` | use the in-file conservative substitute for `computer_use_agent` (documented, slower, lower quality) and set `degraded['computer_use_agent']='local'` |
| `cap.t01.budget.budget_ledger@1` | use the in-file conservative substitute for `budget_ledger` (documented, slower, lower quality) and set `degraded['budget_ledger']='local'` |
| `cap.t07.memory.memory_audit@1` | use the in-file conservative substitute for `memory_audit` (documented, slower, lower quality) and set `degraded['memory_audit']='local'` |
| `cap.t10.reasoning.reasoning_cost_model@1` | use the in-file conservative substitute for `reasoning_cost_model` (documented, slower, lower quality) and set `degraded['reasoning_cost_model']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - visual element detection with role and state inference | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - accessibility-tree fusion where available | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - coordinate-precision measurement and calibration across resoluti | 520 | Third required mechanism. |
| 6 | Core implementation D - grounding accuracy measurement on GUI benchmark suites | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0611_gui_grounding.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.gui.gui_grounding@1`.
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

### P0612 · `mobile_agent` — Mobile Device Automation

| field | value |
|---|---|
| part id | `P0612` (12/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0612_mobile_agent.py` |
| module path | `hyperion.t13.agents.mobile_agent` |
| capability published | `cap.t13.mobile.mobile_agent@1` |
| determinism class | `io` |
| p99 latency budget | 4000 ns (4 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0612_mobile_agent.txt`](prompts/P0612_mobile_agent.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0612-mobile-agent) |

**Mission.** Operates phone and tablet interfaces natively.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **touch-gesture action space including swipe, pinch and long-press** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **mobile-app state tracking across activities**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **BrowseComp** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **platform-specific convention handling** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **task-success measurement on mobile benchmark suites** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **Online-Mind2Web** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t13.mobile.mobile_agent@1`
- `cap.t13.mobile.mobile_agent.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.gui.gui_grounding@1` | use the in-file conservative substitute for `gui_grounding` (documented, slower, lower quality) and set `degraded['gui_grounding']='local'` |
| `cap.t01.compression.compression@1` | use the in-file conservative substitute for `compression` (documented, slower, lower quality) and set `degraded['compression']='local'` |
| `cap.t07.streaming.streaming_ingest@1` | use the in-file conservative substitute for `streaming_ingest` (documented, slower, lower quality) and set `degraded['streaming_ingest']='local'` |
| `cap.t10.collective.collective_reasoning@1` | use the in-file conservative substitute for `collective_reasoning` (documented, slower, lower quality) and set `degraded['collective_reasoning']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - touch-gesture action space including swipe, pinch and long-press | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - mobile-app state tracking across activities | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - platform-specific convention handling | 520 | Third required mechanism. |
| 6 | Core implementation D - task-success measurement on mobile benchmark suites | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0612_mobile_agent.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.mobile.mobile_agent@1`.
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

### P0613 · `api_agent` — REST/GraphQL API Integration Agent

| field | value |
|---|---|
| part id | `P0613` (13/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0613_api_agent.py` |
| module path | `hyperion.t13.agents.api_agent` |
| capability published | `cap.t13.api.api_agent@1` |
| determinism class | `io` |
| p99 latency budget | 5000 ns (5 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0613_api_agent.txt`](prompts/P0613_api_agent.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0613-api-agent) |

**Mission.** Uses arbitrary APIs correctly from their documentation.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **API-documentation comprehension into executable call plans**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **BrowseComp** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **authentication flow handling (OAuth, keys, tokens) with secret hygiene** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **pagination, rate limiting and error-code handling** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **Online-Mind2Web** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **success rate on unseen-API task suites** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t13.api.api_agent@1`
- `cap.t13.api.api_agent.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.mobile.mobile_agent@1` | use the in-file conservative substitute for `mobile_agent` (documented, slower, lower quality) and set `degraded['mobile_agent']='local'` |
| `cap.t01.blake3.blake3_hash@1` | use the in-file conservative substitute for `blake3_hash` (documented, slower, lower quality) and set `degraded['blake3_hash']='local'` |
| `cap.t07.kv.kv_compression_runtime@1` | use the in-file conservative substitute for `kv_compression_runtime` (documented, slower, lower quality) and set `degraded['kv_compression_runtime']='local'` |
| `cap.t10.beam.beam_pruning@1` | use the in-file conservative substitute for `beam_pruning` (documented, slower, lower quality) and set `degraded['beam_pruning']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - API-documentation comprehension into executable call plans | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - authentication flow handling (OAuth, keys, tokens) with secret h | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - pagination, rate limiting and error-code handling | 520 | Third required mechanism. |
| 6 | Core implementation D - success rate on unseen-API task suites | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0613_api_agent.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.api.api_agent@1`.
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

### P0614 · `database_agent` — Database Query & Administration Agent

| field | value |
|---|---|
| part id | `P0614` (14/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0614_database_agent.py` |
| module path | `hyperion.t13.agents.database_agent` |
| capability published | `cap.t13.database.database_agent@1` |
| determinism class | `io` |
| p99 latency budget | 6000 ns (6 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0614_database_agent.txt`](prompts/P0614_database_agent.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0614-database-agent) |

**Mission.** Writes correct SQL against schemas it has never seen.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **schema exploration and semantic understanding** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **query construction with correctness verification before execution** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **Online-Mind2Web** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **migration authoring with rollback plans** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **accuracy measurement on text-to-SQL and admin task suites**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **BrowseComp**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t13.database.database_agent@1`
- `cap.t13.database.database_agent.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.api.api_agent@1` | use the in-file conservative substitute for `api_agent` (documented, slower, lower quality) and set `degraded['api_agent']='local'` |
| `cap.t01.alloc.alloc_arena@1` | use the in-file conservative substitute for `alloc_arena` (documented, slower, lower quality) and set `degraded['alloc_arena']='local'` |
| `cap.t07.forgetting.forgetting_policy@1` | use the in-file conservative substitute for `forgetting_policy` (documented, slower, lower quality) and set `degraded['forgetting_policy']='local'` |
| `cap.t10.planning.planning_engine@1` | use the in-file conservative substitute for `planning_engine` (documented, slower, lower quality) and set `degraded['planning_engine']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - schema exploration and semantic understanding | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - query construction with correctness verification before executio | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - migration authoring with rollback plans | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy measurement on text-to-SQL and admin task suites | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0614_database_agent.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.database.database_agent@1`.
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

### P0615 · `business_automation` — Business Workflow Automation Agent

| field | value |
|---|---|
| part id | `P0615` (15/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0615_business_automation.py` |
| module path | `hyperion.t13.agents.business_automation` |
| capability published | `cap.t13.business.business_automation@1` |
| determinism class | `io` |
| p99 latency budget | 7000 ns (7 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0615_business_automation.txt`](prompts/P0615_business_automation.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0615-business-automation) |

**Mission.** Completes real office work end to end.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **multi-app workflow orchestration with state tracking** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **Online-Mind2Web** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **spreadsheet, CRM, email and document operation competence** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **human-handoff points for judgment calls**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **BrowseComp**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **target: Zapier AutomationBench 92% versus Opus 5's 26.0%** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t13.business.business_automation@1`
- `cap.t13.business.business_automation.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.database.database_agent@1` | use the in-file conservative substitute for `database_agent` (documented, slower, lower quality) and set `degraded['database_agent']='local'` |
| `cap.t01.bitset.bitset_rank@1` | use the in-file conservative substitute for `bitset_rank` (documented, slower, lower quality) and set `degraded['bitset_rank']='local'` |
| `cap.t07.reranker.reranker_model@1` | use the in-file conservative substitute for `reranker_model` (documented, slower, lower quality) and set `degraded['reranker_model']='local'` |
| `cap.t10.counterfactual.counterfactual_reasoning@1` | use the in-file conservative substitute for `counterfactual_reasoning` (documented, slower, lower quality) and set `degraded['counterfactual_reasoning']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - multi-app workflow orchestration with state tracking | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - spreadsheet, CRM, email and document operation competence | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - human-handoff points for judgment calls | 520 | Third required mechanism. |
| 6 | Core implementation D - target: Zapier AutomationBench 92% versus Opus 5's 26.0% | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0615_business_automation.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.business.business_automation@1`.
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

### P0616 · `spreadsheet_agent` — Spreadsheet & Tabular Data Agent

| field | value |
|---|---|
| part id | `P0616` (16/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0616_spreadsheet_agent.py` |
| module path | `hyperion.t13.agents.spreadsheet_agent` |
| capability published | `cap.t13.spreadsheet.spreadsheet_agent@1` |
| determinism class | `io` |
| p99 latency budget | 8000 ns (8 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0616_spreadsheet_agent.txt`](prompts/P0616_spreadsheet_agent.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0616-spreadsheet-agent) |

**Mission.** Handles real workbooks: formulas, pivots, errors, scale.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **formula construction and dependency reasoning** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **data cleaning, reconciliation and anomaly detection**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **BrowseComp**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **large-workbook handling without loading everything into context** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **accuracy measurement on spreadsheet task benchmarks** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Online-Mind2Web** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t13.spreadsheet.spreadsheet_agent@1`
- `cap.t13.spreadsheet.spreadsheet_agent.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.business.business_automation@1` | use the in-file conservative substitute for `business_automation` (documented, slower, lower quality) and set `degraded['business_automation']='local'` |
| `cap.t01.metrics.metrics_core@1` | use the in-file conservative substitute for `metrics_core` (documented, slower, lower quality) and set `degraded['metrics_core']='local'` |
| `cap.t07.belief.belief_revision@1` | use the in-file conservative substitute for `belief_revision` (documented, slower, lower quality) and set `degraded['belief_revision']='local'` |
| `cap.t10.difficulty.difficulty_estimation@1` | use the in-file conservative substitute for `difficulty_estimation` (documented, slower, lower quality) and set `degraded['difficulty_estimation']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - formula construction and dependency reasoning | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - data cleaning, reconciliation and anomaly detection | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - large-workbook handling without loading everything into context | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy measurement on spreadsheet task benchmarks | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0616_spreadsheet_agent.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.spreadsheet.spreadsheet_agent@1`.
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

### P0617 · `document_workflow` — Document Processing Workflow Agent

| field | value |
|---|---|
| part id | `P0617` (17/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0617_document_workflow.py` |
| module path | `hyperion.t13.agents.document_workflow` |
| capability published | `cap.t13.document.document_workflow@1` |
| determinism class | `io` |
| p99 latency budget | 9000 ns (9 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0617_document_workflow.txt`](prompts/P0617_document_workflow.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0617-document-workflow) |

**Mission.** Reads, edits and produces business documents faithfully.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **multi-format document parsing with layout and structure preservation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **BrowseComp**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **tracked-change and comment authoring** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **template-conformant document generation** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Online-Mind2Web** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **fidelity measurement on document-task corpora** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t13.document.document_workflow@1`
- `cap.t13.document.document_workflow.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.spreadsheet.spreadsheet_agent@1` | use the in-file conservative substitute for `spreadsheet_agent` (documented, slower, lower quality) and set `degraded['spreadsheet_agent']='local'` |
| `cap.t01.capability.capability_gate@1` | use the in-file conservative substitute for `capability_gate` (documented, slower, lower quality) and set `degraded['capability_gate']='local'` |
| `cap.t07.retrieval.retrieval_cache@1` | use the in-file conservative substitute for `retrieval_cache` (documented, slower, lower quality) and set `degraded['retrieval_cache']='local'` |
| `cap.t10.evidence.evidence_integration@1` | use the in-file conservative substitute for `evidence_integration` (documented, slower, lower quality) and set `degraded['evidence_integration']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - multi-format document parsing with layout and structure preserva | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - tracked-change and comment authoring | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - template-conformant document generation | 520 | Third required mechanism. |
| 6 | Core implementation D - fidelity measurement on document-task corpora | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0617_document_workflow.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.document.document_workflow@1`.
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

### P0618 · `email_communication` — Communication & Correspondence Agent

| field | value |
|---|---|
| part id | `P0618` (18/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0618_email_communication.py` |
| module path | `hyperion.t13.agents.email_communication` |
| capability published | `cap.t13.email.email_communication@1` |
| determinism class | `io` |
| p99 latency budget | 10000 ns (10 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0618_email_communication.txt`](prompts/P0618_email_communication.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0618-email-communication) |

**Mission.** Writes and manages professional correspondence appropriately.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **thread comprehension and context-appropriate composition** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **tone, formality and stakeholder-awareness control** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Online-Mind2Web** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **action-item extraction and follow-up tracking** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **quality evaluation by professional reviewers**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **BrowseComp** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t13.email.email_communication@1`
- `cap.t13.email.email_communication.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.document.document_workflow@1` | use the in-file conservative substitute for `document_workflow` (documented, slower, lower quality) and set `degraded['document_workflow']='local'` |
| `cap.t01.unit.unit_dimensions@1` | use the in-file conservative substitute for `unit_dimensions` (documented, slower, lower quality) and set `degraded['unit_dimensions']='local'` |
| `cap.t07.user.user_model@1` | use the in-file conservative substitute for `user_model` (documented, slower, lower quality) and set `degraded['user_model']='local'` |
| `cap.t10.reasoning.reasoning_search_bench@1` | use the in-file conservative substitute for `reasoning_search_bench` (documented, slower, lower quality) and set `degraded['reasoning_search_bench']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - thread comprehension and context-appropriate composition | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - tone, formality and stakeholder-awareness control | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - action-item extraction and follow-up tracking | 520 | Third required mechanism. |
| 6 | Core implementation D - quality evaluation by professional reviewers | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0618_email_communication.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.email.email_communication@1`.
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

### P0619 · `scheduling_agent` — Calendar & Coordination Agent

| field | value |
|---|---|
| part id | `P0619` (19/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0619_scheduling_agent.py` |
| module path | `hyperion.t13.agents.scheduling_agent` |
| capability published | `cap.t13.scheduling.scheduling_agent@1` |
| determinism class | `io` |
| p99 latency budget | 11000 ns (11 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0619_scheduling_agent.txt`](prompts/P0619_scheduling_agent.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0619-scheduling-agent) |

**Mission.** Solves the real constraint problem of many people's time.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **constraint-based scheduling across timezones and preferences** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Online-Mind2Web** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **negotiation-style multi-party coordination** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **conflict detection and resolution proposals**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **BrowseComp** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **success rate on scheduling benchmark scenarios** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t13.scheduling.scheduling_agent@1`
- `cap.t13.scheduling.scheduling_agent.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.email.email_communication@1` | use the in-file conservative substitute for `email_communication` (documented, slower, lower quality) and set `degraded['email_communication']='local'` |
| `cap.t01.fs.fs_atomic@1` | use the in-file conservative substitute for `fs_atomic` (documented, slower, lower quality) and set `degraded['fs_atomic']='local'` |
| `cap.t07.memory.memory_sharding@1` | use the in-file conservative substitute for `memory_sharding` (documented, slower, lower quality) and set `degraded['memory_sharding']='local'` |
| `cap.t10.reasoning.reasoning_interpretability@1` | use the in-file conservative substitute for `reasoning_interpretability` (documented, slower, lower quality) and set `degraded['reasoning_interpretability']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - constraint-based scheduling across timezones and preferences | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - negotiation-style multi-party coordination | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - conflict detection and resolution proposals | 520 | Third required mechanism. |
| 6 | Core implementation D - success rate on scheduling benchmark scenarios | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0619_scheduling_agent.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.scheduling.scheduling_agent@1`.
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

### P0620 · `multi_agent_orchestration` — Multi-Agent Orchestration Framework

| field | value |
|---|---|
| part id | `P0620` (20/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0620_multi_agent_orchestration.py` |
| module path | `hyperion.t13.agents.multi_agent_orchestration` |
| capability published | `cap.t13.multi.multi_agent_orchestration@1` |
| determinism class | `io` |
| p99 latency budget | 12000 ns (12 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0620_multi_agent_orchestration.txt`](prompts/P0620_multi_agent_orchestration.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0620-multi-agent-orchestration) |

**Mission.** Runs 1000 sub-agents on one goal without chaos.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **role and responsibility assignment with clear interfaces** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **work partitioning, dependency management and result integration**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **BrowseComp** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **conflict detection between concurrent agents' actions** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured speedup and quality versus single-agent execution** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **Online-Mind2Web**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t13.multi.multi_agent_orchestration@1`
- `cap.t13.multi.multi_agent_orchestration.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.scheduling.scheduling_agent@1` | use the in-file conservative substitute for `scheduling_agent` (documented, slower, lower quality) and set `degraded['scheduling_agent']='local'` |
| `cap.t01.cbor.cbor_canonical@1` | use the in-file conservative substitute for `cbor_canonical` (documented, slower, lower quality) and set `degraded['cbor_canonical']='local'` |
| `cap.t07.kv.kv_dedup@1` | use the in-file conservative substitute for `kv_dedup` (documented, slower, lower quality) and set `degraded['kv_dedup']='local'` |
| `cap.t10.graph.graph_search@1` | use the in-file conservative substitute for `graph_search` (documented, slower, lower quality) and set `degraded['graph_search']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - role and responsibility assignment with clear interfaces | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - work partitioning, dependency management and result integration | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - conflict detection between concurrent agents' actions | 520 | Third required mechanism. |
| 6 | Core implementation D - measured speedup and quality versus single-agent execution | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0620_multi_agent_orchestration.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.multi.multi_agent_orchestration@1`.
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

### P0621 · `agent_communication` — Inter-Agent Communication Protocol

| field | value |
|---|---|
| part id | `P0621` (21/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0621_agent_communication.py` |
| module path | `hyperion.t13.agents.agent_communication` |
| capability published | `cap.t13.agent.agent_communication@1` |
| determinism class | `io` |
| p99 latency budget | 13000 ns (13 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0621_agent_communication.txt`](prompts/P0621_agent_communication.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0621-agent-communication) |

**Mission.** How 1000 agents share findings without drowning each other.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **structured message protocol with typed intents**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **BrowseComp** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **shared-blackboard versus point-to-point policy** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **information-relevance filtering to control communication volume** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **Online-Mind2Web**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured coordination overhead and its reduction** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t13.agent.agent_communication@1`
- `cap.t13.agent.agent_communication.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.multi.multi_agent_orchestration@1` | use the in-file conservative substitute for `multi_agent_orchestration` (documented, slower, lower quality) and set `degraded['multi_agent_orchestration']='local'` |
| `cap.t01.clock.clock_time@1` | use the in-file conservative substitute for `clock_time` (documented, slower, lower quality) and set `degraded['clock_time']='local'` |
| `cap.t07.memory.memory_consolidation@1` | use the in-file conservative substitute for `memory_consolidation` (documented, slower, lower quality) and set `degraded['memory_consolidation']='local'` |
| `cap.t10.decomposition.decomposition@1` | use the in-file conservative substitute for `decomposition` (documented, slower, lower quality) and set `degraded['decomposition']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - structured message protocol with typed intents | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - shared-blackboard versus point-to-point policy | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - information-relevance filtering to control communication volume | 520 | Third required mechanism. |
| 6 | Core implementation D - measured coordination overhead and its reduction | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0621_agent_communication.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.agent.agent_communication@1`.
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

### P0622 · `agent_delegation` — Task Delegation & Subagent Spawning

| field | value |
|---|---|
| part id | `P0622` (22/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0622_agent_delegation.py` |
| module path | `hyperion.t13.agents.agent_delegation` |
| capability published | `cap.t13.agent.agent_delegation@1` |
| determinism class | `io` |
| p99 latency budget | 14000 ns (14 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0622_agent_delegation.txt`](prompts/P0622_agent_delegation.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0622-agent-delegation) |

**Mission.** Knows when to do it itself and when to delegate.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **delegation decision policy from task decomposability and cost** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **subagent briefing quality (context sufficiency without bloat)** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **Online-Mind2Web**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **result verification before accepting subagent output** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured quality/cost improvement from delegation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **BrowseComp** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t13.agent.agent_delegation@1`
- `cap.t13.agent.agent_delegation.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.agent.agent_communication@1` | use the in-file conservative substitute for `agent_communication` (documented, slower, lower quality) and set `degraded['agent_communication']='local'` |
| `cap.t01.bigint.bigint_modmath@1` | use the in-file conservative substitute for `bigint_modmath` (documented, slower, lower quality) and set `degraded['bigint_modmath']='local'` |
| `cap.t07.embedding.embedding_model@1` | use the in-file conservative substitute for `embedding_model` (documented, slower, lower quality) and set `degraded['embedding_model']='local'` |
| `cap.t10.program.program_synthesis_reasoning@1` | use the in-file conservative substitute for `program_synthesis_reasoning` (documented, slower, lower quality) and set `degraded['program_synthesis_reasoning']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - delegation decision policy from task decomposability and cost | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - subagent briefing quality (context sufficiency without bloat) | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - result verification before accepting subagent output | 520 | Third required mechanism. |
| 6 | Core implementation D - measured quality/cost improvement from delegation | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0622_agent_delegation.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.agent.agent_delegation@1`.
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

### P0623 · `agent_supervision` — Agent Supervision & Intervention

| field | value |
|---|---|
| part id | `P0623` (23/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0623_agent_supervision.py` |
| module path | `hyperion.t13.agents.agent_supervision` |
| capability published | `cap.t13.agent.agent_supervision@1` |
| determinism class | `io` |
| p99 latency budget | 15000 ns (15 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0623_agent_supervision.txt`](prompts/P0623_agent_supervision.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0623-agent-supervision) |

**Mission.** Watches its own workers and steps in when needed.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **progress monitoring with stall and drift detection** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **Online-Mind2Web**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **intervention policy: correct, restart, reassign or escalate** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **supervision-overhead measurement**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **BrowseComp** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured improvement in long-horizon success rate** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t13.agent.agent_supervision@1`
- `cap.t13.agent.agent_supervision.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.agent.agent_delegation@1` | use the in-file conservative substitute for `agent_delegation` (documented, slower, lower quality) and set `degraded['agent_delegation']='local'` |
| `cap.t01.logging.logging_events@1` | use the in-file conservative substitute for `logging_events` (documented, slower, lower quality) and set `degraded['logging_events']='local'` |
| `cap.t07.world.world_state_store@1` | use the in-file conservative substitute for `world_state_store` (documented, slower, lower quality) and set `degraded['world_state_store']='local'` |
| `cap.t10.meta.meta_reasoning@1` | use the in-file conservative substitute for `meta_reasoning` (documented, slower, lower quality) and set `degraded['meta_reasoning']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - progress monitoring with stall and drift detection | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - intervention policy: correct, restart, reassign or escalate | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - supervision-overhead measurement | 520 | Third required mechanism. |
| 6 | Core implementation D - measured improvement in long-horizon success rate | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0623_agent_supervision.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.agent.agent_supervision@1`.
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

### P0624 · `consensus_agents` — Multi-Agent Consensus & Conflict Resolution

| field | value |
|---|---|
| part id | `P0624` (24/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0624_consensus_agents.py` |
| module path | `hyperion.t13.agents.consensus_agents` |
| capability published | `cap.t13.consensus.consensus_agents@1` |
| determinism class | `io` |
| p99 latency budget | 16000 ns (16 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0624_consensus_agents.txt`](prompts/P0624_consensus_agents.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0624-consensus-agents) |

**Mission.** Resolves disagreement between agents with evidence.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **disagreement detection and structured resolution protocols** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **evidence-weighted arbitration with tie-breaking rules**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **BrowseComp** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **deadlock prevention in negotiation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured decision quality versus single-agent decisions** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **Online-Mind2Web** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t13.consensus.consensus_agents@1`
- `cap.t13.consensus.consensus_agents.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.agent.agent_supervision@1` | use the in-file conservative substitute for `agent_supervision` (documented, slower, lower quality) and set `degraded['agent_supervision']='local'` |
| `cap.t01.checksum.checksum_verify@1` | use the in-file conservative substitute for `checksum_verify` (documented, slower, lower quality) and set `degraded['checksum_verify']='local'` |
| `cap.t07.subgraph.subgraph_memoize@1` | use the in-file conservative substitute for `subgraph_memoize` (documented, slower, lower quality) and set `degraded['subgraph_memoize']='local'` |
| `cap.t10.hypothesis.hypothesis_management@1` | use the in-file conservative substitute for `hypothesis_management` (documented, slower, lower quality) and set `degraded['hypothesis_management']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - disagreement detection and structured resolution protocols | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - evidence-weighted arbitration with tie-breaking rules | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - deadlock prevention in negotiation | 520 | Third required mechanism. |
| 6 | Core implementation D - measured decision quality versus single-agent decisions | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0624_consensus_agents.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.consensus.consensus_agents@1`.
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

### P0625 · `environment_model` — Environment State Modelling & Prediction

| field | value |
|---|---|
| part id | `P0625` (25/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0625_environment_model.py` |
| module path | `hyperion.t13.agents.environment_model` |
| capability published | `cap.t13.environment.environment_model@1` |
| determinism class | `io` |
| p99 latency budget | 17000 ns (17 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0625_environment_model.txt`](prompts/P0625_environment_model.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0625-environment-model) |

**Mission.** Predicts what an action will do before doing it.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **action-effect prediction with uncertainty estimates**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **BrowseComp** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **state-divergence detection between predicted and observed** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **model updating from observed outcomes** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **Online-Mind2Web** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **prediction accuracy measurement across environments** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t13.environment.environment_model@1`
- `cap.t13.environment.environment_model.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.consensus.consensus_agents@1` | use the in-file conservative substitute for `consensus_agents` (documented, slower, lower quality) and set `degraded['consensus_agents']='local'` |
| `cap.t01.numeric.numeric_limits@1` | use the in-file conservative substitute for `numeric_limits` (documented, slower, lower quality) and set `degraded['numeric_limits']='local'` |
| `cap.t07.multimodal.multimodal_memory@1` | use the in-file conservative substitute for `multimodal_memory` (documented, slower, lower quality) and set `degraded['multimodal_memory']='local'` |
| `cap.t10.proof.proof_sketch@1` | use the in-file conservative substitute for `proof_sketch` (documented, slower, lower quality) and set `degraded['proof_sketch']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - action-effect prediction with uncertainty estimates | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - state-divergence detection between predicted and observed | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - model updating from observed outcomes | 520 | Third required mechanism. |
| 6 | Core implementation D - prediction accuracy measurement across environments | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0625_environment_model.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.environment.environment_model@1`.
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

### P0626 · `action_verification` — Post-Action Verification Loop

| field | value |
|---|---|
| part id | `P0626` (26/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0626_action_verification.py` |
| module path | `hyperion.t13.agents.action_verification` |
| capability published | `cap.t13.action.action_verification@1` |
| determinism class | `io` |
| p99 latency budget | 18000 ns (18 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0626_action_verification.txt`](prompts/P0626_action_verification.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0626-action-verification) |

**Mission.** Confirms every action achieved its intended effect.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **expected-effect specification per action and observation matching** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **silent-failure detection (action reported success but did nothing)** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **Online-Mind2Web** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **retry versus replan decision on verification failure** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured reduction in undetected failures**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **BrowseComp**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t13.action.action_verification@1`
- `cap.t13.action.action_verification.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.environment.environment_model@1` | use the in-file conservative substitute for `environment_model` (documented, slower, lower quality) and set `degraded['environment_model']='local'` |
| `cap.t01.sandbox.sandbox_policy@1` | use the in-file conservative substitute for `sandbox_policy` (documented, slower, lower quality) and set `degraded['sandbox_policy']='local'` |
| `cap.t07.context.context_budget_optimiser@1` | use the in-file conservative substitute for `context_budget_optimiser` (documented, slower, lower quality) and set `degraded['context_budget_optimiser']='local'` |
| `cap.t10.adversarial.adversarial_reasoning@1` | use the in-file conservative substitute for `adversarial_reasoning` (documented, slower, lower quality) and set `degraded['adversarial_reasoning']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - expected-effect specification per action and observation matchin | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - silent-failure detection (action reported success but did nothin | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - retry versus replan decision on verification failure | 520 | Third required mechanism. |
| 6 | Core implementation D - measured reduction in undetected failures | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0626_action_verification.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.action.action_verification@1`.
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

### P0627 · `error_recovery_agent` — Failure Recovery & Adaptation

| field | value |
|---|---|
| part id | `P0627` (27/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0627_error_recovery_agent.py` |
| module path | `hyperion.t13.agents.error_recovery_agent` |
| capability published | `cap.t13.error.error_recovery_agent@1` |
| determinism class | `io` |
| p99 latency budget | 19000 ns (19 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0627_error_recovery_agent.txt`](prompts/P0627_error_recovery_agent.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0627-error-recovery-agent) |

**Mission.** Recovers from unexpected states without human help.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **failure classification and recovery-strategy selection** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **Online-Mind2Web** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **state restoration and safe-point rollback** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **learned recovery patterns from past failures**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **BrowseComp**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **recovery success rate measurement on injected-failure scenarios** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t13.error.error_recovery_agent@1`
- `cap.t13.error.error_recovery_agent.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.action.action_verification@1` | use the in-file conservative substitute for `action_verification` (documented, slower, lower quality) and set `degraded['action_verification']='local'` |
| `cap.t01.abi.abi_result@1` | use the in-file conservative substitute for `abi_result` (documented, slower, lower quality) and set `degraded['abi_result']='local'` |
| `cap.t07.kv.kv_eviction@1` | use the in-file conservative substitute for `kv_eviction` (documented, slower, lower quality) and set `degraded['kv_eviction']='local'` |
| `cap.t10.tree.tree_search@1` | use the in-file conservative substitute for `tree_search` (documented, slower, lower quality) and set `degraded['tree_search']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - failure classification and recovery-strategy selection | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - state restoration and safe-point rollback | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - learned recovery patterns from past failures | 520 | Third required mechanism. |
| 6 | Core implementation D - recovery success rate measurement on injected-failure scenarios | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0627_error_recovery_agent.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.error.error_recovery_agent@1`.
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

### P0628 · `long_horizon_memory` — Long-Horizon Task Memory

| field | value |
|---|---|
| part id | `P0628` (28/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0628_long_horizon_memory.py` |
| module path | `hyperion.t13.agents.long_horizon_memory` |
| capability published | `cap.t13.long.long_horizon_memory@1` |
| determinism class | `io` |
| p99 latency budget | 20000 ns (20 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0628_long_horizon_memory.txt`](prompts/P0628_long_horizon_memory.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0628-long-horizon-memory) |

**Mission.** Remembers everything relevant across a twelve-hour task.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **task-scoped memory with progress, decisions and dead ends recorded** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **context compaction preserving decision-critical information**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **BrowseComp**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **resumption after interruption with full context restoration** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured coherence over very long task horizons** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Online-Mind2Web** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t13.long.long_horizon_memory@1`
- `cap.t13.long.long_horizon_memory.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.error.error_recovery_agent@1` | use the in-file conservative substitute for `error_recovery_agent` (documented, slower, lower quality) and set `degraded['error_recovery_agent']='local'` |
| `cap.t01.trace.trace_context@1` | use the in-file conservative substitute for `trace_context` (documented, slower, lower quality) and set `degraded['trace_context']='local'` |
| `cap.t07.procedural.procedural_memory@1` | use the in-file conservative substitute for `procedural_memory` (documented, slower, lower quality) and set `degraded['procedural_memory']='local'` |
| `cap.t10.debate.debate_ensemble@1` | use the in-file conservative substitute for `debate_ensemble` (documented, slower, lower quality) and set `degraded['debate_ensemble']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - task-scoped memory with progress, decisions and dead ends record | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - context compaction preserving decision-critical information | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - resumption after interruption with full context restoration | 520 | Third required mechanism. |
| 6 | Core implementation D - measured coherence over very long task horizons | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0628_long_horizon_memory.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.long.long_horizon_memory@1`.
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

### P0629 · `progress_tracking` — Progress Estimation & Reporting

| field | value |
|---|---|
| part id | `P0629` (29/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0629_progress_tracking.py` |
| module path | `hyperion.t13.agents.progress_tracking` |
| capability published | `cap.t13.progress.progress_tracking@1` |
| determinism class | `io` |
| p99 latency budget | 21000 ns (21 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0629_progress_tracking.txt`](prompts/P0629_progress_tracking.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0629-progress-tracking) |

**Mission.** Honest answers to 'how much longer'.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **completion estimation from subtask structure and observed velocity**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **BrowseComp**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **milestone reporting with confidence intervals** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **blocked-state detection and escalation** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Online-Mind2Web** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **estimation-accuracy measurement against actual completion** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t13.progress.progress_tracking@1`
- `cap.t13.progress.progress_tracking.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.long.long_horizon_memory@1` | use the in-file conservative substitute for `long_horizon_memory` (documented, slower, lower quality) and set `degraded['long_horizon_memory']='local'` |
| `cap.t01.fixed.fixed_point@1` | use the in-file conservative substitute for `fixed_point` (documented, slower, lower quality) and set `degraded['fixed_point']='local'` |
| `cap.t07.chunking.chunking_strategy@1` | use the in-file conservative substitute for `chunking_strategy` (documented, slower, lower quality) and set `degraded['chunking_strategy']='local'` |
| `cap.t10.induction.induction_engine@1` | use the in-file conservative substitute for `induction_engine` (documented, slower, lower quality) and set `degraded['induction_engine']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - completion estimation from subtask structure and observed veloci | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - milestone reporting with confidence intervals | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - blocked-state detection and escalation | 520 | Third required mechanism. |
| 6 | Core implementation D - estimation-accuracy measurement against actual completion | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0629_progress_tracking.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.progress.progress_tracking@1`.
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

### P0630 · `human_in_loop` — Human Handoff & Approval Workflow

| field | value |
|---|---|
| part id | `P0630` (30/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0630_human_in_loop.py` |
| module path | `hyperion.t13.agents.human_in_loop` |
| capability published | `cap.t13.human.human_in_loop@1` |
| determinism class | `io` |
| p99 latency budget | 22000 ns (22 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0630_human_in_loop.txt`](prompts/P0630_human_in_loop.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0630-human-in-loop) |

**Mission.** Asks for permission at exactly the right moments.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **approval-requirement classification by reversibility and stakes** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **context-sufficient approval requests (human can decide in seconds)** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Online-Mind2Web** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **asynchronous approval handling without blocking other work** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured approval-quality and interruption-rate balance**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **BrowseComp** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t13.human.human_in_loop@1`
- `cap.t13.human.human_in_loop.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.progress.progress_tracking@1` | use the in-file conservative substitute for `progress_tracking` (documented, slower, lower quality) and set `degraded['progress_tracking']='local'` |
| `cap.t01.config.config_system@1` | use the in-file conservative substitute for `config_system` (documented, slower, lower quality) and set `degraded['config_system']='local'` |
| `cap.t07.memory.memory_encryption@1` | use the in-file conservative substitute for `memory_encryption` (documented, slower, lower quality) and set `degraded['memory_encryption']='local'` |
| `cap.t10.commonsense.commonsense_engine@1` | use the in-file conservative substitute for `commonsense_engine` (documented, slower, lower quality) and set `degraded['commonsense_engine']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - approval-requirement classification by reversibility and stakes | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - context-sufficient approval requests (human can decide in second | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - asynchronous approval handling without blocking other work | 520 | Third required mechanism. |
| 6 | Core implementation D - measured approval-quality and interruption-rate balance | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0630_human_in_loop.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.human.human_in_loop@1`.
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

### P0631 · `agent_safety_gate` — Agent Action Safety Gate

| field | value |
|---|---|
| part id | `P0631` (31/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0631_agent_safety_gate.py` |
| module path | `hyperion.t13.agents.agent_safety_gate` |
| capability published | `cap.t13.agent.agent_safety_gate@1` |
| determinism class | `io` |
| p99 latency budget | 23000 ns (23 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0631_agent_safety_gate.txt`](prompts/P0631_agent_safety_gate.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0631-agent-safety-gate) |

**Mission.** The hard stop before anything irreversible happens.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **action classification: reversible, costly, irreversible, prohibited** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Online-Mind2Web** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **mandatory T19 gate consultation with fail-closed behaviour** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **blast-radius estimation before execution**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **BrowseComp** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **verification that no prohibited action can bypass the gate** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t13.agent.agent_safety_gate@1`
- `cap.t13.agent.agent_safety_gate.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.human.human_in_loop@1` | use the in-file conservative substitute for `human_in_loop` (documented, slower, lower quality) and set `degraded['human_in_loop']='local'` |
| `cap.t01.determinism.determinism_replay@1` | use the in-file conservative substitute for `determinism_replay` (documented, slower, lower quality) and set `degraded['determinism_replay']='local'` |
| `cap.t07.tool.tool_result_cache@1` | use the in-file conservative substitute for `tool_result_cache` (documented, slower, lower quality) and set `degraded['tool_result_cache']='local'` |
| `cap.t10.parallel.parallel_reasoning@1` | use the in-file conservative substitute for `parallel_reasoning` (documented, slower, lower quality) and set `degraded['parallel_reasoning']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - action classification: reversible, costly, irreversible, prohibi | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - mandatory T19 gate consultation with fail-closed behaviour | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - blast-radius estimation before execution | 520 | Third required mechanism. |
| 6 | Core implementation D - verification that no prohibited action can bypass the gate | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0631_agent_safety_gate.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.agent.agent_safety_gate@1`.
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

### P0632 · `credential_management` — Credential & Permission Management

| field | value |
|---|---|
| part id | `P0632` (32/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0632_credential_management.py` |
| module path | `hyperion.t13.agents.credential_management` |
| capability published | `cap.t13.credential.credential_management@1` |
| determinism class | `io` |
| p99 latency budget | 24000 ns (24 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0632_credential_management.txt`](prompts/P0632_credential_management.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0632-credential-management) |

**Mission.** Uses secrets correctly and never leaks them.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **scoped credential acquisition with least-privilege defaults** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **secret redaction from all logs, traces and model context**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **BrowseComp** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **credential-lifetime management and rotation handling** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **leak-detection testing across all output channels** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **Online-Mind2Web**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t13.credential.credential_management@1`
- `cap.t13.credential.credential_management.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.agent.agent_safety_gate@1` | use the in-file conservative substitute for `agent_safety_gate` (documented, slower, lower quality) and set `degraded['agent_safety_gate']='local'` |
| `cap.t01.compat.compat_shims@1` | use the in-file conservative substitute for `compat_shims` (documented, slower, lower quality) and set `degraded['compat_shims']='local'` |
| `cap.t07.temporal.temporal_memory@1` | use the in-file conservative substitute for `temporal_memory` (documented, slower, lower quality) and set `degraded['temporal_memory']='local'` |
| `cap.t10.multi.multi_step_arithmetic@1` | use the in-file conservative substitute for `multi_step_arithmetic` (documented, slower, lower quality) and set `degraded['multi_step_arithmetic']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - scoped credential acquisition with least-privilege defaults | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - secret redaction from all logs, traces and model context | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - credential-lifetime management and rotation handling | 520 | Third required mechanism. |
| 6 | Core implementation D - leak-detection testing across all output channels | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0632_credential_management.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.credential.credential_management@1`.
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

### P0633 · `cost_control_agent` — Agent Cost Governance

| field | value |
|---|---|
| part id | `P0633` (33/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0633_cost_control_agent.py` |
| module path | `hyperion.t13.agents.cost_control_agent` |
| capability published | `cap.t13.cost.cost_control_agent@1` |
| determinism class | `io` |
| p99 latency budget | 25000 ns (25 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0633_cost_control_agent.txt`](prompts/P0633_cost_control_agent.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0633-cost-control-agent) |

**Mission.** An autonomous agent must not spend without limit.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **hierarchical budget enforcement across agent trees**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **BrowseComp** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **cost-per-subtask accounting and forecasting** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **budget-exhaustion behaviour with partial-result delivery** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **Online-Mind2Web**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured budget-adherence rate** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t13.cost.cost_control_agent@1`
- `cap.t13.cost.cost_control_agent.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.credential.credential_management@1` | use the in-file conservative substitute for `credential_management` (documented, slower, lower quality) and set `degraded['credential_management']='local'` |
| `cap.t01.secure.secure_zeroize@1` | use the in-file conservative substitute for `secure_zeroize` (documented, slower, lower quality) and set `degraded['secure_zeroize']='local'` |
| `cap.t07.memory.memory_bench@1` | use the in-file conservative substitute for `memory_bench` (documented, slower, lower quality) and set `degraded['memory_bench']='local'` |
| `cap.t10.error.error_taxonomy@1` | use the in-file conservative substitute for `error_taxonomy` (documented, slower, lower quality) and set `degraded['error_taxonomy']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - hierarchical budget enforcement across agent trees | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - cost-per-subtask accounting and forecasting | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - budget-exhaustion behaviour with partial-result delivery | 520 | Third required mechanism. |
| 6 | Core implementation D - measured budget-adherence rate | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0633_cost_control_agent.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.cost.cost_control_agent@1`.
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

### P0634 · `sandbox_execution` — Agent Sandbox & Isolation Runtime

| field | value |
|---|---|
| part id | `P0634` (34/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0634_sandbox_execution.py` |
| module path | `hyperion.t13.agents.sandbox_execution` |
| capability published | `cap.t13.sandbox.sandbox_execution@1` |
| determinism class | `io` |
| p99 latency budget | 26000 ns (26 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0634_sandbox_execution.txt`](prompts/P0634_sandbox_execution.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0634-sandbox-execution) |

**Mission.** Powerful autonomy inside a strong box.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **container/VM isolation profiles per task risk level** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **network egress policy with allowlists and audit** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **Online-Mind2Web**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **resource limits with graceful enforcement** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **escape-attempt testing and verification of containment**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **BrowseComp** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t13.sandbox.sandbox_execution@1`
- `cap.t13.sandbox.sandbox_execution.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.cost.cost_control_agent@1` | use the in-file conservative substitute for `cost_control_agent` (documented, slower, lower quality) and set `degraded['cost_control_agent']='local'` |
| `cap.t07.kv.kv_paging@1` | use the in-file conservative substitute for `kv_paging` (documented, slower, lower quality) and set `degraded['kv_paging']='local'` |
| `cap.t10.search.search_controller@1` | use the in-file conservative substitute for `search_controller` (documented, slower, lower quality) and set `degraded['search_controller']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - container/VM isolation profiles per task risk level | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - network egress policy with allowlists and audit | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - resource limits with graceful enforcement | 520 | Third required mechanism. |
| 6 | Core implementation D - escape-attempt testing and verification of containment | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0634_sandbox_execution.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.sandbox.sandbox_execution@1`.
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

### P0635 · `tool_creation` — Dynamic Tool Creation

| field | value |
|---|---|
| part id | `P0635` (35/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0635_tool_creation.py` |
| module path | `hyperion.t13.agents.tool_creation` |
| capability published | `cap.t13.tool.tool_creation@1` |
| determinism class | `io` |
| p99 latency budget | 27000 ns (27 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0635_tool_creation.txt`](prompts/P0635_tool_creation.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0635-tool-creation) |

**Mission.** Builds the tool it needs when none exists.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **tool synthesis from a described capability gap** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **Online-Mind2Web**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **generated-tool validation, sandboxing and registration** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **tool-library curation and reuse across tasks**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **BrowseComp** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured task-success improvement from created tools** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t13.tool.tool_creation@1`
- `cap.t13.tool.tool_creation.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.sandbox.sandbox_execution@1` | use the in-file conservative substitute for `sandbox_execution` (documented, slower, lower quality) and set `degraded['sandbox_execution']='local'` |
| `cap.t01.envelope.envelope_codec@1` | use the in-file conservative substitute for `envelope_codec` (documented, slower, lower quality) and set `degraded['envelope_codec']='local'` |
| `cap.t07.semantic.semantic_memory@1` | use the in-file conservative substitute for `semantic_memory` (documented, slower, lower quality) and set `degraded['semantic_memory']='local'` |
| `cap.t10.self.self_critique@1` | use the in-file conservative substitute for `self_critique` (documented, slower, lower quality) and set `degraded['self_critique']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - tool synthesis from a described capability gap | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - generated-tool validation, sandboxing and registration | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - tool-library curation and reuse across tasks | 520 | Third required mechanism. |
| 6 | Core implementation D - measured task-success improvement from created tools | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0635_tool_creation.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.tool.tool_creation@1`.
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

### P0636 · `workflow_learning` — Workflow Learning & Skill Acquisition

| field | value |
|---|---|
| part id | `P0636` (36/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0636_workflow_learning.py` |
| module path | `hyperion.t13.agents.workflow_learning` |
| capability published | `cap.t13.workflow.workflow_learning@1` |
| determinism class | `io` |
| p99 latency budget | 28000 ns (28 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0636_workflow_learning.txt`](prompts/P0636_workflow_learning.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0636-workflow-learning) |

**Mission.** Gets faster at repeated work.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **successful-trajectory generalisation into reusable procedures** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **procedure parameterisation and applicability conditions**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **BrowseComp** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **procedure library maintenance with success-rate tracking** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured speedup on repeated task families** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **Online-Mind2Web** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t13.workflow.workflow_learning@1`
- `cap.t13.workflow.workflow_learning.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.tool.tool_creation@1` | use the in-file conservative substitute for `tool_creation` (documented, slower, lower quality) and set `degraded['tool_creation']='local'` |
| `cap.t01.dataflow.dataflow_dag@1` | use the in-file conservative substitute for `dataflow_dag` (documented, slower, lower quality) and set `degraded['dataflow_dag']='local'` |
| `cap.t07.query.query_reformulation@1` | use the in-file conservative substitute for `query_reformulation` (documented, slower, lower quality) and set `degraded['query_reformulation']='local'` |
| `cap.t10.abstraction.abstraction_engine@1` | use the in-file conservative substitute for `abstraction_engine` (documented, slower, lower quality) and set `degraded['abstraction_engine']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - successful-trajectory generalisation into reusable procedures | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - procedure parameterisation and applicability conditions | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - procedure library maintenance with success-rate tracking | 520 | Third required mechanism. |
| 6 | Core implementation D - measured speedup on repeated task families | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0636_workflow_learning.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.workflow.workflow_learning@1`.
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

### P0637 · `observation_compression` — Observation Compression & Attention

| field | value |
|---|---|
| part id | `P0637` (37/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0637_observation_compression.py` |
| module path | `hyperion.t13.agents.observation_compression` |
| capability published | `cap.t13.observation.observation_compression@1` |
| determinism class | `io` |
| p99 latency budget | 29000 ns (29 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0637_observation_compression.txt`](prompts/P0637_observation_compression.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0637-observation-compression) |

**Mission.** Handles megabyte tool outputs without drowning.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **relevance-based observation filtering and summarisation**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **BrowseComp** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **structured extraction from logs, HTML and large outputs** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **information-loss measurement against downstream success** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **Online-Mind2Web** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured token reduction at matched task success** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t13.observation.observation_compression@1`
- `cap.t13.observation.observation_compression.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.workflow.workflow_learning@1` | use the in-file conservative substitute for `workflow_learning` (documented, slower, lower quality) and set `degraded['workflow_learning']='local'` |
| `cap.t01.serialization.serialization_schema@1` | use the in-file conservative substitute for `serialization_schema` (documented, slower, lower quality) and set `degraded['serialization_schema']='local'` |
| `cap.t07.memory.memory_privacy@1` | use the in-file conservative substitute for `memory_privacy` (documented, slower, lower quality) and set `degraded['memory_privacy']='local'` |
| `cap.t10.spatial.spatial_reasoning@1` | use the in-file conservative substitute for `spatial_reasoning` (documented, slower, lower quality) and set `degraded['spatial_reasoning']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - relevance-based observation filtering and summarisation | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - structured extraction from logs, HTML and large outputs | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - information-loss measurement against downstream success | 520 | Third required mechanism. |
| 6 | Core implementation D - measured token reduction at matched task success | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0637_observation_compression.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.observation.observation_compression@1`.
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

### P0638 · `agent_determinism` — Reproducible Agent Execution

| field | value |
|---|---|
| part id | `P0638` (38/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0638_agent_determinism.py` |
| module path | `hyperion.t13.agents.agent_determinism` |
| capability published | `cap.t13.agent.agent_determinism@1` |
| determinism class | `io` |
| p99 latency budget | 30000 ns (30 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0638_agent_determinism.txt`](prompts/P0638_agent_determinism.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0638-agent-determinism) |

**Mission.** The same task run twice does the same thing.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **environment and tool-result recording for exact replay** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **deterministic decision mode with seeded sampling** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **Online-Mind2Web** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **divergence detection during replay** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **replay-fidelity measurement on real trajectories**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **BrowseComp**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t13.agent.agent_determinism@1`
- `cap.t13.agent.agent_determinism.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.observation.observation_compression@1` | use the in-file conservative substitute for `observation_compression` (documented, slower, lower quality) and set `degraded['observation_compression']='local'` |
| `cap.t01.bench.bench_harness@1` | use the in-file conservative substitute for `bench_harness` (documented, slower, lower quality) and set `degraded['bench_harness']='local'` |
| `cap.t07.semantic.semantic_cache@1` | use the in-file conservative substitute for `semantic_cache` (documented, slower, lower quality) and set `degraded['semantic_cache']='local'` |
| `cap.t10.chain.chain_compression@1` | use the in-file conservative substitute for `chain_compression` (documented, slower, lower quality) and set `degraded['chain_compression']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - environment and tool-result recording for exact replay | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - deterministic decision mode with seeded sampling | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - divergence detection during replay | 520 | Third required mechanism. |
| 6 | Core implementation D - replay-fidelity measurement on real trajectories | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0638_agent_determinism.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.agent.agent_determinism@1`.
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

### P0639 · `agent_eval_harness` — Agent Benchmark Harness

| field | value |
|---|---|
| part id | `P0639` (39/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0639_agent_eval_harness.py` |
| module path | `hyperion.t13.agents.agent_eval_harness` |
| capability published | `cap.t13.agent.agent_eval_harness@1` |
| determinism class | `io` |
| p99 latency budget | 31000 ns (31 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0639_agent_eval_harness.txt`](prompts/P0639_agent_eval_harness.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0639-agent-eval-harness) |

**Mission.** Measures agent capability across all major public benchmarks.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **OSWorld 2.0, Online-Mind2Web, AutomationBench and BrowseComp harnesses** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **Online-Mind2Web** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **environment-fidelity verification and version pinning** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **per-task diagnostics with failure taxonomy**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **BrowseComp**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **targets versus Opus 5: OSWorld 95.5 vs 70.5, AutomationBench 92 vs 26** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t13.agent.agent_eval_harness@1`
- `cap.t13.agent.agent_eval_harness.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.agent.agent_determinism@1` | use the in-file conservative substitute for `agent_determinism` (documented, slower, lower quality) and set `degraded['agent_determinism']='local'` |
| `cap.t01.abi.abi_stability@1` | use the in-file conservative substitute for `abi_stability` (documented, slower, lower quality) and set `degraded['abi_stability']='local'` |
| `cap.t07.graph.graph_memory_queries@1` | use the in-file conservative substitute for `graph_memory_queries` (documented, slower, lower quality) and set `degraded['graph_memory_queries']='local'` |
| `cap.t10.reasoning.reasoning_robustness@1` | use the in-file conservative substitute for `reasoning_robustness` (documented, slower, lower quality) and set `degraded['reasoning_robustness']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - OSWorld 2.0, Online-Mind2Web, AutomationBench and BrowseComp har | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - environment-fidelity verification and version pinning | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - per-task diagnostics with failure taxonomy | 520 | Third required mechanism. |
| 6 | Core implementation D - targets versus Opus 5: OSWorld 95.5 vs 70.5, AutomationBench 92  | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0639_agent_eval_harness.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.agent.agent_eval_harness@1`.
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

### P0640 · `trajectory_analysis` — Trajectory Analysis & Improvement Mining

| field | value |
|---|---|
| part id | `P0640` (40/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0640_trajectory_analysis.py` |
| module path | `hyperion.t13.agents.trajectory_analysis` |
| capability published | `cap.t13.trajectory.trajectory_analysis@1` |
| determinism class | `io` |
| p99 latency budget | 32000 ns (32 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0640_trajectory_analysis.txt`](prompts/P0640_trajectory_analysis.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0640-trajectory-analysis) |

**Mission.** Learns from thousands of past runs what to do differently.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **trajectory database with outcome and cost labelling** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **failure-pattern mining and clustering**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **BrowseComp**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **improvement-hypothesis generation and validation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **measured success-rate improvement from mined lessons** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Online-Mind2Web** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t13.trajectory.trajectory_analysis@1`
- `cap.t13.trajectory.trajectory_analysis.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.agent.agent_eval_harness@1` | use the in-file conservative substitute for `agent_eval_harness` (documented, slower, lower quality) and set `degraded['agent_eval_harness']='local'` |
| `cap.t01.retry.retry_idempotency@1` | use the in-file conservative substitute for `retry_idempotency` (documented, slower, lower quality) and set `degraded['retry_idempotency']='local'` |
| `cap.t07.provenance.provenance_tracking@1` | use the in-file conservative substitute for `provenance_tracking` (documented, slower, lower quality) and set `degraded['provenance_tracking']='local'` |
| `cap.t10.reasoning.reasoning_transfer@1` | use the in-file conservative substitute for `reasoning_transfer` (documented, slower, lower quality) and set `degraded['reasoning_transfer']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - trajectory database with outcome and cost labelling | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - failure-pattern mining and clustering | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - improvement-hypothesis generation and validation | 520 | Third required mechanism. |
| 6 | Core implementation D - measured success-rate improvement from mined lessons | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0640_trajectory_analysis.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.trajectory.trajectory_analysis@1`.
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

### P0641 · `agent_interruption` — Interruption, Steering & Course Correction

| field | value |
|---|---|
| part id | `P0641` (41/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0641_agent_interruption.py` |
| module path | `hyperion.t13.agents.agent_interruption` |
| capability published | `cap.t13.agent.agent_interruption@1` |
| determinism class | `io` |
| p99 latency budget | 33000 ns (33 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0641_agent_interruption.txt`](prompts/P0641_agent_interruption.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0641-agent-interruption) |

**Mission.** The user can change direction mid-task without a restart.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **mid-execution instruction incorporation with plan repair**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **BrowseComp**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **priority reconciliation between old and new instructions** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **state consistency after steering** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Online-Mind2Web** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured steering-success rate** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t13.agent.agent_interruption@1`
- `cap.t13.agent.agent_interruption.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.trajectory.trajectory_analysis@1` | use the in-file conservative substitute for `trajectory_analysis` (documented, slower, lower quality) and set `degraded['trajectory_analysis']='local'` |
| `cap.t07.kv.kv_hierarchy@1` | use the in-file conservative substitute for `kv_hierarchy` (documented, slower, lower quality) and set `degraded['kv_hierarchy']='local'` |
| `cap.t10.thought.thought_program_ir@1` | use the in-file conservative substitute for `thought_program_ir` (documented, slower, lower quality) and set `degraded['thought_program_ir']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - mid-execution instruction incorporation with plan repair | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - priority reconciliation between old and new instructions | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - state consistency after steering | 520 | Third required mechanism. |
| 6 | Core implementation D - measured steering-success rate | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0641_agent_interruption.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.agent.agent_interruption@1`.
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

### P0642 · `simulation_env` — Agent Training & Testing Environments

| field | value |
|---|---|
| part id | `P0642` (42/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0642_simulation_env.py` |
| module path | `hyperion.t13.agents.simulation_env` |
| capability published | `cap.t13.simulation.simulation_env@1` |
| determinism class | `io` |
| p99 latency budget | 34000 ns (34 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0642_simulation_env.txt`](prompts/P0642_simulation_env.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0642-simulation-env) |

**Mission.** Thousands of realistic environments for evaluation and training.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **environment generation with controllable difficulty and stochasticity** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Its contribution is measured against **Zapier AutomationBench** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **task-and-verifier pair generation with automatic grading** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Online-Mind2Web** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **environment-fidelity validation against real applications** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **coverage report across task categories**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **BrowseComp** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t13.simulation.simulation_env@1`
- `cap.t13.simulation.simulation_env.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.agent.agent_interruption@1` | use the in-file conservative substitute for `agent_interruption` (documented, slower, lower quality) and set `degraded['agent_interruption']='local'` |
| `cap.t01.omega.omega_bus_ipc@1` | use the in-file conservative substitute for `omega_bus_ipc` (documented, slower, lower quality) and set `degraded['omega_bus_ipc']='local'` |
| `cap.t07.episodic.episodic_memory@1` | use the in-file conservative substitute for `episodic_memory` (documented, slower, lower quality) and set `degraded['episodic_memory']='local'` |
| `cap.t10.self.self_consistency@1` | use the in-file conservative substitute for `self_consistency` (documented, slower, lower quality) and set `degraded['self_consistency']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - environment generation with controllable difficulty and stochast | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - task-and-verifier pair generation with automatic grading | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - environment-fidelity validation against real applications | 520 | Third required mechanism. |
| 6 | Core implementation D - coverage report across task categories | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0642_simulation_env.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.simulation.simulation_env@1`.
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

### P0643 · `robotics_bridge` — Physical Actuation Interface

| field | value |
|---|---|
| part id | `P0643` (43/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0643_robotics_bridge.py` |
| module path | `hyperion.t13.agents.robotics_bridge` |
| capability published | `cap.t13.robotics.robotics_bridge@1` |
| determinism class | `io` |
| p99 latency budget | 35000 ns (35 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0643_robotics_bridge.txt`](prompts/P0643_robotics_bridge.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0643-robotics-bridge) |

**Mission.** The bridge to robots, with safety as the first requirement.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **action-space abstraction over robot control interfaces** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Correctness here is what makes the tier's **Online-Mind2Web** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **safety envelope enforcement with hard limits** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **sensor-feedback integration and closed-loop correction**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **BrowseComp** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **simulation-first validation policy before physical execution** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t13.robotics.robotics_bridge@1`
- `cap.t13.robotics.robotics_bridge.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.simulation.simulation_env@1` | use the in-file conservative substitute for `simulation_env` (documented, slower, lower quality) and set `degraded['simulation_env']='local'` |
| `cap.t01.task.task_runtime@1` | use the in-file conservative substitute for `task_runtime` (documented, slower, lower quality) and set `degraded['task_runtime']='local'` |
| `cap.t07.hybrid.hybrid_retrieval@1` | use the in-file conservative substitute for `hybrid_retrieval` (documented, slower, lower quality) and set `degraded['hybrid_retrieval']='local'` |
| `cap.t10.analogy.analogy_engine@1` | use the in-file conservative substitute for `analogy_engine` (documented, slower, lower quality) and set `degraded['analogy_engine']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - action-space abstraction over robot control interfaces | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - safety envelope enforcement with hard limits | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - sensor-feedback integration and closed-loop correction | 520 | Third required mechanism. |
| 6 | Core implementation D - simulation-first validation policy before physical execution | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0643_robotics_bridge.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.robotics.robotics_bridge@1`.
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

### P0644 · `iot_control` — Device & Infrastructure Control Agent

| field | value |
|---|---|
| part id | `P0644` (44/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0644_iot_control.py` |
| module path | `hyperion.t13.agents.iot_control` |
| capability published | `cap.t13.iot.iot_control@1` |
| determinism class | `io` |
| p99 latency budget | 36000 ns (36 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0644_iot_control.txt`](prompts/P0644_iot_control.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0644-iot-control) |

**Mission.** Operates real infrastructure responsibly.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **device capability discovery and safe command construction** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. This mechanism sits on the critical path of **OSWorld 2.0**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **change-window and blast-radius policy enforcement**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **BrowseComp** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **rollback plan requirement before every change** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **measured incident rate on controlled infrastructure tasks** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **Online-Mind2Web**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t13.iot.iot_control@1`
- `cap.t13.iot.iot_control.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.robotics.robotics_bridge@1` | use the in-file conservative substitute for `robotics_bridge` (documented, slower, lower quality) and set `degraded['robotics_bridge']='local'` |
| `cap.t01.arena.arena_graph@1` | use the in-file conservative substitute for `arena_graph` (documented, slower, lower quality) and set `degraded['arena_graph']='local'` |
| `cap.t07.conflict.conflict_resolution@1` | use the in-file conservative substitute for `conflict_resolution` (documented, slower, lower quality) and set `degraded['conflict_resolution']='local'` |
| `cap.t10.temporal.temporal_reasoning@1` | use the in-file conservative substitute for `temporal_reasoning` (documented, slower, lower quality) and set `degraded['temporal_reasoning']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - device capability discovery and safe command construction | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - change-window and blast-radius policy enforcement | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - rollback plan requirement before every change | 520 | Third required mechanism. |
| 6 | Core implementation D - measured incident rate on controlled infrastructure tasks | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0644_iot_control.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.iot.iot_control@1`.
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

### P0645 · `scientific_agent` — Autonomous Research Agent

| field | value |
|---|---|
| part id | `P0645` (45/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0645_scientific_agent.py` |
| module path | `hyperion.t13.agents.scientific_agent` |
| capability published | `cap.t13.scientific.scientific_agent@1` |
| determinism class | `io` |
| p99 latency budget | 37000 ns (37 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0645_scientific_agent.txt`](prompts/P0645_scientific_agent.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0645-scientific-agent) |

**Mission.** Runs the full research loop: hypothesise, experiment, analyse, iterate.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **hypothesis generation and experiment design with power analysis**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Its contribution is measured against **BrowseComp** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **instrument/tool control and data collection orchestration** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **result analysis with correct statistics and honest reporting** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **Online-Mind2Web**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured research-task success on curated scientific problems** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t13.scientific.scientific_agent@1`
- `cap.t13.scientific.scientific_agent.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.iot.iot_control@1` | use the in-file conservative substitute for `iot_control` (documented, slower, lower quality) and set `degraded['iot_control']='local'` |
| `cap.t01.fuzz.fuzz_engine@1` | use the in-file conservative substitute for `fuzz_engine` (documented, slower, lower quality) and set `degraded['fuzz_engine']='local'` |
| `cap.t07.cache.cache_warm_predict@1` | use the in-file conservative substitute for `cache_warm_predict` (documented, slower, lower quality) and set `degraded['cache_warm_predict']='local'` |
| `cap.t10.reasoning.reasoning_memory@1` | use the in-file conservative substitute for `reasoning_memory` (documented, slower, lower quality) and set `degraded['reasoning_memory']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - hypothesis generation and experiment design with power analysis | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - instrument/tool control and data collection orchestration | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - result analysis with correct statistics and honest reporting | 520 | Third required mechanism. |
| 6 | Core implementation D - measured research-task success on curated scientific problems | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0645_scientific_agent.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.scientific.scientific_agent@1`.
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

### P0646 · `data_analysis_agent` — Autonomous Data Analysis Agent

| field | value |
|---|---|
| part id | `P0646` (46/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0646_data_analysis_agent.py` |
| module path | `hyperion.t13.agents.data_analysis_agent` |
| capability published | `cap.t13.data.data_analysis_agent@1` |
| determinism class | `io` |
| p99 latency budget | 38000 ns (38 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0646_data_analysis_agent.txt`](prompts/P0646_data_analysis_agent.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0646-data-analysis-agent) |

**Mission.** Behaves like a careful scientist, not a plot generator.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **appropriate statistical test selection with assumption checking** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. Correctness here is what makes the tier's **Zapier AutomationBench** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **confounder identification and independent cross-checking of results** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **Online-Mind2Web**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **analysis-narrative generation with limitations stated** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **accuracy measurement on analysis tasks with known ground truth**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **BrowseComp** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t13.data.data_analysis_agent@1`
- `cap.t13.data.data_analysis_agent.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.scientific.scientific_agent@1` | use the in-file conservative substitute for `scientific_agent` (documented, slower, lower quality) and set `degraded['scientific_agent']='local'` |
| `cap.t01.manifest.manifest_parser@1` | use the in-file conservative substitute for `manifest_parser` (documented, slower, lower quality) and set `degraded['manifest_parser']='local'` |
| `cap.t07.memory.memory_replication@1` | use the in-file conservative substitute for `memory_replication` (documented, slower, lower quality) and set `degraded['memory_replication']='local'` |
| `cap.t10.reasoning.reasoning_faithfulness@1` | use the in-file conservative substitute for `reasoning_faithfulness` (documented, slower, lower quality) and set `degraded['reasoning_faithfulness']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - appropriate statistical test selection with assumption checking | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - confounder identification and independent cross-checking of resu | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - analysis-narrative generation with limitations stated | 520 | Third required mechanism. |
| 6 | Core implementation D - accuracy measurement on analysis tasks with known ground truth | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0646_data_analysis_agent.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.data.data_analysis_agent@1`.
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

### P0647 · `agent_ux` — Agent Transparency & Explainability

| field | value |
|---|---|
| part id | `P0647` (47/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0647_agent_ux.py` |
| module path | `hyperion.t13.agents.agent_ux` |
| capability published | `cap.t13.agent.agent_ux@1` |
| determinism class | `io` |
| p99 latency budget | 39000 ns (39 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0647_agent_ux.txt`](prompts/P0647_agent_ux.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0647-agent-ux) |

**Mission.** The user always knows what it is doing and why.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **real-time action narration with rationale** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. This mechanism sits on the critical path of **Online-Mind2Web**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **decision-log artifact for post-hoc review** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **uncertainty and assumption surfacing during execution**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **BrowseComp** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **user-trust and comprehension evaluation** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t13.agent.agent_ux@1`
- `cap.t13.agent.agent_ux.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.data.data_analysis_agent@1` | use the in-file conservative substitute for `data_analysis_agent` (documented, slower, lower quality) and set `degraded['data_analysis_agent']='local'` |
| `cap.t01.circuit.circuit_breaker@1` | use the in-file conservative substitute for `circuit_breaker` (documented, slower, lower quality) and set `degraded['circuit_breaker']='local'` |
| `cap.t07.dedup.dedup_engine@1` | use the in-file conservative substitute for `dedup_engine` (documented, slower, lower quality) and set `degraded['dedup_engine']='local'` |
| `cap.t10.subgoal.subgoal_caching@1` | use the in-file conservative substitute for `subgoal_caching` (documented, slower, lower quality) and set `degraded['subgoal_caching']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - real-time action narration with rationale | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - decision-log artifact for post-hoc review | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - uncertainty and assumption surfacing during execution | 520 | Third required mechanism. |
| 6 | Core implementation D - user-trust and comprehension evaluation | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0647_agent_ux.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.agent.agent_ux@1`.
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

### P0648 · `agent_speed` — Agent Latency Engineering

| field | value |
|---|---|
| part id | `P0648` (48/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0648_agent_speed.py` |
| module path | `hyperion.t13.agents.agent_speed` |
| capability published | `cap.t13.agent.agent_speed@1` |
| determinism class | `io` |
| p99 latency budget | 40000 ns (40 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0648_agent_speed.txt`](prompts/P0648_agent_speed.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0648-agent-speed) |

**Mission.** Long-horizon tasks finished in critical-path time (S6 realisation).

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **parallel subtask execution with dependency-aware scheduling** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Its contribution is measured against **OSWorld 2.0** — a regression on that benchmark is an automatic rejection of this part.
2. Implement **speculative tool execution for side-effect-free calls**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **BrowseComp** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
3. Implement **observation-processing latency reduction** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
4. Implement **measured wall-clock reduction versus serial execution** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **Online-Mind2Web** — a regression on that benchmark is an automatic rejection of this part.

**Published capabilities.**

- `cap.t13.agent.agent_speed@1`
- `cap.t13.agent.agent_speed.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.agent.agent_ux@1` | use the in-file conservative substitute for `agent_ux` (documented, slower, lower quality) and set `degraded['agent_ux']='local'` |
| `cap.t01.shutdown.shutdown_drain@1` | use the in-file conservative substitute for `shutdown_drain` (documented, slower, lower quality) and set `degraded['shutdown_drain']='local'` |
| `cap.t07.memory.memory_spec_doc@1` | use the in-file conservative substitute for `memory_spec_doc` (documented, slower, lower quality) and set `degraded['memory_spec_doc']='local'` |
| `cap.t10.reasoning.reasoning_spec_doc@1` | use the in-file conservative substitute for `reasoning_spec_doc` (documented, slower, lower quality) and set `degraded['reasoning_spec_doc']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - parallel subtask execution with dependency-aware scheduling | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - speculative tool execution for side-effect-free calls | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - observation-processing latency reduction | 520 | Third required mechanism. |
| 6 | Core implementation D - measured wall-clock reduction versus serial execution | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0648_agent_speed.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.agent.agent_speed@1`.
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

### P0649 · `agent_scaling` — 1000-Agent Scale Coordination

| field | value |
|---|---|
| part id | `P0649` (49/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0649_agent_scaling.py` |
| module path | `hyperion.t13.agents.agent_scaling` |
| capability published | `cap.t13.agent.agent_scaling@1` |
| determinism class | `io` |
| p99 latency budget | 41000 ns (41 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0649_agent_scaling.txt`](prompts/P0649_agent_scaling.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0649-agent-scaling) |

**Mission.** Proves the orchestration works at the target scale.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **hierarchical coordination topology for 1000 concurrent agents**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. Correctness here is what makes the tier's **BrowseComp** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
2. Implement **communication and coordination overhead measurement at scale** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
3. Implement **failure isolation so one agent cannot stall the swarm** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **Online-Mind2Web** — a regression on that benchmark is an automatic rejection of this part.
4. Implement **throughput and quality measurement at 1, 10, 100, 1000 agents** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.

**Published capabilities.**

- `cap.t13.agent.agent_scaling@1`
- `cap.t13.agent.agent_scaling.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.agent.agent_speed@1` | use the in-file conservative substitute for `agent_speed` (documented, slower, lower quality) and set `degraded['agent_speed']='local'` |
| `cap.t07.summarisation.summarisation_memory@1` | use the in-file conservative substitute for `summarisation_memory` (documented, slower, lower quality) and set `degraded['summarisation_memory']='local'` |
| `cap.t10.outcome.outcome_verifier@1` | use the in-file conservative substitute for `outcome_verifier` (documented, slower, lower quality) and set `degraded['outcome_verifier']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - hierarchical coordination topology for 1000 concurrent agents | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - communication and coordination overhead measurement at scale | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - failure isolation so one agent cannot stall the swarm | 520 | Third required mechanism. |
| 6 | Core implementation D - throughput and quality measurement at 1, 10, 100, 1000 agents | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0649_agent_scaling.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.agent.agent_scaling@1`.
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

### P0650 · `agent_spec_doc` — Agent Subsystem Specification & Runbook

| field | value |
|---|---|
| part id | `P0650` (50/50 of T13) |
| tier | `T13` — Agents, Tool Use & Computer Control |
| language | Python 3.13 |
| file to produce | `parts/t13_agents/P0650_agent_spec_doc.py` |
| module path | `hyperion.t13.agents.agent_spec_doc` |
| capability published | `cap.t13.agent.agent_spec_doc@1` |
| determinism class | `io` |
| p99 latency budget | 42000 ns (42 µs) |
| line budget | 5000 lines (map below, ±3 %) |
| benchmarks owned by tier | OSWorld 2.0, BrowseComp, Zapier AutomationBench, Online-Mind2Web |
| worker prompt | [`prompts/P0650_agent_spec_doc.txt`](prompts/P0650_agent_spec_doc.txt) · [inline](docs/PROMPTS_T13.md#prompt-p0650-agent-spec-doc) |

**Mission.** The authoritative description of agent behaviour and limits.

**Tier context.** Long-horizon autonomous operation: terminals, browsers, desktops, APIs, and 1000-way agent orchestration.

**Mandate — all four items are required; none is optional.**

1. Implement **specification of loop semantics, safety gates and budget rules** with an explicit *a-priori* cost model. Before doing the work the part must be able to state the tokens, FLOPs and microseconds it intends to consume, and it must abort with an `OmegaError` in the 4xxx budget range rather than silently exceed the envelope's `budget` or `deadline_ns`. This mechanism sits on the critical path of **Zapier AutomationBench**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.
2. Implement **capability register with measured success rates per task class** together with its verification path, so that anything this mechanism produces can be independently re-checked *inside this same file* without contacting any other part. The checker must be cheap enough to run on every call in debug mode and must be wired into `selftest()`. Its contribution is measured against **Online-Mind2Web** — a regression on that benchmark is an automatic rejection of this part.
3. Implement **operator runbook for agent incidents** as a first-class, fully realised mechanism. No stub, no `NotImplementedError`, no configuration flag whose default disables it. Its state must be reportable through `describe()` and it must be exercised by at least eight in-file tests, including one that fails loudly if the mechanism is silently bypassed. Correctness here is what makes the tier's **OSWorld 2.0** target reachable; the part therefore ships a microbenchmark that stands in for that benchmark's inner loop.
4. Implement **spec-versus-implementation drift detection**, and make it correct under concurrency: at least 64 in-flight `OmegaEnvelope`s must be able to traverse it simultaneously. No lock, mutex or borrow may be held across an `await` / `.await` / `yield` boundary, and the part must expose a contention counter so T09 can attribute latency to it. This mechanism sits on the critical path of **BrowseComp**, so its p99 latency assertion is part of the acceptance criteria, not an optional extra.

**Published capabilities.**

- `cap.t13.agent.agent_spec_doc@1`
- `cap.t13.agent.agent_spec_doc.describe@1`

**Required capabilities and their mandatory declared fallbacks.** Because the 1000 workers cannot share a filesystem, a part may *never* assume a requirement resolves. Each row below must be implemented as: try to acquire → on failure use the fallback → record the degradation in `describe()['degraded']`.

| required capability | if unavailable, this part must |
|---|---|
| `cap.t01.abi.abi_types@1` | re-declare the structural minimum locally (a frozen dataclass/struct mirror) and set `degraded['abi']='local-mirror'` |
| `cap.t01.abi.abi_errors@1` | raise the local `_OmegaErrorShim` carrying the same numeric code, and set `degraded['errors']='shim'` |
| `cap.t01.omega.omega_bus_core@1` | run against the in-file `_LoopbackBus` (direct call, no queue) and set `degraded['bus']='loopback'` |
| `cap.t13.agent.agent_scaling@1` | use the in-file conservative substitute for `agent_scaling` (documented, slower, lower quality) and set `degraded['agent_scaling']='local'` |
| `cap.t01.atomics.atomics_sync@1` | use the in-file conservative substitute for `atomics_sync` (documented, slower, lower quality) and set `degraded['atomics_sync']='local'` |
| `cap.t07.sparse.sparse_retrieval@1` | use the in-file conservative substitute for `sparse_retrieval` (documented, slower, lower quality) and set `degraded['sparse_retrieval']='local'` |
| `cap.t10.constraint.constraint_reasoning@1` | use the in-file conservative substitute for `constraint_reasoning` (documented, slower, lower quality) and set `degraded['constraint_reasoning']='local'` |

**Runtime safety obligation (contract clause C8).** This part performs or enables external effects, so every effect must pass the safety gate `cap.t19.gate.action_filter@1`. This is deliberately **not** a static link-time dependency — modelling it as one would make the capability graph cyclic. It is resolved at call time, and it is **fail-closed**: if the gate is not present on the bus, the part must refuse the effect and emit OmegaCode 6001. Executing an unfiltered external action is the single most serious defect a part can contain.

**Determinism.** `io` — the part may touch time, devices, sockets or subprocesses, but every such touch goes through an injected effect handle so that `selftest()` runs fully offline against a deterministic fake, and a replay log can reproduce any production trace.

**Line-count map — this is the acceptance shape of the file.**

| # | section | lines | requirement |
|---:|---|---:|---|
| 1 | Header block + OMEGA CONTRACT verbatim copy + PART_MANIFEST | 180 | Contract digest line, mission, provides/requires, LOC map, revision notes. |
| 2 | Public types, schemas and constants owned by this part | 320 | Every type this part publishes, fully documented, with invariants stated. |
| 3 | Core implementation A - specification of loop semantics, safety gates and budget rules | 600 | Primary algorithm. No TODOs, no placeholders, no stubbed branches. |
| 4 | Core implementation B - capability register with measured success rates per task class | 580 | Second required mechanism, fully independent of A's internals. |
| 5 | Core implementation C - operator runbook for agent incidents | 520 | Third required mechanism. |
| 6 | Core implementation D - spec-versus-implementation drift detection | 480 | Fourth required mechanism, including its measurement/assertion path. |
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

- [ ] File is exactly one file at `parts/t13_agents/P0650_agent_spec_doc.py`, self-contained, no imports of any other `parts/**` module.
- [ ] `PART_MANIFEST` is present and its `capability` field is exactly `cap.t13.agent.agent_spec_doc@1`.
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
