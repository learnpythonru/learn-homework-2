"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

import re


def main():
    with open('referat.txt', 'r', encoding = 'utf-8') as referat:
        
        for string in referat:
            print(len(string.split()))             #Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
            string = string.replace('.', '!')      #Замените точки в тексте на восклицательные знаки
            print(string)
        
    with open('referat.txt', 'r', encoding = 'utf-8') as referat:
        total = referat.read()
        total = total.replace('.', '!')
        print(len(total.split()))                  #Подсчитайте количество слов в тексте

    with open('referat2.txt', 'w', encoding = 'utf-8') as new:
        a = new.write(total)   

if __name__ == "__main__":
    main()
