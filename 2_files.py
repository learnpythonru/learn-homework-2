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
    with open('referat.txt', 'r', encoding='utf-8') as ref_file:
        file_content = ref_file.read()
    words = file_content.split()
    new_content = file_content.replace('.', '!')
    with open('referat2.txt', 'w', encoding='utf-8') as new_file:
        new_file.write(new_content)

    print('Длина содержащейся в файле строки: ', len(file_content))
    print('Количество слов в тексте: ', len(words))
    print('Всё сделано.')


if __name__ == "__main__":
    main()
