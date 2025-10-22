from sqlmodel import Session, select
from api.models.user import User
from api.schemas.auth import UserCreate, UserInDB
from api.utils.auth import get_password_hash


def create_user(session: Session, user_data: UserCreate) -> User:
    db_user = User(
        **user_data.model_dump(exclude={"password"}),
        hash=get_password_hash(user_data.password),
    )

    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


def get_user(session: Session, email: str):
    statement = select(User).where(User.email == email)
    user: UserInDB = session.exec(statement).first()
    if user:
        return user
