from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from api.crud import goal as goal_crud
from api.schemas.manage_goals import GoalCreate
from api.dependencies import get_session
from api.utils.check_token import get_current_user
from api.models.employee import Employee


router = APIRouter(prefix="/goal", tags=["goal"])


@router.post("/create/")
async def create_goal(
    goal: GoalCreate,
    session: Session = Depends(get_session),
    current_employee: Employee = Depends(get_current_user),
):
    
    if current_employee is None:
        raise HTTPException(status_code=401, detail="Unauthorized")

    return await goal_crud.create_goal(
        session=session,
        goal_data=goal,
        owner_id=current_employee.id,
    )


@router.put("/finish/")
async def finish_goal(
    goal_id: int,
    session: Session = Depends(get_session),
    current_employee: Employee = Depends(get_current_user),
):
    
    if current_employee is None:
        raise HTTPException(status_code=401, detail="Unauthorized")

    try:
        return goal_crud.finish_goal(
            session=session,
            goal_id=goal_id,
            owner_id=current_employee.id,
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except PermissionError as e:
        raise HTTPException(status_code=403, detail=str(e))

