"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import date, datetime, timedelta


def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    dt_now = date.today()
    dt_yesterday = dt_now - timedelta(days=1)
    dt_30 = dt_now - timedelta(days=30)
    print(f'Сегодня {dt_now.strftime("%d.%m.%Y")}, вчера было {dt_yesterday.strftime("%d.%m.%Y")}, 30 дней назад {dt_30.strftime("%d.%m.%Y")}')


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    dt = datetime.strptime(date_string,"%m/%d/%y %H:%M:%S.%f")
    return dt

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
