from configurations.settings import config
from pymongo import MongoClient
from schemas.fastapi_schemas import User
from loguru import logger

class MongoDB:
    def __init__(self):
        client = MongoClient(
            config.get("MongoDB", "connection_string")
        )
        base_database = client['base_database']
        self.users_collection = base_database['users_collection']
        self.users_collection.create_index('username')
        self.courses_collection = base_database['courses_collection']

    
    def add_user(self, user: User):
        self.users_collection.insert_one(
            user.to_dict()
        )
        logger.info(f"DONE INSERTING USER WITH USERNAME = {user.username}")
