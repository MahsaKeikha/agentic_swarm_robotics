from orchestration.orchestrator import run
from safety.gate import authorize


def valid_context():
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


def test_reference_system_never_controls_or_deploys_swarm():
    result = run(valid_context())
    assert result["physical_swarm_control"] is False
    assert result["autonomous_deployment"] is False
    assert result["autonomous_retasking"] is False


def test_complete_review_can_release_analysis():
    assert run(valid_context())["release_allowed"] is True


def test_missing_human_approval_fails_closed():
    context = valid_context()
    context["human_approval"] = False
    assert run(context)["release_allowed"] is False


def test_swarm_deployment_is_never_authorized():
    assert authorize("deploy_swarm", valid_context())["allowed"] is False


def test_collision_risk_blocks_release():
    context = valid_context()
    context["collision_risk_unresolved"] = True
    assert run(context)["release_allowed"] is False


def test_coordination_instability_blocks_release():
    context = valid_context()
    context["coordination_instability"] = True
    assert run(context)["release_allowed"] is False


def test_unsafe_partition_behavior_blocks_release():
    context = valid_context()
    context["communication_partition_unsafe"] = True
    assert run(context)["release_allowed"] is False


def test_unbounded_emergent_behavior_blocks_release():
    context = valid_context()
    context["unbounded_emergent_behavior"] = True
    assert run(context)["release_allowed"] is False
