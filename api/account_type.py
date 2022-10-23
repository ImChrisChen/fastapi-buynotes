from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
from enum import Enum

from db.database import session
from db import models

router = APIRouter(tags=['帐单类型'])


class AmountType(str, Enum):
    Negative = "0"
    Positive = "1"


class CreateAccountType(BaseModel):
    amount_type: AmountType
    type_zh_name: str
    type_en_name: Optional[str]


class UpdateAccountType(BaseModel):
    # amount_type: Optional[AmountType]
    # type_zh_name: Optional[str]
    # type_en_name: Optional[str]
    type_zh_name: str


@router.get('/account_types')
async def get_account_types():
    types = session.query(models.AccountType).all()
    session.close()
    return types


@router.get('/account_type/{type_id}')
async def get_account_type(type_id: int):
    t = session.get(models.AccountType, type_id)
    return t


@router.post('/account_type')
async def create_account_type(account_type: CreateAccountType):
    # NOTE created_at 会变成null, 在sql中写入则不会
    item = models.AccountType(**account_type.dict())
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


@router.put('/account_type/{type_id}')
async def update_account_type(type_id: int, account_type: UpdateAccountType):
    t = session.get(models.AccountType, type_id)
    return t
    # for k, v in account_type.dict().items():
    #     if k is not None and v is not None:
    #         t[k] = v
    #
    # session.flush()
    # session.commit()


@router.delete('/account_type/{type_id}')
async def delete_account_type(type_id: int):
    session.begin()
    # session.query(models.AccountType).filter(models.AccountType.id == type_id).delete()
    t = session.get(models.AccountType, type_id)
    if t is None:
        return {
            'code': -1,
            'msg': '数据不存在'
        }
    session.delete(t)
    session.commit()
    return t
