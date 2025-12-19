from fastapi import FastAPI
from typing import Dict
import logging
from app.logging import setup_logging
from app.settings import settings
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

    return app


app = create_app()