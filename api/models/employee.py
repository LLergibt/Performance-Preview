from __future__ import annotations
from typing import TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy.orm import Mapped
from api.schemas.auth import Role
from api.models.goal_respondents import GoalRespondentLink

if TYPE_CHECKING:
    from .goal import Goal

class Employee(SQLModel, table=True):
    __tablename__ = "employees"

    id: int | None = Field(default=None, primary_key=True)
    firstname: str = Field(index=True)
    lastname: str = Field(index=True)
    surname: str
    role: Role
    email: str = Field(index=True, unique=True)
    hash: str
    is_active: bool = Field(default=True)

    supervisor_id: int | None = Field(default=None, foreign_key="employees.id")

    goals_responded: Mapped[list["Goal"]] = Relationship(
        back_populates="respondents",
        link_model=GoalRespondentLink
    )
