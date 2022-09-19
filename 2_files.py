"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""


def words_count(content):

    content_count = content.split()
    word_count = 0
    for word in content_count:
        if len(word) != 0:
            word_count += 1
    return word_count


def replace_sign(f, content):
    return f.write(content.replace(".", "!"))


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open("referat.txt", "r", encoding="utf-8") as f:
        content = f.read()
        print(words_count(content))
    with open("referat2.txt", "w", encoding="utf-8") as f2:
        replace_sign(f2, content)


if __name__ == "__main__":
    main()
