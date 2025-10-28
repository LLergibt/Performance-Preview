from fastapi import FastAPI
from api.dependencies import create_db
from api.routers import auth, token, employee, manage_goals, manage_tasks

app = FastAPI()

app.include_router(auth.router)
app.include_router(token.router)
app.include_router(employee.router)
app.include_router(manage_goals.router)
app.include_router(manage_tasks.router)


@app.get("/")
async def root():
    return {"message": "Hello Wink"}


@app.on_event("startup")
def on_startup():
    create_db()
