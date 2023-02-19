import csv
"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
tab = [
    {"name": "Sergey", "age": 32, "job": "builder"}, {"name": "Nastya", "age": 35, "job": "realtor"},
       {"name": "Nikolay", "age": 24, "job": "office-manager"}, {"name": "Dasha", "age": 31, "job": "photographer"}
]


def main():
    with open("export.csv", "w", encoding="utf-8") as f:
        field = ["name", "age", "job"]
        writer = csv.DictWriter(f, field, delimiter=";")
        writer.writeheader()
        for user in tab:
            writer.writerow(user)


if __name__ == "__main__":
    main()
