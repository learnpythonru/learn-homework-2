import csv 
"""
Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    name_age_job = [
        {'name': 'Bjorn', 'age': 19},
        {'name': 'John', 'age': 99, 'job': 'athlete'},
        {'name': 'Kshishtof', 'age': 79, 'job': 'director'},
        {'name': 'Kate', 'age': 33, 'job': 'surfer'},
        {'name': 'Alisa', 'age': 22, 'job': 'developer'}  
    ]
    with open('example4.csv', 'w', newline='', restval='raise') as csvfile:
        fieldnames = ['name', 'age', 'job']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(name_age_job)
        
    print("Writing complete")

if __name__ == "__main__":
    main()
