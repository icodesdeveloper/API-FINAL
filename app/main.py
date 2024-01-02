from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from typing import List
import auth
import crud
import models
import schemas
import os

print("PRINT")
if not os.path.exists('./sqlitedb'):
    os.makedirs('./sqlitedb')

# Initialiseer database
models.Base.metadata.create_all(bind=engine)

# Initialiseer FastAPI
app = FastAPI()


# Beveiliging: CORS Regeling
origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://localhost.tiangolo.com",
    "http://127.0.0.1:5500"
    "*"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]

)



# Beveiliging: Authenticatie
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")




# Maak database sessie
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




# Get endpoints



# Endpoint om alle boeken op te halen
@app.get("/events/", response_model=list[schemas.Event])
async def get_all_events(db: Session = Depends(get_db)):
    return crud.get_events(db)

@app.get("/events/id/{event_id}", response_model=schemas.Event)
def get_event_by_id_endpoint(event_id: int, db: Session = Depends(get_db)):
    return crud.get_event_by_id(db, event_id)

@app.get("/events/city/{city}", response_model=list[schemas.Event])
async def get_all_events_by_city(city: str, db: Session = Depends(get_db)):
    return crud.get_events_by_city(db, city)




# Put endpoints
@app.put("/events/id/{event_id}", response_model=schemas.Event)
def update_event(event_id: int, event: schemas.EventCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return crud.update_event(db, event_id, event)





# Post endpoints
@app.post("/events/", response_model=schemas.Event)
def create_event(event: schemas.EventCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return crud.add_event(db, event)





# Delete endpoints
@app.delete("/events/id/{event_id}")
async def delete_existing_event(event_id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    return crud.delete_event(db, event_id)




# Oauth functies


#User endpoints
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Gebruiker met dit emailadres bestaat reeds")
    return crud.create_user(db=db, user=user)


@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Try to authenticate the user
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # Add the JWT case sub with the subject(user)
    access_token = auth.create_access_token(
        data={"sub": user.email}
    )

    # Return the JWT as a bearer token to be placed in the headers
    return {"access_token": access_token, "token_type": "bearer"}



