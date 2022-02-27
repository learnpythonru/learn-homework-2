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
    with open('referat.txt', 'r', encoding = 'utf-8') as f:
        ref_read = f.read()
    len_string = len(ref_read)
    count_words = len(ref_read.split())
    ref_read = ref_read.replace('.', '!')

    with open('referat2.txt', 'w', encoding = 'utf-8') as new:
        new.write(f'{ref_read}\n')

    with open('referat2.txt', 'a', encoding = 'utf-8') as new:
        new.write(f'Длина строки: {len_string}\nКоличество слов в тексте: {count_words}\n')

    return

if __name__ == "__main__":
    main()
