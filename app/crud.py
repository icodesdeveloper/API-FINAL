
from sqlalchemy.orm import Session
from datetime import datetime

import models
import schemas
import auth

from fastapi import HTTPException
def get_events(db: Session):
    return db.query(models.Event).all()

def get_event_by_id(db: Session, event_id: int):
    event = db.query(models.Event).filter(models.Event.id == event_id).first()
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return event

# Return all events in specific city
def get_events_by_city(db: Session, city: str):
    events = db.query(models.Event).filter(models.Event.city == city).all()
    if events is None:
        raise HTTPException(status_code=404, detail="No events found in this city")
    return events




def add_event(db: Session, event: schemas.EventCreate):
    new_event = models.Event(name=event.name, city=event.city, isPaid=event.isPaid, startdate=event.startdate, enddate=event.enddate)
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return new_event

def update_event(db: Session, event_id: int, event: schemas.EventCreate):
    existing_event = db.query(models.Event).filter(models.Event.id == event_id).first()
    if existing_event is None:
        raise HTTPException(status_code=404, detail="Event not found")

    existing_event.name = event.name
    existing_event.city = event.city
    existing_event.startdate = event.startdate
    existing_event.enddate = event.enddate
    existing_event.isPaid = event.isPaid

    db.commit()
    db.refresh(existing_event)

    return existing_event

def delete_event(db: Session, event_id: int):
    existing_event = db.query(models.Event).filter(models.Event.id == event_id).first()
    if existing_event is None:
        raise HTTPException(status_code=404, detail="Event not found")

    db.delete(existing_event)
    db.commit()

    return {"message": "Event deleted successfully"}



# User CRUD
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    new_user = models.User(email=user.email, hashed_password=auth.get_password_hash(user.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


