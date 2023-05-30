from fastapi import FastAPI
from .api.routers import router
from .tables import Base
from .database import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='task1'
)

app.include_router(router)
