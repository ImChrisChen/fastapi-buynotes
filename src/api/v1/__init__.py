from fastapi import APIRouter, Request
from . import account_type, user, account_note

router = APIRouter(prefix='/v1')

router.include_router(account_type.router)
router.include_router(account_note.router)
router.include_router(user.router)


@router.get("/")
async def v1_get(request: Request):
    return {
        'code': 0,
        'msg': 'v1'
    }
