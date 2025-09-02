from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI()

# Allow your React app to call FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class AskBody(BaseModel):
    query: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ask")
def ask(body: AskBody):
    try:
        r = requests.post(
            "http://127.0.0.1:11434/api/generate",
            json={"model": "llama3.1", "prompt": body.query, "stream": False},
            timeout=45
        )
        r.raise_for_status()
        data = r.json()
        if "error" in data:
            return {"error": f"Ollama error: {data['error']}"}
        return {"answer": (data.get('response') or '').strip()}
    except Exception as e:
        return {"error": str(e)}
