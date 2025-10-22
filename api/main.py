from fastapi import FastAPI
from api.dependencies import create_db
from api.routers import auth

app = FastAPI()

app.include_router(auth.router)


@app.get("/")
async def root():
    return {"message": "Hello Wink"}


@app.on_event("startup")
def on_startup():
    create_db()
