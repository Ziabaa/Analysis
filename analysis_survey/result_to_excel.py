import pandas as pd
import json

# Загружаем данные из JSON-файла
with open('data.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Преобразуем структуру "Platform" в отдельные столбцы
home = []
street = []
internet = []
other = []

for item in data['data']:
    home.append(', '.join(item['Platform']['Home']))
    street.append(', '.join(item['Platform']['Street']))
    internet.append(', '.join(item['Platform']['Internet']))
    other.append(', '.join(item['Platform'].get('Other', [])))

# Создаем DataFrame
df = pd.DataFrame({
    'id_call': [item['id_call'] for item in data['data']],
    'Result': [item['Result'] for item in data['data']],
    'Home': home,
    'Street': street,
    'Internet': internet,
    'Other': other,
    'Transcribe': [item['Transcribe'] for item in data['data']]
})

# Записываем DataFrame в файл Excel
df.to_excel('data.xlsx', index=False)