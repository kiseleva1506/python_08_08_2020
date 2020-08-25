""" Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран. """
from random import randint
from pathlib import Path


def create_file(file_name):
    with file_name.open('w') as f:
        for _ in range(11):
            num_list = [str(randint(1, 13957)) for __ in range(20)]
            f.write(f"{' '.join(num_list)}\n")


def sum_file(file_name):
    summ = 0
    if file_name.exists():
        with file_name.open() as f:
            for line in f:
                line = line.split()
                line = map(float, line)
                summ += sum(line)
    return summ


fn = Path(__file__).parent.joinpath('text_file5.txt')
create_file(fn)
print(f'{sum_file(fn):.2f}')
