'''Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123]'''
from random import randint

orig_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([orig_list[el] for el in range(1, len(orig_list)) if orig_list[el] > orig_list[el - 1]])

print('-' * 50)

new_list = [randint(0, 200) for _ in range(10)]
print(new_list)
print([new_list[el] for el in range(1, len(new_list)) if new_list[el] > new_list[el - 1]])

print('-' * 50)

my_list = [int(i) for i in input('Enter some symbols: ').split()]
print(my_list)
print([my_list[el] for el in range(1, len(my_list)) if my_list[el] > my_list[el - 1]])