from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.db.database import get_db_session
from src.db.schemas.account_type import CreateAccountType, UpdateAccountType
from src.db.models import AccountType

router = APIRouter(
    tags=['帐单类型'],
    prefix='/account_type',
    responses={403: {"description": "Operation forbidden"}},
)

@router.get('/')
async def get_account_types(session: Session = Depends(get_db_session)):
    items = session.query(AccountType).all()
    session.close()
    return items


@router.get('/{type_id}')
async def get_account_type(
        type_id: int,
        session: Session = Depends(get_db_session)
):
    item = session.query(AccountType).filter(AccountType.id == type_id)
    if item.first() is None:
        return {
            'code': -1,
            'msg': '数据不存在'
        }
    return item.first()


@router.post('/')
async def create_account_type(
        account_type: CreateAccountType,
        session: Session = Depends(get_db_session)
):
    session.begin()
    d = account_type.dict()
    item = AccountType(**d)
    session.add(item)
    session.commit()
    session.refresh(item)  # 内存更新,然后返回,不然为{}
    return {
        'code': 0,
        'data': item,
        'msg': '创建成功'
    }


@router.put('/{type_id}')
async def update_account_type(
        type_id: int,
        account_type: UpdateAccountType,
        session: Session = Depends(get_db_session)
):
    item = session.query(AccountType).filter(AccountType.id == type_id)

    if item.first() is None:
        return {
            'code': -1,
            'msg': '数据不存在'
        }

    d = account_type.dict()

    for k, v in d.copy().items():
        if v is None:
            del d[k]

    session.begin()
    resp = item.update(d)
    session.commit()

    if resp is None:
        return {
            'code': -1,
            'msg': '更新失败,或者已经被更新过了'
        }
    return {
        'code': 0,
        'data': item.one(),
        'msg': '更新成功'
    }


@router.delete('/{type_id}')
async def delete_account_type(
        type_id: int,
        session: Session = Depends(get_db_session)
):
    item = session.query(AccountType).filter(AccountType.id == type_id)
    if item.first() is None:
        return {
            'code': -1,
            'msg': '数据不存在'
        }
        pass
    session.begin()
    res = item.delete()
    session.commit()
    if not res:
        return {
            'code': -1,
            'msg': '删除失败'
        }
    return {
        'code': 0,
        'msg': '删除成功'
    }
