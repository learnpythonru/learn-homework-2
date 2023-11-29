"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""


def main()->None:
    with open('referat.txt', 'r', encoding='utf-8') as f:
        content = f.read()
        print(content)
    length = len(content)
    print(f'Длинна строки: {length}')
    words = len(content.split())
    print(f'Количество слов = {words}')
    modifer_text = content.replace('.', '!')
    print(modifer_text)
    with open('referat2.txt', 'w') as text_file:
        text_file.write(modifer_text)


if __name__ == "__main__":
    main()
