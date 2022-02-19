"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, timedelta


def print_days() -> None:
    """The function outputs the specified dates to the console.

    The function outputs to the console: today, yesterday, 30 days ago.
    """
    number_of_days_ago = 30
    today: datetime = datetime.now()
    delta_days: timedelta = timedelta(days=1)
    dates: list[datetime] = [today]
    dates.append(today - delta_days)
    dates.append(today - delta_days * number_of_days_ago)
    for day in dates:
        print(day.strftime('%d-%m-%y'))


def str_2_datetime(date_string: str) -> datetime:
    """The function convert date from string to datetime object.

    Args:
        date_string (str): date as strihg.

    Returns:
        datetime: set date as datetime object.
    """
    return datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')


if __name__ == '__main__':
    print_days()
    print(str_2_datetime('01/01/20 12:10:03.234567'))
