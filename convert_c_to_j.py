import csv
import json

# Указываем путь к CSV-файлу
csv_file = 'data.csv'
json_file = 'output.json'

# Чтение данных из CSV-файла
with open(csv_file, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    # Преобразование данных в список словарей
    data = list(reader)

# Запись данных в JSON-файл
with open(json_file, mode='w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)

print(f'Данные успешно записаны в {json_file}')
