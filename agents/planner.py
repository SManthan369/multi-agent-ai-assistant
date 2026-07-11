from agents.base_agent import BaseAgent


class PlanningAgent(BaseAgent):

    def build_prompt(self, state):

        return f"""
You are an expert planning agent.

Based on this research:

{state["research"]}

Create a numbered execution plan.
"""

    def process_response(self, state, response):

        state["plan"] = response

        state["messages"].append("Planning completed")

        return state
