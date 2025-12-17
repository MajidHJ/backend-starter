from fastapi import FastAPI
from typing import Dict
import logging

logging.basicConfig(level=logging.INFO)




def create_app() -> FastAPI :
    logging.info('App starting ...')
    app = FastAPI()

    @app.get('/health')
    def health() -> Dict[str,str]:
        return {'status':'ok'}

    return app


app = create_app()