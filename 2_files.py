"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длину получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""


def main():
    with open('referat.txt', 'r', encoding='UTF-8') as myfile:
        content = myfile.read()
        print(f'Длина получившейся строки: {len(content)}')
        print(f'Количество слов: {len(content.split())}')

    with open('referat2.txt', 'w', encoding='UTF-8') as new_file:
        new_file.write(content.replace('.', '!'))


if __name__ == "__main__":
    main()
