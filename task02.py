# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина),
# width (ширина). Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия
# всего дорожного полотна. Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра
# дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    _length: float
    _width: float
    height: float
    weight_ton: float

    def __init__(self, _lenght, _width, height=5.0, weight_ton=25):
        self._length = _lenght
        self._width = _width
        self.height = height
        self.weight_ton = weight_ton

    def mass_calc(self):
        result = self._length * self._width * self.height * self.weight_ton / 1000
        print(f"Масса асфальта для покрытия дорожного полотна составляет: {result} тонн")


road_1 = Road(float(input("Введите длину дороги в метрах:")), float(input("Введите ширину дороги в метрах:")))
road_1.mass_calc()
