from config.llm import llm


def planning_agent(state):
    prompt = f"""
You are an expert planning agent in a multi-agent AI system.

Your responsibility is to create a clear, step-by-step execution plan based on the research provided.

Research:
{state["research"]}

Rules:
- Return only the execution plan.
- Use numbered steps.
- Keep each step concise and actionable.
- Do not repeat the research.
"""

    response = llm.invoke(prompt)

    state["plan"] = response.content

    return state