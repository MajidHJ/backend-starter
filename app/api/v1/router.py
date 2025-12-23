from fastapi import APIRouter
# from app.settings import Settings
from fastapi import Depends
from app.deps import get_settings

v1_router = APIRouter(prefix="/v1")

@v1_router.get("/ping")
def ping()-> dict[str,str]:
    return {"ping":"pong"}


@v1_router.get("/info")
def info(settings = Depends(get_settings) ) ->dict[str,object]:
    return {
        "app": settings.app_name ,
          "debug": settings.debug,
    }