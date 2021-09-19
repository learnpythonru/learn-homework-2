"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

employees = [
    {'name': 'John', 'age': '35', 'job': 'accountant'},
    {'name': 'Maty', 'age': '30', 'job': 'assitant'},
    {'name': 'Bill', 'age': '40', 'job': 'SEO'},
    {'name': 'Rajesh', 'age': '37', 'job': 'technical support', 'note': 'very lazy'},
]

path_to_file = '/Users/apetrov/Downloads/'
out_file = 'employees.csv'


def main():
    file_w_path = path_to_file + out_file
    headers = []
    for row in employees:
        for key in row:
            if key not in headers:
                headers.append(key)
    with open(file_w_path, mode="w+", encoding='utf-8') as file:
        file_writer = csv.writer(file, delimiter=",", lineterminator="\r")
        file_writer.writerow(headers)
        for row in employees:
            write_string = []
            for key in headers:
                try:
                    write_string.append(row[key])
                except KeyError:
                    pass
            file_writer.writerow(write_string)


if __name__ == "__main__":
    main()
