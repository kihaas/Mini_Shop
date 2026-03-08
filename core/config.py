import os
from os import getenv
from pydantic_settings import BaseSettings
from dotenv import load_dotenv


class Settings(BaseSettings):
    db_url: str
    secret_key: str
    DEBUG: bool = False
    APP_NAME: str
    # db_echo: bool = False #должен быть false режим отладки
    db_echo: bool = True

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
    }


settings = Settings()
#.