''' 1) Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел
и строк и сохраните в переменные, выведите на экран.
'''

print('Hi!')
name = input('What\'s your name?: ')
print('Nice to meet you :)')
age = input('How old are you?: ')
print(f'{name}, I know your birthday year! It\'s', 2020 - int(age))
print(type(name), type(age))
