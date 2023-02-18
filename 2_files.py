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
    with open('referat.txt', 'r', encoding='utf8') as f:
        str = f.read()
        len_str = len(str)
        words = 0
        for word in str.split():
            words += 1

    with open('referat2.txt', 'w', encoding='utf8') as text:
        point_to_exclamation_point = str.replace('.', '!')
        text.write(point_to_exclamation_point)

    return len_str, words

if __name__ == "__main__":
    main()
