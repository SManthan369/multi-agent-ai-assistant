from agents.base_agent import BaseAgent
from tools.web_search import web_search


class ResearchAgent(BaseAgent):

    def build_prompt(self, state):

        results = web_search(state["query"])

        search_text = ""

        for item in results:
            search_text += f"""
Title: {item['title']}
Summary: {item['body']}
URL: {item['url']}

"""

        return f"""
You are an expert research assistant.

Research the following topic:

{state["query"]}

Latest Web Search Results:

{search_text}

Using the above information, provide:

- Overview
- Important Facts
- Latest Trends
- Challenges
- Conclusion
"""

    def process_response(self, state, response):

        state["research"] = response
        state["messages"].append("Research completed")

        return state