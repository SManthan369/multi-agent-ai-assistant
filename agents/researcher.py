from langchain_ollama import ChatOllama

from config.settings import MODEL_NAME, TEMPERATURE


llm = ChatOllama(
    model=MODEL_NAME,
    temperature=TEMPERATURE
)


def researcher(state):

    prompt = f"""
You are a Research Agent in a multi-agent AI system.

You have received the following execution plan:

{state["plan"]}

Provide concise research notes for each step.

Do not write a report.

Return only research notes.
"""

    response = llm.invoke(prompt)

    state["research"] = response.content

    return state