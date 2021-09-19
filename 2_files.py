"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""
path_to_file = '/Users/apetrov/Downloads/'
in_file = 'referat.txt'
out_file = 'referat2.txt'


def main():
    input_file_with_path = path_to_file + in_file
    output_file_with_path = path_to_file + out_file
    with open(input_file_with_path) as file:
        file_content = file.read()
    text_len = len(file_content)
    print(f'Text lenght are {text_len} simbols')
    words = file_content.split()
    counted_words = len(words)
    print(f'Number of words are {counted_words} words')
    with open(output_file_with_path, 'w+') as file_out:
        file_out.write(file_content.replace('.', '!'))


if __name__ == "__main__":
    main()
