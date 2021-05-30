"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

import random
import csv

def _generate_list(amount:int, names: list, jobs:list) -> list:
    finall_list = []
    for i in range(int(amount)):
        name = random.choice(names)
        age = random.randint(18, 55)
        job = random.choice(jobs)
        finall_list.append({"name":name, "age":age, "job":job})
    return finall_list
    

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    names=["Валера","Олег", "Сергей", "Игорь", "Александр", "Йован", "Валентин", "Артем"]
    jobs = ["Программист","Стомтатолог", "Архитектор", "Дизайнер", "Фотограф", "Бухгалтер", "Инженер","Летчик"]

    generated_list = _generate_list(100, names, jobs)

    csv_file = "example.csv"
    try:
       with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["name","age","job"])
        writer.writeheader()
        for data in generated_list:
            writer.writerow(data)
    except IOError:
         print("I/O error")

if __name__ == "__main__":
    main()
