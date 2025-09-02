# Local AI Chat (FastAPI + React)

A simple **AI chat app** that runs completely on your computer.  
It combines a **Python FastAPI backend** (for talking to [Ollama](https://ollama.ai) and running local LLMs) with a **React frontend** (chat interface).

---

## 🚀 Features
- ⚡ **FastAPI backend** (Python)
- 💬 **React frontend** (JavaScript)
- 🧠 Uses **Ollama** to run local LLMs (Llama3, Phi3, etc.)
- 🔒 Runs fully offline — your data stays local

---

## 🛠 Setup Instructions

### 1. Backend (FastAPI)
```bash
cd my-ai
python -m venv .venv
# Activate the venv (Windows)
.\.venv\Scripts\activate
# Install dependencies
pip install -r requirements.txt
# Run FastAPI server
uvicorn app:app --reload --port 8000
