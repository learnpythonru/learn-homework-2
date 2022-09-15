"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

def main():
    characters = [
        {'name':'Mabel Pines', 'age':'12', 'job': "Dipper's sister"},
        {'name':'Dipper Pines', 'age':'12', 'job': "Mabel's sister"},
        {'name':'Stan Pines', 'age':'70', 'job': "The greedy, grumpy, yet loving great-uncle of Dipper and Mabel Pines"},
        {'name':'Soos Ramirez', 'age':'22', 'job': "Handyman at the Mystery Shack"},
        {'name':'Soos Ramirez', 'age':'15', 'job': "Part-time employee at the Mystery Shack"},

    ]
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('characters.csv', 'w', encoding='utf-8', newline='') as f:
        fields = ['name', 'age', 'job']
        wr = csv.DictWriter(f, fields, delimiter=';')
        wr.writeheader()
        for user in characters:
            wr.writerow(user)

if __name__ == "__main__":
    main()
