from sqlmodel import SQLModel, Field
from datetime import datetime


class PerformanceEvaluation(SQLModel, table=True):
    __tablename__ = "performance_evaluation"

    id: int | None = Field(default=None, primary_key=True)
    employee_id: int
    supervisor_text_rate: str
    respondent_text_rate: str

    supervisor_id: int = Field(
        default=None,
    )

    goal_id: int | None = None
    task_id: int | None = None

    rating: int
    recommendations: str | None = None
    quarter_date: datetime = None


class EmployeeEvaluation(SQLModel, table=True):
    __tablename__ = "employee_evaluation"

    id: int | None = Field(default=None, primary_key=True)
    employee_id: int
    supervisor_id: int
    performance_rank: int
    potential_rank: int
    verbal_results: str
    quarter_date: datetime = None




