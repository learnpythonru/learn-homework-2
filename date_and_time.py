import datetime
"""
Домашнее задание №2
Дата и время
* Напечатайте в консоль даты: вчера, сегодня, месяц назад
* Превратите строку "01/01/17 12:10:03.234567" в объект datetime
"""
def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    today_date = datetime.date.today()
    yesterday_date = today_date - datetime.timedelta(days=1)
    month_ago = today_date - datetime.timedelta(days=31)
    print(f'Today date  is {today_date}, yesterday date is {yesterday_date}, a date that was month ago {month_ago}')
    
    
def str_2_datetime(string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    format_date = datetime.datetime.strptime(string, "%d/%m/%y %H:%M:%S.%f")
    return format_date

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/17 12:10:03.234567"))
