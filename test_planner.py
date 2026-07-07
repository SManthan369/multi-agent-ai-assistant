from agents.planner import planner

state = {
    "query": "Research the latest AI trends and write a report."
}

result = planner(state)

print(result["plan"])