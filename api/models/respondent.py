from sqlmodel import SQLModel, Field
from typing import Optional


class Respondent(SQLModel, table=True):
    __tablename__ = "respondents"

    id: Optional[int] = Field(default=None, primary_key=True)
    employee_id: int = Field(foreign_key="employees.id")
    goal_id: int = Field(foreign_key="goals.id")