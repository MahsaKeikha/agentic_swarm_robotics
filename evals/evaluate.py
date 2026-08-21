def evaluate(r): return {"passed":r.get("physical_swarm_control") is False and len(r.get("results",[]))==6}
