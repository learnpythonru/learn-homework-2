"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import pprint
from string import ascii_lowercase as a_low
from random import randint, sample
import csv

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    fields = ['name', 'age', 'job']
    values = [''.join(sample(a_low, 5)).capitalize(),
              randint(18,65),
              ''.join(sample(a_low, 10)).capitalize()+' LLC']
    dict_list = [{fields[0]: ''.join(sample(a_low, 5)).capitalize(),
                  fields[1]: randint(18,65),
                  fields[2]: ''.join(sample(a_low, 10)).capitalize()+' LLC'}
                 for x in range(1000)]
    my_dialect = csv.excel()
    my_dialect.delimiter = ';'
    try:
        with open('hw2.csv', 'w', newline='') as write_file:
            writer = csv.DictWriter(write_file, fields, dialect=my_dialect)
            writer.writeheader()
            for each in dict_list:
                writer.writerow(each)
    except (IOError, FileNotFoundError) as e:
        print(e)
    pprint.pprint(dict_list)

if __name__ == "__main__":
    main()
