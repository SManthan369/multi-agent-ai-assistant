from agents.base_agent import BaseAgent
from tools.web_search import web_search
from tools.tool_router import should_use_web_search
from memory.manager import MemoryManager


class ResearchAgent(BaseAgent):

    def build_prompt(self, state):

        memory = MemoryManager()
        previous_memory = memory.load()

        # Last 3 memories
        memory_text = ""

        for item in previous_memory[-3:]:
            memory_text += f"""
Previous Query:
{item['query']}

Previous Research:
{item['research']}

"""

        # Decide whether web search is required
        if should_use_web_search(state["query"]):

            results = web_search(state["query"])

            search_text = ""

            for item in results:
                search_text += f"""
Title: {item['title']}
Summary: {item['body']}
URL: {item['url']}

"""

            state["messages"].append("Web Search Tool Used")

        else:

            search_text = "No web search required. Use your own knowledge."

            state["messages"].append("LLM Knowledge Used")

        return f"""
You are an expert research assistant.

Previous Memory:

{memory_text}

Research the following topic:

{state["query"]}

Supporting Information:

{search_text}

Instructions:
- Use previous memory only if it is relevant.
- Otherwise ignore it.

Provide:

- Overview
- Important Facts
- Latest Trends
- Challenges
- Conclusion

Write the answer in clean markdown.
"""

    def process_response(self, state, response):

        state["research"] = response

        # Save current research into memory
        memory = MemoryManager()
        memory.save(state["query"], response)

        state["messages"].append("Memory Updated")
        state["messages"].append("Research completed")

        return state
