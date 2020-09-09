'''Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.'''


class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Complex((self.a * other.a - self.b * other.b), (self.a * other.b + self.b * other.a))

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


z_1 = Complex(1, -5)
z_2 = Complex(13, 4)
z_3 = Complex(2, -3)

print(z_1)
print(z_1 + z_2 + z_3)
print(z_1 * z_2 * z_3)
