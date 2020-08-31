'''Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.'''

with open('Test_5.txt', 'x+', encoding='utf-8') as f:
    print(input('Enter some numbers with spaces: '), file=f)
    f.seek(0)
    content = f.read().split()
    summ = 0
    for num in content:
        summ += int(num)
    print(summ)



