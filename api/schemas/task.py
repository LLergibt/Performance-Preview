from pydantic import BaseModel
from datetime import datetime


class Task(BaseModel):
    title: str
    expection: str
    done: bool = False


class TaskCreate(Task):
    goal_id: int


class TaskInDB(Task):
    id: int


class TaskResponse(TaskInDB):
    created_at: datetime



