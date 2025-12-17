from fastapi import FastAPI
from typing import Dict
import logging
from app.settings import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



def create_app() -> FastAPI:
    logger.info("App starting ... APP_NAME: %r  DEBUG: %r ",settings.app_name,settings.debug)

    app = FastAPI(title=settings.app_name,debug=settings.debug)

    @app.get("/health")
    def health() -> Dict[str,str]:
        return {"status": "ok"}

    return app


app = create_app()