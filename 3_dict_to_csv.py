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
csv_columns = ['Name','Age','Job'] 

dict_data = [ 
    {'Name': 'Alex', 'Age': 26, 'Job': 'Software Engineer'}, 
    {'Name': 'Sam', 'Age': 32, 'Job': 'Consultant'},  
    {'Name': 'Eric', 'Age': 34, 'Job': 'Policeman'}, 
    {'Name': 'Tom', 'Age': 21, 'Job': 'Business Assistant'},  
    {'Name': 'Phil', 'Age': 22, 'Job': 'Courier'}, 

] 

csv_file = "Names.csv" 

try: 
    with open(csv_file, 'w') as csvfile: 
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns) 
        writer.writeheader() 
        for data in dict_data: 
            writer.writerow(data)
except IOError: print("I/O error")


if __name__ == "__main__":
    main()
