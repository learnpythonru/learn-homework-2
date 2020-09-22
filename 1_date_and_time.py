'''Дата и время
1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime'''

from datetime import datetime, timedelta


def print_days():
    dt_now = datetime.now()
    format = '%Y-%m-%d'
    print((dt_now).strftime(format))
    delta = timedelta(days=1)
    print((dt_now - delta).strftime(format))
    delta30 = timedelta(days=30)
    print((dt_now - delta30).strftime(format))


def str_2_datetime(date_string):

        change_format = '%Y-%m-%d'
        print(datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f').strftime(change_format))


if __name__ == "__main__":
    print_days()
    str_2_datetime("01/01/20 12:10:03.234567")