# Програма для аналізу діалогів за допомогою GPT

Цей проект розроблений для аналізу діалогів з використанням моделі Generative Pre-trained Transformer (GPT) від OpenAI.

## Послідовність роботи програми:

1. **create_dialogs.py**: Цей скрипт отримує на вхід посилання на API та назву файла, у який будуть записані дані. Він форматує діалоги для подальшого відправлення на аналіз в LLM.

2. **to_gpt.py**: Даний скрипт отримує інструкції для дії, модель GPT, структуру відповіді та файл, у який потрібно записати відповідь моделі.

3. **to_exel.py**: Цей скрипт виконує запис даних до файлу Excel. **ОБОВ'ЯЗКОВО**, щоб був файл, у який відбувається запис.

## Установка

Для коректної роботи програми встановіть наступні бібліотеки:
 
 `pip install requests openai openpyxl`
