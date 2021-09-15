import locale
from datetime import datetime, timedelta
"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""


def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    locale.setlocale(locale.LC_ALL, "russian")
    date_now = datetime.now()
    delta_1 = timedelta(days=1)
    date_1 = date_now - delta_1
    print('Вчера: ' + date_1.strftime('%A %d %B %Y'))
    print('Сегодня: ' + date_now.strftime('%A %d %B %Y'))
    delta_30 = timedelta(days=30)
    date_30 = date_now - delta_30
    print('30 дней назад: ' + date_30.strftime('%A %d %B %Y'))


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
