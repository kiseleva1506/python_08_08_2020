""" Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д. """


class Matrix:

    def __init__(self, data_list):
        """
        создание экземпляра класса Matrix
        :param data_list: список списков int
        """
        self.__data_list = data_list

    def __str__(self):
        res = ''
        for row in self.__data_list:
            for itm in row:
                res += f'{str(itm): >5}'
            res += '\n'
        return res

    def __getitem__(self, index):
        return tuple(self.__data_list[index])

    def __add__(self, other):
        """
        сложение матриц
        :param other: Matrix - матрица того же размера, что и текущая
        :return: Matrix - результат сложения матриц
        """
        res_list = []
        for idx, el in enumerate(self.__data_list):
            res_list.append([x + y for x, y, in zip(el, other[idx])])
        return Matrix(res_list)


if __name__ == '__main__':
    mtx1 = Matrix([[10, 20, 30], [5, 15, 23]])
    print(mtx1)
    mtx2 = Matrix([[11, -10, 15], [33, 10, 0]])
    print(mtx2)

    mtx3 = mtx1 + mtx2
    print(mtx3)
