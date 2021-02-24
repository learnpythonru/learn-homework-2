# Вывести последнюю букву в слове
# word = 'Архангельск'
# last_letter = word[-1]
# print(last_letter)


# Вывести количество букв "а" в слове
# word = 'Архангельск'.lower()
# amount_a = word.count('а')
# print(amount_a)

# Вывести количество гласных букв в слове
# word = 'Архангельск'
# vowels = 'ауоыиэяюёеАУОЫИЭЯЮЕЁ'

# i = 0
# for letter in vowels:
#     if letter in word: 
#         i += 1

# print(i)


# Вывести количество слов в предложении
# sentence = 'Мы приехали в гости'
# print(len(sentence.split()))


# Вывести первую букву каждого слова на отдельной строке
# sentence = 'Мы приехали в гости'

# for word in sentence.split(): 
#     print(word[0])

# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'

total_len_words = 0
for word in sentence.split():
    total_len_words += len(word)

average_len = total_len_words / len(sentence.split())
print(average_len)