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
    with open('referat.txt', 'r', encoding='utf-8') as f:  
        text = f.read()
        get_text = len(text)
        words = len(text.split())
        get_word = text.replace('.', '!')
        print(text, get_text, words, get_word)

        with open('referat2.txt', 'w', encoding='utf-8') as new_f: 
            new_f.write(text)


if __name__ == "__main__":
    main()
