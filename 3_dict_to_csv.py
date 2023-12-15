"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

import csv


def main():
    with open("info.csv", "w", encoding="utf-8") as file:
        information = [
            {"name": "Pavel", "age": 23, "job": "Data-Scientist"},
            {"name": "Alex", "age": 25, "job": "Driver"},
            {"name": "Max", "age": 20, "job": "Football-player"},
            {"name": "Leo", "age": 35, "job": "Professor"},
            {"name": "Andrey", "age": 27, "job": "Police officer"}
        ]
        fields = ["name", "age", "job"]
        writer = csv.DictWriter(file, fields, delimiter=";")
        writer.writeheader()
        for user in information:
            writer.writerow(user)
    

if __name__ == "__main__":
    main()
