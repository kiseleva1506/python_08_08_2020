""" Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой. """

class MyDivisionByZeroException(Exception):
    def __init__(self, txt):
        self.txt = txt


if __name__ == '__main__':
    print('Для прекращения ввода напечатайте мохнатую точку')
    while True:
        in_data = input('Введите числитель и знаменатель, разделенные пробелами: ')
        if in_data == '*':
            break
        num, den = map(float, in_data.split())
        try:
            if den == 0:
                raise MyDivisionByZeroException('Вы ввели ноль, на него делить нельзя')
            print('Результат деления: ', num / den)
        except MyDivisionByZeroException as e:
            print(e)
