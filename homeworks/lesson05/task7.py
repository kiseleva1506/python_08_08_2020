""" Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со
средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста. """

from pathlib import Path
import json


def read_data(file_name):
    firms = {}
    with file_name.open() as f:
        for line in f:
            data = line.split()
            firms[data[0]] = data[2:]
    for key, value in firms.items():
        firms[key] = int(value[0]) - int(value[1])
    return firms


file_parent = Path(__file__).parent
fn = file_parent.joinpath('text_file7.txt')
jfn = file_parent.joinpath('json_file7.json')

if fn.exists():
    firms_dict = read_data(fn)
    print(firms_dict)

    try:
        av_pr = sum(val for val in firms_dict.values() if val > 0) \
                / sum(1 for val in firms_dict.values() if val > 0)
    except ZeroDivisionError:
        av_pr = 0

    finance = {'average_profit': av_pr}

    data_list = [firms_dict, finance]
    with jfn.open('w') as jf:
        json.dump(data_list, jf)
else:
    print('Файл источник не найден')
