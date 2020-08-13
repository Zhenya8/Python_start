'''Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте
цикл while и арифметические операции'''

number = int(input('Enter a number: '))

max = number % 10
num = number // 10

while number > 0:
    num = number % 10
    if max <= num:
        max = num
    number //= 10

print(max)
