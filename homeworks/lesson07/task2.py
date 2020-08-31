""" Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся
пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property. """

from abc import ABC, abstractmethod
import enum


class ClothesTypes(enum.Enum):
    coat = enum.auto
    suit = enum.auto


class Clothes(ABC):
    """
    абстрактный класс
    """
    def __init__(self, name, cl_type=None):
        self.name = name
        self.cl_type = cl_type

    def __str__(self):
        return f'{self.cl_type.name} {self.name}: {self.fabric_consumption()}'

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):

    def __init__(self, name, v):
        super().__init__(name, ClothesTypes.coat)
        self.v = v

    def fabric_consumption(self):
        return self.v / 6.5 + 0.5


class Suit(Clothes):

    def __init__(self, name, h):
        super().__init__(name, ClothesTypes.suit)
        self.h = h

    def fabric_consumption(self):
        return 2 * self.h + 0.3


if __name__ == '__main__':
    cl_list = [Coat('модный', 13), Suit('современный', 1.7)]
    res = 0
    for itm in cl_list:
        print(itm)
        res += itm.fabric_consumption()
    print(f'Общий расход: {res}')
