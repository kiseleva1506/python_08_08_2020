"""Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое
слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func()."""


def upper_case(text):
    if len(text) == 0:
        return
    return chr(ord(text[0]) - 32) + text[1:]


def is_input_error(text):
    for itm in text:
        itm_code = ord(itm)
        if itm_code == 32 or 96 < itm_code < 123:
            pass
        else:
            print(itm, itm_code)
            print("Ошибка ввода.")
            return True

    return False


while True:
    text_in = input("""Введите строку из слов, разделенных пробелом. Каждое слово должно состоять из 
    латинских букв в нижнем регистре: """)
    if is_input_error(text_in):
        continue
    break

text_list = text_in.split()
for itm in text_list:
    print(upper_case(itm), end=' ')
