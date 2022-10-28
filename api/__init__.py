from fastapi import APIRouter

from api import v1

router = APIRouter(prefix='/api', tags=['API'])
router.include_router(v1.router)


@router.get("/")
async def root():
    return {
        "msg": "api",
        'code': 0
    }
