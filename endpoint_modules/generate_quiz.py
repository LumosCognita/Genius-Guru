import random
import json
from schemas.fastapi_schemas import Quiz
from loguru import logger

def generate_quiz_from(source) -> Quiz:
    logger.info("HITTTTT")
    path = ""
    if source == 'ML':
        path = "offline_database/Machine_Learning.json"
    elif source == 'SE':
        path = "offline_database/Software_Eng.json"
    elif source == 'PM':
        path = "offline_database/Product_Manager.json"
    
    with open(path, "r") as json_file:
        questions = json.load(json_file)
    
    logger.info(len(questions['questions']))
    
    return Quiz(questions=random.sample(questions["questions"], 10))
