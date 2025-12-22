from fastapi import APIRouter,Depends
from app.settings import Settings
from app.deps import get_settings

api_router = APIRouter()



@api_router.get("/ping")
def ping()-> dict[str,str]:
    return {"ping":"pong"}

@api_router.get("/health")
def health() -> dict[str,str]:
    return {"status": "ok"}


@api_router.get("/info")
def info(settings:Settings = Depends(get_settings) ) ->dict[str,object]:
    return {"app": settings.app_name , "debug": settings.debug}

