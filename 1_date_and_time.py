"""
Домашнее задание №2.1

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
import datetime

def print_days():
    dt_now = datetime.datetime.now()
    delta_1 = datetime.timedelta(days=1)
    delta_30 = datetime.timedelta(days=30)

    print(dt_now-delta_1)
    print(dt_now)
    print(dt_now-delta_30)


def str_2_datetime(date_string):
    datetime_obj = datetime.datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
    print(f'INFO: {datetime_obj=}   |   type: ', type(datetime_obj))
    return datetime_obj

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
