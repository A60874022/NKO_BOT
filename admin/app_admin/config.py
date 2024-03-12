import os
from pydantic_settings import BaseSettings

from typing import Optional

MONGO_HOST = os.environ.get("MONGO_HOST", "localhost")
MONGO_PORT = os.environ.get("MONGO_PORT", 27017)
MONGO_URL = f"mongodb://{MONGO_HOST}:{MONGO_PORT}/"


class Config(BaseSettings):
    mongo_uri: str = f"mongodb://{MONGO_HOST}:{MONGO_PORT}/admin"
    mongo_host: str = MONGO_URL
    mongo_db: str = "bot_db"
    upload_dir: str = "upload/"
    secret: str = "123456789"
    gtag: Optional[str] = None


config = Config()
