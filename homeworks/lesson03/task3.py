"""Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов."""


def minimum(*args):
    min_el = args[0]
    i = 1
    while i < len(args):
        if args[i] < min_el:
            min_el = args[i]
        i += 1
    return min_el

def my_func(arg1, arg2, arg3):
    min_el = minimum(arg1, arg2, arg3)
    arg_list = [arg1, arg2, arg3]
    arg_list.remove(min_el)
    sum = arg_list[0] + arg_list[1]
    return sum


print(my_func(3, 3, 3))