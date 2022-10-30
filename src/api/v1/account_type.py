import pymysql
from fastapi import APIRouter

# from src.db.database import session
from src.db import models
from src.db.schemas.account_type import CreateAccountType, UpdateAccountType
from src.db.database import get_db, connection

router = APIRouter(
    tags=['帐单类型'],
    prefix='/account_type',
    responses={403: {"description": "Operation forbidden"}},
)


@router.get('/')
async def get_account_types():
    sql = 'select * from account_type limit 0,1000'
    cursor = connection.cursor()
    print(cursor.execute(sql))
    return cursor.fetchall()


@router.get('/{type_id}')
async def get_account_type(type_id: int):
    # item = session.query(models.AccountType).filter(models.AccountType.id == type_id)
    sql = f"select * from account_type where account_type.id={type_id} limit 1"
    cursor = connection.cursor()
    cursor.execute(sql)
    item = cursor.fetchone()
    if item is None:
        return {
            'code': -1,
            'msg': '数据不存在'
        }
        pass
    return item


@router.post('/')
async def create_account_type(account_type: CreateAccountType):
    # NOTE created_at 会变成null, 在sql中写入则不会
    # item = models.AccountType(**account_type.dict())
    # session.add(item)
    # session.commit()
    # session.refresh(item)
    # return item
    cursor = connection.cursor()
    sql = "insert into account_type(amount_type, type_zh_name, type_en_name) values (%s,%s,%s)"
    d = account_type.dict()
    values = tuple(d.values())
    res = cursor.execute(sql, values)
    if res == 0 or res is None:
        connection.rollback()
        return {
            'code': -1,
            'msg': '创建失败'
        }

    connection.commit()
    return {
        'code': 0,
        'msg': '创建成功'
    }


@router.put('/{type_id}')
async def update_account_type(type_id: int, account_type: UpdateAccountType):
    cursor = connection.cursor()
    sql = f"update account_type set amount_type = %s, type_zh_name = %s, type_en_name = %s where id={type_id}"
    values = account_type.dict().values()
    res = cursor.execute(sql, tuple(values))

    if res == 0 or res is None:
        connection.rollback()
        return {
            'code': -1,
            'msg': '更新失败'
        }

    connection.commit()
    return {
        'code': 0,
        'msg': '更新成功'
    }


    # item = session.query(models.AccountType).filter(models.AccountType.id == type_id)
    #
    # if item.first() is None:
    #     return {
    #         'code': -1,
    #         'msg': '数据不存在'
    #     }
    #
    # d = account_type.dict()
    #
    # for k, v in d.copy().items():
    #     if v is None:
    #         del d[k]
    #
    # resp = item.update(d)
    # session.commit()
    # if resp is None:
    #     return {
    #         'code': -1,
    #         'msg': '更新失败,或者已经被更新过了'
    #     }
    # return {
    #     'code': 0,
    #     'msg': '更新成功'
    # }
    pass


@router.delete('/{type_id}')
async def delete_account_type(type_id: int):
    cursor = connection.cursor()
    sql = f"delete from account_type where id={type_id}"
    res = cursor.execute(sql)

    if res == 0 or res is None:
        connection.rollback()
        return {
            'code': -1,
            'msg': '删除失败'
        }

    connection.commit()
    return {
        'code': 0,
        'msg': '删除成功'
    }

    # pass
    # item = session.query(models.AccountType).filter(models.AccountType.id == type_id)
    # print(item)
    # if item.first() is None:
    #     return {
    #         'code': -1,
    #         'msg': '数据不存在'
    #     }
    #     pass
    # res = item.delete()
    # session.flush()
    # session.commit()
    # if not res:
    #     return {
    #         'code': -1,
    #         'msg': '删除失败'
    #     }
    # return {
    #     'code': 0,
    #     'msg': '删除成功'
    # }
