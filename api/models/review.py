from sqlmodel import SQLModel, Field
from utils.enums import RaterEnum


class Review(SQLModel, table=True):
    __tablename__ = "reviews"

    id: int | None = Field(default=None, primary_key=True)

    reviewer_id: int = Field(foreign_key="employees.id")

    goal_id: int = Field(foreign_key="goals.id")

    task_id: int = Field(foreign_key="tasks.id")

    rating: int

    rater: RaterEnum = None
