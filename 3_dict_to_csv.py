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
    import csv

    input_list =  [
            {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
            {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
            {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
            {'name': 'Игнат', 'age': 14, 'job': 'Jun'},
            ]

    with open('csv_output.csv', 'w', encoding='utf-8',newline='') as f:
        fields = ['name', 'age', 'job']
        writer=csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader
        for line in input_list:
            writer.writerow(line)



if __name__ == "__main__":
    main()
