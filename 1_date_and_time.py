"""
Домашнее задание №2

"""
from datetime import datetime, timedelta, date

def print_days():
    today = date.today()
    yesterday = today - timedelta(days=1)
    month_ago = today.month - 1
    date_month_ago = date(today.year,  month_ago, today.day)
    print(today, yesterday, date_month_ago, sep = "\n")


def str_2_datetime(date_string):
    date_format = datetime.strptime(date_string, "%d/%m/%y %H:%M:%S.%f")
    return date_format

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
