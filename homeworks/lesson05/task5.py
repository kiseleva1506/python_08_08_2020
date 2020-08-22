""" Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран. """

from pathlib import Path


def create_file(file_name):
    with file_name.open('w') as f:
        i = 1
        while i < 11:
            num_list = [str(round((i + j) * i / j, 2)) for j in range(20, 80, 2)]
            f.write(' '.join(num_list))
            f.write('\n')
            i += 1


def sum_file(file_name):
    summ = 0
    if file_name.exists():
        with file_name.open() as f:
            for line in f:
                line = line.split()
                line = [float(el) for el in line]
                summ += sum(line)
    return summ


fn = Path(__file__).parent.joinpath('text_file5.txt')
create_file(fn)
print(f'{sum_file(fn):.2f}')
