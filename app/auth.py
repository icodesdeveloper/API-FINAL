from passlib.context import CryptContext
from datetime import datetime, timedelta
import crud
from jose import JWTError, jwt
from sqlalchemy.orm import Session


# Variable voor JWT
SECRET_KEY = "62db0aac848d4c6ebb5e4ef18eb53687935d1e584735c15cfb73b9deff4618cc"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


pwd_context = CryptContext(schemes=["argon2", "bcrypt"], deprecated="auto")



# Functie hash wachtwoord
def get_password_hash(password):
    return pwd_context.hash(password)
# Functie om wachtwoord te verifiëren
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
# Functie om gebruiker te authenticeren
def authenticate_user(db: Session, username: str, password: str):
    user = crud.get_user_by_email(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

# Functie om JWT token te maken
def create_access_token(data: dict):
    to_encode = data.copy()
    expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        # Default to 15 minutes of expiration time if ACCESS_TOKEN_EXPIRE_MINUTES variable is empty
        expire = datetime.utcnow() + timedelta(minutes=15)
    # Adding the JWT expiration time case
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

