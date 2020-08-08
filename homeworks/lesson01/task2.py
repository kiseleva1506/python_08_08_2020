# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс. Используйте форматирование строк.

time_in_sec = int(input('enter time in seconds '))

time_min, time_sec = divmod(time_in_sec, 60)
time_hour, time_min = divmod(time_min, 60)

print(f'{time_hour:02d}:{time_min:02d}:{time_sec:02d}')