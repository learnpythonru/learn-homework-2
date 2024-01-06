"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
import datetime

def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    print ('Текущая дата и время: {}'.format(datetime.datetime.now()))
    
    print ('Вчерашняя дата: {}' .format(datetime.datetime.now() - datetime.timedelta(days = 1)) )

    



def str_2_datetime():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

date_time_str = '01/01/20 12:10:03.234567'
date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')
print('Дата:', date_time_obj.date())
print('Время:', date_time_obj.time())
print('Дата и время:', date_time_obj)

 

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
