from sqlmodel import SQLModel, Field
from datetime import date


class Potential(SQLModel, table=True):
    __tablename__ = "potentials"

    id: int | None = Field(default=None, primary_key=True)

    supervisor_id: int = Field(
        foreign_key="employees.id",
        unique=True
    )

    employee_id: int = Field(
        foreign_key="employees.id",
        unique=True
    )

    potential_rank: int
    performance_rank: int

    quarter_date: date
