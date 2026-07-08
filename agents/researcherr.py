from config.llm import llm


def research_agent(state):
    prompt = f"""
You are an expert research assistant.

Research the following topic thoroughly.

Topic:
{state["query"]}

Return:
- Overview
- Important points
- Key facts
"""

    response = llm.invoke(prompt)

    state["research"] = response.content

    return state