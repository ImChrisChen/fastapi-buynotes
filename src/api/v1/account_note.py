import logging

from fastapi import APIRouter, HTTPException

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
    try:
        note = AccountNote(**note.dict())
        session.add(note)
        session.commit()
        session.refresh(note)
        return {
            'code': 0,
            'data': note,
            'msg': '创建成功'
        }
    except BaseException as e:
        print(e)
        logging.error('插入失败，回滚数据', e)
        session.rollback()
        # raise HTTPException(status_code=500, detail=e)
        return {
            'code': -1,
            'data': e,
            'msg': '数据插入失败'
        }


# TODO 这里还有个问题
@router.put('/{note_id}')
async def update_account_note(note_id, account_note: CreateAccountNote):
    note = session.query(AccountNote).filter(AccountNote.id == note_id)
    if note.first() is None:
        return dict(
            code=-1,
            msg='数据不存在'
        )
    d = account_note.dict()
    for k, v in d.copy().items():
        if v is None:
            del d[k]

    resp = note.update(d)
    session.commit()
    if resp is None:
        return {
            'code': -1,
            'msg': '更新失败,或者已经被更新过了'
        }

    return {
        'code': 0,
        'data': note.one(),
        'msg': '更新成功'
    }


@router.delete('/{note_id}')
async def delete_account_note(note_id):
    item = session.query(AccountNote).filter(AccountNote.id == note_id)
    if item.first() is None:
        return dict(
            code=-1,
            msg='数据不存在'
        )

    try:
        res = item.delete()
        session.flush()
        session.commit()

        if not res:
            return dict(
                code=-1,
                msg='删除失败'
            )
        return dict(
            code=0,
            msg='删除成功'
        )
    except BaseException as e:
        return dict(
            code=-1,
            data=e,
            msg='error'
        )
