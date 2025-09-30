import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

try:
    import openai
    openai.api_key = OPENAI_API_KEY
except Exception:
    openai = None

# Researcher: stub for web search
class Researcher:
    def run(self, query: str):
        # placeholder results
        return [
            f"Result snippet about {query} - source A",
            f"Result snippet about {query} - source B",
        ]

# Summarizer: uses OpenAI LLM
class Summarizer:
    def run(self, snippets):
        joined = "\n\n".join(snippets)
        if not openai:
            return "(mock summary) " + joined[:150]
        prompt = f"Summarize the following snippets concisely:\n\n{joined}\n\nSummary:"
        resp = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role":"user","content":prompt}],
            max_tokens=250
        )
        return resp["choices"][0]["message"]["content"]

# Planner: breaks summary into tasks
class Planner:
    def run(self, summary: str):
        tasks = [s.strip() for s in summary.split('.') if s.strip()]
        return [f"Task: {t}" for t in tasks]
