# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

n = 0
while n < 1 or n > 9:
    n = int(input('enter n (0 < n < 10): '))

sum = 0
range = counter = 3
while counter:
    sum += counter * n * 10 ** (range - counter)
    counter -= 1
print(sum)