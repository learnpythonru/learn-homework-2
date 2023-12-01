"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

dict = [
    {"name": "Alice", "age": 7, "job": "pupil"},
    {"name": "Frank", "age": 37, "job": "plumber"},
    {"name": "John", "age": 24, "job": "driver"},
    {"name": "Jerry", "age": 50, "job": "farmer"},
]


def main():
    """
    main function
    """
    with open('citizens.csv', 'w', encoding='utf-8') as f:
        fields = ['name', 'age', 'job']
        write_object = csv.DictWriter(f, fields, delimiter=";")
        write_object.writeheader()
        for user in dict:
            write_object.writerow(user)

if __name__ == "__main__":
    main()
