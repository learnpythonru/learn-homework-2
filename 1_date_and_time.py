"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import date, datetime, timedelta

def print_days():

    dt_now = datetime.now()
    print(dt_now)
    delta = timedelta(days=1)
    dt_yesterday = dt_now - delta
    print(dt_yesterday)
    delta_1 = timedelta(days=30)
    dt_month = dt_now - delta_1
    print(dt_month)



from datetime import datetime
def str_2_datetime(date_string):
    
    timestring = datetime.strptime("01/01/20 12:10:03.234567", '%d/%m/%y %H:%M:%S.%f')
    print (timestring)

    
    
    

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
