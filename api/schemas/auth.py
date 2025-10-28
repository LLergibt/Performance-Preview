from pydantic import BaseModel
from enum import Enum


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str


class Role(str, Enum):
    ADMIN = "admin"
    SUPERVISOR = "supervisor"
    EMPLOYEE = "employee"


class RoleCreate(str, Enum):
    SUPERVISOR = "supervisor"
    EMPLOYEE = "employee"


class User(BaseModel):
    firstname: str
    surname: str
    lastname: str
    email: str | None = None


class UserCreate(User):
    role: RoleCreate
    password: str
    supervisor_email: str


class UserInDB(User):
    id: int
    hashed_password: str
    is_active: bool | None = None
    role: Role


class UserLogin(BaseModel):
    email: str
    password: str


class RefreshRequest(BaseModel):
    refresh_token: str


class UserRespondents(BaseModel):
    user_id: int
