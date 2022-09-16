"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

from datetime import datetime, timedelta


def get_date(count_day=0):

    return datetime.strftime(datetime.now() + count_day * timedelta(days=1), "%d.%m.%Y")


def print_days():

    print(
        f"Вчера: {get_date(-1)}, \nСегодня: {get_date()},\n30дней назад: {get_date(-30)}"
    )


def str_2_datetime(date_string):
    date_string = date_string.replace("/", " ").replace(":", " ")
    date_string = date_string.replace(".", " ")
    date_string = date_string.split()
    for element in range(len(date_string)):
        date_string[element] = int(date_string[element])
    date_time = datetime(
        date_string[2],
        date_string[1],
        date_string[0],
        date_string[3],
        date_string[4],
        date_string[5],
    )
    return date_time.strftime("%d.%m.%Y %H:%M:%S")


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
