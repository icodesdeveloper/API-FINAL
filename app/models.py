from sqlalchemy import create_engine, Column, Integer, String, Date, Boolean


# Model voor alle evenementen
from database import Base
class Event(Base):
    # Model wordt in tabel 'events' opgeslagen
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(25), index=True)
    city = Column(String(25), index=True)
    startdate = Column(Date, index=True)
    enddate = Column(Date, index=True)
    isPaid = Column(Boolean, index=True)


# Model voor alle gebruikers
class User(Base):
    # Model wordt in tabel 'users' opgeslagen
    __tablename__ = 'users'
    id=Column(Integer, primary_key=True, index=True)
    email=Column(String(128), index=True)
    hashed_password=Column(String, index=True)
