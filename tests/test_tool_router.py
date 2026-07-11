from tools.tool_router import should_use_web_search

queries = [
    "What is Machine Learning?",
    "Latest AI news",
    "Current GPU prices",
    "Explain LangGraph",
    "Today's weather"
]

for q in queries:
    print(q)
    print(should_use_web_search(q))
    print("-" * 40)