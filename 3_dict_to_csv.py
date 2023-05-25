"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

from names_and_jobs import names, jobs
import random

people = [
    {
        'name': random.choice(names),
        'age': random.randint(18, 55),
        'job': random.choice(jobs)
    } for _ in range(random.randint(4, 20))
]


def main(list_of_dicts):
    with open('export.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, list(list_of_dicts[0].keys()))
        writer.writeheader()
        for elem in list_of_dicts:
            writer.writerow(elem)


if __name__ == "__main__":
    main(people)
