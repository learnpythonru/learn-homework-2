"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
import datetime as dt
from datetime import timedelta


def print_days():

    today = dt.today()
    delta = timedelta(days=1)
    yesterday = today - delta
    days_30 = today - 30*delta
    
    print(today, yesterday, days_30)


def str_2_datetime(date_string):
    date_object = dt.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
    return date_object


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))