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

    str1 = ''
    num_of_words = 0
    with open('.\\referat.txt','r', encoding='utf-8') as fi, open('.\\referat2.txt','w', encoding='utf-8') as fo:
        for line in fi:
            a = line.rstrip() + ('\n')
            str1 += a
            num_of_words += len(a.split())
            a = a.replace('.', '!')
            fo.write(a)
    print('Длина файла, как одной строки :', len(str1))
    print('Количество слов в файле : ', num_of_words)



if __name__ == "__main__":
    main()
