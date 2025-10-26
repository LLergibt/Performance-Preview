from fastapi import APIRouter, Depends
from sqlmodel import Session

from api.crud import goal as goal_crud
from api.dependencies import get_session
from api.utils.check_token import get_current_user
from api.models.employee import Employee


router = APIRouter()


@router.post("/create_goal/")
async def create_goal(
    goal: goal_crud.GoalCreate,
    session: Session = Depends(get_session),
    current_employee: Employee = Depends(get_current_user),
):
    return await goal_crud.create_goal(
        session=session,
        created_goal=goal,
        owner_id=current_employee,
    )


@router.put("/finish_goal/")
async def finish_goal(
    goal: goal_crud.GoalCreate,
    session: Session = Depends(get_session),
    current_employee: Employee = Depends(get_current_user),
):
    pass
