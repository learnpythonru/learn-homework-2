"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

def print_days():
    from datetime import datetime, timedelta

    dt_today = datetime.now()
    dt_today.strftime('%d.%m.%Y %H:%M')
    print(dt_today)

    delta1 = timedelta(days=1)
    dt_yesterday = dt_today - delta1
    dt_yesterday.strftime('%d.%m.%Y %H:%M')
    print(dt_yesterday)

    delta2 = timedelta(days=30)
    dt_month_ago = dt_today - delta2
    dt_month_ago.strftime('%d.%m.%Y %H:%M')
    print(dt_month_ago)

# Превратите строку "01/01/20 12:10:03.234567" в объект datetime
def str_2_datetime(date_string):
    from datetime import datetime

    # date_string = '01/01/20 12:10:03.234567'
    date_dt = datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')
    print(date_dt)

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
