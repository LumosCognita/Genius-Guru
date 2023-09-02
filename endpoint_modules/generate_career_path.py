from configurations.settings import config
from datetime import datetime
import openai
import json

openai.api_key = config.get('OpenAI', 'OpenAI_secret_key')

def read_json_file(file_path):
    with open(file_path, 'r',encoding='utf-8') as f:
        data = json.load(f)
    return data

def generate_prompt(quiz_summary_path, courses_path):
    quiz_summary_data = read_json_file(quiz_summary_path)
    quiz_summary = quiz_summary_data.get("questions", [])
    courses = read_json_file(courses_path).get('courses', [])
    
    prompt = "Career advice based on quiz and courses:\n"

    for entry in quiz_summary:
        prompt += f'Question: {entry["question"]}\n'
        
        user_answer_id = entry["user_answer"]
        user_answer_label = [opt["label"] for opt in entry["options"] if opt["id"] == user_answer_id][0]
        
        correct_answer_id = entry["answer"]
        correct_answer_label = [opt["label"] for opt in entry["options"] if opt["id"] == correct_answer_id][0]
        prompt += f'User Answer: {user_answer_label}\n'
        prompt += f'Correct Answer: {correct_answer_label}\n'

    prompt += '\nAvailable careers and courses:\n'
    
    for course in courses:
        prompt += f"Course Name: {course['course_name']}\n"
        prompt += f"Provider: {course['course_provider']}\n"
        prompt += f"URL: {course['course_url']}\n"
        prompt += f"Duration: {course['course_duration']}\n"
        prompt += f"Price: {course['course_price']}\n"
        prompt += "----\n"
    
    return prompt



def generate_career_path(quiz_summary, courses_data):
    prompt = generate_prompt(quiz_summary, courses_data)

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", 
             "content": "You're a career expert that can generate from a given quiz answers and the courses we have, recommend top 3 courses based on the quiz answers,respond with a JSON object. The format should include GPT-4_Suggestions array , each with response-intro, courses and additional_info, each course has name ,link ,Provider ,Duration and Price"},
            {"role": "user", 
             "content": prompt}
        ]
    )

    generated_text = response['choices'][0]['message']['content']

    parsed_json = json.loads(generated_text)

    with open(f"offline_database/career_path_output/{datetime.now().timestamp()}.json", "w") as f:
        json.dump(parsed_json, f, indent=4)

    return generated_text



