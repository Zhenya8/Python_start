# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». В рамках класса
# реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй,  с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу
# полученной структуры на реальных данных.

class Data:
    def __init__(self, data):
        self.data = str(data)

    @classmethod
    def get_data(cls, data):
        y_m_d = []
        for i in data.split('-'):
            if i != '-':
                y_m_d.append(i)

        return f'{int(y_m_d[0]):02d} - {int(y_m_d[1]):02d} - {int(y_m_d[2])}'

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 9999 >= year >= 0:
                    return day, month, year
                else:
                    return f'Incorrectly entered year!'
            else:
                return f'Incorrectly entered month!'
        else:
            return f'Incorrect entered day!'


data = Data('01 01 1000')
print(data.data)
print(data.get_data('08-02-2020'))
print(data.valid(1, 13, 2100))
print(data.valid(41, 13, 2100))
print(data.valid(1, 11, 2100))

