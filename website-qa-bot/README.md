# Website Q/A Bot

A RAG-style (Retrieval-Augmented Generation) Q/A bot for websites and documents.  
This bot allows users to ingest text or PDF files, store embeddings in Pinecone, and answer queries using OpenAI's LLM.

---

## Features

- Upload text or PDF files for embeddings.
- Semantic search with Pinecone vector database.
- Context-aware answers using OpenAI LLM.
- FastAPI backend with REST endpoints.
- Easy deployment on cloud platforms like Render, Railway, or Vercel.

---

## API Endpoints

### POST `/ingest/file`
Upload a file to create embeddings.

**Form Data:**
- `file`: Text or PDF file  
- `source` (optional): Source name, default: `web_upload`

**Response:**
```json
{
  "inserted": 5,
  "status": "ok"
}
```

---

### POST `/query/ask`

**Body JSON:**
```json
{
  "q": "What is the company mission?"
}
```

**Response:**
```json
{
  "answer": "The company mission is ...",
  "sources": [
    {"id": "doc-1", "text": "..."},
    {"id": "doc-2", "text": "..."}
  ]
}
```

---

## Setup

1. Copy `.env.example` to `.env` and add your OpenAI & Pinecone API keys.
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the server:
    ```bash
    uvicorn app.main:app --reload --port 8000
    ```

---

## File Tree
```
website-qa-bot/
├─ app/
│  ├─ main.py
│  ├─ ingest.py
│  ├─ query.py
│  ├─ utils.py
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

