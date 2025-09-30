# Multi-Agent Workflow

A minimal multi-agent orchestrator demonstrating collaboration between AI agents to solve tasks.  
This starter project includes three agents:

- **Researcher:** Fetches information (stub for web or database search)  
- **Summarizer:** Summarizes results using OpenAI LLM  
- **Planner:** Breaks summaries into actionable tasks  

This workflow is perfect for portfolio demos and as a foundation for multi-agent AI projects.

---

## Features

- Multi-agent orchestration with a FastAPI backend.
- OpenAI integration for summarization.
- Mock mode available when API keys are not provided.
- Simple setup and ready-to-run endpoints.

---

## API

### POST `/run`
Submit a query to the agents.

**Body JSON:**
```json
{
  "q": "Plan a weekend trip to Lisbon"
}
```

**Response:**
```json
{
  "query": "Plan a weekend trip to Lisbon",
  "results": [
    "Result snippet about Plan a weekend trip to Lisbon - source A",
    "Result snippet about Plan a weekend trip to Lisbon - source B"
  ],
  "summary": "Concise summary of results...",
  "tasks": [
    "Task: Research flight options",
    "Task: Book accommodations",
    "Task: Prepare itinerary"
  ]
}
```

---

### GET `/`
Health check endpoint.

**Response:**
```json
{
  "ok": true
}
```

---

## Setup

1. Copy `.env.example` to `.env` and add your OpenAI API key.
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the server:
    ```bash
    uvicorn app.orchestrator:app --reload --port 8200
    ```

---

## File Tree
```
multi-agent-workflow/
├─ app/
│  ├─ agents.py
│  ├─ orchestrator.py
├─ requirements.txt
├─ .env.example
├─ README.md
```

---

## Author / Contact

**Name:** Muhammad Umer  
**Email:** umerhayat282@gmail.com  
**LinkedIn:** [Muhammad Umer](https://www.linkedin.com/in/therealumerhayat/)

Feel free to connect with me for collaboration, freelance projects, or questions about this multi-agent workflow.
