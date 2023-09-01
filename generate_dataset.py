from configs.settings import config
import openai
import glob
from tqdm import tqdm

openai.api_key = config.get('OpenAI', 'OpenAI_secret_key')

def read_article(file_path):
    with open(file_path, 'r',encoding='utf-8') as file:
        return file.read().replace('\n', ' ')
    
def save_quiz_questions(file_path, json_data):
    with open(file_path, 'w') as file:
        return file.write(json_data)
    
def generate_question(article_body):
    prompt = f"{article_body}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", 
             "content": "You're a career expert that can generate 25 multiple-choice questions for assessment purposes based on an a given article's content, respond with a JSON object. The format should include questions array, each with question, options, each option has id and label, and an answer which is the id of the correct option"},
            {"role": "user", "content": prompt}
        ])

    return response['choices'][0]['message']['content']

if __name__ == '__main__':
    articles = glob.glob("offline_database/*.txt")
    for article in tqdm(articles, desc="Requests to OpenAI API..."):
        article_text = read_article(article)

        model_result = generate_question(article_text)
        save_quiz_questions(f'{article.replace(".txt", "")}.json', model_result)