"""
Домашнее задание №2

Работа с файлами

"""

def main():
    with open("referat.txt", "r", encoding="utf-8") as input_file, open("referat2.txt", "w", encoding="utf-8") as output_file:
        full_text = input_file.read()
        len_full = len(full_text)
        words_count = len(full_text.split())
        full_text = full_text.replace(".", "!")
        print(f"Всего символов: {len_full}", f"Всего слов: {words_count}", full_text, sep="\n", file=output_file)

if __name__ == "__main__":
    main()
