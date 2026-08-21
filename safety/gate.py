def authorize(action):
    blocked={"swarm_command","deploy_swarm","disable_containment","override_stop"}
    return {"allowed":action not in blocked,"reason":"physical swarm execution outside scope" if action in blocked else "reviewable"}
