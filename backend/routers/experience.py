from fastapi import APIRouter
from backend.data.experience_data import experience

router = APIRouter(prefix="/api/experience", tags=["Experience"])


@router.get("/")
def get_experience():
    return {"status": "success", "count": len(experience), "data": experience}