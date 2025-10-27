from sqlmodel import SQLModel, Field, Relationship
from api.models.goal_respondents import GoalRespondentLink

class Goal(SQLModel, table=True):
    __tablename__ = "goals"

    id: int | None = Field(default=None, primary_key=True)
    title: str
    expectation: str
    done: bool
    task_id: int = Field(foreign_key="tasks.id")
    owner_id: int = Field(foreign_key="employees.id")

    respondents: list["Employee"] = Relationship(
        back_populates="goals_responded",
        link_model=GoalRespondentLink,
    )
