"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv


def main():
    with open("Cvs_list.csv", "w", encoding="utf-8") as file:
        information = [
            {"name": "Yana", "age": 35, "job": "programmist", "email": "nnn@gmail.com"},
            {"name": "Masha", "age": 40, "job": "disayner", "email": "mmm@gmail.com"},
            {"name": "Misha", "age": 15, "job": "student", "email": "aaa@gmail.com"},
            {"name": "Vova", "age": 22, "job": "student", "email": "sss@gmail.com"},
        ]
        fields = ["name", "age", "job", "email"]
        write = csv.DictWriter(file, fields, delimiter=";")
        write.writeheader()
        for info in information:
            write.writerow(info)


if __name__ == "__main__":
    main()
