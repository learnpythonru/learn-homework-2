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
    with open('referat.txt', 'r', encoding='utf-8') as referat:
        content = referat.read()
        print(len(content))
        words_in_content = len(content.split())
        print(words_in_content)
        replace_symbol = content.replace('.', '!')
        print(replace_symbol)
    with open('referat2.txt', 'w', encoding='utf-8') as referat2:
        content2 = referat2.write(replace_symbol)
        print(content2)


if __name__ == "__main__":
    main()
