import json # 9.1
import os  # 6.
from datetime import datetime # 4. нам нужна библиотека определяющая когда сработала программа

WD = 'data_processor'    # 12 отладка - определяем рабочую директорию
# 2. определяем все глобальные переменные, которые не меняются и задаются изначально
PATH_INBOX = os.path.join(WD, 'inbox')      
PATH_PROCESSED = 'processed'
PATH_ARCHIVE = 'archive'

# 7. возвращает список файлов
def get_files (path):
    return os.listdir(path)

# 8. обработка файлов из папки
def process_files():
    full_data = {}                        # 8.2  надо агрегировать данные по всем файлам напр. продажи какого либо товара
    for file in files:
        process_data = process_file(file)      # 8.1 функция обработчик и переменная, в которую помещаем результат
                                               # обработки  в виде словаря как оказалось по результату 9.
#        full_data.append(process_data)        # 8.2
        for k,v in for process_data.items():   # 10 получаем файл (output = {}) в виде словаря и парсим его
            if k in full_data.keys():          # 10.
                full_data [k] += v             # по ключ\значение и записываем в новый словарь.
            else:
                full_data [k] = v
        archive (file)                         # 11. прошлись по файлу, записали и перенесли в директорию archive
    return full_data

def archive (file, from_dir = PATH_INBOX, to_dir = PATH_ARCHIVE):
    os.replase(
        os.path.join(from_dir, files),   # берем файл и одной директории
)       os.path.join(to_dir, file)       # и помещаем в другую директорию

# 9. делаем ф-ю обработчик. открываем файл. файл для тренировки строка - словарь
def process_file(file):
    # 9.3 нам надо агрегировать данные в словарь типа:
    # {
    #  'наименование продукта': 'количество продаж'
    # }
    output = {} # 9.4
    with open (file, 'r') as f:
        for line in f:                 # читаем строки
            data = json.loads(lines)  # записываем их в data в формате json  в словарь
            item = data ['item']
            quantity = data ['quantity']  # 9.2 определяем переменные из словаря файла
            if item in output.keys():
                output[item] += quantity
            else:
                output[item] = quantity
    return output

def save_data(data, dir = PATH_PROCESSED):



def main():
    file = get_files (PATH_INBOX)  # 1. начинаем с мазков. сосздаем основную программу, которая смотрит в папку INBOX, есть ли там файлы
    if len (files) > 0:             # 3. проверяем есть ли в папке файлы
        process_files(files)        #    если есть то обрабатываем
 #       archive (files)             # 5.  обработали файлы и надо их заархивировать т.е. перебросить в папку archive см.п.11
    print (f'{datetime.now()} - {len(files)} processed')

if __name__ == '__main__':
    main()
