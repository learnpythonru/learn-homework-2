"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

def main():
    people_list = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 66, 'job': 'Big boss'},
        {'name': 'Ваня', 'age': 15, 'job': 'COOK'},
        {'name': 'Паша', 'age': 23, 'job': 'manager'},
        {'name': 'Таня', 'age': 25, 'job': 'taxi driver'},
        {'name': 'Глеб', 'age': 50, 'job': 'military'}
    ]

    with open('people_job.csv', 'w', encoding='utf-8', newline='') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for people in people_list:
            writer.writerow(people)


if __name__ == "__main__":
    main()
