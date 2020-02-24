"""

Домашнее задание №2

Работа с файлами


* Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
* Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
* Подсчитайте количество слов в тексте
* Замените точки в тексте на восклицательные знаки
* Сохраните результат в файл referat2.txt
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open ('referat.txt', 'r') as readfile:
        content = readfile.read()
        length = len(content)
        print(length)
        count = content.split()
        count_length = len(count)
        print(count_length)
        content = content.replace('.','!')
    with open('referat2.txt', 'w') as readfile2:
        readfile2.write(content)

if __name__ == "__main__":
    main()
