from app.schemas.user import UserResponse
from app.settings import Settings, settings
from app.application.users.service import UserService
from fastapi import Depends

_storage : list[UserResponse] = [] 


def get_storage() -> list[UserResponse]:
    return _storage

def get_user_service(storage: list[UserResponse] = Depends(get_storage)) -> UserService:
    return UserService(storage = storage)

def get_settings()-> Settings:
    return settings

