# F79 | Agentic Swarm Robotics | L3 Gold Standard | v1.0

A governed, simulation-oriented multi-agent reference implementation for swarm architecture, coordination strategy, simulation, communication resilience, safety analysis, and evaluation.

F79 is designed as a reusable engineering reference for multi-robot and swarm systems in which many autonomous or semi-autonomous units coordinate through local rules, shared state, communication, or emergent collective behavior. The repository focuses on architecture review, coordination logic, resilience, simulation, safety, containment, evaluation, and human governance.

It does not authorize physical deployment, swarm commands, autonomous retasking of deployed robots, disabling containment, bypassing safety functions, or autonomous replication.

## Swarm system model

A swarm should be evaluated as a system of interacting agents rather than as a collection of independent robots.

```text
mission / task objective
        |
        v
swarm architecture
        |
        v
coordination strategy
        |
        v
communication topology
        |
        v
simulation + scenario testing
        |
        v
resilience + safety analysis
        |
        v
evaluation
        |
        v
qualified human approval
```

Collective behavior can produce effects that are not obvious from any one agent's local controller. F79 therefore treats emergent behavior, communication partitions, topology changes, collision risk, containment, and stop behavior as first-class safety concerns.

## Six-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Swarm Architecture Agent | Defines swarm composition, roles, topology, interfaces, mission boundaries, and assumptions | What entities make up the swarm, how are they connected, and what is each allowed to do? |
| Coordination Strategy Agent | Reviews allocation, formation, consensus, flocking, coverage, task assignment, and local decision rules | Does the coordination strategy remain stable and bounded under realistic conditions? |
| Simulation Agent | Builds scenario-based evidence across normal, degraded, and edge cases | Has the swarm been tested across representative interactions and failure modes? |
| Communication Resilience Agent | Reviews connectivity, latency, loss, partitions, stale state, and reconnection behavior | What happens when communication becomes delayed, partial, inconsistent, or unavailable? |
| Safety Agent | Reviews collision, containment, human proximity, unsafe emergence, stop functions, and high-risk hazards | Can the swarm enter or propagate an unsafe collective state? |
| Evaluation Agent | Consolidates metrics, robustness evidence, unresolved gaps, and release-readiness findings | Is the evidence sufficient for qualified human review without overclaiming safety? |

No single specialist can independently authorize deployment.

## Repository structure

```text
AGENTS/
├── swarm_architecture_agent.py
├── coordination_strategy_agent.py
├── simulation_agent.py
├── communication_resilience_agent.py
├── safety_agent.py
└── evaluation_agent.py

SKILLS/
├── swarm_architecture.py
├── coordination_review.py
├── resilience_analysis.py
├── swarm_safety.py
└── evaluation_design.py

TOOLS/
├── topology_tool.py
├── coordination_matrix_tool.py
├── scenario_tool.py
├── hazard_tool.py
└── metric_tool.py

orchestration/
memory/
state/
schemas/
prompts/
config/
safety/
observability/
evals/
benchmarks/
examples/
tests/
docs/
.github/workflows/ci.yml
run.py
pyproject.toml
README.md
```

The separation between agents, deterministic tools, state, safety, evaluation, and observability makes the reference architecture easier to inspect and extend.

## Swarm architecture

The Swarm Architecture Agent defines the system before coordination performance is optimized.

A swarm architecture record should identify, where applicable:

```text
swarm_id
mission_type
agent_types
agent_count
heterogeneous_or_homogeneous
leadered_or_leaderless
coordination_mode
communication_topology
local_sensing
shared_state
operating_environment
containment_boundary
human_interaction_model
safe_state
stop_mechanism
cybersecurity_assumptions
version
```

The architecture should distinguish between simulation-only studies, laboratory fleets, and real-world physical deployments.

## Homogeneous and heterogeneous swarms

Homogeneous swarms use largely similar agents and capabilities. Heterogeneous swarms can combine different robots, sensors, mobility classes, payloads, or authority levels.

Heterogeneity increases interface and coordination complexity. Important questions include:

