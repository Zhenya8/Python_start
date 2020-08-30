'''Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.'''

from random import choice


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'Car: {self.name}, color: {self.color}')

    def show_speed(self):
        print(f'Your speed: {self.speed} km/h')

    def go(self):
        print(f'GO!')

    def stop(self):
        print(f'STOP!')

    def turn(self):
        way = ['left', 'right']
        print(f'TURN: -', choice(way))


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Your speed: {self.speed} km/h is faster for town')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)
        print(f'Police car: {self.is_police}')


class WorkCar(Car):
    def go(self):
        if self.speed > 40:
            print(f'Your speed: {self.speed} km/h is faster for town')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name)
        self.is_police = True
        print(f'Police car: {self.is_police}')


print('-' * 70, 'Town Car', '-' * 70)
town = TownCar(70, 'black', 'Skoda')
town.show_speed()
town.stop()
town.turn()
print('-' * 70, 'Sport Car', '-' * 70)
sport = SportCar(220, 'pink', 'Ferrari')
sport.show_speed()
sport.go()
print('-' * 70, 'Work Car', '-' * 70)
work = WorkCar(40, 'red', 'Lada')
work.turn()
work.stop()
print('-' * 70, 'Police Car', '-' * 70)
police = PoliceCar(160, 'yellow', 'Mazda', True)
police.show_speed()
police.go()
police.turn()
# Не разобралась, как правильно переопределить переменную is_police для всех