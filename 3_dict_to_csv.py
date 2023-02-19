import csv

"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

list_of_dicts = [
    {"name": "Bob", "age": 25, "job": "driver"},
    {"name": "Alice", "age": 18, "job": "police officer"},
    {"name": "John", "age": 55, "job": "cook"},
    {"name": "Maggy", "age": 42, "job": "artist"},
    {"name": "Den", "age": 20, "job": "teacher"}
]

def main(dicts: list[dict]):
    with open("peoples.csv", "w", encoding="utf-8", newline="") as file:
        fields = ["name", "age", "job"]
        writer = csv.DictWriter(file, fields, delimiter=";")
        writer.writeheader()
        for person in dicts:
            writer.writerow(person)


if __name__ == "__main__":
    main(list_of_dicts)
