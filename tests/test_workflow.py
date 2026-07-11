from graphs.workflow import graph


def test_workflow_execution(sample_state):
    """
    Test the complete LangGraph workflow.
    """

    sample_state["approval"] = True

    result = graph.invoke(sample_state)

    assert "research" in result
    assert "plan" in result
    assert "report" in result

    assert result["research"] != ""
    assert result["plan"] != ""
    assert result["report"] != ""

    assert "Research completed" in result["messages"]
    assert "Planning completed" in result["messages"]
    assert "Report generated" in result["messages"]


def test_workflow_without_approval(sample_state):
    """
    Workflow should stop after approval if approval=False.
    """

    sample_state["approval"] = False

    result = graph.invoke(sample_state)

    assert result["research"] != ""
    assert result["plan"] != ""

    # Writer should never run
    assert result["report"] == ""

    assert "Planning completed" in result["messages"]
    assert "Report generated" not in result["messages"]
