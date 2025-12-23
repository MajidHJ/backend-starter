from fastapi import APIRouter,Depends
from app.settings import Settings
from app.deps import get_settings
from app.api.health import health_router
api_router = APIRouter()
api_router.include_router(health_router)


@api_router.get("/ping")
def ping()-> dict[str,str]:
    return {"ping":"pong"}


@api_router.get("/info")
def info(settings:Settings = Depends(get_settings) ) ->dict[str,object]:
    return {"app": settings.app_name , "debug": settings.debug}

