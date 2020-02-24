"""

Домашнее задание №2

Работа csv

* Создайте список словарей с ключами name, age и job
* Запишите содержимое списка словарей в файл в формате csv

"""
import csv

users = [{"name": "Медет", "age": 32, "job":"CRM manager"},
         {"name": "Олжас", "age": 34, "job": "IT manager"},
         {"name": "Гани", "age": 30, "job": "Accountant"}]


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open ("file.csv", 'w', newline ='') as file:
        fields = ['name','age','job']
        writer = csv.DictWriter(file, fields, delimiter = ",")
        writer.writeheader()
        for person in users:
            writer.writerow(person)

if __name__ == "__main__":
    main()
