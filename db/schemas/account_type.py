from pydantic import BaseModel
from typing import Optional
from enum import Enum


class AmountType(str, Enum):
    Negative = "0"
    Positive = "1"


class CreateAccountType(BaseModel):
    amount_type: AmountType
    type_zh_name: str
    type_en_name: Optional[str]


class UpdateAccountType(BaseModel):
    amount_type: Optional[AmountType]
    type_zh_name: Optional[str]
    type_en_name: Optional[str]
