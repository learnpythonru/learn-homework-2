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
    list = [{'name':'Nick','age':'30','job':'it'},
            {'name':'Sam','age':'20','job':'managment'},
            {'name':'Bob','age':'25','job':'developer'},
            {'name':'Billy','age':'40','job':'accounter'}]
    with open('export.csv', 'w', encoding='utf-8', newline='') as file:
        string = ['name', 'age', 'job']
        write = csv.DictWriter(file, string, delimiter=';')
        write.writeheader()
        for user in list:
            write.writerow(user)

if __name__ == "__main__":
    main()
