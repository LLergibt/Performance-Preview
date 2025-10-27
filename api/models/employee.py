from sqlmodel import SQLModel, Field, Relationship
from api.schemas.auth import Role
from api.models.goal_respondents import GoalRespondentLink

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

    supervisor_id: int = Field(default=None, foreign_key="employees.id")

    goals_responded: list["Goal"] = Relationship(
        back_populates="respondents",
        link_model=GoalRespondentLink
    )
