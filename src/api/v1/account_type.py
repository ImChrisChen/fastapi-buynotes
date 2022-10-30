from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder

from src.db.database import session
from src.db.schemas.account_type import CreateAccountType, UpdateAccountType
from src.db.models import AccountType

router = APIRouter(
    tags=['帐单类型'],
    prefix='/account_type',
    responses={403: {"description": "Operation forbidden"}},
)


@router.get('/')
async def get_account_types():
    items = session.query(AccountType).all()
    session.close()
    return items


@router.get('/{type_id}')
async def get_account_type(type_id: int):
    item = session.query(AccountType).filter(AccountType.id == type_id)
    if item.first() is None:
        return {
            'code': -1,
            'msg': '数据不存在'
        }
    return item.first()


@router.post('/')
async def create_account_type(account_type: CreateAccountType):
    # NOTE created_at 会变成null, 在sql中写入则不会
    item = AccountType(**account_type.dict())
    session.add(item)
    session.commit()
    session.refresh(item)      # 内存更新,然后返回,不然为{}
    return {
        'code': 0,
        'data': item,
        'msg': '创建成功'
    }


@router.put('/{type_id}')
async def update_account_type(type_id: int, account_type: UpdateAccountType):
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
    item = session.query(AccountType).filter(AccountType.id == type_id)
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
