from langgraph.graph import StateGraph, END

from memory.state import AgentState
from agents.researcher import research_agent
from agents.planner import planning_agent
from agents.writer import writer_agent


builder = StateGraph(AgentState)

builder.add_node("Research", research_agent)
builder.add_node("Planning", planning_agent)

builder.set_entry_point("Research")

builder.add_edge("Research", "Planning")
builder.add_edge("Planning", END)

graph = builder.compile()