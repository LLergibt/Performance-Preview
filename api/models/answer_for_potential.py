from sqlmodel import SQLModel, Field


class AnswerForPotential(SQLModel, table=True):
    __tablename__ = "answers_for_potential"

    id: int | None = Field(default=None, primary_key=True)

    potential_id: int = Field(
        foreign_key="potentials.id",
        unique=True
    )

    question_id: int = Field(
        foreign_key="questions.id"
    )

    response: str
    rating: int
