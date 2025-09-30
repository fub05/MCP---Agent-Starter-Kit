from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from pathlib import Path
from .mcp_adapter import MCPServer
import os


app = FastAPI(title="MCP Docs Server")
BASE = Path(__file__).parent / "docs"


mcp = MCPServer(base_docs=BASE)


@app.get("/health")
def health():
    return {"ok": True}


# simple HTTP tool endpoint (for demo & non-MCP clients)
@app.get("/tool/list")
def list_docs():
    files = [p.name for p in BASE.glob("**/*") if p.is_file()]
    return {"docs": files}


@app.get("/tool/get/{name}")
def get_doc(name: str):
    target = BASE / name
    if not target.exists():
        raise HTTPException(status_code=404, detail="doc not found")
    return FileResponse(str(target))


# start MCP server (if environment supports fastmcp)
@app.on_event("startup")
def startup_event():
    mcp.start()
