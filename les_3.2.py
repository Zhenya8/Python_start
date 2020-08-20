'''Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.'''


def info(name, surname, year, city, email, phone):
    print(name, surname, year, city, email, phone)


info(name=input('Enter your name: '), surname=input('Enter your surname: '), year=input('Enter your birthday year: '),
           city=input('Enter your city: '), email=input('Enter your email: '), phone=input('Enter your phone number: '))


# --------------------------------------------------------------- **kwargs ----------------------------------------------------------

def info(**kwargs):
    return kwargs


print(info(name=input('Enter your name: '), surname=input('Enter your surname: '), year=input('Enter your birthday year: '),
           city=input('Enter your city: '), email=input('Enter your email: '), phone=input('Enter your phone number: ')))

# ---------------------------------------------------------------- Lambda -----------------------------------------------------------

print((lambda **kwargs: kwargs)(name='Zhenya', surname='Bogdasheva', year=1986, city='SPb', email='zhenya@ya.ru', phone=1234567))
