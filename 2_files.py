"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0 
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки 
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

#import urllib.request
# urllib.request.urlretrieve('https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0', 'korneev.txt') # это было слишком просто, чтобы быть правдой. ссылка не прямая, скачался код всей страницы %)

def filesize(): 
    with open('referat.txt', 'r', encoding='utf-8') as f:
        print('Общее количество символов в файле (длина строки):' + str(len(f.read())))
        f.close() # этим надо заканчивать функцию работы с файлами?

def counter():
    with open('referat.txt', 'r', encoding='utf-8') as f:
        data = f.read()
        words = data.split() # метод для возвращения списка слов в строке
        print('Общее количество слов в тексте:', len(words)) 
        f.close()

def spaces_switch():
    with open("referat.txt", 'r', encoding='utf-8') as fr: # начальный файл для чтения
        with open("referat2.txt", 'w', encoding='utf-8') as fw: # т.к. данного файла нет -> создается для записи
                for line in fr.readlines(): # построчное чтение
                    line = line.replace('.', '!') # замена точек на восклицательный знак
                    fw.writelines(line) # запись во второй файл измененные строки первого

if __name__ == "__main__":
    filesize()
    counter()
    spaces_switch()