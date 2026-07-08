from typing import TypedDict


class AgentState(TypedDict):
    query: str

    research: str

    plan: str