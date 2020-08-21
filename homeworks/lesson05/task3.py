""" Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников. """

from pathlib import Path

num_emp = 0
sum_emp = 0
min_sum = 20000.0

file_name = Path(__file__).parent.joinpath('text_file3.txt')
if file_name.exists():
    with file_name.open() as f:
        while True:
            nxt_str = f.readline()
            if not len(nxt_str):
                break

            emp_data = nxt_str.split()
            try:
                emp_data[1] = float(emp_data[1])
            except ValueError:
                continue
            except IndexError:
                continue

            if emp_data[1] < min_sum:
                print(emp_data[0], emp_data[1])

            num_emp += 1
            sum_emp += emp_data[1]

        print(f'Средний доход сотрудников {(sum_emp / num_emp):.2f}')
else:
    print('Файл не найден')
