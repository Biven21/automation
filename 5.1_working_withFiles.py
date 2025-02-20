import os
import csv
import json

from Tools.scripts.generate_global_objects import Printer
from pip._internal.cli.cmdoptions import python

#python.exe -m pip install --upgrade pip
print ()

print (os.getcwd())

#target_dir = 'ekulich'
#os.chdir('\Users\User\ekulich')

obj = (os.listdir())               # список объектов в текущей директории


print (obj)
for o in obj:
    print (o, os.path.isfile(o),   # проверяет фийл ли это.
           os.path.exists(o),      # проверяет существует ли объект
           os.path.isdir(o))       # проверяет директория ли это. И если да то True если нет - то False

print("")
# как открыть файл
#f = open('/Users/User/ekulich/WB_120225c.csv', 'r')
#f.close()
# читаем файл, записывая его в  f и выводя содержимое построчно
with open('/Users/User/ekulich/WB_120225c.csv', 'r') as f:
    for line in f:
        print (line)
    #txt = f.readlines()

#записываем что то в конец файла
with open('/Users/User/ekulich/WB_120225c.csv', 'a') as f:
    f.write('************* Privet!Privet!')

# файла с именем WB__.txt не существует и мы его создаем м записываем его в директорию
with open('/Users/User/ekulich/WB__.txt', 'w') as f:
    f.write('************* Privet!Privet!')

print ("Работа с csv")

new_user = {
    'first_name': 'Alexander',
    'last_name': 'Pushkin',
    'is_alive': False,
    'books': ['Капитанская дочка', 'Евгений Онегин']
}

with open('/Users/User/ekulich/WB__.txt', 'w') as f:
   f.write(json.dumps(new_user))

with open('/Users/User/ekulich/WB__.txt', 'r') as f:  # открываем файл для чтения как f
    li = f.readline() # вкладываем первую строку файла (там одна строка) в перемменную li
    print (li, 'это мой файл')
    u = json.loads(li) # с помощью пакета json и метода loads(li) загоняем строку  li в формат
                       # json в переменную u
    print (u['first_name']) #  печатаем значение по ключу 'first_name'

with open('/Users/User/ekulich/WB__.txt', 'r') as f:
    u = json.load(f)              # сдесь берется сразу весь файл и преобразуется в формат
    print(u['first_name'])

# добавил на github