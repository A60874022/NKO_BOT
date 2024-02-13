from typing import Optional

from pydantic_settings import BaseSettings


class Config(BaseSettings):
    mongo_uri: str = "mongodb://127.0.0.1:27017/admin"
    mongo_host: str = "mongodb://127.0.0.1:27017/"
    mongo_db: str = "bot_db"
    upload_dir: str = "upload/"
    secret: str = "123456789"
    gtag: Optional[str] = None


config = Config()
