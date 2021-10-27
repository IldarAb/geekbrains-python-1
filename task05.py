# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

# with open('numbers.txt', 'w') as file:

try:
    with open('numbers.txt', 'w+') as file_obj:
        line = input('Введите цифры через пробел:')
        file_obj.writelines(line)
        my_numb = line.split()
        print(sum(map(float, my_numb)))
except ValueError:
    print('Необходимо вводить числовые значения, разделенные пробелами!')

