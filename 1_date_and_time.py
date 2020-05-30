"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

from datetime import datetime, timedelta

def print_days():
    current_date = datetime.now()
    yesterday = current_date - timedelta(days=1)
    minus_30_day = current_date - timedelta(days=30)
    print(f"Вчера - {yesterday:%Y/%m/%d}")
    print(f"Сегодня - {current_date:%Y/%m/%d}")
    print(f"30 дней назад - {minus_30_day:%Y/%m/%d}\r\n")

def str_2_datetime(date_string):
    print(f"Изначальная строка - {date_string}")
    converted_date = datetime.strptime(date_string, "%d/%m/%y %H:%M:%S.%f")
    return f"Тоже самое, но теперь в формате datetime - {converted_date:%d/%m/%y %H:%M:%S.%f}"
    

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
