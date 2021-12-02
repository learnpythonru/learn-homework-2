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
def main():
    with open('referat.txt', 'r', encoding='utf-8') as f:
    
        for line in f:
            line = line.replace('\n', '')
            print(len(line.strip())) #кол-во символов по абзацам
            line = line.replace('.', '!')
            print(line)





if __name__ == "__main__":
    main()