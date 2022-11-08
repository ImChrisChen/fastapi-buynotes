from fastapi import APIRouter

from src.api import v1
from src.config.config import settings

router = APIRouter(prefix=settings.API_V1_STR)
router.include_router(v1.router)


@router.get("/")
async def root():
    return {
        "msg": "api",
        'code': 0
    }
