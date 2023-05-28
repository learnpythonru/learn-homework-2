def main():
    with open('referat.txt', 'r', encoding='utf-8') as file_handler:
        original_text = file_handler.read()  # Прочитайте содержимое файла в переменную
    print(f'Знаков: {len(original_text)}')   # Подсчитайте длину получившейся строки
    print(f'Слов: {len(original_text.split())}')   # Подсчитайте количество слов в тексте
    new_text = original_text.replace('.', '!')  # Замените точки в тексте на восклицательные знаки
    with open('referat2.txt', 'w', encoding='utf-8') as new_file_handler:
        new_file_handler.write(new_text)    # Сохраните результат в файл referat2.txt


if __name__ == "__main__":
    main()
