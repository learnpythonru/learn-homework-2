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
    with open("referat.txt", "r", encoding="utf-8") as file:
        content = file.read()
    lenght = len(content)
    count_of_word = len(content.split(' '))
    new_str = content.replace(".", "!")
    with open("referat2.txt", "w", encoding="utf-8") as file:
        file.write(new_str)
    print(f"Длина строки: {lenght} символов, количество слов: {count_of_word}")
    

if __name__ == "__main__":
    main()
