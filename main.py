# main.py
# FastAPI backend that calls a real LLM (OpenAI by default, optional Groq)

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import os
from dotenv import load_dotenv, find_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

# ---- Load environment (.env) ----
_ = load_dotenv(find_dotenv())

app = FastAPI(title="FastAPI + LLM Demo")

# ---- Pydantic schema for /chat ----
class ChatRequest(BaseModel):
    message: str
    thread_id: Optional[str] = None  # not used here, but kept for future memory

# ---- Lazy model factory (OpenAI by default, optional Groq) ----
_chat_model = None

def get_model():
    """Create a singleton chat model. Uses OpenAI by default, Groq if LLM_PROVIDER=groq."""
    global _chat_model
    if _chat_model is not None:
        return _chat_model

    provider = os.getenv("LLM_PROVIDER", "openai").lower()

    if provider == "groq":
        # Requires: langchain-groq and GROQ_API_KEY
        from langchain_groq import ChatGroq
        model_name = os.getenv("GROQ_MODEL", "llama-3.1-70b-versatile")
        _chat_model = ChatGroq(model=model_name)
    else:
        # OpenAI (default). Requires: OPENAI_API_KEY
        model_name = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        _chat_model = ChatOpenAI(model=model_name)

    return _chat_model


# ---- Simple health endpoint ----
@app.get("/hello")
def say_hello(name: str = "World"):
    return {"message": f"Hello, {name}!"}


# ---- POST /chat: calls the LLM ----
@app.post("/chat")
async def chat(req: ChatRequest):
    """
    Minimal chat endpoint:
    - Builds a short system instruction.
    - Sends user's message to the LLM.
    - Returns the model's text content.
    """
    model = get_model()
    messages = [
        SystemMessage(content="You are a helpful and concise assistant."),
        HumanMessage(content=req.message),
    ]
    try:
        # Async for better throughput; you can use .invoke() if you prefer sync
        resp = await model.ainvoke(messages)
        return {"reply": resp.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM error: {e}")