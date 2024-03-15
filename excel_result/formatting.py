import json

def process_analysis_json(input_file, output_file):
    # Чтение JSON из файла
    with open(input_file, 'r', encoding='utf-8') as f:
        source_json = f.read()

    # Преобразование исходного JSON
    parsed_json = json.loads(source_json)

    # Создание словаря для хранения данных операторов
    operators_data = {}

    # Заполнение словаря данными из исходного JSON
    for item in parsed_json['data']:
        operator_id = item['id']
        operator_name = item['analysis']['operator']
        chat_count = 1
        correct_punctuation = item['analysis']['chat']['correct_punctuation']
        simplicity_of_language = item['analysis']['chat']['simplicity_of_language']
        operator_rating = item['analysis']['chat']['operator_rating']
        dialogue_assessment = item['analysis']['chat'].get('dialogue_assessment', 0)
        customer_insight = item['analysis']['chat'].get('customer_insight', 0)

        if operator_name in operators_data:
            # Проверяем наличие ID чата в списке чатов оператора
            if operator_id not in operators_data[operator_name]['chats']:
                operators_data[operator_name]['count'] += 1
                operators_data[operator_name]['correct_punctuation'] += correct_punctuation
                operators_data[operator_name]['simplicity_of_language'] += simplicity_of_language
                operators_data[operator_name]['operator_rating'] += operator_rating
                operators_data[operator_name]['dialogue_assessment'] += dialogue_assessment
                operators_data[operator_name]['customer_insight'] += customer_insight
                operators_data[operator_name]['chats'].append(operator_id)
        else:
            operators_data[operator_name] = {
                'count': chat_count,
                'correct_punctuation': correct_punctuation,
                'simplicity_of_language': simplicity_of_language,
                'operator_rating': operator_rating,
                'dialogue_assessment': dialogue_assessment,
                'customer_insight': customer_insight,
                'chats': [operator_id]
            }

    # Запись новых данных в JSON файл
    new_json_data = [{'operator': operator, **data} for operator, data in operators_data.items()]
    new_json = {"data": new_json_data}

    # Запись нового JSON в файл
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(new_json, f, ensure_ascii=False, indent=4)



