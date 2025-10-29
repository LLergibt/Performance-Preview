from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.dependencies import get_session
from api.utils.check_token import get_current_user
from api.models.employee import Employee
from api.schemas.respondent import RespondentCreate
from api.crud import respondent as respondent_crud


router = APIRouter(prefix="/respondent", tags=["respondent"])


@router.post("/add_respondent")
async def add_respondent(
    respondent_data: RespondentCreate,
    session: Session = Depends(get_session)
):
    
    try:
        return await respondent_crud.add_respondent(
            session=session,
            respondent_data=respondent_data
        )
    
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))