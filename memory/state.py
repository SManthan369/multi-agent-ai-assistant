from typing import TypedDict, List


class AgentState(TypedDict):
    query: str

    research: str

    plan: str

    report: str

    messages: List[str]

    approval: bool