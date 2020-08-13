# Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два
# элемента — номер товара и словарь с параметрами (характеристиками товара: название,
# цена, количество, единица измерения). Структуру нужно сформировать программно,
# т.е. запрашивать все данные у пользователя.
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый
# ключ — характеристика товара, например название, а значение — список значений-характеристик,
# например список названий товаров.

prod_list = []
it = 1

while True:
    while True:
        prod_name = input('Введите название товара: ')
        if len(prod_name) == 0:
            continue
        break

    while True:
        prod_price = input('Введите цену товара: ')
        try:
            prod_price = float(prod_price)
        except ValueError:
            continue
        if prod_price <= 0:
            continue
        break

    while True:
        prod_quantity = input('Введите количество товара: ')
        try:
            prod_quantity = float(prod_quantity)
        except ValueError:
            continue
        if prod_quantity <= 0:
            continue
        break

    while True:
        prod_unit = input('Введите единицу измерения товара: ')
        if len(prod_unit) == 0:
            continue
        break

    prod_list.append((it, {'название': prod_name, 'цена': prod_price, 'количество': prod_quantity, 'ед': prod_unit}))
    it += 1

    answer = input('Для ввода следующего товара введите +: ')
    if answer != '+':
        break

print(prod_list)

params = ['название', 'цена', 'количество', 'ед']
result = {}

for itm in params:
    result[itm] = []

for itm in prod_list:
    for param in params:
        result[param].append(itm[1][param])

print(result)
