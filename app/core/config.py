from pydantic_settings import BaseSettings
import os
from functools import lru_cache
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    """ Configurações da API usando Pydantic """

    # Banco de Dados:
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: str = os.getenv("DB_PORT")
    DB_NAME: str = os.getenv("DB_NAME")

@lru_cache
def get_settings():
    """ Cache das configurações da API """
    return Settings()

""" Instância das configurações da API """
settings = get_settings()