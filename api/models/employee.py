from sqlmodel import SQLModel, Field
from api.schemas.auth import Role
from typing import Optional


class Employee(SQLModel, table=True):
    __tablename__ = "employees"

    id: int | None = Field(default=None, primary_key=True)
    firstname: str = Field(index=True)
    surname: str = Field(index=True)
    lastname: str = Field(index=True)
    role: Role
    email: str = Field(index=True)
    hash: str = Field(index=True)
    is_active: bool = Field(default=True)

    supervisor_id: Optional[int] = Field(
        default=None,
        foreign_key="employees.id"
    )
