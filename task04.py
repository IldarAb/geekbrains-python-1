# 4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed,
# color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, speed: int, color: str, name: str, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала.'

    def stop(self):
        return f'\n{self.name} остановилась.'

    def turn(self, direction):
        return f'\n{self.name} повернула {direction}'

    def show_speed(self):
        return f'\nскорость оставляет:{self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Ваша скорость превышает разрешенную и составляет {self.speed}!'
        else:
            return f'Ваша скорость составляет: {self.speed}'


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Ваша скорость превышает разрешенную и составляет {self.speed}!'
        else:
            return f'Ваша скорость составляет: {self.speed}'

class SportCar(Car):
    pass

class PoliceCar(Car):
    pass

towncar1 = TownCar(65, 'красный','Шкода рапид', False)
print(towncar1.go(), towncar1.show_speed(), towncar1.turn('направо'), towncar1.turn('направо'), towncar1.stop())

workcar1 = WorkCar(30, 'синий', 'Газель', False)
print(workcar1.go(), workcar1.show_speed(), workcar1.turn('налево'), workcar1.stop())

sportcar1 = SportCar(170, 'желтый', 'Ламборгини', False)
print(sportcar1.go(), sportcar1.show_speed(), sportcar1.turn('налево'), sportcar1.stop())


policecar1 = PoliceCar(100, 'черный', 'ДЖ-ЭМ-СИ', True)
print(policecar1.go(), policecar1.show_speed(), policecar1.turn('направо'), policecar1.stop())