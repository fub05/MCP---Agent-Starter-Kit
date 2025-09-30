# mcp-docs-server

A FastAPI-based server that exposes a local `docs` folder as a tool for document retrieval.  
Supports both simple HTTP endpoints and integration with MCP via the optional `fastmcp` package.

---

## Overview

This project allows you to serve documents from a folder via REST API endpoints.  
Optionally, you can enable MCP (Multi-Agent Collaboration Protocol) integration for agent-based workflows by installing `fastmcp`.

---

## Features

- List available documents in the `docs` folder.
- Retrieve the contents of any document by name.
- Simple REST API for demo and non-MCP clients.
- Optional MCP integration for agent workflows (requires `fastmcp`).
- Easy setup and deployment.

---

## API Endpoints

### GET `/tool/list`
Returns a list of all files in the `docs` folder.

**Response:**
```json
{
  "docs": [
    "README.md",
    "sample-doc.md"
  ]
}
```

### GET `/tool/get/{name}`
Returns the contents of the specified document.

**Response:**  
Returns the file as a download.  
If the file does not exist, returns a 404 error.

### GET `/health`
Health check endpoint.

**Response:**
```json
{
  "ok": true
}
```

---

## MCP Integration

If you want to use MCP agent workflows, install `fastmcp` and configure as needed.  
The server will automatically register a document reading tool with MCP if `fastmcp` is available.

---

## Setup

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2. Run the server:
    ```bash
    uvicorn app.server:app --reload --port 8100
    ```

3. (Optional) For MCP integration, install `fastmcp`:
    ```bash
    pip install fastmcp
    ```

---

## File Tree
```
mcp-docs-server/
├─ app/
│  ├─ server.py         # FastAPI app and endpoints
│  ├─ mcp_adapter.py    # MCP integration logic
│  ├─ docs/             # Folder containing documents to serve
│  │  ├─ README.md
│  │  └─ sample-doc.md
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
