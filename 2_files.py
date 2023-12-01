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
        print(text)
        line_length = len(text)
        print(line_length)
        word_count = text.count(' ')
        print(word_count)
        
        ln_2 = text.replace('.', '!')
        print(ln_2)
    with open('referat2_2.txt', 'w', encoding='utf-8') as file:
        file.write(ln_2)

           

    
            
        
   
            
        
    
    


if __name__ == "__main__":
    main()
