from create_dialogs import *
from to_gpt import *
from to_exel import *
import os
import sys
sys.path.append('D:/Anthropic/analysis')

if os.path.exists('dialogs.json'):
        os.remove('dialogs.json')

try:
    # Подготовка для обработки LLM моделью
    fetch_and_update_dialogs("dialogs.json", "https://oc.triolan.com/tApi/ServiceDummy/GetDummyChats")

    role = """Hello, you are a brilliant analyzer that produces a response only in json format and put information in ukrainian.
                Финансы — mentions of money or balance
                Отключение — in case of service suspension, or transfer to another provider
                Ремонт — setting up the router, if the service does not work and with the help of the operator, the service starts working
                ПА — resuming the service if it was suspended or paused, even if a wizard was required to resume
                Подключение - новое — if you found out about a new connection at the address or the principle of television and the Internet
                негативний - when the client is completely dissatisfied, use it in cases of almost a complaint"""
    structure = """Give ansver in this format:
    "analysis": {
            "operator": "",
            "chat": {
                "short_topic": "",
                "classification": фінанси/обслуговування/відключення/ремонт/ПА/підключення,
                "mood": негативний/позитивний/нейтральний
                "errors_in_operator_words": []
                "issue_resolved": yes/no,
                "master_is_called": yes/no,
                "correct_punctuation": 1-10,
                "customer_insight": 1-10,
                "simplicity_of_language": 1-10,
                "operator_rating": 1-10,
                "dialogue_assessment": 1-10,
                "client_satisfied": 1-10,
            }
        }"""

    llm = "gpt-3.5-turbo-0125"
    # Путь откуда берем информацию
    file_path = 'dialogs.json'
    # Путь куда записать информацию
    output_file_path = 'analysis.json'
    # Вызов функции для анализа данных из указанного файла и сохранения результатов в указанный файл
    recording_messages_from_llm(file_path, output_file_path, llm, role, structure)

    # Вызов функции для записи в ексель файл.
    add_data_to_excel('analysis.json', 'output.xlsx')
except Exception as e:
    print(f"Произошла ошибка: {e}")
finally:
    print("Successfully end...")