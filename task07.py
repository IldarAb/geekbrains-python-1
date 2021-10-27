# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка
# должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь
# со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json
try:
    my_dict = {}
    my_dict2 = {}
    with open("firms.txt", encoding='utf-8') as my_file:
        for_avg_profit = 0
        counter = 0
        my_list = my_file.readlines()
        for line in my_list:
            line = line.split()
            fin_result = float(line[2]) - float(line[3])
            key, value = line[0], fin_result
            my_dict[key] = value
        total_profit = sum(my_dict.values())
        for profit in my_dict.values():
            if profit > 0:
                for_avg_profit += profit
                counter += 1
                avg_profit = for_avg_profit/counter
                my_dict2["average_profit"] = avg_profit
        my_list = [my_dict, my_dict2]
        print(my_list)
    with open('firms.json', 'w', encoding='utf-8') as json_file:
        json.dump(my_list, json_file)

except IOError:
    print("Файл не обнаружен")