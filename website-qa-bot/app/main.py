from fastapi import FastAPI
from app.ingest import router as ingest_router
from app.query import router as query_router


app = FastAPI(title="Website Q/A Bot")


app.include_router(ingest_router, prefix="/ingest")
app.include_router(query_router, prefix="/query")


@app.get("/")
def root():
    return {"status": "ok", "service": "website-qa-bot"}