from configs.settings import config
import openai
import json

openai.api_key = config.get('OpenAI', 'OpenAI_secret_key')


def generate_prompt(quiz_summary, courses):
    prompt = "Career advice based on quiz and courses:\n"

    for entry in quiz_summary:
        prompt += f'Question: {entry["question"]}\nUser Answer: {entry["user_answer"]}\nCorrect Answer: {entry["correct_answer"]}\n'
    
    prompt += '\nAvailable careers and courses:\n'
    
    for career, career_courses in courses['topics'].items():
        course_names = [course['course_name'] for course in career_courses]
        prompt += f'Career: {career}\nCourses: {", ".join(course_names)}\n'
    
    return prompt

def generate_career_path(username, quiz_summary, courses=None):
    prompt = generate_prompt(quiz_summary, courses)

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
    with open(f"career_path_output/{username}.json", "w") as f:
        json.dump(output_json, f, indent=4)
