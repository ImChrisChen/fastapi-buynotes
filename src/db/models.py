from src.db.database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey, text
from sqlalchemy.orm import relationship


class AccountType(Base):
    __tablename__ = 'account_type'
    id = Column(Integer, primary_key=True, index=True)
    amount_type = Column(String)
    type_zh_name = Column(String)
    type_en_name = Column(String)

    # 默认时间
    created_at = Column(TIMESTAMP, nullable=True, server_default=text('CURRENT_TIMESTAMP'))
    updated_at = Column(TIMESTAMP, nullable=True, server_default=text('CURRENT_TIMESTAMP'))

    # notes 要关联数据表的back_populates的值一样
    notes = relationship('AccountNote', back_populates="type")


class AccountNote(Base):
    __tablename__ = 'account_note'

    id = Column(Integer, primary_key=True, index=True)
    remark = Column(String, index=True)
    amount = Column(Integer)
    created_at = Column(TIMESTAMP, nullable=True, server_default=text('CURRENT_TIMESTAMP'))
    updated_at = Column(TIMESTAMP, nullable=True, server_default=text('CURRENT_TIMESTAMP'))

    type_id = Column(Integer, ForeignKey('account_type.id'))

    # type 要关联数据表的back_populates的值一样
    type = relationship('AccountType', back_populates="notes")


class Budget(Base):
    __tablename__ = 'budget'

    id = Column(Integer, primary_key=True, index=True)
    zh_name = Column(String)
    en_name = Column(String)
    date_type_zh = Column(String)
    date_type_en = Column(String)
    created_at = Column(TIMESTAMP, nullable=True, server_default=text('CURRENT_TIMESTAMP'))
    updated_at = Column(TIMESTAMP, nullable=True, server_default=text('CURRENT_TIMESTAMP'))
