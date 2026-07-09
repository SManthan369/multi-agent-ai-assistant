from graphs.workflow import graph

state = {
    "query": input("Enter your research topic: "),
    "research": "",
    "plan": "",
    "report": "",
    "messages": [],
    "approval": False
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

# Only print the report if it was generated
if result.get("approval"):
    print("\n" + "=" * 80)
    print("FINAL REPORT")
    print("=" * 80)
    print(result["report"])
else:
    print("\nReport generation was cancelled by the user.")

print("\n" + "=" * 80)
print("WORKFLOW LOG")
print("=" * 80)

for msg in result["messages"]:
    print(f"✓ {msg}")