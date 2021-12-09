"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
#было не сложно, доки читать интересно)
from datetime import datetime, timedelta

def print_days(day):

    dt_now = datetime.now()
    result = dt_now - timedelta(days=day)
    print(result)

def str_2_datetime(date_string):
    new_date = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
    return (new_date)

if __name__ == "__main__":
    print_days(1)
    print_days(0)
    print_days(30)
    print(str_2_datetime("01/01/20 12:10:03.234567"))
