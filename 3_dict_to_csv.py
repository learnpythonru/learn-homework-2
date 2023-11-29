"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

my_dict = [{'name': 'Aleks',
            'age': 37,
            'job': 'Sysadmin'},
           {
               'name': 'Olga',
               'age': 33,
               'job': 'buh'
           },
           {
               'name': 'Artemii',
               'age': 7,
               'job': 'scool'
           },
           {
               'name': 'Bob',
               'age': 22,
               'job': 'engineer'

           }
           ]


def main() -> None:
    with open('my_base.txt', 'w', encoding='utf-8') as working:
        fields = ['name', 'age', 'job']
        reader = csv.DictWriter(working, fields, delimiter=':')
        reader.writeheader()

        for i in my_dict:
            reader.writerow(i)


if __name__ == "__main__":
    main()
