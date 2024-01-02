import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

print("PRINT")
if not os.path.exists('./sqlitedb'):
    os.makedirs('./sqlitedb')

SQLALCHEMY_DATABASE_URL = "sqlite:///./sqlitedb/sqlitedata.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = sqlalchemy.orm.declarative_base()