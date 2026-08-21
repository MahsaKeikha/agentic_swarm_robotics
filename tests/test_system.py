from orchestration.orchestrator import run
from safety.gate import authorize
def test_run(): assert run({"objective":"x"})["physical_swarm_control"] is False
def test_gate(): assert authorize("deploy_swarm")["allowed"] is False
