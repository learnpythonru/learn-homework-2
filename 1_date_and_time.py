"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import date, datetime, timedelta
from my_log_settings import logger


def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    today_date = date.today()
    yesterday_date = (today_date - timedelta(1))
    thirty_days_ago = today_date - timedelta(30)
    logger.info(today_date.strftime('%d.%m.%Y'))
    logger.info(yesterday_date.strftime('%d.%m.%Y'))
    logger.info(thirty_days_ago.strftime('%d.%m.%Y'))


def str_2_datetime(date_string: str) -> datetime:
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    data_from_str = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
    return data_from_str


if __name__ == "__main__":
    print_days()
    logger.info(str_2_datetime("01/01/20 12:10:03.234567"))
