import os

from dotenv import load_dotenv

load_dotenv()
SECRET =  os.getenv("SECRET")
ADMIN = os.getenv("ADMIN")
PASS = os.getenv("PASS")
MONGO_HOST = "5.35.88.241"#os.getenv("MONGO_HOST", "127.0.0.1")
MONGO_PORT = os.getenv("MONGO_PORT", 27017)
MONGO_INITDB_ROOT_USERNAME = os.getenv("MONGO_INITDB_ROOT_USERNAME", "Anton")
MONGO_INITDB_ROOT_PASSWORD = os.getenv("DB_PASSWORD", "60874022")
MONGO_URL = f"mongodb://{MONGO_INITDB_ROOT_USERNAME}:{MONGO_INITDB_ROOT_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}"
