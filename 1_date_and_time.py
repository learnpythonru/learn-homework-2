import datetime


# Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
def print_days():
    current_date = datetime.date.today()
    daily_delta = datetime.timedelta(days=1)
    monthly_delta = datetime.timedelta(days=30)
    print(current_date.strftime('%d/%m/%Y'))
    print((current_date - daily_delta).strftime('%d/%m/%Y'))
    print((current_date - monthly_delta).strftime('%d/%m/%Y'))


# Превратите строку "01/01/20 12:10:03.234567" в объект datetime
def str_2_datetime(date_string):
    return datetime.datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')


def main():
    print_days()
    print(str_2_datetime('01/01/20 12:10:03.234567'))


if __name__ == "__main__":
    main()
