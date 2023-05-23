"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv
def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    dict = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist', 'status': 'married'},
        {'name': 'Вася', 'age': 8, 'job': 'Programmer', 'status': 'unmarried'},
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss', 'status': 'married'},
    ]

    print(dict[0])
    with open('export.csv', 'w', encoding='utf-8', newline='') as f:
        fields = ['name', 'age', 'job', 'status']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for element in dict:
            writer.writerow(element)

if __name__ == "__main__":
    main()
