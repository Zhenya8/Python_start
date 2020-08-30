''' Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных атрибутов должны
передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т '''


class Road:

    def __init__(self, length, width):
        self._lenth = length
        self._width = width

    def asphalt(self):
        thickness = 5
        mass = 25
        return f'Потребуется {self._lenth * self._width * mass * thickness / 1000} т'


road66 = Road(float(input('Введите длину дороги: ')), float(input('Введите ширину дороги: ')))
print(road66.asphalt())