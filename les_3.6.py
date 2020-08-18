'''Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().'''


def int_func(a):
    return a.capitalize(), a.title()


print(int_func('this is a string of small latin letters'))


# ---------------------------------------------------- ord ------------------------------------------------------------------------

def ord_func(a):
    for i in a:
        if 97 <= ord(i) <= 122:
            return a.title()


print(ord_func('this is a string of small latin letters'))
print(ord_func(input('Enter some string of small Latin letters: ')))
