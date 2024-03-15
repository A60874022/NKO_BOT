import os

from dotenv import load_dotenv

load_dotenv()
#DATABASE_URL = os.getenv("DATABASE_URL")
SECRET = os.getenv("SECRET")
ADMIN = os.getenv("ADMIN")
PASS = os.getenv("PASS")
MONGO_HOST = os.environ.get("MONGO_HOST", "localhost")
MONGO_PORT = os.environ.get("MONGO_PORT", 27017)
MONGO_URL = f"mongodb://{MONGO_HOST}:{MONGO_PORT}/"