# 🤖 AgentFlow AI

<p align="center">
  <strong>A Production-Ready Multi-Agent AI Assistant built with LangGraph, Ollama, Streamlit, and Python.</strong>
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![LangGraph](https://img.shields.io/badge/LangGraph-Multi--Agent-purple)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red?logo=streamlit)
![Docker](https://img.shields.io/badge/Docker-Container-blue?logo=docker)
![License](https://img.shields.io/badge/License-MIT-green)

</p>

---

## 📖 Overview

AgentFlow AI is a modular **Multi-Agent AI Assistant** designed using **LangGraph** and powered by **Ollama**.

The application coordinates multiple AI agents to perform:

- 🔍 Intelligent Research
- 📝 Planning
- 📄 Technical Report Generation
- 📊 CSV Data Analysis
- 🧠 Persistent Memory
- 🔀 Intelligent Tool Routing

The project follows a scalable agent-based architecture and includes Docker support, Streamlit UI, and local LLM execution.

---

# 🚀 Features

- 🔍 Research Agent with intelligent web search
- 📝 Planning Agent
- 📄 Writer Agent
- 📊 CSV Analysis Agent
- 🧠 Persistent JSON Memory
- 🔀 Smart Tool Router
- 🤖 Local LLM using Ollama
- 🎨 Streamlit Dashboard
- 📥 Download Reports
- 📈 Workflow Logs
- 🐳 Docker Support
- ⚙️ Environment Variables
- 🧪 Unit Testing (Coming Soon)
- 🔄 GitHub Actions CI/CD (Coming Soon)

---

# 🏗️ System Architecture

<p align="center">
<img src="assets/architecture.png" width="950">
</p>

---

# ⚙️ Workflow

```text
User
   │
   ▼
Streamlit UI
   │
   ▼
LangGraph Workflow
   │
   ├── Research Agent
   │       │
   │       ├── Tool Router
   │       │       ├── DuckDuckGo Search
   │       │       └── Local Knowledge
   │
   ├── Planning Agent
   │
   ├── Writer Agent
   │
   ├── Data Analysis Agent
   │
   └── Memory Manager
            │
            ▼
      Final Report
```

---

# 📂 Project Structure

```text
multi-agent-ai-assistant/
│
├── agents/
├── config/
├── graphs/
├── memory/
├── tools/
├── ui/
├── sample_data/
├── assets/
├── tests/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 🛠️ Tech Stack

| Technology | Usage |
|------------|------|
| Python | Programming Language |
| LangGraph | Multi-Agent Workflow |
| LangChain | LLM Framework |
| Ollama | Local LLM |
| Streamlit | User Interface |
| Pandas | CSV Analysis |
| DuckDuckGo | Web Search |
| Docker | Containerization |
| GitHub | Version Control |

---

# ⚡ Installation

### Clone Repository

```bash
git clone https://github.com/<YOUR_USERNAME>/AgentFlow-AI.git

cd AgentFlow-AI
```

### Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install Requirements

```bash
pip install -r requirements.txt
```

---

# 🤖 Install Ollama

Download:

https://ollama.com

Pull model:

```bash
ollama pull gemma2:2b
```

---

# ▶️ Run Application

```bash
streamlit run ui/app.py
```

Open

```
http://localhost:8501
```

---

# 🐳 Docker

Build Image

```bash
docker build -t agentflow-ai .
```

Run Container

```bash
docker run -p 8501:8501 \
-e OLLAMA_HOST=http://host.docker.internal:11434 \
agentflow-ai
```

---

# 📸 Screenshots

## Home

<img src="assets/home.png">

---

## Research

<img src="assets/research.png">

---

## Planning

<img src="assets/planning.png">

---

## Data Analysis

<img src="assets/analysis.png">

---

## Final Report

<img src="assets/report.png">

---

# 🧪 Testing

```bash
pytest
```

Coverage

```bash
pytest --cov
```

---

# 🔄 CI/CD

GitHub Actions automatically:

- Install dependencies
- Run unit tests
- Check formatting
- Build Docker image

---

# 🎯 Future Improvements

- RAG Support
- ChromaDB Memory
- Vector Search
- PDF Export
- Authentication
- Cloud Deployment
- Multi-LLM Support
- Voice Interface

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Open a Pull Request

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Manthan Soni**

GitHub: https://github.com/YOUR_USERNAME

LinkedIn: https://linkedin.com/in/YOUR_PROFILE
