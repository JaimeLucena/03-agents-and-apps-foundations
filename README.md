# 03-agents-and-apps-foundations

> **A complete, hands-on guide to building and orchestrating modern AI agents — from LangGraph and CrewAI to FastAPI and Streamlit deployment.**

This repository is the **third module** in the progressive learning path on **Generative AI Engineering**, designed to bridge the gap between basic LangChain concepts and full AI application development.

---

## 📚 Overview

This course introduces the essential frameworks and architecture patterns needed to **build, manage, and deploy AI agents**.  
You'll learn to combine **LangGraph**, **CrewAI**, **FastAPI**, and **Streamlit** into cohesive systems — the same technologies used in production-grade AI applications.

- **Agent Fundamentals**: Learn what AI agents are and how they differ from workflows  
- **Modern Orchestrators**: Work hands-on with **LangGraph** and **CrewAI**  
- **Practical Memory Management**: Build short-term and persistent memory using LangGraph  
- **App Architecture**: Explore modular, layered, and hexagonal structures for real-world projects  
- **Backend & UI**: Expose your AI through **FastAPI** and connect it to a **Streamlit frontend**

Perfect for AI developers, data scientists, or engineers who want to move from building chains to building full **AI-powered applications**.

---

## 📘 Course Structure

| Notebook | Topic | Description |
|----------|-------|-------------|
| `01` | **Intro to AI Agents** | What AI agents are, how they differ from workflows, and overview of orchestrators (LangGraph & CrewAI). |
| `02` | **LangGraph Basics** | Visual, conceptual intro to LangGraph — nodes, edges, state, memory, and control flow. |
| `03` | **Memory with LangGraph** | Implement short-term and persistent memory (RAM + SQLite checkpointers). |
| `04` | **CrewAI Basics** | Understand the CrewAI architecture — agents, tasks, crews, and processes. |
| `05` | **Code Architecture Patterns** | Learn modular app structures: monolithic, layered, and hexagonal architectures. |
| `06` | **FastAPI Intro** | Build your first backend API to serve model responses via OpenAI or Groq. |
| `07` | **Streamlit Intro** | Create a lightweight web UI that interacts with your FastAPI `/chat` endpoint. |

---

## 🚀 Getting Started

### Prerequisites

- **Python**: 3.10, 3.11, or 3.12  
- **uv**: Fast Python package manager ([installation guide](https://github.com/astral-sh/uv))  
- **OpenAI or Groq API Key** (for examples using real LLMs)

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/JaimeLucena/03-agents-and-apps-foundations.git
cd 03-agents-and-apps-foundations
```

2. **Install dependencies:**
```bash
uv sync
```

3. **Set up your environment variables:**  
Create a `.env` file in the root directory:
```env
OPENAI_API_KEY=your_openai_api_key_here
GROQ_API_KEY=your_groq_api_key_here  # Optional
```

4. **Launch JupyterLab:**
```bash
uv run jupyter lab
```

---

## 🧠 Run the API + UI

Once you understand the architecture, you can run the full system locally:

**1️⃣ Start the FastAPI backend**
```bash
uv run uvicorn main:app --reload --port 8000
```
Visit Swagger docs at `http://localhost:8000/docs`

**2️⃣ Start the Streamlit frontend**
```bash
uv run streamlit run app_streamlit.py
```
Open `http://localhost:8501` and interact with your app.

---

## 🛠️ Technology Stack

- **LangGraph** – Graph-based orchestration for agent state management  
- **CrewAI** – Multi-agent coordination and task execution  
- **LangChain** – Core LLM interface (LCEL-based)  
- **FastAPI** – High-performance Python web framework for serving LLM endpoints  
- **Streamlit** – Python-native web UI for interactive apps  
- **SQLite / MemorySaver** – Persistent and in-memory state storage  
- **OpenAI / Groq** – Model providers for LLM inference

---

## 🎓 Learning Path

### Phase 1: Fundamentals (Notebooks 01–03)
Understand what agents are, how LangGraph works, and how to manage memory in your apps.

### Phase 2: Agent Orchestration (Notebooks 04–05)
Dive into CrewAI and learn scalable app architectures (monolithic, modular, hexagonal).

### Phase 3: App Deployment (Notebooks 06–07)
Expose your models via FastAPI and connect them to a live Streamlit frontend.

---

## 🎯 What You'll Build

By the end of this repository, you'll be able to:

✅ Build agent graphs using LangGraph  
✅ Implement short-term and persistent memory  
✅ Orchestrate multi-agent systems with CrewAI  
✅ Design modular AI app architectures  
✅ Serve your model with FastAPI  
✅ Build a simple UI in Streamlit connected to your backend  
✅ Run end-to-end AI apps locally

---

## 📋 Recommended Knowledge

This is the **third module** in the learning series. You should be comfortable with:

- Python fundamentals ([01-python-fundamentals](https://github.com/JaimeLucena/01-python-fundamentals))  
- Basic LangChain concepts ([02-langchain-beginners](https://github.com/JaimeLucena/02-langchain-beginners))  
- Working in Jupyter notebooks

---

## 🔗 Related Resources

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)  
- [CrewAI Documentation](https://docs.crewai.com/)  
- [FastAPI Documentation](https://fastapi.tiangolo.com/)  
- [Streamlit Documentation](https://docs.streamlit.io/)  
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)

---

## 📝 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Jaime Lucena**  
Generative AI Engineer — Building AI applications & sharing what I learn along the way 🚀

- **GitHub**: [@JaimeLucena](https://github.com/JaimeLucena)  
- **LinkedIn**: [linkedin.com/in/jaimelucena](https://linkedin.com/in/jaimelucena)

---

## ⭐ Support

If you find this project useful, consider giving it a star on GitHub ⭐  
It helps others discover this learning series!

---

**Ready to build real AI agents?**  
Start with notebook `01` and move step by step! 🚀