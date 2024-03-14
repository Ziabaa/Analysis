import json
import openpyxl

def add_data_to_excel(json_file_path, excel_file_path):
    # Загрузка данных из JSON файла
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Открытие существующего файла Excel
    workbook = openpyxl.load_workbook(excel_file_path)
    sheet = workbook.active  # получаем активный лист

    # Определение последней строки в файле Excel
    last_row = sheet.max_row

    # Создание множества уже записанных ID
    existing_ids = set(sheet[f'A{row}'].value for row in range(2, last_row + 1))

    # Добавление данных из JSON в файл Excel
    for item in data["data"]:
        if item["id"] not in existing_ids:
            last_row += 1
            sheet[f'A{last_row}'] = item["id"]
            sheet[f'B{last_row}'] = item["analysis"]["operator"]
            sheet[f'C{last_row}'] = item["analysis"]["chat"]["classification"]
            sheet[f'D{last_row}'] = item["analysis"]["chat"]["issue_resolved"] 
            sheet[f'E{last_row}'] = item["analysis"]["chat"]["operator_rating"]
            sheet[f'F{last_row}'] = item["analysis"]["chat"]["dialogue_assessment"]
            sheet[f'G{last_row}'] = item["analysis"]["chat"]["short_topic"]
            sheet[f'H{last_row}'] = item["analysis"]["chat"]["mood"]
            existing_ids.add(item["id"])

    # Сохранение изменений
    workbook.save(excel_file_path)