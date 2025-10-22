from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from datetime import timedelta
from api.utils.auth import create_token
from api.schemas.auth import UserCreate, Token
from api.crud.user import create_user, get_user
from dotenv import load_dotenv
from api.dependencies import get_session
import os

load_dotenv()
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
REFRESH_TOKEN_EXPIRE_MINUTES = int(os.getenv("REFRESH_TOKEN_EXPIRE_MINUTES"))


router = APIRouter()


@router.post("/signup/", status_code=201)
async def signup(*, session: Session = Depends(get_session), user_form: UserCreate):
    user = get_user(session, user_form.email)
    if user:
        return {"message": "already exists"}
        raise HTTPException(status_code=200, detail="Already exists")
    user = create_user(session, user_form)
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    refresh_token_expires = timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    access_token = create_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    refresh_token = create_token(
        data={"sub": user.email}, expires_delta=refresh_token_expires
    )
    return Token(
        access_token=access_token, refresh_token=refresh_token, token_type="bearer"
    )
