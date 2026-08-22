from AGENTS.communication_resilience_agent import CommunicationResilienceAgent
from AGENTS.coordination_strategy_agent import CoordinationStrategyAgent
from AGENTS.evaluation_agent import EvaluationAgent
from AGENTS.safety_agent import SafetyAgent
from AGENTS.simulation_agent import SimulationAgent
from AGENTS.swarm_architecture_agent import SwarmArchitectureAgent
from safety.gate import authorize

AGENTS = [
    SwarmArchitectureAgent(),
    CoordinationStrategyAgent(),
    SimulationAgent(),
    CommunicationResilienceAgent(),
    SafetyAgent(),
    EvaluationAgent(),
]


def run(context: dict) -> dict:
    """Run six specialists and apply the fail-closed swarm release gate."""
    results = [agent.run(context) for agent in AGENTS]
    governance = authorize("analysis_release", context)
    return {
        "system": "F79",
        "results": results,
        "governance": governance,
        "release_allowed": governance["allowed"],
        "physical_swarm_control": False,
        "autonomous_deployment": False,
        "autonomous_retasking": False,
    }
