from sqlmodel import Session

from api.models.goal import Goal
from api.schemas.manage_goals import GoalCreate


def create_goal(session: Session, goal_data: GoalCreate, owner_id: int) -> Goal:
    db_goal = Goal(
        **goal_data.model_dump(),
        owner_id=owner_id,
    )

    session.add(db_goal)
    session.commit()
    session.refresh(db_goal)
    return db_goal


def finish_goal(session: Session, goal_id: int, owner_id: int) -> Goal:
    db_goal = session.get(Goal, goal_id)
    if not db_goal:
        raise ValueError("Цель не найдена")

    if db_goal.owner_id != owner_id:
        raise PermissionError("Нет доступа")
    
    db_goal.done = True

    session.add(db_goal)
    session.commit()
    session.refresh(db_goal)
    return db_goal

# def get_goal_byId(session: Session, goal_id: int) -> GoalInDB | None:
#     statement = select(Goal).where(Goal.id == goal_id)
#     goal: GoalInDB = session.exec(statement).first()
#     if goal:
#         return goal
