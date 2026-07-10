from agents.base_agent import BaseAgent
from tools.csv_reader import read_csv


class DataAnalysisAgent(BaseAgent):

    def analyze_dataset(self, file_path):

     df = read_csv(file_path)

     summary = {
        "rows": len(df),
        "columns": len(df.columns),
        "column_names": list(df.columns),
        "data_types": df.dtypes.astype(str).to_dict(),
        "missing_values": df.isnull().sum().to_dict(),
        "statistics": df.describe(include="all").to_string(),
        "sample_data": df.head(5).to_string()
        }

     return summary

    def build_prompt(self, state):

        summary = self.analyze_dataset(state["dataset"])

        return f"""
You are a experienced Data Analyst.

Analyze this dataset carefully.

Dataset Summary:

{summary}

enerate a professional report with these sections:

# Dataset Overview

# Data Quality

# Statistical Summary

# Important Trends

# Business Insights

# Recommendations

Keep the report professional.
"""

    def process_response(self, state, response):

        state["analysis"] = response

        state["messages"].append("Dataset analyzed")

        return state