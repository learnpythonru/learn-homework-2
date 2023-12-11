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
    with open('referat.txt','r', encoding='utf-8') as f:
        str=f.read()
        len_str=len(str)
        print(len_str)
        words=str.split()
        len_words=len(words)
        print(len_words)
    
    with open('referat2.txt','w', encoding='utf-8') as f2:
        content=str.replace('.', '!')
        f2.write(content)

if __name__ == "__main__":
    main()
