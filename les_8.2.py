'''Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.'''


class MyError(Exception):
    def __init__(self, text):
        self.txt = text


divident = input("Input an integer: ")
denominator = input("Input an integer: ")

try:
    divident = int(divident)
    denominator = int(denominator)
    if denominator == 0:
        raise MyError("You cannot divide by zero!")
except ValueError:
    print("Error type of value!")
except MyError as error:
    print(error)
else:
    print(round((divident / denominator), 2))
