from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="pai‑6 — Operational AI (Render Edition v1.17)", version="1.17.0")

# CORS (adjust as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simple health
@app.get("/health")
def health():
    return {"ok": True, "version": "1.17.0"}

# Example API
class Echo(BaseModel):
    message: str
    meta: Optional[dict] = None

@app.post("/api/echo")
def echo(body: Echo):
    return {"echo": body.message, "meta": body.meta}

# Serve static frontend from /frontend folder
app.mount("/", StaticFiles(directory="frontend", html=True), name="static")
