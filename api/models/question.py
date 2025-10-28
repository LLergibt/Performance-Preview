from sqlmodel import SQLModel, Field
from utils.enums import RaterEnum, PotentialPerformanceEnum


class Question(SQLModel, table=True):
    __tablename__ = "questions"

    id: int | None = Field(default=None, primary_key=True)
    question_text: str
    is_rating: bool
    rate: int

    potential_or_performance: PotentialPerformanceEnum = None

    rater: RaterEnum = None

    
