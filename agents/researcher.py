from agents.base_agent import BaseAgent


class ResearchAgent(BaseAgent):

    def build_prompt(self, state):

        return f"""
You are an expert research assistant.

Research the following topic.

Topic:
{state["query"]}

Provide:
- Overview
- Important facts
- Challenges
- Latest trends
"""

    def process_response(self, state, response):

        state["research"] = response

        state["messages"].append("Research completed")

        return state