from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="gemma2:2b",
    temperature=0.3
)

response = llm.invoke("Explain LangGraph in one paragraph.")

print(response.content)