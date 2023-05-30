from fastapi import APIRouter
from api.user import user_router
from api.record import record_router

router = APIRouter()
router.include_router(user_router)
router.include_router(record_router)
