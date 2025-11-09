from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from datetime import timedelta
from api.utils.auth import create_token
from api.schemas.auth import UserCreate, Token, UserInDB, UserLogin, RoleCreate
from api.crud.employee import (
    create_user,
    get_user,
    check_user_password,
    find_supervisor_by_email,
)
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
        raise HTTPException(status_code=400, detail="Пользователь уже существует")

    if user_form.role == RoleCreate.EMPLOYEE and not user_form.supervisor_email:
        raise HTTPException(
            status_code=400, detail="Сотрудник должен иметь руководителя"
        )

    if user_form.role == RoleCreate.SUPERVISOR:
        supervisor_id = None
    else:
        supervisor_id = find_supervisor_by_email(session, user_form.supervisor_email)
        if not supervisor_id and user_form.role == RoleCreate.EMPLOYEE:
            raise HTTPException(
                status_code=400, detail="Руководитель с таким email не найден"
            )

    user = create_user(session, user_form, supervisor_id=supervisor_id)
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


@router.post("/signin/", status_code=200)
async def signin(*, session: Session = Depends(get_session), user_form: UserLogin):
    user = get_user(session, user_form.email)
    if not user:
        raise HTTPException(status_code=401, detail="Неверная почта или пароль")

    status = check_user_password(session, user_form.email, user_form.password)

    if not status:
        raise HTTPException(status_code=401, detail="Неверная почта или пароль")

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
