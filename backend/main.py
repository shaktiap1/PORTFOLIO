from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Shaktesh Pandey – Portfolio API",
    description="Production-grade REST API powering the portfolio of Shaktesh Pandey, AI/ML Engineer.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from backend.routers import projects as projects_router
from backend.routers import blogs as blogs_router
from backend.routers import experience as experience_router
from backend.routers import achievements as achievements_router

app.include_router(projects_router.router)
app.include_router(blogs_router.router)
app.include_router(experience_router.router)
app.include_router(achievements_router.router)

@app.get("/")
def root():
    return {"message": "Shaktesh Pandey Portfolio API", "status": "live", "docs": "/docs"}

@app.get("/api/health")
def health():
    return {"status": "healthy", "version": "1.0.0"}

@app.post("/api/ml/inference")
def mock_inference(payload: dict):
    query = payload.get("query", "")
    return {
        "status": "success",
        "query": query,
        "result": {
            "top_match": "Enterprise RAG System",
            "confidence": 0.94,
            "latency_ms": 12,
            "cache_hit": False,
            "note": "In production, semantic cache reduces this to ~2ms on repeated queries.",
        },
    }
