"""Fail-closed governance for F79 swarm robotics."""

BLOCKED_ACTIONS = {
    "swarm_command",
    "deploy_swarm",
    "disable_containment",
    "override_stop",
    "physical_swarm_control",
    "autonomous_retasking",
    "autonomous_replication",
}

REQUIRED_REVIEWS = (
    "architecture_reviewed",
    "coordination_reviewed",
    "simulation_reviewed",
    "communication_resilience_reviewed",
    "collision_avoidance_verified",
    "containment_reviewed",
    "emergency_stop_verified",
    "cybersecurity_reviewed",
    "evaluation_reviewed",
    "human_approval",
)


def authorize(action: str, context: dict | None = None) -> dict:
    """Authorize analysis release only after complete swarm-safety review."""
    context = context or {}
    if action in BLOCKED_ACTIONS:
        return {"allowed": False, "reason": "physical or autonomous swarm execution is outside reference-system authority"}

    missing = [key for key in REQUIRED_REVIEWS if not context.get(key)]
    if missing:
        return {"allowed": False, "reason": "missing required swarm review", "missing": missing}

    blockers = []
    if context.get("unresolved_high_risk_hazard"):
        blockers.append("unresolved high-risk hazard")
    if context.get("collision_risk_unresolved"):
        blockers.append("collision avoidance not demonstrated")
    if context.get("coordination_instability"):
        blockers.append("coordination instability detected")
    if context.get("communication_partition_unsafe"):
        blockers.append("unsafe behavior under communication partition")
    if context.get("containment_failure"):
        blockers.append("containment verification failed")
    if context.get("emergency_stop_failed"):
        blockers.append("emergency-stop verification failed")
    if context.get("cybersecurity_gap"):
        blockers.append("cybersecurity gap unresolved")
    if context.get("unbounded_emergent_behavior"):
        blockers.append("emergent behavior is not adequately bounded")

    if blockers:
        return {"allowed": False, "reason": "swarm governance blocker", "blockers": blockers}

    return {"allowed": True, "reason": "analysis release approved after qualified human review"}
