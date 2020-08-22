''' Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n). Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24
'''

n = input('Enter an integer: ')


def fact(n):
    try:
        mult = 1
        my_list = range(1, int(n))
        for el in my_list:
            mult *= el
            yield mult
    except:
        print('Error!')


for el in fact(n):
    print(el)

print(fact(n))