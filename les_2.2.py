'''Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input()'''

my_list = []
n = int(input('How long the list do you want: '))

for _ in range(n):
    elem = input('Enter some element: ')
    my_list.append(elem)

print(my_list)

for el in range(1, len(my_list), 2):
    my_list[el - 1], my_list[el] = my_list[el], my_list[el - 1]

print(my_list)