- Which agents can perform which tasks?
- Are roles fixed or dynamically reassigned?
- Can one agent issue commands to another?
- Are capabilities represented accurately after failures or degradation?
- Can a less-capable agent be assigned an unsafe role?
- Are role transitions bounded and traceable?

The architecture should not assume all swarm members are interchangeable unless that property is actually validated.

## Topology

`TOOLS/topology_tool.py` provides the reference representation for swarm connectivity.

Possible coordination topologies include:

- fully connected
- mesh
- nearest-neighbor
- radius-based
- leader-follower
- hierarchical
- dynamic graph
- opportunistic peer-to-peer

Relevant topology properties include:

```text
node_count
edge_count
connectivity
neighbor_definition
communication_range
update_rate
partition_behavior
reconnection_behavior
single_points_of_failure
```

A topology that is connected in nominal simulation may fragment under mobility, interference, physical obstruction, node loss, or battery depletion.

## Coordination strategies

The Coordination Strategy Agent reviews the rules that convert local information into collective behavior.

Common research patterns include:

- flocking
- formation control
- consensus
- distributed coverage
- task allocation
- auction-based coordination
- leader-follower behavior
- decentralized path coordination
- stigmergic coordination
- distributed exploration
- collective transport

F79 is strategy-neutral. The repository evaluates whether the selected coordination logic is bounded, traceable, and safe under the intended conditions.

## Coordination matrix

`TOOLS/coordination_matrix_tool.py` can represent relationships such as:

```text
agent_or_role
observes
communicates_with
influences
can_reassign
can_override
shared_state_dependency
failure_propagation_path
```

This helps make hidden authority and dependency relationships visible.

## Decentralized control

A decentralized swarm can continue operating when no central coordinator exists. That resilience can also make safety intervention harder.

Important questions include:

- How are local objectives reconciled with global constraints?
- What stops unsafe local behavior from propagating?
- How is stale neighbor state handled?
- Can a partitioned subgroup continue operating safely?
- What happens when two subgroups reconnect with inconsistent state?
- Is there a globally enforceable containment or stop mechanism?

Decentralization should not be treated as an excuse for unbounded behavior.

## Emergent behavior

Emergent behavior is behavior that arises from interactions among agents rather than from a single explicitly commanded trajectory.

Potential risks include:

- unexpected clustering
- oscillation
- deadlock
- congestion
- runaway dispersion
- unstable formations
- local positive-feedback loops
- resource competition
- unsafe pursuit or attraction dynamics
- collision cascades
- task starvation

The system should identify emergent behavior that appears only at larger swarm sizes or under particular communication patterns.

Simulation should therefore vary swarm size, density, topology, latency, environment complexity, and fault combinations rather than testing only one nominal configuration.

## Stability and boundedness

Coordination performance should be assessed for boundedness rather than only whether a task eventually completes.

Useful properties can include:

- convergence
- bounded position error
- bounded velocity
- bounded acceleration
- bounded control effort
- formation stability
- consensus stability
- absence of runaway oscillation
- recovery after disturbance

The exact metrics depend on the coordination strategy.

## Collision avoidance

Collision avoidance is a hard safety concern in physical multi-robot systems.

The Safety Agent should consider:

- agent-agent collisions
- agent-human collisions
- static obstacles
- dynamic obstacles
- localization uncertainty
- perception uncertainty
- communication delay
- simultaneous evasive maneuvers
- deadlock resolution
- dense-swarm interactions
- actuator limits
- stopping distance

A collision-avoidance strategy should be tested under worst-case density and degraded sensing rather than only in sparse nominal scenes.

## Human proximity

If a swarm can operate near people, additional constraints are required.

Examples include:

- exclusion zones
- speed limits
- approach limits
- minimum separation
- human detection confidence
- safe-stop behavior
- controlled restart
- accessible emergency stop

F79 does not authorize physical operation near people. Such applications require system-specific safety engineering and qualified approval.

## Containment

Containment defines where the swarm is allowed to operate.

Containment mechanisms can include:

- geofences
- mapped boundaries
- physical barriers
- virtual keep-out zones
- altitude or depth limits
- role-specific zones
- communications boundaries
- task-space constraints

