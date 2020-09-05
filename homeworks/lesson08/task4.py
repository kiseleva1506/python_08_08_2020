""" Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.

Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также
других данных, можно использовать любую подходящую структуру, например словарь.

Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например,
для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных. """

from abc import ABC, abstractmethod


class OfficeEquipment(ABC):

    @abstractmethod
    def specify_properties(self, **kwargs):
        pass


class Printer(OfficeEquipment):
    def __init__(self, brand, name, manufacture_date):
        self.brand = brand
        self.name = name
        self.manufacture_date = manufacture_date
        self.format = 'A4'
        self.is_color = False

    def __str__(self):
        return f'printer: {self.brand} {self.name} {self.manufacture_date}, ' \
               f'{"color" if self.is_color else "black-white"}, format {self.format}'

    def specify_properties(self, **kwargs):
        if kwargs.get('format') is not None:
            self.format = kwargs['format']
        if kwargs.get('is_color') is not None:
            self.is_color = kwargs['is_color']


class Scanner(OfficeEquipment):
    def __init__(self, brand, name, manufacture_date):
        self.brand = brand
        self.name = name
        self.manufacture_date = manufacture_date
        self.resolution = 0
        self.speed = 0

    def specify_properties(self, **kwargs):
        if kwargs.get('resolution') is not None:
            self.resolution = kwargs['resolution']
        if kwargs.get('speed') is not None:
            self.speed = kwargs['speed']

    def __str__(self):
        return f'printer: {self.brand} {self.name} {self.manufacture_date}, ' \
               f'resolution {self.resolution}, speed {self.speed}'


class Copier(OfficeEquipment):
    def __init__(self, brand, name, manufacture_date):
        self.brand = brand
        self.name = name
        self.manufacture_date = manufacture_date
        self.is_color = False
        self.speed = 0

    def specify_properties(self, **kwargs):
        pass


class Unit:
    def __init__(self, name):
        self.name = name
        self.list_of_stored = []

    def register(self, equip):
        self.list_of_stored.append(equip)

    def give_equipment(self, unit, equip, quantity=1):
        for i in range(quantity):
            try:
                ind = self.list_of_stored.index(equip)
                self.list_of_stored.pop(ind)
                unit.register(equip)
            except ValueError:
                raise ValueError('Вы пытаетесь передать оборудование, которого нет в остатках')


class Warehouse(Unit):
    def __init__(self, name, warehouseman, s=0):
        super().__init__(name)
        self.warehouseman = warehouseman
        self.s = s

    def __str__(self):
        return f'{self.name}, {self.warehouseman}, s={self.s}' \
               f'\n{[itm.__str__() for itm in self.list_of_stored]}'


class Department(Unit):
    def __init__(self, name, employees=0):
        super().__init__(name)
        self.employees = employees

    def __str__(self):
        return f'{self.name}: {self.employees}'


if __name__ == '__main__':
    pr = Printer('HP', 'DHY-548 PL', '15-06-2019')
    pr.specify_properties(is_color=True)
    sc = Scanner('Acer', 'NMH-234', '12-04-2020')
    sc.specify_properties(resolution=600, speed=8)

    wh = Warehouse('base', 'Ivan', 1545)
    wh.register(pr)
    wh.register(sc)
    print(wh)

    dep = Department('accounting', 3)
    print(dep)

    wh.give_equipment(dep, pr)
    print(wh)
