"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import date, timedelta, datetime


def print_days():
    print(date.today() - timedelta(days=1))
    print(date.today())
    print(date.today() - timedelta(days=30))


def str_2_datetime(date_string):
    date_t = datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')
    print(type(date_t))
    return date_t


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
