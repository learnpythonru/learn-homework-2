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
    with open('referat.txt','r',encoding='utf-8') as file:
        file_data = file.read()
        print('Длина строки:', len(file_data))
        words = file_data.split()
        print('Колличество слов в тексте:', len(words))
        file_data.replace('.', '!')

        with open('referat2.txt','w',encoding='utf-8') as file2:
            file2.write(file_data.replace('.', '!'))
            print(f'Файл был перезаписан в referat2.txt!')


if __name__ == "__main__":
    main()
