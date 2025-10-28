from sqlmodel import Session, select
from api.models.employee import Employee
from api.schemas.auth import UserCreate, UserInDB
from api.utils.auth import get_password_hash, verify_password
from typing import Optional


def create_user(session: Session, user_data: UserCreate, supervisor_id: Optional[int]) -> Employee:
    db_user = Employee(
        **user_data.model_dump(exclude={"password"}),
        supervisor_id=supervisor_id,
        hash=get_password_hash(user_data.password),
    )

    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


def get_user(session: Session, email: str):
    statement = select(Employee).where(Employee.email == email)
    user: UserInDB = session.exec(statement).first()
    if user:
        return user


def check_user_password(session: Session, email: str, password: str):
    statement = select(Employee).where(Employee.email == email)
    user: UserInDB = session.exec(statement).first()
    if verify_password(password, user.hash):
        return True

    return False


def find_supervisor_by_email(session: Session, email: str):
    statement = select(Employee).where(
        (Employee.email == email) & (Employee.role == "supervisor")
    )
    supervisor: UserInDB = session.exec(statement).first()
    if supervisor:
        return supervisor.id
    

def check_employee_exist(session: Session, employee_email: str) -> bool:
    statement = select(Employee).where(Employee.email == employee_email)
    employee: Employee = session.exec(statement).first()
    if employee:
        return True
    else:
        raise ValueError("Работник не найден")
