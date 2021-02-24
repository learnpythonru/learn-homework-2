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

    with open('referat.txt', 'r', encoding='utf-8') as essay:
        content = essay.read()

        len_essay = len(content)
        print(f'Количество символов: {len_essay}')

        words_amount = len(content.split())
        print(f'Количество слов: {words_amount}')

        new_content = content.replace('.', '!')
    
    with open('referat2.txt', 'w', encoding='utf-8') as new_essay: 
        new_essay.write(new_content)

if __name__ == "__main__":
    main()
