from configurations.settings import config
from datetime import datetime
import openai
import json

openai.api_key = config.get('OpenAI', 'OpenAI_secret_key')

def read_json_file(file_path):
    with open(file_path, 'r',encoding='utf-8') as f:
        data = json.load(f)
    return data

def generate_prompt(quiz_summary, courses_data):
    prompt = "Career advice based on quiz and courses:\n"

    for question in quiz_summary:
        prompt += f'Question: {question.question}\n'
        
        user_answer_id = question.user_answer
        user_answer_label = [opt.label for opt in question.options if opt.id == user_answer_id][0]
        
        correct_answer_id = question.answer
        correct_answer_label = [opt.label for opt in question.options if opt.id == correct_answer_id][0]
        prompt += f'User Answer: {user_answer_label}\n'
        prompt += f'Correct Answer: {correct_answer_label}\n'

    prompt += '\nAvailable careers and courses:\n'
    
    for course in courses_data:
        prompt += f"Course Name: {course['course_name']}\n"
        prompt += f"Provider: {course['course_provider']}\n"
        prompt += f"URL: {course['course_url']}\n"
        prompt += f"Duration: {course['course_duration']}\n"
        prompt += f"Price: {course['course_price']}\n"
        prompt += "----\n"
    
    return prompt



def generate_career_path(quiz_summary, courses_data):
    prompt = generate_prompt(quiz_summary.questions, courses_data["courses"])

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", 
             "content": "You're a career expert that can generate from a given quiz answers and the courses we have, recommend top 3 courses based on the quiz answers,respond with a JSON object. The format should include Path array , each with response-intro, courses and additional_info, each course has name ,link ,Provider ,Duration and Price"},
            {"role": "user", 
             "content": prompt}
        ]
    )

    generated_text = response['choices'][0]['message']['content']

    parsed_json = json.loads(generated_text)

    with open(f"offline_database/career_path_output/{datetime.now().timestamp()}.json", "w") as f:
        json.dump(parsed_json, f, indent=4)

    return generated_text



