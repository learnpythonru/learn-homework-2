import csv
"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    my_dict_list = [
        {
            'name': 'Brainwashed',
            'age' : '1',
            'job' : 'lol'
        },
        {
            'name': 'Cakewall',
            'age' : '3',
            'job' : 'laywer'
        },
        {
            'name': 'Silkykiss',
            'age' : '5',
            'job' : 'judge'
        },
        {
            'name': 'Fattylips',
            'age' : '7',
            'job' : 'teacher'
        }
    ]
    
    with open('export.csv', 'w', encoding ='utf-8') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields)
        writer.writeheader()
        for name in my_dict_list:
            writer.writerow(name)
    print("Done")

if __name__ == "__main__":
    main()
