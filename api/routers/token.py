import os
from datetime import timedelta

from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException, status
import jwt

from api.schemas.auth import RefreshRequest
from api.utils.auth import create_token, decode_token

load_dotenv()
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
REFRESH_TOKEN_EXPIRE_MINUTES = int(os.getenv("REFRESH_TOKEN_EXPIRE_MINUTES"))

router = APIRouter()


@router.post("/refresh_token/")
async def refresh_token(request: RefreshRequest):
    decoded = decode_token(request.refresh_token)

    if decoded == jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Refresh токен просрочен"
        )
    elif decoded == jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Некорректный refresh токен"
        )

    if decoded.get("type") != "refresh":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Передан не refresh токен"
        )

    new_access_token = create_token(
        data={"sub": decoded.get("sub")},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    return {
        "access_token": new_access_token,
        "token_type": "bearer"
    }
