# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор
# натуральных чисел. У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент
# с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например,
# my_list = [7, 5, 3, 3, 2].

my_list = [7, 5, 3, 3, 2]
print(my_list)

while True:
    new_el = input('Введите натуральное число: ')
    try:
        new_el = int(new_el)
    except ValueError:
        continue
    if new_el < 1:
        continue
    break

# если новый элемент больше первого элемента списка, то вставим его нулевым
# если новый элемент меньше последнего элемента списка, то добавим его в конец
# проверим, есть ли такие же элементы, как нужно вставить, если есть, вставим после
# последнего
# если не подошел ни один предыдущий вариант, то ищем, куда вставить элемент
# делением пополам
if new_el > my_list[0]:
    my_list.insert(0, new_el)
elif new_el < my_list[len(my_list) - 1]:
    my_list.append(new_el)
else:
    new_index = -1
    for ind, itm in enumerate(reversed(my_list)):
        if itm == new_el:
            new_index = len(my_list) - 1 - ind
            break
    if new_index > -1:
        my_list.insert(new_index + 1, new_el)
    else:
        low = 0
        high = len(my_list) - 1
        while low <= high:
            mid = (low + high) // 2
            if new_el > my_list[mid]:
                if my_list[mid - 1] > new_el:
                    my_list.insert(mid, new_el)
                    break
                high = mid - 1
            elif new_el < my_list[mid]:
                if my_list[mid + 1] < new_el:
                    my_list.insert(mid + 1, new_el)
                    break
                high = mid + 1

print(my_list)
