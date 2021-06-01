"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

def main():
    import csv
    csv_columns = ['Name', 'Age', 'Job']
    dict_data = [
        {'Name': 'Dasha', 'Age': '26', 'Job': 'Scientist'},
        {'Name': 'Masha', 'Age': '27', 'Job': 'Painter'},
        {'Name': 'Pasha', 'Age': '28', 'Job': 'Sales manager'},
        {'Name': 'Sasha', 'Age': '29', 'Job': 'Teacher'},
        {'Name': 'Misha', 'Age': '30', 'Job': 'Gardener'},
    ]

    csv_file = "my_dictionary.csv"

    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns, delimiter=';')
            writer.writeheader()
            for data in dict_data:
                writer.writerow(data)
    except IOError:
        print("I/O error")

if __name__ == "__main__":
    main()



