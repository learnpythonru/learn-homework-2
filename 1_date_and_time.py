"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import date, datetime,timedelta
def print_days():
    dt_now = datetime.now()
    delta = timedelta(days=1)
    delta_2 = timedelta(days=30)
    yesterday = dt_now - delta
    delta_days_ago = dt_now - delta_2

    return dt_now, yesterday, delta_days_ago 

def str_2_datetime(date_string):
    print_days = datetime.strptime("01/01/20 12:10:03.234567", "%m/%d/%y %H:%M:%S.%f")
    return print_days

if __name__ == "__main__":
    print(print_days())
    print(str_2_datetime("01/01/20 12:10:03.234567"))
