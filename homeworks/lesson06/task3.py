""" Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения полного
имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). Проверить работу примера на реальных
данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы
экземпляров). """


class Worker:

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {"wage": 0, "bonus": 0}

    def __str__(self):
        return f'{self.name} {self.surname}: {self.position}'

    def set_income(self, wage, bonus):
        self.__income['wage'] = wage
        self.__income['bonus'] = bonus

    def get_income(self):
        return tuple(self.__income.values())


class Position(Worker):

    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return sum(self.get_income())


p = Position('Ivan', 'Ivanov', 'engineer')
p.set_income(60000, 5000)

print(p.get_full_name())
print(p.get_total_income())
