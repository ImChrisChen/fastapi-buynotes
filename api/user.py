from typing import List

from fastapi import APIRouter

router = APIRouter(tags=['用户相关'])


class User:
    def __init__(self, **kwargs):
        self.uid = kwargs.get('uid')
        self.age = kwargs.get('age')
        self.name = kwargs.get('name')

    uid: int
    age: int
    name: str


users: List[User] = [User(uid=index, name=f"Chris-{index}", age=18 + index) for index in range(0, 5)]


@router.get("/users")
async def getUsers():
    return users


@router.get("/user/{uid}")
async def getUser(uid: int):
    result = filter(lambda user: user.uid == uid, users)
    return list(result)

