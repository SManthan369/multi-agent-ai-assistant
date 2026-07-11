from unittest.mock import patch

from agents.researcher import ResearchAgent


@patch("agents.researcher.should_use_web_search")
@patch("agents.researcher.web_search")
def test_research_agent_with_web_search(mock_web_search, mock_router):

    mock_router.return_value = True

    mock_web_search.return_value = [
        {
            "title": "AI",
            "body": "Artificial Intelligence",
            "url": "https://example.com"
        }
    ]

    agent = ResearchAgent()

    state = {
        "query": "Latest AI",
        "messages": []
    }

    prompt = agent.build_prompt(state)

    assert "Artificial Intelligence" in prompt
    assert "Web Search Tool Used" in state["messages"]


@patch("agents.researcher.should_use_web_search")
def test_research_agent_without_web_search(mock_router):

    mock_router.return_value = False

    agent = ResearchAgent()

    state = {
        "query": "Explain Python",
        "messages": []
    }

    prompt = agent.build_prompt(state)

    assert "No web search required" in prompt
    assert "LLM Knowledge Used" in state["messages"]


def test_process_response():

    agent = ResearchAgent()

    state = {
        "query": "Artificial Intelligence",
        "research": "",
        "messages": []
    }

    updated = agent.process_response(
        state,
        "Research Output"
    )

    assert updated["research"] == "Research Output"
    assert "Memory Updated" in updated["messages"]
    assert "Research completed" in updated["messages"]