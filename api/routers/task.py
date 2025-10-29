from fastapi import APIRouter, Depends
from sqlmodel import Session
from api.crud import task as task_crud
from api.dependencies import get_session
from api.utils.check_token import get_current_user
from api.schemas.task import TaskCreate
from api.models.employee import Employee

router = APIRouter(prefix="/task", tags=["task"])

@router.post("/create/")
async def create_task(
    task: TaskCreate,
    session: Session = Depends(get_session),
    current_employee: Employee = Depends(get_current_user)

):
    
    if current_employee is None:
        raise HTTPException(status_code=401, detail="Unauthorized")

    return await task_crud.create_task(
        session=session, 
        created_task=task,
        owner_id=current_employee,
    )
