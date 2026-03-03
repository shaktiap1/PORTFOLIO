from fastapi import APIRouter

router = APIRouter(prefix="/api/projects", tags=["Projects"])

projects = [
    {
        "id": 1,
        "title": "Enterprise RAG System",
        "category": "LLM / RAG",
        "summary": "Production-grade Retrieval-Augmented Generation pipeline with 30% improvement in search relevance.",
        "impact": "+30% search relevance",
        "stack": ["LangChain", "FAISS", "FastAPI", "Redis", "Weaviate", "Python"],
        "details": [
            "Designed chunking strategy with sliding-window + semantic boundary detection.",
            "Implemented hybrid dense-sparse retrieval (BM25 + vector ANN).",
            "Deployed re-ranking with cross-encoder models reducing hallucination rate.",
            "Integrated Redis semantic caching layer — 40% cache hit rate, saving ~60% LLM token costs.",
        ],
        "metrics": {"relevance_improvement": "30%", "cache_hit_rate": "40%", "token_cost_reduction": "60%"},
    },
    {
        "id": 2,
        "title": "Vector Database Optimization",
        "category": "MLOps / Infra",
        "summary": "Advanced vector compression strategies reducing FAISS memory footprint by 70%.",
        "impact": "-70% memory usage",
        "stack": ["FAISS", "Product Quantization", "HNSW", "Python", "NumPy"],
        "details": [
            "Benchmarked IVF-PQ vs HNSW vs Flat index across recall@10, QPS, and RAM.",
            "Applied Product Quantization (PQ-64) achieving 70% memory reduction with <2% recall drop.",
            "Automated index rebuild triggers via MLflow pipeline on data drift detection.",
        ],
        "metrics": {"memory_reduction": "70%", "recall_drop": "<2%"},
    },
    {
        "id": 3,
        "title": "Multimodal Inference Engine",
        "category": "ML Systems",
        "summary": "End-to-end multimodal API with semantic search and caching, reducing p95 latency by 40%.",
        "impact": "-40% latency",
        "stack": ["FastAPI", "Redis", "CLIP", "Docker", "Kubernetes", "GCP"],
        "details": [
            "Implemented image+text embedding fusion for cross-modal semantic search.",
            "Built async FastAPI endpoints with batch inference support.",
            "Deployed Redis-based semantic cache — eliminates redundant model calls.",
            "Containerised with Docker, orchestrated on GKE with horizontal pod autoscaling.",
        ],
        "metrics": {"latency_reduction": "40%", "throughput_gain": "3x"},
    },
    {
        "id": 4,
        "title": "MLOps & Vectorized ETL Pipeline",
        "category": "Data Engineering / MLOps",
        "summary": "Vectorized ETL enabling 100x faster data ingestion + automated retraining improving model stability by 15-20%.",
        "impact": "100x faster ingestion",
        "stack": ["Apache Kafka", "Python", "MLflow", "Pandas", "NumPy", "GCP", "Airflow"],
        "details": [
            "Replaced row-wise pandas iteration with vectorized NumPy ops — 100x ingestion speedup.",
            "Built streaming pipeline on Kafka for real-time feature ingestion.",
            "Designed automated retraining trigger on data drift (KL divergence monitoring).",
            "Tracked experiments and model registry with MLflow — full lineage and reproducibility.",
            "Improved model stability by 15-20% through automated retraining cadence.",
        ],
        "metrics": {"ingestion_speedup": "100x", "stability_improvement": "15-20%"},
    },
]

@router.get("/")
def get_projects():
    return {"status": "success", "count": len(projects), "data": projects}

@router.get("/{project_id}")
def get_project(project_id: int):
    project = next((p for p in projects if p["id"] == project_id), None)
    if not project:
        return {"status": "error", "message": f"Project {project_id} not found."}
    return {"status": "success", "data": project}