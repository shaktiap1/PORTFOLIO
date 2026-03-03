from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
import random

from backend.routers import projects, blogs, experience, achievements, community

app = FastAPI(
    title="Shaktesh Pandey — Portfolio API",
    description="Production-grade FastAPI backend powering the portfolio of Shaktesh Pandey — AI/ML Engineer.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(projects.router)
app.include_router(blogs.router)
app.include_router(experience.router)
app.include_router(achievements.router)
app.include_router(community.router)

@app.get("/", tags=["Root"])
def root():
    return {
        "service": "Shaktesh Pandey Portfolio API",
        "version": "1.0.0",
        "status": "online",
        "docs": "/docs",
    }

@app.get("/api/health", tags=["Health"])
def health_check():
    return {"status": "healthy", "message": "All systems operational."}

class InferenceRequest(BaseModel):
    query: str
    mode: Optional[str] = "semantic"
    top_k: Optional[int] = 5

class InferenceResponse(BaseModel):
    query: str
    mode: str
    results: list
    latency_ms: float
    cache_hit: bool
    model: str

@app.post("/api/ml/inference", response_model=InferenceResponse, tags=["ML Demo"])
def mock_inference(request: InferenceRequest):
    """
    Mock multimodal inference endpoint demonstrating:
    - Semantic search simulation
    - Redis-style cache-hit logic
    - Latency benchmarking
    Production equivalent: FAISS ANN search + embedding model + Redis semantic cache.
    """
    mock_results = [
        {"id": i + 1, "score": round(random.uniform(0.72, 0.99), 4), "text": f"Result chunk {i+1} for: '{request.query}'"}
        for i in range(request.top_k)
    ]
    cache_hit = random.random() > 0.6
    latency = round(random.uniform(4.2, 12.8) if cache_hit else random.uniform(28.0, 95.0), 2)

    return InferenceResponse(
        query=request.query,
        mode=request.mode,
        results=sorted(mock_results, key=lambda x: x["score"], reverse=True),
        latency_ms=latency,
        cache_hit=cache_hit,
        model="text-embedding-3-small (mock)",
    )
