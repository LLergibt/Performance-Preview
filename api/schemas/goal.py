from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, ConfigDict

from .auth import UserInDB
from .task import TaskResponse, TaskCreate


class Goal(BaseModel):
    title: str
    expection: str
    done: bool = False


class GoalInDB(Goal):
    id: int
    owner_id: int

    model_config = ConfigDict(from_attributes=True)

class GoalCreate(Goal):
    owner_id: int
    tasks: Optional[List[TaskCreate]] = None


class GoalResponse(Goal):
    id: int
    tasks: List[TaskResponse] = []
    created_at: datetime
    owner: UserInDB

    model_config = ConfigDict(from_attributes=True)

class TaskWithGoal(TaskResponse):
    goal: GoalInDB
