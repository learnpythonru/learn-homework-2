import datetime 

"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

def print_days():
    dt_now = datetime.datetime.today()
    delta = datetime.timedelta(days=1)
    delta_30days = datetime.timedelta(days=30)

    yesterday = dt_now - delta
    today = datetime.datetime.today()
    thirty_days_ago = dt_now - delta_30days

    print(f'Вчера: {yesterday},\nСегодня: {today},\n30 дней назад: {thirty_days_ago}')

def str_2_datetime(date_string):
    obj_dt = datetime.datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
    return obj_dt

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
