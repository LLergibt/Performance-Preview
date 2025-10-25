from sqlmodel import SQLModel, Field


class Answer(SQLModel, table=True):
    __tablename__ = "answers"

    id: int | None = Field(default=None, primary_key=True)

    review_id: int = Field(
        foreign_key="reviews.id"
    )

    question_id: int = Field(
        foreign_key="questions.id"
    )

    response: str
    rating: int
