from flask_pymongo import PyMongo
import os
from dotenv import load_dotenv


load_dotenv()


def init_db():
    from main import app
    mongodb_client = PyMongo(app, uri=f"mongodb://{os.getenv('MONGO_HOST')}:27017/{os.getenv('MONGO_DB')}")
    db = mongodb_client.db
    return db
