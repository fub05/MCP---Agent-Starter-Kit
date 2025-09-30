from fastapi import APIRouter, UploadFile, File, Form
from .utils import load_env, upsert_embeddings


router = APIRouter()


env = load_env()


@router.post("/file")
async def ingest_file(file: UploadFile = File(...), source: str = Form("web_upload")):
    content = await file.read()
    text = content.decode(errors="ignore")
    # naive splitter
    docs = [p.strip() for p in text.split('\n\n') if p.strip()]
    resp = upsert_embeddings(docs, source=source)
    return {"inserted": len(resp.get("ids", [])), "status": "ok"}