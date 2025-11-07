from pydantic import BaseModel


class Respondent(BaseModel):
    employee_id: int
    goal_id: int


class RespondentCreate(Respondent):
    pass