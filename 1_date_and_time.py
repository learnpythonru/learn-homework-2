"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, date, timedelta

def print_days():
    today = date.today()
    yesterday = today - timedelta(days=1)
    thirty_days_ago = today - timedelta(days=30)
    print(f'Сегодня: {today.strftime("%d-%m-%Y")}')
    print(f'Вчера: {yesterday.strftime("%d-%m-%Y")}')
    print(f'30 дней назад: {thirty_days_ago.strftime("%d-%m-%Y")}')


def str_2_datetime(date_string):    
    date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
    return date_dt


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