Containment should be robust to localization error, map error, connectivity loss, controller faults, and individual-node failure.

Containment failure is a release blocker.

## Communication resilience

Swarm behavior often depends on distributed communication.

The Communication Resilience Agent reviews:

- packet loss
- latency
- jitter
- stale state
- inconsistent clocks
- node dropout
- network partitions
- bandwidth limits
- congestion
- spoofed or corrupted messages
- reconnection behavior

A safe swarm should degrade predictably when communication assumptions fail.

## Partition behavior

Network partitions deserve explicit testing because a swarm may split into multiple independently acting groups.

Useful questions include:

```text
Can each subgroup remain within containment?
Can each subgroup avoid collisions?
Can each subgroup continue the mission safely?
Should the subgroup stop instead?
What state is reconciled after reconnection?
Can duplicate or conflicting task ownership occur?
```

Unsafe communication-partition behavior is a hard blocker.

## Cybersecurity

Cybersecurity can directly affect swarm safety because compromised coordination or state can influence many robots at once.

Security review should consider:

- node identity
- message authenticity
- authorization
- key management
- replay protection
- command integrity
- update integrity
- secure boot where applicable
- network segmentation
- compromised-node containment
- anomaly detection
- denial-of-service behavior

The swarm should not automatically trust every peer message simply because it originated from an expected network address.

## Compromised or Byzantine nodes

Some research systems may need to consider malicious, corrupted, or inconsistent participants.

Potential behaviors include:

- false position reports
- false task completion
- conflicting leadership claims
- malicious consensus values
- spoofed health state
- repeated collision-inducing behavior
- refusal to stop

F79 can support analysis of resilience to such conditions, but it does not provide a blanket claim of Byzantine fault tolerance.

## Simulation strategy

The Simulation Agent uses scenario-based testing to evaluate collective behavior before physical deployment.

`TOOLS/scenario_tool.py` provides the reference scenario abstraction.

A strong simulation matrix should vary:

- swarm size
- density
- initial positions
- task complexity
- obstacle density
- communication latency
- packet loss
- network partitions
- sensor noise
- localization error
- agent failures
- battery depletion
- hardware degradation
- environmental disturbance
- human intrusion into the operating area

Randomized trials can be useful, but important edge cases should also be explicitly constructed.

## Scenario categories

Useful categories include:

```text
nominal
high density
partial communication loss
complete partition
single-agent failure
multi-agent failure
localization degradation
sensor disagreement
containment boundary challenge
emergency-stop event
reconnection after partition
adversarial or corrupted message case
```

Passing only nominal scenarios is insufficient evidence for a physical swarm.

## Swarm size scaling

Collective behavior can change as swarm size increases.

A coordination strategy validated on five agents should not automatically be assumed valid on fifty or five hundred.

Evaluation should consider:

- communication scaling
- computational load
- congestion
- interaction density
- convergence time
- collision probability
- topology fragmentation
- emergent modes
- stop propagation latency

The tested swarm-size range should be explicit.

## Stop behavior

Emergency-stop behavior can be challenging in decentralized systems.

Important questions include:

- Is stop authority centralized, distributed, or both?
- How quickly does stop propagate?
- What happens if the network is partitioned?
- Can a local robot refuse or fail to stop?
- Is a physical stop channel independent of high-level coordination?
- Is restart controlled and deliberate?

An emergency-stop failure is a hard blocker.

## Autonomous retasking

Dynamic task allocation is common in swarm research, but deployed autonomous retasking can change operational risk.

The system must not autonomously authorize a deployed physical swarm to take on a materially new mission, enter a new operating area, change payload use, or expand its authority without qualified review.

## Autonomous replication boundary

F79 explicitly prohibits autonomous replication authority.

The reference architecture does not authorize systems to manufacture, commission, activate, spawn, or deploy additional physical swarm members without explicit human-controlled processes.

## Safety analysis

`TOOLS/hazard_tool.py` supports structured hazard tracking.

A hazard record can include:

```text
hazard_id
scenario
initiating_condition
local_failure
collective_effect
possible_harm
severity
likelihood_or_exposure
risk_control
verification_evidence
residual_risk
review_owner
status
```

