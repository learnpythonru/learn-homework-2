"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

test_animals_dict = [
        {'name': 'Alex', 'age': '10', 'job': 'Lion'},
        {'name': 'Melman', 'age': '10', 'job': 'Giraffe'},
        {'name': 'Gloria', 'age': '10', 'job': 'Hippo'},
        {'name': 'Marty', 'age': '10', 'job': 'Zebra'},
    ]


def main():

    with open('export.csv', 'w') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for animal in test_animals_dict:
            writer.writerow(animal)


if __name__ == "__main__":
    main()
