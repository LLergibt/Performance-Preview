from sqlmodel import Session
from api.models.goal import Goal
from api.models.task import Task
from api.schemas.manage_goals import TaskCreate


def create_task(session: Session, task_data: TaskCreate, goal_id: int) -> Task:
    goal = session.get(Goal, goal_id)
    if not goal:
        raise

    db_task = Task(
        **task_data.model_dump(),
    )
    task_id = db_task.id
    goal.task_id = task_id

    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task


# def get_goal_byId(session: Session, goal_id: int) -> GoalInDB | None:
#     statement = select(Goal).where(Goal.id == goal_id)
#     goal: GoalInDB = session.exec(statement).first()
#     if goal:
#         return goal
