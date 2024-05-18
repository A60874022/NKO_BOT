import os

from dotenv import load_dotenv

load_dotenv()
SECRET =  os.getenv("SECRET")
ADMIN = os.getenv("ADMIN")
PASS = os.getenv("PASS")
MONGO_HOST = os.getenv("MONGO_HOST", "127.0.0.1")
MONGO_PORT = os.getenv("MONGO_PORT", 27017)
DB_USER = os.getenv("DB_USER", "Anton")
DB_PASSWORD = os.getenv("DB_PASSWORD", "60874022")
MONGO_URL = f"mongodb://{DB_USER}:{DB_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}"
