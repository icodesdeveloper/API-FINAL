from pydantic import BaseModel
from datetime import date

class EventBase(BaseModel):
    name: str
    city: str
    startdate: date
    enddate: date
    isPaid: bool


class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True


