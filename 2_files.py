"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке
https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную,
подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

from my_log_settings import logger


FIRST_FILE = 'referat.txt'
SECOND_FILE = 'referat2.txt'


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    with (open(FIRST_FILE, 'r', encoding='utf-8') as first_file,
            open(SECOND_FILE, 'w', encoding='utf-8') as second_file):
        file_text = first_file.read()
        logger.info(len(file_text))
        logger.info(len(file_text.split()))

        file_text = file_text.replace('.', '!')
        second_file.write(file_text)


if __name__ == "__main__":
    main()
