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
    with open('referat.txt', 'r', encoding='utf-8') as f:

        # print(help(str.__len__))
        content = f.read()
        print(f'{content.__len__() = }')

        w_count = content.split()
        # print(w_count)
        print(f'{len(w_count) = }')

        dot_replace = content.replace('.', '!')
        # print(dot_replace)
        with open('referat2.txt', 'w', encoding='utf-8') as x:
            x.write(dot_replace)


if __name__ == "__main__":
    main()