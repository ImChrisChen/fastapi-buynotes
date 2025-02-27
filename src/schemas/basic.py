from enum import Enum
from typing import Any


class ApiCodeEnum(Enum):
    """状态码枚举类"""

    OK = (0, '成功')
    ERROR = (-1, '错误')

    DATA_NOT_EXIST = (10010, '数据不存在')
    DATA_EXIST = (10020, '数据已存在')

    SERVER_ERR = (500, '服务器异常')

    IMAGE_CODE_ERR = (4001, '图形验证码错误')
    THROTTLING_ERR = (4002, '访问过于频繁')
    NECESSARY_PARAM_ERR = (4003, '缺少必传参数')
    USER_ERR = (4004, '用户名错误')
    PWD_ERR = (4005, '密码错误')
    CPWD_ERR = (4006, '密码不一致')
    MOBILE_ERR = (4007, '手机号错误')
    SMS_CODE_ERR = (4008, '短信验证码有误')
    ALLOW_ERR = (4009, '未勾选协议')
    SESSION_ERR = (4010, '用户未登录')

    DB_ERR = (5000, '数据错误')
    EMAIL_ERR = (5001, '邮箱错误')
    TEL_ERR = (5002, '固定电话错误')
    NODATA_ERR = (5003, '无数据')
    NEW_PWD_ERR = (5004, '新密码错误')
    OPENID_ERR = (5005, '无效的openid')
    PARAM_ERR = (5006, '参数错误')
    STOCK_ERR = (5007, '库存不足')

    @property
    def code(self):
        """获取状态码"""
        return self.value[0]

    @property
    def errmsg(self):
        """获取状态码信息"""
        return self.value[1]


class ApiResponseModel:
    code: int
    msg: str
    data: Any = {}

    def __init__(self, status: ApiCodeEnum, data=None, message=None):
        code, msg = status.value

        if data is None:
            data = {}

        if message is not None:
            msg = message

        self.code = code
        self.data = data
        self.msg = msg
