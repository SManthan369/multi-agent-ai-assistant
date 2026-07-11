from agents.planner import PlanningAgent


def test_build_prompt(sample_state):
    """
    Test that the planning prompt contains the research text.
    """

    agent = PlanningAgent()

    sample_state["research"] = "Artificial Intelligence is transforming industries."

    prompt = agent.build_prompt(sample_state)

    assert "Artificial Intelligence is transforming industries." in prompt
    assert "Create a numbered execution plan." in prompt


def test_process_response(sample_state):
    """
    Test that the generated plan is stored correctly.
    """

    agent = PlanningAgent()

    response = """
1. Gather requirements
2. Perform research
3. Implement solution
4. Test
"""

    updated_state = agent.process_response(sample_state, response)

    assert updated_state["plan"] == response
    assert "Planning completed" in updated_state["messages"]
