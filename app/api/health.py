from fastapi import APIRouter,Depends,status
from fastapi.responses import JSONResponse
from app.deps import get_settings

router = APIRouter()


@router.get("/health")
def health() -> dict[str,str]:
    return {"status": "ok"}



@router.get("/ready")
def ready():
    checks = {"db": "not_connected"}

    is_ready = all(v=="ok" for v in checks.values())

    if not is_ready:
        return JSONResponse(
            status_code= status.HTTP_503_SERVICE_UNAVAILABLE,
            content={"status": "not ready", "checks": checks}
        )
    
    return {
        "status": "ready",
        "checks": checks
    }


@router.get("/info")
def info(settings = Depends(get_settings) ) ->dict[str,object]:
    return {
        "app": settings.app_name ,
          "debug": settings.debug,
    }