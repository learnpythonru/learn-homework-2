"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, timedelta


def print_days():
    dt_now = datetime.now()
    one_day = timedelta(days=1)
    delta_month = timedelta(days=30)
    dt_yesterday = dt_now - one_day
    dt_month = dt_now - delta_month 
    print(f'Вчера: {dt_yesterday}', f'сегодня: {dt_now}', f'30 дней назад: {dt_month}', sep='\n')


def str_2_datetime(date_string):
    date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
    return date_dt

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))



