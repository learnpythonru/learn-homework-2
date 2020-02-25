import csv
"""
Домашнее задание №2
Работа csv
* Создайте список словарей с ключами name, age и job
* Запишите содержимое списка словарей в файл в формате csv
"""
person_data =  [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
        {'name': 'Вася', 'age': 19, 'job': 'Programmer'},
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
        {'name': 'Артур', 'age': 20, 'job': 'Разносчик пиццы'},
        {'name': 'Ирина', 'age': 23, 'job': 'Процесс менеджер'},
        {'name': 'Глеб', 'age': 48, 'job': 'Парикмахер'},
        {'name': 'Наталья', 'age': 40, 'job': 'Начальник тендерного отдела'},
        {'name': 'Василиса', 'age': 30, 'job': 'Big boss'},
        {'name': 'Виталий', 'age': 26, 'job': 'Монтажник'}
 ]

def main():
    with open('data.csv', 'w', encoding="utf8") as res:
        d_keys = ["name", "age", "job"]
        writer = csv.DictWriter(res, d_keys, delimiter=';', newline='')
        writer.writeheader()
        for person in person_data:
            writer.writerow(person)

if __name__ == "__main__":
    main()
