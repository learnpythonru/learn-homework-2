"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""


import csv


user_list = [
    {'name': 'Gloria', 'age': '31', 'job': 'disigner'},
    {'name': 'Robert', 'age': '27', 'job': 'ingineer'},
    {'name': 'Sofia', 'age': '51', 'job': 'arhitect'},
    {'name': 'John', 'age': '33', 'job': 'boss'},
]


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
with open('user_list.csv', 'w', encoding='utf-8', newline='') as new_file:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(new_file, fields, delimiter=';')
    writer.writeheader()
    for user in user_list:
        writer.writerow(user)

if __name__ == "__main__":
    main()
