import requests
import json

def fetch_and_update_dialogs(file_path, url):
    # Выполняем GET-запрос для получения JSON-данных
    response = requests.get(url)
    
    if response.status_code == 200:  # Проверяем успешность запроса
        json_data = response.json()  # Разбираем JSON-данные из ответа
        dialogs = {}  # Создаем пустой словарь для диалогов

        # Перебираем элементы в списке "data"
        for item in json_data["data"]:
            id_dialog = str(item["id"])  # Преобразуем идентификатор в строку
            text_dialog = ""  # Инициализируем пустую строку для текста диалога

            # Перебираем сообщения в текущем элементе
            for message in item["messages"]:
                # Проверяем, является ли сообщение от оператора
                if message["type"] == "Оператор":
                    operator_name = message["name"]
                    text = message["message"].rstrip('\n')
                    text_dialog += f"Оператор {operator_name}: '{text}' "
                else:
                    text = message["message"].rstrip('\n')
                    text_dialog += f"Клиент: '{text}' "

            dialogs[id_dialog] = text_dialog  # Добавляем текст диалога в словарь с ключом id_dialog

        # Загружаем существующие диалоги из файла или создаем пустой словарь
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                existing_dialogs = json.load(file)
        except FileNotFoundError:
            existing_dialogs = {}

        # Обновляем существующие диалоги новыми
        existing_dialogs.update(dialogs)

        # Сохраняем обновленные диалоги обратно в файл
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(existing_dialogs, file, ensure_ascii=False, indent=4)

        print(f"Диалоги добавлены в {file_path}")
    else:
        print("Не удалось получить данные по указанному URL")
