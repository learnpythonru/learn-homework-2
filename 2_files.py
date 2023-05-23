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
    with open('referat.txt', 'r', encoding='utf-8') as f:
        context = f.read()
    number_of_words = len(context.split())
    print(f'Количество слов составляет - {number_of_words}')

    replace_example = context.replace('.', '!')
    print(replace_example)
    with open('referat.txt', 'w', encoding='utf-8') as new_f:
        new_f.write(replace_example)


if __name__ == "__main__":
    main()
