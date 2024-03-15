from formatting import *
from result_operators import *
from total_operator import *

# Пример использования функции
process_analysis_json('..//analysis.json', 'operators.json')

# Пример использования функции
generate_excel_report('operators.json', 'result_operator.xlsx')

# Пример использования функции
generate_summary_report('operators.json', 'result_total.xlsx')