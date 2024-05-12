import os

from dotenv import load_dotenv

load_dotenv()
SECRET =  os.getenv("SECRET")
ADMIN = os.getenv("ADMIN")
PASS = os.getenv("PASS")
MONGO_HOST = os.environ.get("MONGO_HOST")
MONGO_PORT = os.environ.get("MONGO_PORT")
MONGO_URL = f"mongodb://{MONGO_HOST}:{MONGO_PORT}/"