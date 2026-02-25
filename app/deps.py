from typing import Any
from app.settings import Settings, settings
from app.application.users.service import UserService
from fastapi import Depends

_storage : list[Any] = [] 


def get_storage() -> list[Any]:
    return _storage

def get_user_service(storage: list[Any] = Depends(get_storage)) -> UserService:
    return UserService(storage = storage)

def get_settings()-> Settings:
    return settings

