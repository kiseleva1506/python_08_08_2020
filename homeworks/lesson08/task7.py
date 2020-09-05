""" Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте
перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры
класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность
полученного результата. """


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a}{"+" if self.b >= 0 else ""}{self.b}i'

    def __add__(self, other):
        if not isinstance(other, ComplexNumber):
            raise ValueError
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        if not isinstance(other, ComplexNumber):
            raise ValueError
        return ComplexNumber(self.a * other.a - self.b * other.b, self.a * other.b + other.a * self.b)


if __name__ == '__main__':
    cn1 = ComplexNumber(2, 3)
    cn2 = ComplexNumber(3, -4)
    cn3 = cn1 + cn2
    cn4 = cn1 * cn2

    print(cn1)
    print(cn2)
    print(cn3)
    print(cn4)
