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


def financial_result(file_name):
    firms = {}
    firms_number = 0
    av_profit = 0

    with file_name.open() as f:
        for line in f:
            data = line.split()
            try:
                result = float(data[2]) - float(data[3])
            except ValueError:
                continue

            firms[data[0]] = result
            if result > 0:
                av_profit += result
                firms_number += 1

        try:
            av_profit /= firms_number
        except ZeroDivisionError:
            av_profit = 0

    return firms, {'average_profit': av_profit}


file_parent = Path(__file__).parent
fn = file_parent.joinpath('text_file7.txt')
jfn = file_parent.joinpath('json_file7.json')

if fn.exists():
    data_list = financial_result(fn)
    with jfn.open('w') as jf:
        json.dump(data_list, jf)
else:
    print('Файл источник не найден')
