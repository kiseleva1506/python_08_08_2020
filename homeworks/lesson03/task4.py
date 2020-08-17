""" Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде
функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции
возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью
оператора **. Второй — более сложная реализация без оператора **, предусматривающая использование
цикла. """


def my_func_1(x, y):
    return x ** y


def my_func_2(x, y):
    res = 1
    i = y
    while i < 0:
        res /= x
        i += 1
    return res


while True:
    base = input('Введите действительное положительное число: ')
    try:
        base = float(base)
    except ValueError:
        continue
    if base <= 0:
        continue
    break

while True:
    exp = input('Введите целое отрицательное число: ')
    try:
        exp = int(exp)
    except ValueError:
        continue
    if exp >= 0:
        continue
    break

print(my_func_1(base, exp))
print(my_func_2(base, exp))
