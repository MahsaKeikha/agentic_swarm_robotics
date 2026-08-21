from AGENTS.swarm_architecture_agent import SwarmArchitectureAgent
from AGENTS.coordination_strategy_agent import CoordinationStrategyAgent
from AGENTS.simulation_agent import SimulationAgent
from AGENTS.communication_resilience_agent import CommunicationResilienceAgent
from AGENTS.safety_agent import SafetyAgent
from AGENTS.evaluation_agent import EvaluationAgent
A=[SwarmArchitectureAgent(),CoordinationStrategyAgent(),SimulationAgent(),CommunicationResilienceAgent(),SafetyAgent(),EvaluationAgent()]
def run(c): return {"system":"F79","results":[a.run(c) for a in A],"physical_swarm_control":False}
