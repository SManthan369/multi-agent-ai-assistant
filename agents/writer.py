from config.llm import llm


def writer_agent(state):

    prompt = f"""
You are a professional technical writer.

Using the research:

{state["research"]}

Using the execution plan:

{state["plan"]}

Write a clean report with headings.

"""

    response = llm.invoke(prompt)

    state["report"] = response.content

    return state