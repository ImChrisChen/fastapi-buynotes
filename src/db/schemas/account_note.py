from pydantic import BaseModel


class CreateAccountType(BaseModel):
    amount_type: str
    type_zh_name: str
    type_en_name: str

    # class Config:
    #     orm_mode = True


class CreateAccountNote(BaseModel):
    remark: str
    amount: int
    type_id: int

    # class Config:
    #     orm_mode = True
