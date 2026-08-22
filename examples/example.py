from orchestration.orchestrator import run

context = {
    "objective": "review a simulated swarm coordination strategy",
    "architecture_reviewed": True,
    "coordination_reviewed": True,
    "simulation_reviewed": True,
    "communication_resilience_reviewed": True,
    "collision_avoidance_verified": True,
    "containment_reviewed": True,
    "emergency_stop_verified": True,
    "cybersecurity_reviewed": True,
    "evaluation_reviewed": True,
    "human_approval": True,
}

print(run(context))
