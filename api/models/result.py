from sqlmodel import SQLModel, Field


class Result(SQLModel, table=True):
    __tablename__ = "results"

    id: int | None = Field(default=None, primary_key=True)
    supervisor_id: int = Field(
        default=None,
        foreign_key="employees.id"
    )

    goal_id: int = Field(
        foreign_key="goals.id"
    )

    rating: int
    recommendations: str
