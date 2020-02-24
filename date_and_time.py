"""

Домашнее задание №2

Дата и время

* Напечатайте в консоль даты: вчера, сегодня, месяц назад
* Превратите строку "01/01/17 12:10:03.234567" в объект datetime

"""
import datetime
from dateutil.relativedelta import relativedelta

def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    date_now = datetime.date.today()
    date_yesterday = date_now - datetime.timedelta(days=1)
    delta = relativedelta(month=1)
    date_month = date_now - delta

    print(date_yesterday)
    print(date_now)
    print(date_month)
    
def str_2_datetime(string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    x = datetime.datetime.strptime(string,"%d/%m/%y %H:%M:%S.%f")
    return x

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/17 12:10:03.234567"))
