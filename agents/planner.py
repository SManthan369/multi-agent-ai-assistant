from config.llm import llm


def planning_agent(state):
    prompt = f"""
You are an expert planner.

Based on this research:

{state["research"]}

Create a step-by-step execution plan.
"""

    response = llm.invoke(prompt)

    state["plan"] = response.content

    return state