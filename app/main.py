from fastapi import FastAPI
from app.settings import settings
import logging
from app.api.router import api_router
from app.logging import setup_logging
from contextlib import asynccontextmanager

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info('Application startup')
    logger.info('Debug mode is %s', settings.debug)
    yield
    logger.info('Application shutdown')


def create_app() -> FastAPI:
    setup_logging(settings.debug)
    app = FastAPI(lifespan=lifespan,title=settings.app_name)
    app.include_router(api_router)
    return app


app = create_app()