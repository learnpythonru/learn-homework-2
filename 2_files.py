"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

import requests
import re
from html.parser import HTMLParser

class MLStripper(HTMLParser):
    """
    Class for stripping Html Tags
    """
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []

    #this function takes html string as input and put data in
    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    url = 'https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0'
    r = requests.get(url, allow_redirects=True)
    open('referat1.txt', 'wb').write(r.content)
    with open('referat1.txt','r') as f:
          output = f.read()
          print('Lenght of the string is {0}'.format(len(output)))
          word_string = strip_tags(output)
          words = re.findall(r'\w+', word_string)
          print('Count of words {0}'.format(len(words)))
          with open("referat2.txt", "w") as text_file:
               text_file.write(output.replace('.','!'))
          print("Done!")


if __name__ == "__main__":
    main()
