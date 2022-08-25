from typing import List
import logging

from pydantic import BaseSettings

class ServerSettings(BaseSettings):
    PORT: int
    PROJECT_PATH: str

class MySQlSettings(BaseSettings):
    MYSQL_HOST: str
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_DB: str

class Settings(
    ServerSettings,
    MySQlSettings,
):
    pass


settings: Settings
try:
    settings = Settings(_env_file=".env")
except Exception as exception:
    logging.exception(exception)
    raise exception