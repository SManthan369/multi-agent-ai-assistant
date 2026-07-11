from typing import TypedDict


class AgentState(TypedDict):
    query: str
    plan: str
    research: str
    draft: str
    review: str
    final: str
    dataset: str
    analysis: str
