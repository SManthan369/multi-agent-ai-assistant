from unittest.mock import patch
from agents.data_analysis import DataAnalysisAgent


@patch("agents.data_analysis.read_csv")
def test_analyze_dataset(mock_read_csv):

    import pandas as pd

    df = pd.DataFrame({"Name": ["A", "B"], "Age": [20, 21]})

    mock_read_csv.return_value = df

    agent = DataAnalysisAgent()

    summary = agent.analyze_dataset("dummy.csv")

    assert summary["rows"] == 2
    assert summary["columns"] == 2
    assert "Name" in summary["column_names"]
    assert "Age" in summary["column_names"]


@patch("agents.data_analysis.DataAnalysisAgent.analyze_dataset")
def test_build_prompt(mock_summary, sample_state):

    mock_summary.return_value = {
        "rows": 10,
        "columns": 2,
        "column_names": ["Name", "Age"],
        "data_types": {},
        "missing_values": {},
        "statistics": "Statistics",
        "sample_data": "Sample",
    }

    sample_state["dataset"] = "sample.csv"

    agent = DataAnalysisAgent()

    prompt = agent.build_prompt(sample_state)

    assert "Dataset Summary" in prompt
    assert "Statistics" in prompt
    assert "# Business Insights" in prompt


def test_process_response(sample_state):

    agent = DataAnalysisAgent()

    response = "Analysis Complete"

    updated = agent.process_response(sample_state, response)

    assert updated["analysis"] == "Analysis Complete"
    assert "Dataset analyzed" in updated["messages"]
