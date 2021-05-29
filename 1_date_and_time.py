"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03" в объект datetime

"""
from datetime import datetime, timedelta


def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    date_format = '%d.%m.%Y'
    dt_now = datetime.now()
    dt_yesterday = dt_now - timedelta(days=1)
    dt_month_ago = dt_now - timedelta(days=30)
    print('сегодня:', dt_now.strftime(date_format))
    print('вчера:', dt_yesterday.strftime(date_format))
    print('30 дней назад:', dt_month_ago.strftime(date_format))


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
    return date_dt


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
