# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
#
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

rus_num = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
rus_text = []
try:
    with open('english.txt', 'r') as file:
        with open('russian.txt', 'w') as new_file:
            prev = file.readlines()
            for i in prev:
                i = i.split(' ', 1)
                rus_text.append(rus_num[i[0]] + ' ' + i[1])
            new_file.writelines(rus_text)
    with open('russian.txt') as d:
        print(d.read())
except IOError:
    print("Файл не обнаружен")
