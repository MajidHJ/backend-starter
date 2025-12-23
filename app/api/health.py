from fastapi import APIRouter,status
from fastapi.responses import JSONResponse

health_router = APIRouter()


@health_router.get("/health")
def health() -> dict[str,str]:
    return {"status": "ok"}



@health_router.get("/ready")
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