Swarm safety should consider both single-agent failures and failure propagation across the collective.

## Failure propagation

Examples include:

- one incorrect leader state affecting followers
- corrupted shared map data propagating through peers
- one failed unit creating congestion
- collision avoidance producing a chain reaction
- communication retries causing network collapse
- task reassignment overloading healthy units
- a local boundary failure pulling neighbors outside containment

The Safety Agent should examine whether local faults remain local.

## Evaluation

`TOOLS/metric_tool.py` provides the reference metric abstraction.

Useful metrics can include:

- task completion rate
- completion time
- coverage
- formation error
- consensus error
- collision count
- near-miss rate
- minimum separation
- containment violations
- communication load
- packet-loss tolerance
- recovery time
- partition survival
- stop propagation time
- energy consumption
- task-allocation fairness
- deadlock frequency

Metrics should be interpreted together rather than reduced to one performance number.

## Evaluation under uncertainty

Simulation evidence should record uncertainty and assumptions.

Important assumptions include:

- sensor models
- physics fidelity
- communication models
- actuator models
- environment models
- localization models
- failure distributions

Simulation results are not equivalent to proof of physical safety.

## Observability

The `observability/` layer supports traceable workflow execution.

Useful swarm telemetry includes:

- active agent count
- topology state
- partition count
- communication quality
- coordination error
- collision alerts
- containment proximity
- stop state
- task allocation
- degraded nodes
- safety-gate state

Observability can help detect unexpected collective behavior, but monitoring is not a substitute for safe architecture.

## Fail-closed governance

F79 is fail closed. Analysis release requires architecture, coordination, simulation, communication-resilience, collision-avoidance, containment, emergency-stop, cybersecurity, evaluation, and qualified-human reviews.

Release is blocked for:

- unresolved high-risk hazards
- unresolved collision risk
- coordination instability
- unsafe emergent behavior
- inadequate scenario coverage
- unsafe communication-partition behavior
- containment failure
- emergency-stop failure
- unbounded scaling behavior
- unresolved cybersecurity gaps
- inadequate evidence quality
- unreviewed major changes
- physical deployment authority requested
- swarm command authority requested
- autonomous retasking of deployed robots requested
- safety override requested
- autonomous replication requested
- qualified human approval missing

Human approval cannot convert failed safety evidence into passing evidence.

## Human authority boundaries

The reference system has no authority to:

- issue swarm commands
- deploy a physical swarm
- enable motors or actuators
- disable containment
- override safety limits
- bypass stop functions
- autonomously retask deployed robots
- authorize operation near people
- authorize weaponization or harmful payload use
- authorize autonomous replication
- certify the swarm as safe

Qualified engineers and authorized operators retain physical and deployment authority.

## End-to-end reference workflow

A typical F79 workflow follows this sequence:

1. Define the mission, environment, swarm composition, and authority boundary.
2. Document topology, communication, sensing, and coordination assumptions.
3. Define coordination rules and safety constraints.
4. Build scenario matrices across swarm sizes and densities.
5. Simulate nominal, degraded, partitioned, and faulted states.
6. Evaluate collision avoidance and containment.
7. Evaluate communication resilience and reconnection.
8. Examine emergent behavior and failure propagation.
9. Test emergency-stop behavior.
10. Review cybersecurity assumptions.
11. Consolidate performance, resilience, and safety metrics.
12. Record unresolved limitations and evidence gaps.
13. Apply fail-closed governance gates.
14. Require qualified human review before any physical next step.

## Held-out safety evaluation

The repository includes:

```text
evals/evaluate.py
evals/held_out.py
benchmarks/reference_case.json
```

The verification layer includes eight direct governance tests and a 10-scenario held-out swarm-safety suite.

Useful evaluation dimensions include:

- architecture completeness
- topology review
- coordination stability
- collision-risk detection
- containment enforcement
- communication-partition handling
- emergent-behavior detection
- stop-function enforcement
- cybersecurity review
- deployment-boundary enforcement
- autonomous-replication blocking
- human-review enforcement

