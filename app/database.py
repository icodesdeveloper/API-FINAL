from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql

# Creëer een engine om verbinding te maken met de SQLite-database (in dit geval)
# SQLALCHEMY_DATABASE_URL = "sqlite:///db/books.db"
SQLALCHEMY_DATABASE_URL = "sqlite:///../db/events.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Maak een sessiemaker voor het beheren van de sessies met de database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Maak een Base-klasse voor declaratieve class mapping
Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
