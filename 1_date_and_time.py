from datetime import date, timedelta, datetime
"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""


def print_days(days):
    dt = date.today()
    print(dt - days)


def str_2_datetime(date_string):
    date_dt = datetime.strptime(date_string, "%m/%d/%y %H:%M:%S.%f")
    return date_dt


if __name__ == "__main__":
    print_days(timedelta(days=0))
    print_days(timedelta(days=1))
    print_days(timedelta(days=30))
    print(str_2_datetime("01/01/20 12:10:03.234567"))
