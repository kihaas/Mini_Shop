import os
from os import getenv
from pydantic_settings import BaseSettings
from dotenv import load_dotenv


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    DEBUG: bool = False
    APP_NAME: str

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
    }


settings = Settings()
