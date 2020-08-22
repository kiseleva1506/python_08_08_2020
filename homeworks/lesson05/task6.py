""" Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно,
чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий
название предмета и общее количество занятий по нему. Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30} """

from pathlib import Path


def extract_numerical(s):
    d = ''
    for el in s:
        if el.isdigit():
            d += el
    try:
        d = int(d)
    except ValueError:
        d = 0
    return d


classes = {}
file_name = Path(__file__).parent.joinpath('text_file6.txt')

if file_name.exists():
    with file_name.open() as f:
        for line in f:
            data = line.split()
            cl_sum = 0
            for el in data[1:]:
                cl_sum += extract_numerical(el)
            classes[data[0].replace(':', '')] = cl_sum

print(classes)
