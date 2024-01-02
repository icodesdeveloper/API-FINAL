import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# Fixed some errors cuzz okteto being hard
if not os.path.exists('./sqlitedb'):
    os.makedirs('./sqlitedb')

# Make connection to DB
SQLALCHEMY_DATABASE_URL = "sqlite:///./sqlitedb/sqlitedata.db"



# Create db engine and session
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Define the base we use for commuinication with the db
Base = sqlalchemy.orm.declarative_base()