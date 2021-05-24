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
    f = open(r"/Users/filatov1-av/Downloads/referat.txt", "r")
    data = f.read()
    print(f"длина строки:",len(data))
    print(f"слов в строке:", len(data.split()))
    new_data = ''
    for x in data:
        if x != ".":
            new_data += x
        else:
            new_data += "!"
    print(new_data)
    newf = open("/Users/filatov1-av/Downloads/referat2.txt", "w+")
    newf.write(new_data)
    f.close()
    newf.close()

if __name__ == "__main__":
    main()
