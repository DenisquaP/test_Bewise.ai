from fastapi import FastAPI

from api.routers import router


app = FastAPI(
    title='task2'
)

app.include_router(router)
