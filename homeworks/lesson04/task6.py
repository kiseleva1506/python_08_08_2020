""" Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл
не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено."""

from itertools import count
from itertools import cycle
from sys import argv


def int_gen(start):
    for i in count(start):
        if i > start + 9:
            print('')
            break
        print(i, end=' ')


def cyc_gen(iter_count):
    i = 0
    for itm in cycle("TEST"):
        if i == iter_count:
            print('')
            break
        i += 1
        print(itm, end=' ')


def input_error(num):
    fl = False
    try:
        num = int(num)
    except ValueError:
        print('Ошибка ввода. Третий параметр должен быть целым положительным числом.')
        fl = not fl

    if num <= 0:
        print('Ошибка ввода. Третий параметр должен быть целым положительным числом.')
        fl = not fl

    return fl, num


if __name__ == '__main__':

    _, func_name, param = argv
    fl_error_input, param = input_error(param)
    if fl_error_input:
        exit(0)

    menu = {'int_gen': int_gen, 'cyc_gen': cyc_gen}
    func = menu.get(func_name)
    if func is None:
        print('Ошибка ввода. Функция {} не определена.'.format(func_name))
        exit(0)

    func(param)
