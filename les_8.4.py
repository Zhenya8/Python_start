'''4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым
для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
5.  Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании. Для хранения данных о
наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь. '''


class Warehouse:
    def __init__(self, warehouse):
        self.warehouse = []

class Equipment:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price


class Printer(Equipment):
    def __init__(self, name, description, weight, price):
        self.description = description
        super().__init__(name, weight, price)
        print(f'Name - {name}; description - {description}; weight - {weight}; price - {price}')


class Scanner(Equipment):
    def __init__(self, name, weight, price):
        super().__init__(name, weight, price)
        print(f'Name - {name}, weight - {weight}; price - {price}')


class Xerox(Equipment):
    def __init__(self, name, weight, price):
        super().__init__(name, weight, price)
        print(f'Name - {name}, weight - {weight}; price - {price}')


printer = Printer('Epson L120', 'Jet printer', 20, 142)
scanner = Scanner('Epson Perfection V19', 24.5, 99.99)
xerox = Xerox('Xerox Phaser 3330VDNI', 15.45, 100.1)
