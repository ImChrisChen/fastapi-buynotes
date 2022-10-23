from datetime import datetime

from pydantic import BaseModel

from db.database import session

from fastapi import APIRouter
from typing import Optional

from db import models

router = APIRouter(tags=['帐单记录表'])


@router.get("/account_notes")
async def get_account_notes():
    res = session.query(models.AccountNote).all()
    return res


@router.get("/account_note/{note_id}")
async def get_account_note(note_id: int):
    res = session.query(models.AccountNote).filter(models.AccountNote.id == note_id).one()
    print(res)
    return None


class CreateAccountType(BaseModel):
    amount_type: str
    type_zh_name: str
    type_en_name: str


class CreateAccountNote(BaseModel):
    remark: str
    amount: int
    # type_id: Optional[int] = None


@router.post("/account_note")
async def create_account_note(note: CreateAccountNote):
    # print(note)
    # return note
    note_item = models.AccountNote(**note.dict())
    session.add(note_item)
    session.commit()
    session.refresh()
    return note_item
