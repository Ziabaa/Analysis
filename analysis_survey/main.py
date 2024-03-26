from request_whisper import *
from request_gpt import *
import json

prompt = """Your task is to analyze the dialogues according to the given criteria, and give an answer according to the given structure.
        Be attentive to details, and take into account all the words when analyzing. Give your answer only using the given parameters,
        don't make up anything.
        You've got three result:
        1. Hint - in the beginning the subscriber did not remember, the operator called the places and the subscriber remembered.
        2. Independently - independently answered the question of where they saw the commercial. 
        3. Not seen - didn't remember where they saw or didn't see the commercial at all.
        You've got three places you could have been seen:
        1. At home - Stickers, paper booklet, signs on entryways
        2. Street - Billboard, employee car, employee uniform, paper booklet
        3. Internet - YouTube, county Telegram channel, Facebook
        Give analysis in this json format:
        "Result":  
        "Platform": {
                "Home": [],
                "Street": [],
                "Internet": [],
                "Other": []
        }"""

# Директория с аудиофайлами
audio_directory = 'D:\PyCharmProject\get_result\calls'

# Перечисляем все файлы в директории
# Перечисляем все файлы в директории
for filename in os.listdir(audio_directory):
    if filename.endswith(".wav"):
        file_path = os.path.join(audio_directory, filename)
        id_call = filename  # Используем только имя файла без пути

        # Загружаем данные из файла, если он уже существует
        try:
            with open('data.json', 'r', encoding='utf-8') as json_file:
                existing_data = json.load(json_file)
        except FileNotFoundError:
            # Если файла нет, создаем пустой список данных
            existing_data = {"data": []}

        # Проверяем, существует ли id_call в уже существующих записях
        id_call_exists = any(entry["id_call"] == id_call for entry in existing_data["data"])

        # Если id_call уже существует в данных, пропускаем итерацию
        if id_call_exists:
            continue

        # Транскрибируем аудиофайл
        audios = split_audio(file_path, 750)
        transcribe = transcribe_audio(audios)

        # Запрашиваем анализ от GPT
        answer = request_gpt(prompt, transcribe)

        # Создаем запись данных
        data_entry = {
            "id_call": id_call,
            "Result": answer["Result"],
            "Platform": answer["Platform"],
            "Transcribe": transcribe
        }

        # Добавляем новую запись в список данных
        existing_data["data"].append(data_entry)

        # Преобразуем данные в JSON-строку с отступами
        formatted_json_string = json.dumps(existing_data, indent=4, ensure_ascii=False)

        # Записываем отформатированную JSON-строку в файл с указанием кодировки UTF-8
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json_file.write(formatted_json_string)


