import os

from dotenv import load_dotenv

load_dotenv()
SECRET =  os.getenv("SECRET")
ADMIN = os.getenv("ADMIN")
PASS = os.getenv("PASS")
MONGO_HOST = "0.0.0.0"#os.getenv("MONGO_HOST", "localhost")
MONGO_PORT = "27017"#os.getenv("MONGO_PORT", 27017)
MONGO_URL = f"mongodb://{MONGO_HOST}:{MONGO_PORT}"