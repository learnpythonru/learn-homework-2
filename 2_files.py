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

    with open('referat.txt', 'r') as f:
        content = f.read()
        content_len = len(content)
        content_word_count = len(content.split())
        content_replace = content.replace('.', '!')

    with open('referat2.txt', 'w') as f2:
        f2.write(str(content_len) + '\n')
        f2.write(str(content_word_count) + '\n')
        f2.write(content_replace)


if __name__ == "__main__":
    main()
