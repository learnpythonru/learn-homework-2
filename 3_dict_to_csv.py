"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

import csv

workers =    [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
        {'name': 'Костя', 'age': 31, 'job': 'janitor'}
    ]

def main():
    with open('export.csv', 'w', encoding='utf-8') as ex:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(ex, fields, delimiter=';')
        writer.writeheader()

        for users in workers:
            writer.writerow(users)

if __name__ == "__main__":
    main()
