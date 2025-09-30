import os
from typing import List, Dict

from dotenv import load_dotenv

# optional imports
try:
    import pinecone
except Exception:
    pinecone = None

try:
    import openai
except Exception:
    openai = None

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENV")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

index_name = os.getenv("PINECONE_INDEX", "runtribe-index")


def load_env():
    return {
        "pinecone_api_key": PINECONE_API_KEY,
        "pinecone_env": PINECONE_ENV,
        "openai_api_key": OPENAI_API_KEY,
    }


def upsert_embeddings(docs: List[str], source: str = "local") -> Dict:
    """Create embeddings and upsert to Pinecone. If Pinecone/OpenAI keys missing, run in mock mode."""
    if not OPENAI_API_KEY or not PINECONE_API_KEY or pinecone is None or openai is None:
        # mock
        ids = [f"mock-{i}" for i in range(len(docs))]
        return {"ids": ids}

    openai.api_key = OPENAI_API_KEY
    pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)
    idx = pinecone.Index(index_name)
    vectors = []
    for i, d in enumerate(docs):
        emb = openai.Embedding.create(input=d, model="text-embedding-3-small")["data"][0]["embedding"]
        meta = {"source": source, "text_snippet": d[:200]}
        vectors.append((f"doc-{i}", emb, meta))
    idx.upsert(vectors)
    return {"ids": [v[0] for v in vectors]}


def semantic_search(query: str, top_k: int = 4):
    if not OPENAI_API_KEY or not PINECONE_API_KEY or pinecone is None or openai is None:
        # mock hits
        return [{"id": "mock-1", "text": "This is mock context"}]
    openai.api_key = OPENAI_API_KEY
    qemb = openai.Embedding.create(input=query, model="text-embedding-3-small")["data"][0]["embedding"]
    pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENV)
    idx = pinecone.Index(index_name)
    res = idx.query(vector=qemb, top_k=top_k, include_metadata=True)
    hits = []
    for match in res.get("matches", []):
        hits.append({"id": match["id"], "score": match.get("score"), "text": match.get("metadata", {}).get("text_snippet")})
    return hits


def answer_from_llm(query: str, contexts: List[dict]):
    if not OPENAI_API_KEY or openai is None:
        return "(mock answer) add OPENAI_API_KEY to .env to get real answers"
    openai.api_key = OPENAI_API_KEY
    context_text = "\n---\n".join([c.get("text", c.get("text_snippet", "")) for c in contexts])
    prompt = f"You are an assistant. Use the following context to answer the question. Context:\n{context_text}\n\nQuestion: {query}\nAnswer concisely."
    resp = openai.ChatCompletion.create(model="gpt-4o-mini", messages=[{"role":"user","content":prompt}], max_tokens=300)
    return resp["choices"][0]["message"]["content"]