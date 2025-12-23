from fastapi import APIRouter
from app.api.health import health_router
from app.api.v1.router import v1_router



api_router = APIRouter()
api_router.include_router(health_router)
api_router.include_router(v1_router)




