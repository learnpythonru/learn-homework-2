"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору.
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv


def main():
    employees = [{'name': 'Jiro', 'age': 33, 'job': 'backend dev'},
                 {'name': 'Bum', 'age': 28, 'job': 'backend dev'},
                 {'name': 'Tata', 'age': 32, 'job': 'game dev'},
                 {'name': 'Andry', 'age': 34, 'job': 'analyst'},
                 {'name': 'Snooch', 'age': 28, 'job': 'analyst'}]

    with open('employees.csv', 'w', encoding='UTF-8', newline='') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for i in employees:
            writer.writerow(i)


if __name__ == "__main__":
    main()
