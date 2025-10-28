from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from sqlmodel import SQLModel, Field

if TYPE_CHECKING:
    pass

class Goal(SQLModel, table=True):
    __tablename__ = "goals"

    id: Optional[int] = Field(default=None, primary_key=True)

    title: str
    expectation: str
    done: bool = Field(default=False)

    task_id: int = Field(foreign_key="tasks.id")
    owner_id: int = Field(foreign_key="employees.id")
