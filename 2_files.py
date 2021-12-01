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
    
    with open('referat.txt', 'r', encoding='utf-8') as file:
        text = file.read()
        length = len(text)
        number_of_words = len(text.split())
        text_with_exclamation_marks = text.replace('.', '!')

    with open('referat2.txt', 'w', encoding='utf-8') as new_file:
        new_file.write(f'Длина всей строки: {length}\n')
        new_file.write(f'Количество слов в тексте: {number_of_words}\n\n')
        new_file.write(text_with_exclamation_marks)

if __name__ == "__main__":
    main()
