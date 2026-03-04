from fastapi import APIRouter

from app.domain.user.routes import router as user_router
from app.domain.automation.routes import router as automation_router
from app.domain.auth.routes import router as auth_router

router = APIRouter()

router.include_router(auth_router, tags=["Auth"])
router.include_router(user_router, tags=["User"])
router.include_router(automation_router, tags=["Automation"])