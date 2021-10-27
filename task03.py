# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину
# их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

try:
    with open('salary.txt', 'r') as my_file:
        salary = []
        poor = []
        my_list = my_file.readlines()
        for i in my_list:
            i = i.split()
            if float(i[1]) < 20000.00:
                poor.append(i[0])
            salary.append(i[1])
        print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(float, salary)) / len(salary)}')
except IOError:
    print("Файл не обнаружен")
