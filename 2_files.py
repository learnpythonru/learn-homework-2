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
    with open(r'referat.txt', 'r', encoding='utf-8') as f:
        for line in f:
            lines_count = 0
            line_len = len(line)
            lines_count += line_len
            with open(r'referat2.txt', 'a', encoding='utf-8') as ref2:
                ref2.write(f'Длина строки: {line} равна: {lines_count}')
                ref2.write('\n')
            lines_count = 0

    with open(r'referat.txt', 'r', encoding='utf-8') as f:
        for line in f:
            words = 0
            text = line.split(' ')
            words += len(text)
            with open(r'referat2.txt', 'a', encoding='utf-8') as ref3:
                ref3.write(f'Количество слов в строке: {words}')
                ref3.write('\n')
            words = 0

    with open(r'referat.txt', 'r', encoding='utf-8') as f:
        for line in f:
            text = line.replace('.', '!')
            with open(r'referat2.txt', 'a', encoding='utf-8') as ref4:
                ref4.write(text)


if __name__ == "__main__":
    main()
