from sqlmodel import SQLModel, Field


class Goal(SQLModel, table=True):
    __tablename__ = "goals"

    id: int | None = Field(default=None, primary_key=True)

    title: str
    expection: str
    done: bool

    task_id: int = Field(
        foreign_key="tasks.id"
    )

    owner_id: int = Field(
        foreign_key="employees.id"
    )