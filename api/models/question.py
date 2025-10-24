from sqlmodel import SQLModel, Field


class Question(SQLModel, table=True):
    __tablename__ = "questions"

    id: int | None = Field(default=None, primary_key=True)
    question_text: str

    is_rating: bool
    is_for_potential: bool
