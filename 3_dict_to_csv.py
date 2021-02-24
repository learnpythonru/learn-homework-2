import csv
"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

def main():

    user_info = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
        {'name': 'Ксения', 'age': 29, 'job': 'Python developer'},
    ]

    with open('user_info.csv', 'w', encoding='utf-8') as csv_file:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(csv_file, fields, delimiter=';')
        writer.writeheader()

        for user in user_info:
            writer.writerow(user)

if __name__ == "__main__":
    main()
