from agents.base_agent import BaseAgent
from memory.state import AgentState


class ResearchAgent(BaseAgent):

    def build_prompt(self, state: AgentState) -> str:
        return f"""
You are a senior AI research assistant.

Research the following topic:

{state["query"]}

Provide:
1. Overview
2. Key concepts
3. Current trends
4. Challenges
5. References (if known)

Return the response in well-structured markdown.
"""

    def process_response(
        self,
        state: AgentState,
        response: str
    ) -> AgentState:

        state["research"] = response
        state["messages"].append("Research completed")

        return state