from configs.settings import config
from pymongo import MongoClient

class MongoDB:
    def __init__(self):
        client = MongoClient(
            config.get("MongoDB_ConnectionString", "connection_string")
        )
    
    
