from fastapi import FastAPI
from api.dependencies import create_db
from api.routers import auth, token

app = FastAPI()

app.include_router(auth.router)
app.include_router(token.router)


@app.get("/")
async def root():
    return {"message": "Hello Wink"}


@app.on_event("startup")
def on_startup():
    create_db()
