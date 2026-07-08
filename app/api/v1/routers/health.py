from datetime import datetime

from fastapi import APIRouter

router = APIRouter(
    prefix="/health",
    tags=["Health"]
)


@router.get("/")
async def health():

    return {
        "status": "Healthy",
        "service": "Enterprise FastAPI",
        "timestamp": datetime.utcnow()
    }


@router.get("/ping")
async def ping():

    return {
        "message": "pong"
    }