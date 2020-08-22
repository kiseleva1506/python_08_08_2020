""" Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка. """

from pathlib import Path

file_name = Path(__file__).parent.joinpath('text_file.txt')

with file_name.open('w') as f:
    print('Введите строки. Для прекращения введите пустую строку')
    while True:
        line = input()
        if not len(line):
            break
        f.write(line + '\n')
