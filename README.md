# 🤖 Multi-Agent AI Assistant

A production-ready **Multi-Agent AI Assistant** built with **LangGraph, Ollama, Streamlit, and Python**. The system uses multiple specialized AI agents to perform research, planning, report generation, and CSV data analysis through an interactive web interface.

---

## 🚀 Features

- 🔍 Research Agent with intelligent web search
- 📝 Planning Agent for structured execution plans
- 📄 Writer Agent for professional report generation
- 📊 Data Analysis Agent for CSV file analysis
- 🧠 Persistent memory for previous interactions
- 🔀 Tool Router for deciding when to use web search
- 🤖 Local LLM support using Ollama
- 🎨 Interactive Streamlit dashboard
- 📥 Download generated reports
- 📈 Workflow logs and execution statistics
- 🐳 Docker support
- ⚙️ Environment-based configuration

---

## 🏗️ Architecture

```text
                User
                  │
        Streamlit Web Interface
                  │
           LangGraph Workflow
                  │
    ┌────────┬────────┬────────┬────────┐
    │        │        │        │
Research  Planning  Writer  Data Analysis
    │                 │
DuckDuckGo         Ollama LLM
    │
 Memory Manager
    │
 Final Report
```

---

## 📂 Project Structure

```text
multi-agent-ai-assistant/
│
├── agents/
│   ├── base_agent.py
│   ├── researcher.py
│   ├── planner.py
│   ├── writer.py
│   └── data_analysis.py
│
├── config/
│   ├── llm.py
│   ├── logger.py
│   └── settings.py
│
├── graphs/
│   └── workflow.py
│
├── memory/
│   ├── manager.py
│   ├── state.py
│   └── chat_memory.json
│
├── tools/
│   ├── web_search.py
│   ├── tool_router.py
│   └── csv_tool.py
│
├── ui/
│   └── app.py
│
├── sample_data/
├── logs/
├── assets/
├── tests/
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── README.md
└── LICENSE
```

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| AI Framework | LangGraph |
| LLM | Ollama (Gemma 2B / Llama 3.1) |
| UI | Streamlit |
| Data Analysis | Pandas |
| Search | DuckDuckGo |
| Containerization | Docker |
| Version Control | Git & GitHub |

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/multi-agent-ai-assistant.git
cd multi-agent-ai-assistant
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the environment

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🤖 Install Ollama

Download Ollama from:

https://ollama.com

Pull the required model:

```bash
ollama pull gemma2:2b
```

---

## ▶️ Run the Project

```bash
streamlit run ui/app.py
```

Open:

```
http://localhost:8501
```

---

## 🐳 Docker

Build

```bash
docker build -t multi-agent-ai-assistant .
```

Run

```bash
docker run -p 8501:8501 \
-e OLLAMA_HOST=http://host.docker.internal:11434 \
multi-agent-ai-assistant
```

---

## 📸 Screenshots

Coming Soon

- Home Screen
- Research Agent
- Planning Agent
- CSV Analysis
- Final Report

---

## 🎯 Future Improvements

- Support for multiple LLM providers
- Voice input
- PDF report generation
- Authentication
- Cloud deployment
- GitHub Actions CI/CD

---

## 🤝 Contributing

Contributions are welcome.

Fork the repository and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Manthan Soni**

GitHub: https://github.com/YOUR_USERNAME

LinkedIn: https://linkedin.com/in/YOUR_PROFILE
