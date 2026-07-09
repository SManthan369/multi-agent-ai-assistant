from agents.base_agent import BaseAgent


class WriterAgent(BaseAgent):

    def build_prompt(self, state):

        return f"""
You are a professional technical writer.

Using the research:

{state["research"]}

Using the execution plan:

{state["plan"]}

Write a professional report with the following sections:

# Introduction

# Main Discussion

# Action Plan

# Conclusion
"""

    def process_response(self, state, response):

        state["report"] = response

        state["messages"].append("Report generated")

        return state