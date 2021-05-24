"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime


today = datetime.strptime(str(date.today()), "%Y-%m-%d").strftime('%Y/%m/%d')

"""
from datetime import datetime, date, time

def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    now = datetime.now()
    yesterday = '{:%Y%m}{}'.format(now, now.day - 1)  # Вчерашний день
    day30_ago = '{:%Y%m}{}'.format(now, now.day - 30)  # 30 дней назад

    ans_string = "Даты: вчера:{}, сегодня:{}, 30 дней назад:{} ".format(yesterday,now,day30_ago)
    print(ans_string)

def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    return datetime.strptime(date_string.split(".")[0], '%d/%m/%y %H:%M:%S')



if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
