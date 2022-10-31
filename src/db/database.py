from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# https://fastapi.tiangolo.com/zh/tutorial/sql-databases/#orms

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine("mysql://root:rootadmin@chrisorz.tpddns.cn:3306/buy_notes", echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# sqlalchemy modulenotfounderror: no module named 'mysqldb'问题
# https://stackoverflow.com/questions/14087598/python-3-importerror-no-module-named-configparser

Base = declarative_base()

session = SessionLocal()


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
