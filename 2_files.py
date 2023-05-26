def main():
    with open('referat.txt', 'r', encoding='utf-8') as referat:
        original_text = referat.read()  # Прочитайте содержимое файла в переменную
    referat.close()
    print(f'Знаков: {len(original_text)}')   # Подсчитайте длину получившейся строки
    print(f'Слов: {len(original_text.split())}')   # Подсчитайте количество слов в тексте
    new_text = original_text.replace('.', '!')  # Замените точки в тексте на восклицательные знаки
    with open('referat2.txt', 'w', encoding='utf-8') as referat2:
        referat2.write(new_text)    # Сохраните результат в файл referat2.txt
    referat2.close()


if __name__ == "__main__":
    main()
