''' Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage,
"bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения полного имени
сотрудника  (get_full_name) и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров). '''


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f'A full name of worker is: {self.name} {self.surname}'

    def get_total_income(self):
        return f"{self.name} {self.surname} earns per month: {self._income['wage'] + self._income['bonus']}$"


man = Position(input('Enter a name: '), input('Enter a surname: '), input('Enter a position: '), float(input('Enter a wage per month: ')),
               float(input('Enter a bonus: ')))
print(man.get_full_name())
print(man.get_total_income())