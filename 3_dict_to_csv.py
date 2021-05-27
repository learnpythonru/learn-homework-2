"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

import csv, random

jobs = ['токарь', 'пекарь', 'аптекарь', 'lawer', 'jobless']
my_list = []

def names_gen(l):
    f = ['бек', 'джан', 'ли', 'лей', 'слав']
    n = ['ив', 'ол', 'ал', 'ни', 'вла', 'эр', 'джэт']
    name = ''
    for c in range(l-(random.randrange(1))):
        name += random.choice(n)

    name += random.choice(f)
    return name


for e in range(100):
    entry = {'name':names_gen(2), 'age': random.randrange(15,63), 'job': random.choice(jobs)}
    my_list.append(entry)



def main():
    with open('test.csv', 'w', encoding='utf-8', newline='') as cf:
        fields = ['name', 'age', 'job']

        writer = csv.DictWriter(cf, fields, delimiter=';')
        writer.writeheader()
        for y in my_list:
            writer.writerow(y)


if __name__ == "__main__":
    main()
