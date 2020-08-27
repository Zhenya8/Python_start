'''1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных
свидетельствует пустая строка.'''

try:
    f = open('Test_5.1_5.2.txt', 'x+', encoding='utf-8')
    while True:
        string = input('Enter some info: ')
        f.writelines(f'{string}\n')
        if not string:
            break
    f.seek(0)
    print('You typed: ')
    for ind, line in enumerate(f, 1):
        words = len(line.split())
        print(f'{ind}) word(s): {words} {line}', end='')
except FileExistsError:
    print('A file with the same name already exists')
