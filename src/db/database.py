# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, Session
import MySQLdb.connections
import pymysql.cursors

connection = pymysql.connect(
    host='chrisorz.tpddns.cn',
    port=3306,
    user='root',
    password='rootadmin',
    database='buy_notes',
    cursorclass=pymysql.cursors.DictCursor,
)


async def get_db():
    # cursor: MySQLdb.connections.Connection
    cursor = connection.cursor()
    return cursor
    # try:
    #     yield cursor
    # finally:
    #     cursor.close()

# https://fastapi.tiangolo.com/zh/tutorial/sql-databases/#orms

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# engine = create_engine("mysql://root:rootadmin@chrisorz.tpddns.cn:3306/buy_notes")

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# sqlalchemy modulenotfounderror: no module named 'mysqldb'问题
# https://stackoverflow.com/questions/14087598/python-3-importerror-no-module-named-configparser

# Base = declarative_base()

# session = SessionLocal()


# def get_db() -> Session:
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
