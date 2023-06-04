from fastapi import APIRouter
from api.question import question_router

router = APIRouter()
router.include_router(question_router)
