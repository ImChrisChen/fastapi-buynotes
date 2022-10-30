from src.db.database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship


class AccountType(Base):
    __tablename__ = 'account_type'
    id = Column(Integer, primary_key=True, index=True)
    amount_type = Column(String)
    type_zh_name = Column(String)
    type_en_name = Column(String)
    created_at = Column(TIMESTAMP)
    updated_at = Column(TIMESTAMP)

    # notes = relationship('AccountNote', back_populates="account_type")


class AccountNote(Base):
    __tablename__ = 'account_note'

    id = Column(Integer, primary_key=True, index=True)
    remark = Column(String, index=True)
    amount = Column(Integer)
    created_at = Column(TIMESTAMP, nullable=True)
    updated_at = Column(TIMESTAMP, nullable=True)

    type_id = Column(Integer, ForeignKey('account_type.id'))

    # type = relationship('AccountType', back_populates="account_note")


class Budget(Base):
    __tablename__ = 'budget'

    id = Column(Integer, primary_key=True, index=True)
    zh_name = Column(String)
    en_name = Column(String)
    date_type_zh = Column(String)
    date_type_en = Column(String)
    created_at = Column(TIMESTAMP, nullable=True)
    updated_at = Column(TIMESTAMP, nullable=True)
