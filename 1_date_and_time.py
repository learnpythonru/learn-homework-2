"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

from datetime import datetime

import locale

def print_days():
    
    locale.setlocale(locale.LC_ALL, "russian")

    dt_yesterday = datetime(2022, 2, 21)
    yesterday = dt_yesterday.strftime('%A %d %B %Y')
    dt_now = datetime(2022, 2, 22)
    now = dt_now.strftime('%A %d %B %Y')
    dt_30_ago = datetime(2022, 1, 22)
    ago_30 = dt_30_ago.strftime('%A %d %B %Y')
    print(f'{yesterday}, {now}, {ago_30}')
    
  

def str_2_datetime(date_string):


    date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f') 
    return date_dt

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))  
