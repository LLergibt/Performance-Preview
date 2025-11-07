from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from api.dependencies import get_session
from api.utils.check_token import get_current_user
from api.models.employee import Employee
from api.crud import employee as employee_crud
from api.schemas.auth import RoleCreate

router = APIRouter(
    prefix="/employee", tags=["employee"]
)


@router.get("/check_exist/")
async def employee_check_exist(
    employee_email: str,
    session: Session = Depends(get_session),
    current_user: Employee = Depends(get_current_user),
):
    if current_user is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    

    if current_user.role != RoleCreate.SUPERVISOR:
        raise HTTPException(status_code=403, detail="Forbidden")

    try:
        return await employee_crud.check_employee_exist(
            session=session,
            employee_email=employee_email,
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.get("is_supervisor/")
async def employee_is_supervisor(
    employee_email: str,
    session: Session = Depends(get_session),
    current_user: Employee = Depends(get_current_user),
):
    if current_user is None:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    if current_user.role != RoleCreate.SUPERVISOR:
        raise HTTPException(status_code=403, detail="Forbidden")

    supervisor_id = await employee_crud.find_supervisor_by_email(
        session=session,
        email=employee_email,
    )
    if supervisor_id:
        return True
    else:
        return False