from orchestration.orchestrator import run


def base():
    return {
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


SCENARIOS = [
    ({}, False),
    (base(), True),
    ({**base(), "human_approval": False}, False),
    ({**base(), "unresolved_high_risk_hazard": True}, False),
    ({**base(), "collision_risk_unresolved": True}, False),
    ({**base(), "coordination_instability": True}, False),
    ({**base(), "communication_partition_unsafe": True}, False),
    ({**base(), "containment_failure": True}, False),
    ({**base(), "emergency_stop_failed": True}, False),
    ({**base(), "unbounded_emergent_behavior": True}, False),
]


def main():
    passed = 0
    for context, expected in SCENARIOS:
        passed += run(context)["release_allowed"] is expected
    print(f"held-out: {passed}/{len(SCENARIOS)} passed")
    raise SystemExit(0 if passed == len(SCENARIOS) else 1)


if __name__ == "__main__":
    main()
