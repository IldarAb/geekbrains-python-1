# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

while True:
    sentence = input('Введите несколько слов, разделяя их пробелами:')
    if sentence.count(' ') < 1:
        print('Вы ввели одно слово, введите несколько слов:')
        continue

    break

for number_string, word in enumerate(sentence.split(' ')):
    print(number_string + 1, word[:10])