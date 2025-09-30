# MCP & Agent Starter Kit

A collection of minimal, production-ready starter projects for building multi-agent and retrieval-augmented AI workflows.  
This kit includes three main components:

- **mcp-docs-server:** Exposes a folder of documents as a tool via REST API and optional MCP agent integration.
- **website-qa-bot:** Retrieval-Augmented Generation (RAG) Q/A bot for websites and documents, with Pinecone and OpenAI integration.
- **multi-agent-workflow:** Demonstrates multi-agent orchestration for collaborative AI tasks.

---

## Projects Overview

### 1. mcp-docs-server

- FastAPI server to serve documents from a local folder.
- REST endpoints for listing and retrieving documents.
- Optional MCP integration via `fastmcp` for agent workflows.

### 2. website-qa-bot

- Upload text or PDF files, store embeddings in Pinecone.
- Semantic search and context-aware answers using OpenAI LLM.
- FastAPI backend with endpoints for ingestion and querying.

### 3. multi-agent-workflow

- Orchestrates multiple AI agents (Researcher, Summarizer, Planner).
- Demonstrates agent collaboration for solving tasks.
- OpenAI integration for summarization, mock mode available.

---

## Setup

1. Clone this repository and navigate to the desired project folder.
2. Copy `.env.example` to `.env` in each project and add your API keys.
3. Install dependencies for each project:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the server for each project (see individual README files for details).

---

## File Tree

```
MCP & Agent Starter Kit/
├─ mcp-docs-server/
│  ├─ app/
│  │  ├─ server.py
│  │  ├─ mcp_adapter.py
│  │  ├─ docs/
│  │  │  ├─ README.md
│  │  │  └─ sample-doc.md
│  ├─ requirements.txt
│  ├─ .env.example
│  ├─ README.md
├─ website-qa-bot/
│  ├─ app/
│  │  ├─ main.py
│  │  ├─ ingest.py
│  │  ├─ query.py
│  │  ├─ utils.py
│  ├─ requirements.txt
│  ├─ .env.example
│  ├─ README.md
├─ multi-agent-workflow/
│  ├─ app/
│  │  ├─ agents.py
│  │  ├─ orchestrator.py
│  ├─ requirements.txt
│  ├─ .env.example
│  ├─ README.md
```

---

## Author / Contact

**Name:** Muhammad Umer  
**Email:** umerhayat282@gmail.com  
**LinkedIn:** [Muhammad Umer](https://www.linkedin.com/in/therealumerhayat/)

Feel free to connect for collaboration, freelance projects, or questions about multi-agent workflows.
