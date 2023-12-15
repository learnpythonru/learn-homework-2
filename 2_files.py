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
    with open("referat.txt", "r", encoding="utf-8") as file, open("referat2.txt", "w", encoding="utf-8") as answer:
        text = ""
        words = []
        for line in file:
            text += line
            words += line.split()
            new_line = line.replace(".", "!")
            answer.write(new_line)
        print(len(text)) #длина строки
        print(len(words)) #кол-во слов
        

if __name__ == "__main__":
    main()
