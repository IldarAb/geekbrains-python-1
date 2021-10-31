# 5. Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.

class Stationery:
    title: str

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки: {self.title}")


class Pen(Stationery):

    def draw(self):
        return f"Запуск отрисовки: {self.title}"


class Pencil(Stationery):

    def draw(self):
        return f"Запуск отрисовки: {self.title}"


class Handle(Stationery):

    def draw(self):
        return f"Запуск отрисовки: {self.title}"

pen = Pen('Ручка')
print(pen.draw())
pencil = Pencil('Карандаш')
print(pencil.draw())
handle = Handle('Маркер')
print(handle.draw())
