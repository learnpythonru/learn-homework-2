from datetime import date, timedelta, datetime
from calendar import monthrange
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
    datetime_now = date.today()
    datetime_yesturday = datetime_now - timedelta(1,)
    month = date.today().strftime("%m")
    year = date.today().strftime("%Y")
    num_of_days = monthrange(int(year), int(month))
    datetime_month_ago = datetime_now - timedelta(num_of_days[1],)


    print(f"Вчера {datetime_yesturday}")
    print(f"Сегодня {datetime_now}")
    print(f'Месяц назад {datetime_month_ago}')

  


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
   
    date_result = datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')
    return date_result

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
