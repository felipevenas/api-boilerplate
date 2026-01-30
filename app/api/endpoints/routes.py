from fastapi import APIRouter

from app.domain.user.routes import router as user_router
from app.domain.automation.routes import router as automation_router

router = APIRouter()

router.include_router(user_router, tags=["User"])
router.include_router(automation_router, tags=["Automation"])