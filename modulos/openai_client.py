from openai import OpenAI
import config

client = OpenAI(api_key=config.OPENAI_API_KEY)
import config


def generate_text(prompt):
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
    ],
    max_tokens=500)
    return response.choices[0].message.content.strip()