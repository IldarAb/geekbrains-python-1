# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в
# качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class Zero_div(Exception):
    def __init__(self, data):
        self.data = data


inp_data_1 = input("Введите делимое: ")
inp_data_2 = input("Введите делитель: ")

try:
    inp_data_1 = float(inp_data_1)
    inp_data_2 = float(inp_data_2)
    if inp_data_2 == 0:
        raise Zero_div("На ноль делить нельзя!")
except ValueError:
    print("Вы ввели не число!")
except Zero_div as err:
    print(err)
else:
    print(f"Частное равно: {inp_data_1 / inp_data_2}")
