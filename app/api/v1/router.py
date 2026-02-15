from fastapi import APIRouter
from app.api.v1.users import router as users_router
from app.api.v1.demo import router as demo_router
router = APIRouter(prefix="/v1")
router.include_router(users_router)
router.include_router(demo_router)