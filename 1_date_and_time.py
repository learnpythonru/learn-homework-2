"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

import datetime


def print_days() -> None:
    dt_now = datetime.date.today()
    print(dt_now)
    delta = datetime.timedelta(days=1)
    print(delta)
    yesterday = dt_now - delta
    print(yesterday)
    delta_30 = datetime.timedelta(days=30)
    print(dt_now - delta_30)


def str_2_datetime(date_string)-> datetime:

    format = "%d/%m/%y %H:%M:%S.%f"
    datetime_obj = datetime.datetime.strptime(date_string, format)
    return datetime_obj


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
