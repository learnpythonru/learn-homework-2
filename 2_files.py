"""
Домашнее задание №2

Работа с файлами

1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в переменную, подсчитайте длину получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    with open('referat.txt', 'r', encoding='utf-8') as my_file:
        text = my_file.read()
        print('Length: ', len(text))
        # print(text)

        words_count = text.split()
        print('Number of words: ', len(words_count))

        for text_lines in my_file:
            text_lines = text_lines.replace('.', '!')
            print(text_lines)

if __name__ == "__main__":
    main()
