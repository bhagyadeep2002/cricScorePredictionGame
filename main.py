from fastapi import FastAPI

from api.auth import router as auth_router

app = FastAPI()
app.include_router(auth_router)


@app.get("/")
def start():
    return {"message": "working as expected"}
