from fastapi import APIRouter
from backend.data.achievements_data import achievements

router = APIRouter(prefix="/api/achievements", tags=["Achievements"])


@router.get("/")
def get_achievements():
    return {"status": "success", "count": len(achievements), "data": achievements}