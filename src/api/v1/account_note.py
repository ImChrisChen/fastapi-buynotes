from pydantic import BaseModel

from fastapi import APIRouter,Body

from src.db.models import AccountNote
from src.db.database import session
from src.db.schemas.account_note import CreateAccountNote

router = APIRouter(
    tags=['帐单记录'],
    prefix='/account_note'
)


@router.get("/")
async def get_account_notes():
    notes = session.query(AccountNote).all()
    session.close()
    return notes


@router.get("/{note_id}")
async def get_account_note(note_id: int):
    note = session.query(AccountNote).filter(AccountNote.id == note_id).limit(1)
    if note.first() is None:
        return {
            'code': -1,
            'data': {},
            'msg': '数据不存在'
        }
    return note.first()


@router.post("/")
async def create_account_note(note: CreateAccountNote):
    note = AccountNote(**note.dict())
    session.add(note)
    session.commit()
    session.refresh(note)
    return {
        'code': 0,
        'data': note,
        'msg': '创建成功'
    }
