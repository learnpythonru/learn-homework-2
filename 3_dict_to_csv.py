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
    characters = [
        {'name':'Frodo', 'age':56, 'job':'ring keeper'},
        {'name':'Aragorn', 'age':90, 'job':'king of Gondor'},
        {'name':'Gandalf', 'age':10000, 'job':'white wizard'},
        {'name':'Legolas', 'age':2000, 'job':'marksman'}
    ]
    fields = ['name', 'age', 'job']

    with open('LOTR_characters.csv', 'w') as file:
        writer = csv.DictWriter(file, fields, delimiter=';')
        writer.writeheader()
        for person in characters:
            writer.writerow(person)

if __name__ == "__main__":
    main()
