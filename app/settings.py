from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name : str = 'Backend Starter'
    debug : bool = False

    class Config():
        env_file = '.env'


settings = Settings()
