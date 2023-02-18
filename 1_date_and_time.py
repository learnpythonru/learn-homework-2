"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import *


def print_days():
    date = datetime.now()
    delta_1 = timedelta(days=1)
    delta_30 = timedelta(days=30)
    date_1 = date - delta_1
    date_30 = date - delta_30
    return date.strftime('%d.%m.%Y'), date_1.strftime('%d.%m.%Y'), date_30.strftime('%d.%m.%Y')


def str_2_datetime(date_string):
    date = datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')
    return date

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
