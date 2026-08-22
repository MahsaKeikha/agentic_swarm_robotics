# F79 | Agentic Swarm Robotics | L3 Gold Standard | v1.0

A governed, simulation-oriented multi-agent reference implementation for swarm architecture, coordination strategy, simulation, communication resilience, safety analysis, and evaluation.

## Six-agent architecture

- [Swarm Architecture](AGENTS/swarm_architecture_agent.py)
- [Coordination Strategy](AGENTS/coordination_strategy_agent.py)
- [Simulation](AGENTS/simulation_agent.py)
- [Communication Resilience](AGENTS/communication_resilience_agent.py)
- [Safety](AGENTS/safety_agent.py)
- [Evaluation](AGENTS/evaluation_agent.py)

Tools and skills are exposed in `TOOLS/` and `SKILLS/`, with orchestration, memory, state, schemas, prompts, configuration, safety, observability, evals, benchmarks, examples, tests, docs, and CI.

## Gold-standard governance

F79 is fail closed. Analysis release requires architecture, coordination, simulation, communication-resilience, collision-avoidance, containment, emergency-stop, cybersecurity, evaluation, and qualified-human reviews.

Release is blocked for unresolved high-risk hazards, unresolved collision risk, coordination instability, unsafe communication-partition behavior, containment failure, emergency-stop failure, cybersecurity gaps, or inadequately bounded emergent behavior.

The reference system has no authority to issue swarm commands, deploy a physical swarm, disable containment, override stop functions, physically control a swarm, autonomously retask deployed robots, or authorize autonomous replication.

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python examples/example.py
python run.py
```

The verification layer includes eight direct governance tests and a 10-scenario held-out swarm-safety suite.
