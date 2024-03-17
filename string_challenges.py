# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
count = 0
for i in word:
    count += 1

print(count)

# Вывести количество гласных букв в слове
word = 'Архангельск'

lowel_letters = ('а', 'я', 'я', 'ю', 'о', 'е', 'ё', 'э', 'и', 'ы')
lowel_count = 0

for i in word:
    if i.lower() in lowel_letters:
        lowel_count += 1

print(lowel_count)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'

words_count = sentence.split()

print(len(words_count))



# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'

first_letters = []

for i in words_count:
    first_letters.append(i[0])

print(first_letters)


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'

split_words = sentence.split()



letters_sum = 0

for i in split_words:
    letters_sum += len(i)
    
average_word = letters_sum / len(split_words)

print(int(average_word))





