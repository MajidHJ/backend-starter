from fastapi import FastAPI
from typing import Dict
import logging

app = FastAPI()
logging.basicConfig(level=logging.INFO)

logging.info('App starting ...')


@app.get('/health')
def health() -> Dict[str,str]:
    return {'status':'ok'}