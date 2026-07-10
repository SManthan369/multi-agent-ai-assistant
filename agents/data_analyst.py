from agents.base_agent import BaseAgent
from tools.csv_reader import read_csv


class DataAnalysisAgent(BaseAgent):

    def analyze_dataset(self, file_path):

        df = read_csv(file_path)

        summary = {
            "rows": len(df),
            "columns": len(df.columns),
            "column_names": list(df.columns),
            "missing_values": df.isnull().sum().to_dict(),
            "statistics": df.describe(include="all").to_string()
        }

        return summary

    def build_prompt(self, state):

        summary = self.analyze_dataset(state["dataset"])

        return f"""
You are a professional Data Analyst.

Dataset Summary:

{summary}

Generate:

1. Dataset Overview
2. Important Statistics
3. Missing Values
4. Interesting Patterns
5. Business Insights

Use markdown.
"""

    def process_response(self, state, response):

        state["analysis"] = response

        state["messages"].append("Dataset analyzed")

        return state