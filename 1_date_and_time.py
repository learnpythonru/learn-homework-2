from datetime import datetime, date, timedelta
"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

def display_ymd(var):
    return datetime.strftime(var, "%Y-%m-%d")

def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    today = datetime.today()
    delta1 = timedelta(days=1)
    delta30 = timedelta(days=30)
    
    yesterday = today - delta1
    thirty_days_earlier = today - delta30
    print(f'Today is: {display_ymd(today)}')
    print(f'Yesterday used to be: {display_ymd(yesterday)}')
    print(f'Thirty days ago used to be: {display_ymd(thirty_days_earlier)}')


def str_to_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    return datetime.strptime(date_string[:24], "%m/%d/%y %H:%M:%S.%f")
    
if __name__ == "__main__":
    date_time_obj = str_to_datetime("01/01/20 12:10:03.234567")
    print(date_time_obj)
    print_days()