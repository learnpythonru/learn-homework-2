"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
import datetime
from datetime import date

def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    today = date.today()

    yesterday = today - datetime.timedelta(days=1)
    yesterday_formated = yesterday.strftime("%B %d, %Y")
    print(yesterday_formated)

    today_formated = today.strftime("%B %d, %Y")
    print(today_formated)

    days_before = today - datetime.timedelta(days=30)
    days_before_formated = days_before.strftime("%B %d, %Y")
    print(days_before_formated)


def str_2_datetime(date_string):
    from datetime import datetime
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    date_dt1 = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
    return date_dt1

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
