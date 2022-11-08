from enum import Enum
from typing import Any

from pydantic import BaseModel, Field, dataclasses


class CodeEnum(int, Enum):
    SUCCESS = 0
    FAIL = -1


class ResponseBasic(BaseModel):
    code: CodeEnum = Field(default=CodeEnum.SUCCESS, description="业务状态码")
    data: Any = Field(default=dict(), description="数据结果")
    msg: str = Field(default='ok', description='提示信息')


class ResponseOK(ResponseBasic):
    pass


class ResponseToken(ResponseOK):
    pass


class ResponseError(ResponseBasic):
    pass
