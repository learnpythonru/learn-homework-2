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
    from datetime import datetime, timedelta
    today=datetime.now()
    yesterday=today-timedelta(days=1)
    yesterday_formated=yesterday.strftime('%m/%d/%Y')
    today_minus_30=(today-timedelta(days=30)).strftime('%m/%d/%Y')
    print(yesterday_formated)
    print(today.strftime('%m/%d/%Y'))
    print(today_minus_30)


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    from datetime import datetime, timedelta
    datetime_str1=datetime.strptime(date_string, '%y/%m/%d %H:%M:%S.%f')
    return(datetime_str1)

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
