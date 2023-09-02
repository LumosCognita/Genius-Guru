from configurations.settings import config
from datetime import datetime
import openai
import json

openai.api_key = config.get('OpenAI', 'OpenAI_secret_key')


def generate_prompt(quiz_summary, courses):
    prompt = "Career advice based on quiz and courses:\n"

    for entry in quiz_summary:
        prompt += f'Question: {entry.question}\nUser Answer: {entry.user_answer}\nCorrect Answer: {entry.answer}\n'
    
    prompt += '\nAvailable careers and courses:\n'
    
    course_names = [course['course_name'] for course in courses]
    prompt += f'Courses: {", ".join(course_names)}\n'
    
    return prompt

def generate_career_path(quiz_summary, courses_data):
    prompt = generate_prompt(quiz_summary.questions, courses_data["courses"])

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", 
             "content": "You're a career expert that can generate from a given quiz answers and the courses we have, recommend top 3 courses based on the quiz answers."},
            {"role": "user", 
             "content": prompt}
        ]
    )


    generated_text = response['choices'][0]['message']['content']

    output_json = {
        'GPT-4_Suggestions': generated_text
    }
    with open(f"offline_database/career_path_output/{datetime.now().timestamp()}.json", "x") as f:
        json.dump(output_json, f, indent=4)

    return generated_text
