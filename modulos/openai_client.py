import openai
import modulos.config as config

openai.api_key = config.OPENAI_API_KEY

def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )
    return response.choices[0].text.strip()
