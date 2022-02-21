"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name,
age и job и значениями по вашему выбору.
В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv
"""
import csv


PEOPLES = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
        {'name': 'Петя', 'age': 34, 'job': 'Small boss'},
    ]


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('peoples_info.csv', 'w', encoding='utf-8', newline='') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for people in PEOPLES:
            writer.writerow(people)


if __name__ == "__main__":
    main()
