from langgraph.graph import StateGraph, END

from memory.state import AgentState

from agents.researcher import ResearchAgent
from agents.planner import PlanningAgent
from agents.writer import WriterAgent
from agents.human_approval import human_approval

research_agent = ResearchAgent()
planning_agent = PlanningAgent()
writer_agent = WriterAgent()


builder = StateGraph(AgentState)

builder.add_node("Research", research_agent.run)
builder.add_node("Planning", planning_agent.run)
builder.add_node("Approval", human_approval)
builder.add_node("Writer", writer_agent.run)


builder.set_entry_point("Research")


builder.add_edge("Research", "Planning")
builder.add_edge("Planning", "Approval")


def approval_router(state):

    if state["approval"]:
        return "Writer"

    return END


builder.add_conditional_edges(
    "Approval", approval_router, {"Writer": "Writer", END: END}
)


builder.add_edge("Writer", END)


graph = builder.compile()
