from sqlmodel import SQLModel, Field
from api.schemas.auth import Role


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    firstname: str = Field(index=True)
    surname: str = Field(index=True)
    lastname: str = Field(index=True)
    role: Role
    email: str
    hash: str = Field(index=True)
    is_active: bool = Field(default=True)
