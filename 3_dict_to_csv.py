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
    workers = [
                {'name': 'John', 'age': 42,'job': 'John Wick'},
                {'name': 'James', 'age': 'unknown','job': 'Spy'},
                {'name': 'Jocker', 'age': 'guess','job': 'WhySoSerious'},
                {'name': 'Batman', 'age': 45,'job': 'Gotham Guardian'}
              ]
    with open('jobs.csv', 'w', encoding='utf-8') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=";")
        writer.writeheader()
        for person in workers:
            writer.writerow(person)

if __name__ == "__main__":
    main()
