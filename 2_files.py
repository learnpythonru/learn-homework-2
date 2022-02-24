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
with open('referat.txt', 'r', encoding = 'utf-8') as text_file:
    this_text = text_file.read()
    line_string = str(len(this_text))
    number_words = this_text.split()
    change_sings = this_text.replace('.', '!')

with open('referat2.txt', 'w', encoding = 'utf-8') as text_file:
    text_file.write(change_sings )
   



if __name__ == "__main__":
    print(this_text)
    print(f'\nДлина строки: {line_string}')
    print('\nКоличество слов в тексте:', len(number_words))
    main()
