import json
from openpyxl import Workbook

def generate_summary_report(json_file, excel_file):
    # Открываем файл JSON
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)['data']

    # Создаем новую книгу Excel
    wb = Workbook()
    ws = wb.active

    # Заголовки столбцов
    headers = ["Оператор", "Количество чатов", "Пунктуація", "Простота розмови", "Рейтинг"]

    # Записываем заголовки
    for col_num, header in enumerate(headers, 1):
        ws.cell(row=1, column=col_num, value=header)

    # Суммируем значения по всем операторам
    total_chats = 0
    total_punctuation = 0
    total_simplicity = 0
    total_rating = 0

    for operator_data in data:
        total_chats += len(operator_data["chats"])
        total_punctuation += operator_data["correct_punctuation"]
        total_simplicity += operator_data["simplicity_of_language"]
        total_rating += operator_data["operator_rating"]

    # Вычисляем средние значения
    if total_chats > 0:
        avg_punctuation = total_punctuation / total_chats
        avg_simplicity = total_simplicity / total_chats
        avg_rating = total_rating / total_chats
    else:
        avg_punctuation = 0
        avg_simplicity = 0
        avg_rating = 0

    # Записываем общие значения
    ws.append(["Все операторы", total_chats, avg_punctuation, avg_simplicity, avg_rating])

    # Сохраняем книгу Excel
    wb.save(excel_file)


