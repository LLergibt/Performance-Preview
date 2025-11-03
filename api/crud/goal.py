from sqlmodel import Session, select

from api.models.goal import Goal
from api.schemas.manage_goals import GoalCreate
from models.employee import Employee
from utils.transaction import transaction_over


def create_goal(session: Session, goal_data: GoalCreate, owner_id: int) -> Goal:
    db_goal = Goal(
        **goal_data.model_dump(),
        owner_id=owner_id,
    )

    # session.add(db_goal)
    # session.commit()
    # session.refresh(db_goal)
    # return db_goal
    
    return transaction_over(
        obj=db_goal,
        session=session,
    )


def finish_goal(session: Session, goal_id: int, respondents_ids: list[int], owner_id: int) -> Goal:
    db_goal = session.get(Goal, goal_id)
    if not db_goal:
        raise ValueError("Цель не найдена")

    if db_goal.owner_id != owner_id:
        raise PermissionError("Нет доступа")
    
    db_goal.done = True

    respondents = session.exec(
        select(Employee).where(Employee.id.in_(respondents_ids))
    ).all()

    if len(respondents) > 5:
        raise ValueError("Можно добавить не более 5 респондентов")

    db_goal.respondents = respondents

    # session.add(db_goal)
    # session.commit()
    # session.refresh(db_goal)
    # return db_goal

    return transaction_over(
        obj=db_goal,
        session=session,
    )


