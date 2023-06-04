from fastapi import FastAPI
from api.routers import router

app = FastAPI(
    title='task1'
)

app.include_router(router)
