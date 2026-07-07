from agents.researcher import researcher

state = {
    "plan": """
1. Explain AI
2. Explain Machine Learning
3. Explain Deep Learning
4. Compare them
"""
}

result = researcher(state)

print(result["research"])