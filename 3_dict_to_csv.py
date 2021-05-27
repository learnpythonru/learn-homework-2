"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    staff = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
        {'name': 'Федя', 'age': 33, 'job': 'Cleaner'}
    ]
    with open('my_staff.csv', 'w', newline='', encoding='utf-8') as my_staff:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(my_staff, fields, delimiter=';')
        writer.writeheader()
        for member in staff:
            writer.writerow(member)


if __name__ == "__main__":
    main()
