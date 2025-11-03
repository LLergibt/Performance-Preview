from __future__ import annotations
from typing import TYPE_CHECKING

from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy.orm import Mapped
from api.models.goal_respondents import GoalRespondentLink

if TYPE_CHECKING:
    from .employee import Employee

class Goal(SQLModel, table=True):
    __tablename__ = "goals"

    id: int | None = Field(default=None, primary_key=True)
    title: str
    expectation: str
    done: bool = Field(default=False)
    task_id: int = Field(foreign_key="tasks.id")
    owner_id: int = Field(foreign_key="employees.id")

    respondents: Mapped[list["Employee"]] = Relationship(
        back_populates="goals_responded",
        link_model=GoalRespondentLink,
    )

