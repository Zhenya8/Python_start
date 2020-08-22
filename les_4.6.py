'''Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие,
при котором повторение элементов списка будет прекращено.'''
from itertools import count, cycle, islice, repeat

for i in count(3):
    if i <= 10:
        print(i)
    else:
        break

print('-------------------------------------------------------------------------------------------------------------------------------')
for el in islice(count(3), 8):
    print(el)

print('-------------------------------------------------------------------------------------------------------------------------------')

counter = count(3)
print(list(next(counter) for i in range(8)))

print('-------------------------------------------------------------------------------------------------------------------------------')

count = 0
some_list = [None, [1, 2, 3], 'AaBbCcDdEeFf', 777, 1.0, {'a', 's'}]
for el in cycle(some_list):
    if count == 12:
        break
    else:
        print(el)
    count += 1

print('-------------------------------------------------------------------------------------------------------------------------------')

print([i for i in repeat([None, [1, 2, 3], 'AaBbCcDdEeFf', 777, 1.0, {'a', 's'}], 3)])