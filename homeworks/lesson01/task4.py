# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

num_str = '0'
while int(num_str) < 1 :
    num_str = input('enter num (num > 0): ')

max_num = 0
i = 0
while i < len(num_str):
    max_num = max(max_num, int(num_str[i]))
    i += 1

print(max_num)