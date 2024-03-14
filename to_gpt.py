import json
import openai

#Открытие файла с ключем openai
file = open('config.json', 'r')
config = json.load(file)
openai.api_key = config['openai']

#Считывает запись и делает запрос в llm, после чего записывает в файл json
def recording_messages_from_llm(file_path, output_file_path, model_llm, first_prompt, second_prompt):
    # Открытие файла JSON и загрузка данных
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Проход по всем записям и вывод текста
    for key, value in data.items():
        inquiry = first_prompt + value + second_prompt
        #Запрос в llm
        messages = [{"role": "system", "content": inquiry}]
        response = openai.ChatCompletion.create(
            model=model_llm,
            response_format={ "type": "json_object" },
            messages=messages,
            temperature=0.7
        )

        # Преобразование строки данных в словарь Python
        parsed_data = json.loads(response['choices'][0]['message']['content'])

        parsed_data_with_id = {"id": int(key), **parsed_data}

        # Загрузка данных из существующего файла JSON, если он существует
        try:
            with open(output_file_path, 'r', encoding='utf-8') as json_file:
                existing_data = json.load(json_file)
        except FileNotFoundError:
            existing_data = {"data": []}

        # Добавление новых данных к существующим данным
        existing_data["data"].append({"id": parsed_data_with_id["id"], "analysis": parsed_data_with_id["analysis"]})

        # Запись обновленных данных в файл JSON
        with open(output_file_path, 'w', encoding='utf-8') as json_file:
            json.dump(existing_data, json_file, ensure_ascii=False, indent=4)