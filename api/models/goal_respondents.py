from sqlmodel import SQLModel, Field, Relationship


class GoalRespondentLink(SQLModel, table=True):
    __tablename__ = "goal_respondents"

    goal_id: int = Field(foreign_key="goals.id", primary_key=True)
    employee_id: int = Field(foreign_key="employees.id", primary_key=True)
