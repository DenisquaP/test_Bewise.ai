from fastapi import APIRouter
from .question import question_router

router = APIRouter()
router.include_router(question_router)
