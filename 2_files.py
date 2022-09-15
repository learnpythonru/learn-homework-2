"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

from multiprocessing import context


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('referat.txt', 'r', encoding='utf-8') as f:
         content = f.read()
         print(content.split())
         print(f'Длина строки – {len(content)}. \nВ тексте {len(content.split())} слов(а).')
    with open('referat2.txt', 'w', encoding='utf-8') as f2:
        f2.write(content.replace(".", "!"))

if __name__ == "__main__":
    main()
