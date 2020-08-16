""" Реализовать функцию, принимающую два числа (позиционные аргументы) и
выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
обработку ситуации деления на ноль. """


def func_div(num, den):
    try:
        return num / den
    except ZeroDivisionError:
        return None


def number_enter():
    while True:
        num = input('Введите число: ')
        try:
            return float(num)
        except ValueError:
            print('Неправильный ввод.')
            continue


num1 = number_enter()
num2 = number_enter()
print(func_div(num1, num2))
