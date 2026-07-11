from agents.writer import WriterAgent


def test_build_prompt(sample_state):
    """
    Test that the writer prompt contains the research
    and execution plan.
    """

    agent = WriterAgent()

    sample_state["research"] = "Artificial Intelligence research"

    sample_state["plan"] = """
1. Collect Data
2. Train Model
3. Evaluate
"""

    prompt = agent.build_prompt(sample_state)

    assert "Artificial Intelligence research" in prompt
    assert "Collect Data" in prompt
    assert "professional technical writer" in prompt
    assert "# Introduction" in prompt
    assert "# Conclusion" in prompt


def test_process_response(sample_state):
    """
    Test that the report is stored correctly.
    """

    agent = WriterAgent()

    report = """
# Introduction

Artificial Intelligence is...

# Conclusion

AI will continue to evolve.
"""

    updated_state = agent.process_response(sample_state, report)

    assert updated_state["report"] == report
    assert "Report generated" in updated_state["messages"]
