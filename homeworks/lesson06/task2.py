""" Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * числосм толщины полотна. Проверить работу метода.

Например: 20м * 5000м * 25кг * 5см = 12500 т """


class Road:

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calculate_mass(self, weight_per_cm, thick):
        return self.__length * self.__width * weight_per_cm * thick


r = Road(5000, 20)
print(r.calculate_mass(25, 5))
