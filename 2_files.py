"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    read_string = ''
    try:
        with open('referat.txt', 'r', encoding='UTF-8') as read_file:
            while True:
                line = read_file.readline()
                if not line:
                    break
                else:
                    read_string += line

    except (IOError, FileNotFoundError) as e:
        print(e)
    print(read_string)
    print(len(read_string.split()))
    print(read_string.replace('.', '!'))
    try:
        with open('referat2.txt', 'w', encoding='UTF-8') as write_file:
            write_file.write(read_string.replace('.', '!'))
    except (IOError, FileNotFoundError) as e:
        print(e)


if __name__ == "__main__":
    main()
