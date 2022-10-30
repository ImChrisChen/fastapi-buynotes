from pydantic import BaseModel


class CreateAccountType(BaseModel):
    amount_type: str
    type_zh_name: str
    type_en_name: str


class CreateAccountNote(BaseModel):
    remark: str
    amount: int
    type_id: int
    # type_id: Optional[int] = None
