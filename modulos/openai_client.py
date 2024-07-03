from openai import OpenAI
from config import OPENAI_API_KEY, UNSPLASH_ACCESS_KEY, TERMS

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_text(prompt):
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ],
    max_tokens=500)
    return response.choices[0].message.content.strip()

