'''Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.'''

def my_func(a, b, c):
    d = [a, b, c]
    d.remove(min(d))
    return sum(d)


print(my_func(11, 3, 12))

....................................................................................................................................................
def my_func(a):
    '''
    Функция для нахождения суммы чисел

    :param a: удаляем минимальное число

    :return: возвращаем сумму оставшихся значений
    '''
    a.remove(min(a))
    return sum(a)


a = [11, 3, 12]
print(my_func(a))
