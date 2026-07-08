from graphs.workflow import graph

state = {
    "query": input("Enter your research topic: "),
    "research": "",
    "plan": ""
}

result = graph.invoke(state)

print("\n")
print("=" * 80)
print("RESEARCH")
print("=" * 80)

print(result["research"])

print("\n")
print("=" * 80)
print("PLAN")
print("=" * 80)

print(result["plan"])