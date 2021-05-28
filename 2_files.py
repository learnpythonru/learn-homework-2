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
    with open('referat.txt', 'r', encoding='utf-8') as referat:
        for line in referat:
            str_length = len(line)

            words = line.split()
            number_words = len(words)

            #НЕ РАБОТАЕТ замена точек на воскл знаки и запись в файл referat2
            # exclaim = line.replace(".", "!")
            # with open('referat2.txt', encoding='utf-8') as referat2:
            #     referat2.write(exclaim)

            print(str_length)
            print(number_words)
            print('---')




if __name__ == "__main__":
    main()
