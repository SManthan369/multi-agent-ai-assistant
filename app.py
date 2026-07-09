from graphs.workflow import graph

state = {
    "query": input("Enter your research topic: "),
    "research": "",
    "plan": "",
    "report": "",
    "messages": []
}

result = graph.invoke(state)

print("\n" + "=" * 80)
print("RESEARCH")
print("=" * 80)
print(result["research"])

print("\n" + "=" * 80)
print("PLAN")
print("=" * 80)
print(result["plan"])

print("\n" + "=" * 80)
print("FINAL REPORT")
print("=" * 80)
print(result["report"])

print("\n" + "=" * 80)
print("WORKFLOW LOG")
print("=" * 80)

for msg in result["messages"]:
    print(f"✓ {msg}")