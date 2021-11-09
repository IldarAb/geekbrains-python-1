# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем
# данных. Например, для указания количества принтеров, отправленных на склад, нельзя использовать
# строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум
# возможностей, изученных на уроках по ООП.

class CapacityException(Exception):
    def __init__(self, current, needle):
        self.current = current
        self.needle = needle

    def __str__(self):
        return f'Недостаточно места, текущее свободное место - {self.current}, необходимо - {self.needle}'


class Stock:
    max_count: int
    equipment: list

    def __init__(self, count=3):
        self.max_count = count
        self.equipment = []

    def store(self, equipment: list):
        # проверяем перед расширением списка максимальную вместимость склада
        if sum(self.equipment) >= self.max_count:
            raise CapacityException(self.max_count-sum(self.equipment), sum(self.equipment)-sum(equipment))
        elif sum(equipment) > (self.max_count - sum(self.equipment)):
            raise CapacityException(self.max_count-sum(self.equipment), sum(self.equipment)-sum(equipment))
        self.equipment.extend(equipment)


class Equipment:
    name: str
    model: str
    purchase_price: float
    quantity: int

    def __init__(self, name, model, purchase_price, quantity):
        self.name = name
        self.model = model
        self.purchase_price = purchase_price
        self.quantity = quantity


class Printer(Equipment):

    def __init__(self, name, model, purchase_price, quantity, printer_type):
        super().__init__(name, model, purchase_price, quantity)
        self.name = 'printer'
        self.printer_type = printer_type


class Scanner(Equipment):

    def __init__(self, name, model, purchase_price, quantity, scanner_type):
        super().__init__(name, model, purchase_price, quantity)
        self.name = 'scanner'
        self.scanner_type = scanner_type


class Xerox(Equipment):

    def __init__(self, name, model, purchase_price, quantity, xerox_type):
        super().__init__(name, model, purchase_price, quantity)
        self.name = 'xerox'
        self.xerox_type = xerox_type


stock = Stock(5)
my_list = [3]
stock.store(my_list)
print(stock.equipment)
my_list2 = [1]
stock.store(my_list2)
print(stock.equipment)
my_list3 = [2]
stock.store(my_list3)
print(stock.equipment)