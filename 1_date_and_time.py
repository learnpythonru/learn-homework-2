"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, timedelta, date
def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    dt_now = datetime.now()
    print(f"Сегодня: {dt_now.strftime('%d.%m.%Y')}")

    delta_yesterday = timedelta(days=1)
    dt_yesterday = (dt_now - delta_yesterday).strftime('%d.%m.%Y')
    print(f"Вчера было: {dt_yesterday}")

    delta_30_days_age = timedelta(days=30)
    dl_30_days_ago = (dt_now-delta_30_days_age).strftime('%d.%m.%Y')
    print(f'30 дней назад дата была: {dl_30_days_ago}')


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    incorrect_format = '01/01/20 12:10:03.234567'
    date_time_obj = datetime.strptime(incorrect_format, '%d/%m/%y %H:%M:%S.%f')
    print(type(date_time_obj))
    print(date_time_obj)

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
