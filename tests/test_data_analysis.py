from agents.data_analyst import DataAnalysisAgent

agent = DataAnalysisAgent()

state = {
    "dataset": "sample_data/sales.csv",
    "analysis": "",
    "messages": []
}

result = agent.run(state)

print(result["analysis"])