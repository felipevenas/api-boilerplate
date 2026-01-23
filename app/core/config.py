from pydantic_settings import BaseSettings
import os
from pathlib import Path
from functools import lru_cache
from dotenv import load_dotenv

env_path = Path(__file__).parent.parent.parent / ".env"
load_dotenv()

class Settings(BaseSettings):
    """ Configurações da API usando Pydantic """

    # Banco de Dados:
    DB_USER: str = os.getenv("DB_USER")
    DB_PASS: str = os.getenv("DB_PASS")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: str = os.getenv("DB_PORT")
    DB_NAME: str = os.getenv("DB_NAME")

    class Config:
        env_file = str(env_path)
        env_file_encoding = "utf-8"

@lru_cache
def get_settings():
    """ Cache das configurações da API """
    return Settings()

""" Instância das configurações da API """
settings = get_settings()