from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import os
from api.models import user  # noqa: F401

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL, echo=True)


def create_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session
