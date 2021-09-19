import datetime
"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

def print_days():
    today = datetime.datetime.now() 
    yesterday = today - datetime.timedelta(days=1)
    back30 = today - datetime.timedelta(days=30)
    today = today.strftime("%d/%m/%Y")
    yesterday = yesterday.strftime("%d/%m/%Y")
    back30 = back30.strftime("%d/%m/%Y")
    print(f"Today is {today}")
    print(f"Yesterday is {yesterday}")
    print(f"30 dais ago is {back30}")

def str_2_datetime(date_string):
    str_to_date = datetime.datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
    print('Дата:', str_to_date.date())
    print('Время:', str_to_date.time())   

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
