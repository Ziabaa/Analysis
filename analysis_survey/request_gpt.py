import openai
import json

# Открытие файла с ключем openai
with open('config.json', 'r') as file:
    config = json.load(file)
    openai.api_key = config['openai']

def request_gpt(system_prompt, transcribe):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0125",
        messages=[{
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": transcribe
            }
            ],
        response_format={"type": "json_object"},
        temperature=0.6
    )
    parsed_data = json.loads(completion['choices'][0]['message']['content'])
    return parsed_data

