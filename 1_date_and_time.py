from datetime import datetime, timedelta, date
"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

def print_days() -> str:
    dt_today = datetime.now().strftime("%d.%m.%Y")    
    dt_yesterday = (datetime.now() - timedelta(days=1)).strftime("%d.%m.%Y")
    dt_30_days_before = dt_yesterday = (datetime.now() - timedelta(days=30)).strftime("%d.%m.%Y")
    print(f"Вчера: {dt_yesterday}, сегодня: {dt_today}, 30 дней назад: {dt_30_days_before}")


def str_2_datetime(date_string: str) -> datetime:
    date_dt = datetime.strptime(date_string, "%m/%d/%y %H:%M:%S.%f")
    return date_dt

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
