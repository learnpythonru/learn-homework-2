"""
Домашнее задание №2
Работа с файлами
* Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
* Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
* Подсчитайте количество слов в тексте
* Замените точки в тексте на восклицательные знаки
* Сохраните результат в файл referat2.txt
"""
def main():
    with open("referat.txt", "r", encoding="utf8") as r:
        data = r.read()
        lenth_of_string = f"Quantity of strings {len(data)}\n"
        words = data.split()
        quantity_of_wrods = f"Quantity of words is {len(words)}\n"
        replace_dots = data.replace(".", "!")

    with open("referat2.txt", "w", encoding="utf8") as writer:
        writer.write(lenth_of_string)
        writer.write(quantity_of_wrods)
        writer.write(replace_dots)


if __name__ == "__main__":
    main()
