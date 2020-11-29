from datetime import datetime, timedelta
import locale

"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

def print_days():
    locale.setlocale(locale.LC_ALL, "russian")
    dt_now = datetime.now()
    dt_yesterday =  dt_now - timedelta(days=1)
    dt_30ago = dt_now - timedelta(days=30)
    print('Вчера было '+ dt_yesterday.strftime('%A %d %B %Y'))
    print('Сейчас ' + dt_now.strftime('%A %d %B %Y'))
    print('30 дней назад было ' + dt_30ago.strftime('%A %d %B %Y'))
    

def str_2_datetime(date_string):
    return datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))

