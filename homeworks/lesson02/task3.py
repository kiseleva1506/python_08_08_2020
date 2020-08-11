# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
# относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

while True:
    month = input('Введите целое число от 1 до 12: ')
    try:
        month = int(month)
    except ValueError:
        continue
    if month < 1 or month > 12:
        continue
    break

# вариант 1 list
summer = [6, 7, 8]
autumn = [9, 10, 11]
winter = [12, 1, 2]
spring = [3, 4, 5]

if month in summer:
    print('Месяц относится к лету')

if month in autumn:
    print('Месяц относится к осени')

if month in winter:
    print('Месяц относится к зиме')

if month in spring:
    print('Месяц относится к весне')

# вариант 2 dict
seasons = {12: 'зиме', 1: 'зиме', 2: 'зиме', 3: 'весне', 4: 'весне', 5: 'весне',
           6: 'лету', 7: 'лету', 8: 'лету', 9: 'осени', 10: 'осени', 11: 'осени'}
print('Месяц относится к', seasons[month])
