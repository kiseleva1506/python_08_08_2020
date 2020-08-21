""" Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны
войти четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения
всех элементов списка.
Подсказка: использовать функцию reduce(). """

from functools import reduce


def my_reduce(func, iter_list):
    it = iter(iter_list)
    res = next(it)
    for itm in it:
        res = func(res, itm)
    return res


my_list = [itm for itm in range(100, 1001) if not itm % 2]
result = reduce(lambda x, y: x + y, my_list)
print(result)

result2 = my_reduce(lambda x, y: x + y, my_list)
print(result2)
