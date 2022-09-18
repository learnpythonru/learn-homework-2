"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

from datetime import datetime, timedelta


def formatted_date_shifted_on(count_day=0):

    return datetime.strftime(datetime.now() + timedelta(days=count_day), "%d.%m.%Y")


def print_days():
    print(
        f"Вчера: {formatted_date_shifted_on(-1)},")
    print(f"Сегодня: {formatted_date_shifted_on()},")
    print(f"30дней назад: {formatted_date_shifted_on(-30)}")


def str_2_datetime(date_string):

    time = datetime.strptime(date_string, "%d/%m/%y %H:%M:%S.%f")
    
    return time


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
