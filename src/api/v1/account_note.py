from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.schemas.basic import ApiCodeEnum,ApiResponseModel

from src.db.database import get_db_session
from src.db.models import AccountNote
from src.db.schemas.account_note import CreateAccountNote

router = APIRouter(
    tags=['帐单记录'],
    prefix='/account_note',
)


@router.get("/")
async def get_account_notes(session: Session = Depends(get_db_session)):
    notes = session.query(AccountNote).all()
    return notes


@router.get("/{note_id}")
async def get_account_note(
        note_id: int,
        session: Session = Depends(get_db_session)
):
    note = session.query(AccountNote).filter(AccountNote.id == note_id).limit(1)
    if note.first() is None:
        return {
            'code': -1,
            'data': {},
            'msg': '数据不存在'
        }
    return note.first()


@router.post("/")
async def create_account_note(
        account_note: CreateAccountNote,
        session: Session = Depends(get_db_session)
):
    try:
        session.begin()
        d = account_note.dict()
        item = AccountNote(**d)
        session.add(item)
        session.commit()
        session.refresh(item)
        return {
            'code': 0,
            'data': item,
            'msg': '创建成功'
        }
    except BaseException as e:
        session.rollback()
        print(e)
        # raise HTTPException(status_code=500, detail=e)
        return {
            'code': -1,
            'data': e,
            'msg': '数据插入失败'
        }


# TODO 这里还有个问题
@router.put('/{note_id}')
async def update_account_note(
        note_id,
        account_note: CreateAccountNote,
        session: Session = Depends(get_db_session)
):
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

    try:
        session.begin()
        resp = note.update(d)
        session.commit()
        if resp is None:
            return {
                'code': -1,
                'msg': '更新失败,或者已经被更新过了'
            }
    except BaseException as e:
        session.rollback()
        print(e)
        return dict(code=-1, msg='更新异常')

    return {
        'code': 0,
        'data': note.one(),
        'msg': '更新成功'
    }


@router.delete('/{note_id}')
async def delete_account_note(
        note_id,
        session: Session = Depends(get_db_session)
):
    item = session.query(AccountNote).filter(AccountNote.id == note_id)
    if item.first() is None:
        return dict(
            code=-1,
            msg='数据不存在'
        )

    try:
        session.begin()
        res = item.delete()
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
        session.rollback()
        return dict(
            code=-1,
            data=e,
            msg='error'
        )
