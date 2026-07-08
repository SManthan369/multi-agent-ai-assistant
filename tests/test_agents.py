from agents.researcher import ResearchAgent

state = {
    "query": "Future of AI in healthcare",
    "research": "",
    "plan": "",
    "report": "",
    "messages": []
}

agent = ResearchAgent()

result = agent.run(state)

print(result["research"])