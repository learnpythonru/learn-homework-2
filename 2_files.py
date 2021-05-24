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
    with open('referat.txt', 'r', encoding='utf-8') as ref:
        content = ref.read()
        print(content)
        print(len(content))
        print(len(content.split()))
        ref_2 = content.replace(".", "!")
        print(ref_2)
    with open('referat2.txt', 'a', encoding='utf-8') as f:
        f.write(ref_2)


if __name__ == "__main__":
    main()
