'''Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.'''

n = int(input('Enter a number: '))

print(f'Summ of n + nn + nnn = {str(n) + str(n + n) + str(n + n + n)}')

