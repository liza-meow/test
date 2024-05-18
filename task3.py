import json

# Чтение данных из файлов
with open('values.json', 'r') as f:
    values_data = json.load(f)
with open('tests.json', 'r') as f:
    tests_data = json.load(f)

# Сопоставление значений по id
id_to_value = {value['id']: value['value'] for value in values_data['values']}

# Функция для заполнения значений по id
def fill_values(node):
    if 'id' in node: # Если есть id, заполняем значение
        node['value'] = id_to_value.get(node['id'], '')
    if 'values' in node: # Рекурсивно обрабатываем дочерние узлы
        for child in node['values']:
            fill_values(child)

# Заполнение значений для тестов
    for test in tests_data['tests']:
        fill_values(test)

# Запись результата в файл report.json
with open('report.json', 'w') as f:
    json.dump(tests_data, f, indent=4)