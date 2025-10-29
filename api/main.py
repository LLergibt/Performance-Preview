from fastapi import FastAPI
from api.dependencies import create_db
from api.routers import auth, goal, task, token, employee, respondent

app = FastAPI()

app.include_router(auth.router)
app.include_router(token.router)
app.include_router(employee.router)
app.include_router(goal.router)
app.include_router(task.router)
app.include_router(respondent.router)


@app.get("/")
async def root():
    return {"message": "Hello Wink"}


@app.on_event("startup")
def on_startup():
    create_db()
