from sqlmodel import Session
from api.models.respondent import Respondent
from api.schemas.respondent import RespondentCreate

def add_respondent(session: Session, respondent_data: RespondentCreate):
    if respondent_data is None:
        raise ValueError("Форма не заполнена")
    
    if respondent_data.employee_id is None or respondent_data.goal_id is None:
        raise ValueError("Предоставленные данные неполны")

    db_respondent = Respondent(
        **respondent_data.model_dump(),
    )

    session.add(db_respondent)
    session.commit()
    session.refresh(db_respondent)
    return db_respondent
