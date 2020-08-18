'''Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.'''


def division(a, b):
    try:
        return round(float(a) / float(b), 2)
    except ZeroDivisionError:
        return 'You cannot divide by zero!'
    except ValueError:
        return 'Enter only the number!'


print(division(input('Enter the number: '), input('Enter the number: ')))
