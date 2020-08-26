""" Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и
метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого
из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет
описанный метод для каждого экземпляра. """


class Stationery:

    def __init__(self, title=''):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self}')

    def __str__(self):
        return type(self).__name__


class Pen(Stationery):

    def __init__(self):
        super(Pen, self).__init__()

    def draw(self):
        super(Pen, self).draw()


class Pencil(Stationery):

    def __init__(self):
        super(Pencil, self).__init__()

    def draw(self):
        super(Pencil, self).draw()

class Handle(Stationery):

    def __init__(self):
        super().__init__('Handle')

    def draw(self):
        super(Handle, self).draw()


st = Stationery()
st.draw()

hand = Handle()
hand.draw()

pen = Pen()
pen.draw()
