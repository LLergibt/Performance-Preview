from sqlmodel import SQLModel, Field


class Review(SQLModel, table=True):
    __tablename__ = "reviews"

    id: int | None = Field(default=None, primary_key=True)

    reviewer_id: int = Field(
        foreign_key="employees.id"
    )

    goal_id: int = Field(
        foreign_key="goals.id"
    )

    average_rank: int
