"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
from asyncore import write
import csv


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    user_list = [
        {"name": "Adil", "age": "27", "job": "Engeneer"},
        {"name": "Adel", "age": "26", "job": "Devrel"},
        {"name": "Regina", "age": "25", "job": "HR-manager"},
        {"name": "Alex", "age": "41", "job": "Head of Departament"},
    ]
    with open("export.csv", "w", encoding="utf-8", newline="") as f:
        fields = ["name", "age", "job"]
        writer = csv.DictWriter(f, fields, delimiter=";")
        writer.writeheader()
        for user in user_list:
            writer.writerow(user)


if __name__ == "__main__":
    main()
