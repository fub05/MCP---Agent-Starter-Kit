from fastapi import APIRouter
from pydantic import BaseModel
from .utils import semantic_search, answer_from_llm


router = APIRouter()


class QueryReq(BaseModel):
    q: str


@router.post("/ask")
def ask(req: QueryReq):
    # 1) semantic search against vectors
    hits = semantic_search(req.q, top_k=4)
    # 2) call LLM with context
    answer = answer_from_llm(req.q, hits)
    return {"answer": answer, "sources": hits}