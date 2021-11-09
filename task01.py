# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
# формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором
# @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

import datetime


class Data:
    def __init__(self, my_string):
        self.my_string = my_string
        print(my_string)

    @classmethod
    def extract_number(cls, my_string):
        try:
            day, month, year = [int(el) for el in my_string.split('-')]
            return f"{type(day), day}\n{type(month), month}\n{type(year), year}"
        except ValueError:
            return 'Необходимо указать день, месяц и год в заданном формате!'

    @staticmethod
    def check_date(my_string):
        try:
            day, month, year = my_string.split('-')
            datetime.datetime(int(year), int(month), int(day))
            return 'Введенная дата валидирована!'
        except ValueError:
            return 'Введенная дата не существует!'


a = Data(input(f'Введите дату в формате "день-месяц-год":'))
b = input(f'Введите дату в формате "день-месяц-год":')
print(Data.extract_number(b))
print(Data.check_date(b))
