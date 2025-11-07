from sqlmodel import Session
from api.models.respondent import Respondent
from api.schemas.respondent import RespondentCreate

from api.models.employee import Employee
from api.models.goal import Goal

def add_respondent(session: Session, respondent_data: RespondentCreate):
    if respondent_data is None:
        raise ValueError("Форма не заполнена")
    
    if respondent_data.employee_id is None or respondent_data.goal_id is None:
        raise ValueError("Предоставленные данные неполны")

    is_employee_exists = session.query(Employee).filter(Employee.id == respondent_data.employee_id).first()
    if not is_employee_exists:
        raise ValueError("Сотрудник с таким ID не найден")
    
    is_goal_exists = session.query(Goal).filter(Goal.id == respondent_data.goal_id).first()
    if not is_goal_exists:
        raise ValueError("Цель с таким ID не найдена")
    
    goal_owner_id = session.query(Goal.owner_id).filter(Goal.id == respondent_data.goal_id).scalar()
    if goal_owner_id == respondent_data.employee_id:
        raise ValueError("Сотрудник не может быть респондентом своей собственной цели")

    respondents_count = session.query(Respondent).filter(Respondent.goal_id == respondent_data.goal_id).count()

    if respondents_count > 5:
        raise ValueError("Максимальное количество респондентов для этой цели достигнуто")

    
    db_respondent = Respondent(
        **respondent_data.model_dump(),
    )

    session.add(db_respondent)
    session.commit()
    session.refresh(db_respondent)
    return db_respondent
