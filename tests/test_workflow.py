from unittest.mock import patch, MagicMock

from graphs.workflow import graph


class FakeResponse:
    def __init__(self, text):
        self.content = text


@patch("config.llm.llm.invoke")
def test_workflow_execution(mock_invoke, sample_state):

    mock_invoke.side_effect = [
        FakeResponse("Research Output"),
        FakeResponse("Planning Output"),
        FakeResponse("Final Report"),
    ]

    sample_state["approval"] = True

    result = graph.invoke(sample_state)

    assert result["research"] == "Research Output"
    assert result["plan"] == "Planning Output"
    assert result["report"] == "Final Report"

    assert "Research completed" in result["messages"]
    assert "Planning completed" in result["messages"]
    assert "Report generated" in result["messages"]


@patch("config.llm.llm.invoke")
def test_workflow_without_approval(mock_invoke, sample_state):

    mock_invoke.side_effect = [
        FakeResponse("Research Output"),
        FakeResponse("Planning Output"),
    ]

    sample_state["approval"] = False

    result = graph.invoke(sample_state)

    assert result["research"] == "Research Output"
    assert result["plan"] == "Planning Output"
    assert result["report"] == ""

    assert "Report generated" not in result["messages"]