Strong held-out cases should intentionally contain unsafe or incomplete swarm evidence.

## Failure states

Useful explicit states include:

```text
ARCHITECTURE INCOMPLETE
TOPOLOGY UNVERIFIED
COORDINATION UNSTABLE
COLLISION RISK UNRESOLVED
EMERGENT BEHAVIOR UNBOUNDED
COMMUNICATION PARTITION UNSAFE
CONTAINMENT FAILED
STOP FUNCTION FAILED
CYBERSECURITY REVIEW REQUIRED
SCALING BEHAVIOR UNVERIFIED
PHYSICAL DEPLOYMENT PROHIBITED
SWARM COMMAND AUTHORITY PROHIBITED
AUTONOMOUS RETASKING PROHIBITED
AUTONOMOUS REPLICATION PROHIBITED
HUMAN APPROVAL REQUIRED
```

The system should never fabricate simulation evidence, communication resilience, containment status, collision safety, stop verification, or human approval.

## Reproduce the reference implementation

Install development dependencies:

```bash
python -m pip install -e '.[dev]'
```

Run CI-equivalent checks:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python examples/example.py
python run.py
```

CI runs on Python 3.10, 3.11, and 3.12.

## Reproducibility

A reproducible swarm evaluation should version at minimum:

- architecture
- swarm size
- agent types
- topology
- coordination algorithm
- controller parameters
- scenario definitions
- random seeds
- simulator version
- physics settings
- sensor models
- communication models
- failure injections
- cybersecurity assumptions
- evaluation metrics
- safety thresholds
- software environment

Changed coordination or topology should generate new evidence rather than silently inheriting prior results.

## L3 Gold Standard

F79 follows the library's L3 Gold Standard structure through six specialist agents, deterministic tools, explicit state and safety layers, held-out governance evaluation, CI, observability, fail-closed gates, and mandatory qualified-human review.

This maturity designation describes the repository's engineering and governance structure. It is not certification that any swarm is safe for physical deployment, operation near people, regulated use, or autonomous field operation.

## Extending F79

Common extensions include:

- multi-robot simulators
- ROS 2 research integrations
- distributed task allocators
- formation-control modules
- coverage planners
- consensus algorithms
- network emulation
- packet-loss injection
- fault injection
- hardware-in-the-loop testing
- topology visualization
- collision-risk dashboards
- containment monitoring
- cybersecurity test harnesses
- experiment tracking
- fleet telemetry

Extensions should preserve the separation between analysis, recommendation, command generation, physical execution, and deployment authority.

## Example applications

F79 can serve as a reference architecture for research and engineering involving:

- warehouse robot fleets
- multi-drone coordination research
- agricultural robot fleets
- search and exploration swarms
- environmental sensing swarms
- collective transport research
- formation-control research
- distributed coverage
- swarm resilience studies
- multi-robot simulation

Physical applications require additional hardware-specific, environmental, operational, legal, and safety controls.

## Design principles

1. Treat the swarm as a collective dynamical system, not merely a list of robots.
2. Make topology and coordination authority explicit.
3. Test communication partitions and reconnection behavior.
4. Evaluate emergent behavior across swarm size and density.
5. Treat collision avoidance and containment as hard safety requirements.
6. Prevent local failures from silently propagating through the swarm.
7. Test emergency-stop behavior independently of nominal coordination.
8. Include cybersecurity in collective safety analysis.
9. Fail closed when safety evidence is incomplete or contradictory.
10. Keep physical deployment, retasking, safety overrides, and replication under qualified human control.

## Documentation

Additional architecture documentation is available under `docs/`, including `docs/ARCHITECTURE.md`.

## Citation and reuse

Use the repository metadata and citation information supplied by the project when referencing this implementation. The repository can be studied, cited, adapted, and extended subject to its license terms.

## Responsible use

Use F79 as a swarm robotics engineering, simulation, safety, and multi-agent governance reference. Validate coordination stability, communication resilience, collision avoidance, containment, cybersecurity, stop behavior, scaling assumptions, and physical safety against the actual application before deployment. Final physical, operational, and deployment authority remains with appropriately qualified and authorized humans.