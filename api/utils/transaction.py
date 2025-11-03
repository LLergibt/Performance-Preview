from sqlmodel import Session
from sqlmodel import SQLModel

def transaction_over(obj: SQLModel, session: Session) -> SQLModel:
    session.add(obj)
    session.commit()
    session.refresh(obj)
    
    return obj