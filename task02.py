# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных
# классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size, height, my_list):
        self.size = size
        self.height = height
        self.my_list = my_list

    def consumption_total(self, my_list):
        ct = sum(my_list)
        print(ct)

    @property

    def example_prop(self):
        self.my_str = "Как в методичке - сплошной print"
        print(self.my_str)

    @abstractmethod
    def absurd_method(self):
        return 'В стиле лекции по этой теме - полная абстракция от любого смысла'


class Coat(Clothes):

    def __init__(self, size):
        super().__init__(size, 0, 0)
        self.consumption = self.size / 6.5 + 0.5

    def __str__(self):
        return f'Расход ткани на пальто {self.consumption}'

    def absurd_method(self):
        pass


class Suit(Clothes):
    def __init__(self, height):
        super().__init__(0, height, 0)
        self.consumption = self.height * 2 + 0.3

    def __str__(self):
        return f'Расход ткани на костюм {self.consumption}'

    def absurd_method(self):
        pass


coat = Coat(65)
coat1 = Coat(650)
suit = Suit(6)
suit1 = Suit(60)
print(coat)
print(coat1)
print(suit)
print(suit1)

c = coat.consumption
c1 = coat1.consumption
s = suit.consumption
s1 = suit1.consumption

coat.consumption_total([c, c1, s, s1])
print(coat.example_prop)
