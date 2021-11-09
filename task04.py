# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Stock:
    name: str
    max_count: int
    equipment: dict

    def __init__(self, name, equipment, max_count):
        self.name = name
        self.equipment = equipment
        self.max_count = max_count


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
