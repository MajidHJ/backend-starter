from fastapi import FastAPI
from typing import Dict
import logging
from dotenv import load_dotenv
import os

logging.basicConfig(level=logging.INFO)




def create_app() -> FastAPI :
    load_dotenv()
    app_name = os.getenv('APP_NAME')
    debug = os.getenv('DEBUG')
    
    logging.info(
        "App starting ... name=%s debug=%s",
         app_name,
         debug
    )

    app = FastAPI()

    @app.get('/health')
    def health() -> Dict[str,str]:
        return {'status':'ok'}

    return app


app = create_app()