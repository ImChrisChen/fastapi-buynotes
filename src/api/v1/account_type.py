from fastapi import APIRouter

from src.db.database import session
from src.db import models
from src.db.schemas.account_type import CreateAccountType, UpdateAccountType

router = APIRouter(
    tags=['帐单类型'],
    prefix='/account_type',
    responses={403: {"description": "Operation forbidden"}},
)


@router.get('/')
async def get_account_types():
    types = session.query(models.AccountType).all()
    session.close()
    return types


@router.get('/{type_id}')
async def get_account_type(type_id: int):
    item = session.query(models.AccountType).filter(models.AccountType.id == type_id)
    if item.first() is None:
        return {
            'code': -1,
            'msg': '数据不存在'
        }
        pass
    return item.first()


@router.post('/')
async def create_account_type(account_type: CreateAccountType):
    # NOTE created_at 会变成null, 在sql中写入则不会
    item = models.AccountType(**account_type.dict())
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


@router.put('/{type_id}')
async def update_account_type(type_id: int, account_type: UpdateAccountType):
    item = session.query(models.AccountType).filter(models.AccountType.id == type_id)

    if item.first() is None:
        return {
            'code': -1,
            'msg': '数据不存在'
        }

    d = account_type.dict()

    for k, v in d.copy().items():
        if v is None:
            del d[k]

    resp = item.update(d)
    session.commit()
    if resp is None:
        return {
            'code': -1,
            'msg': '更新失败,或者已经被更新过了'
        }
    return {
        'code': 0,
        'msg': '更新成功'
    }


@router.delete('/{type_id}')
async def delete_account_type(type_id: int):
    item = session.query(models.AccountType).filter(models.AccountType.id == type_id)
    print(item)
    if item.first() is None:
        return {
            'code': -1,
            'msg': '数据不存在'
        }
        pass
    res = item.delete()
    session.flush()
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
