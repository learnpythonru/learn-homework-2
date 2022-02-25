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
    with open('./referat.txt', encoding = 'utf-8') as f:
        content = f.read()
        num_of_words = content.split()
        print(len(content))
        print(len(num_of_words))
        replace_symbol = content.replace(".", "!")
        print("Im here")

    with open('referat2.txt', 'w', encoding = 'utf-8') as new:
        # new.write(replace_symbol)
        print(replace_symbol, file=new)
        
if __name__ == "__main__":
    main()
