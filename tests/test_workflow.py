from unittest.mock import patch

from graphs.workflow import build_graph


def fake_research_run(state):
    """Mock ResearchAgent."""
    state["research"] = "Research Output"
    state["messages"].append("Research completed")
    return state


def fake_planning_run(state):
    """Mock PlanningAgent."""
    state["plan"] = "Planning Output"
    state["messages"].append("Planning completed")
    return state


def fake_writer_run(state):
    """Mock WriterAgent."""
    state["report"] = "Final Report"
    state["messages"].append("Report generated")
    return state


def fake_human_approval(state):
    """
    Simulate the human approval node.

    The approval value is already provided
    by the test through sample_state.
    """

    if state["approval"]:
        state["messages"].append("Plan Approved")
    else:
        state["messages"].append("Plan Rejected")

    return state


@patch("graphs.workflow.research_agent.run", side_effect=fake_research_run)
@patch("graphs.workflow.planning_agent.run", side_effect=fake_planning_run)
@patch("graphs.workflow.writer_agent.run", side_effect=fake_writer_run)
@patch("graphs.workflow.human_approval", side_effect=fake_human_approval)
def test_workflow_execution(
    mock_approval,
    mock_writer,
    mock_planner,
    mock_research,
    sample_state,
):
    sample_state["approval"] = True

    result = graph.invoke(sample_state)

    assert result["research"] == "Research Output"
    assert result["plan"] == "Planning Output"
    assert result["report"] == "Final Report"

    assert "Research completed" in result["messages"]
    assert "Planning completed" in result["messages"]
    assert "Plan Approved" in result["messages"]
    assert "Report generated" in result["messages"]

    mock_research.assert_called_once()
    mock_planner.assert_called_once()
    mock_writer.assert_called_once()


@patch("graphs.workflow.research_agent.run", side_effect=fake_research_run)
@patch("graphs.workflow.planning_agent.run", side_effect=fake_planning_run)
@patch("graphs.workflow.writer_agent.run", side_effect=fake_writer_run)
@patch("graphs.workflow.human_approval", side_effect=fake_human_approval)
def test_workflow_without_approval(
    mock_approval,
    mock_writer,
    mock_planner,
    mock_research,
    sample_state,
):
    sample_state["approval"] = False

    result = graph.invoke(sample_state)

    assert result["research"] == "Research Output"
    assert result["plan"] == "Planning Output"
    assert result["report"] == ""

    assert "Research completed" in result["messages"]
    assert "Planning completed" in result["messages"]
    assert "Plan Rejected" in result["messages"]
    assert "Report generated" not in result["messages"]

    mock_research.assert_called_once()
    mock_planner.assert_called_once()
    mock_writer.assert_not_called()
