# 1. Создать программно файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

with open('text_file.txt', 'w') as file:
    while True:
        user_data = input('Введите данные:')
        file.write(user_data + '\n')
        if not user_data:
            break
my_f = open('text_file.txt', 'r')
content = my_f.read()
print(content)
my_f.close()
