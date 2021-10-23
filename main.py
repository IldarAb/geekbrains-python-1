# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной
# платы сотрудника. В расчете необходимо использовать формулу:
# (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

import sys
from lesson4 import task01

try:
    file, hours, s_rate, bonus = sys.argv
except ValueError:
    print("Invalid args")
    exit()

print(task01.calc_salary(float(hours), float(s_rate), float(bonus)))

