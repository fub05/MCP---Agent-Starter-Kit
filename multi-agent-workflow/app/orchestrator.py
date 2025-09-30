from fastapi import FastAPI
from pydantic import BaseModel
from app.agents import Researcher, Summarizer, Planner

app = FastAPI(title="Multi-Agent Workflow")

researcher = Researcher()
summarizer = Summarizer()
planner = Planner()

class Query(BaseModel):
    q: str

@app.post("/run")
def run(query: Query):
    q = query.q
    # Step 1: Research
    results = researcher.run(q)
    # Step 2: Summarize
    summary = summarizer.run(results)
    # Step 3: Plan tasks
    tasks = planner.run(summary)
    return {
        "query": q,
        "results": results,
        "summary": summary,
        "tasks": tasks
    }

@app.get("/")
def health():
    return {"ok": True}
