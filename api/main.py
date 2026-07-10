from fastapi import FastAPI
from pydantic import BaseModel

from graphs.workflow import graph

app = FastAPI(
    title="Multi-Agent AI Assistant",
    version="1.0.0"
)


class ResearchRequest(BaseModel):
    query: str


@app.get("/")
def home():

    return {
        "message": "Multi-Agent AI Assistant API",
        "status": "running"
    }


@app.post("/research")
def research(request: ResearchRequest):

    state = {
        "query": request.query,
        "dataset": "",
        "research": "",
        "plan": "",
        "report": "",
        "analysis": "",
        "messages": [],
        "approval": True
    }

    result = graph.invoke(state)

    return {
        "research": result["research"],
        "plan": result["plan"],
        "report": result["report"]
    }