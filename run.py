from orchestration.orchestrator import run

REFERENCE_CONTEXT = {
    "objective": "swarm robotics review",
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

if __name__ == "__main__":
    print(run(REFERENCE_CONTEXT))
