from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# Creëer een engine om verbinding te maken met de SQLite-database (in dit geval)
# SQLALCHEMY_DATABASE_URL = "sqlite:///db/books.db"
SQLALCHEMY_DATABASE_URL = "sqlite:///./sqlitedb/sqlitedata.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
