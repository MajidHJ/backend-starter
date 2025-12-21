from fastapi import FastAPI,Depends
from app.deps import get_settings
from app.settings import Settings,settings
from typing import Dict
import logging
from app.logging import setup_logging
from contextlib import asynccontextmanager

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info('Application startup')
    yield
    logger.info('Application shutdown')


def create_app() -> FastAPI:
    setup_logging(settings.debug)
    app = FastAPI(lifespan=lifespan,title=settings.app_name)

    @app.get("/health")
    def health() -> Dict[str,str]:
        return {"status": "ok"}


    @app.get("/info")
    def info(settings:Settings = Depends(get_settings) ) ->Dict[str,object]:
        return {"app": settings.app_name , "debug": settings.debug}
    return app


app = create_app()