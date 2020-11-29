import csv
"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

def main():
    csv_data = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Pupil'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
        {'name': 'Коля', 'age': 20, 'job': 'Student'}, 
        {'name': 'Петя', 'age': 35, 'job': 'Head of department'}, 
        {'name': 'Максим', 'age': 34, 'job': 'Teamlead'},
    ]

    with open('export.csv', 'w', encoding='utf-8', newline='') as fo:
        fields = ['name', 'age', 'job']
        fo = csv.DictWriter(fo, fields, delimiter=';')
        fo.writeheader()
        for line in csv_data:
            fo.writerow(line)

if __name__ == "__main__":
    main()
