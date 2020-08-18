""" Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения
расчета для конкретных значений необходимо запускать скрипт с параметрами."""

from sys import argv


def salary(hours: float, rate: float, bonus: float) -> float:
    """
    Функция рассчитывает заработную плату сотрудника по формуле (выработка в часах * ставка в час) + премия
    :param hours: float - отработанные часы
    :param rate: float - ставка в час
    :param bonus: float - премия
    :return: float - рассчитанная з/п
    """
    return hours * rate + bonus


if __name__ == '__main__':

    _, *func_args = argv
    if len(func_args) != 3:
        print('Ошибка ввода. Нужно ввести 3 параметра: выработку в часах, ставка в час, премия.')
        exit(0)

    i = 0
    while i < len(func_args):
        try:
            func_args[i] = float(func_args[i])
            i += 1
        except ValueError:
            print('Ошибка ввода. Параметры должны быть числовые, разделены пробелами.')
            exit(0)

    print(salary(*func_args))
