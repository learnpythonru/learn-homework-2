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
    one_day = timedelta(days = 1)
    days_30 = one_day * 30
    today = date.today()
    yesterday = today - one_day
    days_30_ago = today - days_30

    print(f'\tВчера: {yesterday}\n\tСегодня: {today}\n\t30 дней назад: {days_30_ago}')
    
def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    this_date = datetime.strptime(date_string,'%d/%m/%y %H:%M:%S.%f' )
    return this_date

if __name__ == "__main__":
    print_days()
    print(str_2_datetime('01/01/20 12:10:03.234567'))
